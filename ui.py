import getpass
import logging
import re
from datetime import datetime
from controller import book, show_rooms, show_clients, show_reservations, add_room, add_client, del_room, del_client, \
    del_reservation, update_room, update_client, show_room

# globals
username = getpass.getuser()
Helper = 1

# colors
input_color = '\033[34m'
client_color = '\033[35m'
green = '\033[92m'
reset = '\033[0m'


def display_menu():
    """Display 'input' and return the user's command"""
    global Helper

    if Helper == 1:
        Helper = 0
        return input(f"\n{green}hotel booking manager{client_color} @{username} {reset}"
                     f"(try '{input_color}help{reset}')\n$ ")
    return input(f"\n{green}hotel booking manager{client_color} @{username} {reset}\n$ ")


def validate_room(args):
    if len(args) != 3:
        return "Invalid number of arguments. Expected 3 arguments."

    room, room_type, price = args

    if not room.isdigit():
        return "Invalid room number. Room number should be numeric."

    if not re.match("^[A-Za-z ]*$", room_type):
        return "Invalid name. Name should only contain letters and spaces."

    if not price.isdigit():
        return "Invalid room number. Room number should be numeric."

    return "Valid"


def validate_client(args):
    if len(args) != 4:
        return ("Invalid number of arguments. Expected 5 arguments: [first name] [last name] [birth date] [phone "
                "number]")

    first_name, last_name, birth_date, phone = args

    if not re.match("^[A-Za-z ]*$", first_name):
        return "Invalid first name. Name should only contain letters and spaces."

    if not re.match("^[A-Za-z ]*$", last_name):
        return "Invalid last name. Name should only contain letters and spaces."

    if not validate_phone_number(phone):
        return "Invalid phone number. It should be a French format"

    if not validate_date(birth_date):
        return "Invalid birth date. Expected [dd/mm/yyyy]"

    return "Valid"


def check_for_update_client(args):
    pass


def check_for_add_room(args):
    validation = validate_room(args)
    if validation != 'valid':
        logging.warning(validation)
        return
    add_room(args)


def check_for_add_client(args):
    validation = validate_client(args)
    if validation != 'valid':
        logging.warning(validation)
        return
    add_client(args)


def check_for_del_room(args):
    pass


def check_for_del_client(args):
    pass


def check_for_del_reservation(args):
    pass


def check_for_update_room(args):
    validation = validate_room(args)
    if validation != 'valid':
        logging.warning(validation)
        return
    update_room(args)


def check_for_show_room(args):
    if len(args) != 2:
        return "Invalid number of arguments. Expected 1 arguments: show room [room_number]"

    room = args[1]

    if not room.isdigit():
        return "Invalid room number. Room number should be numeric."

    show_room(room)


def process_command(command):
    """Process the user's command"""
    parts = command.split()
    action = parts[0]
    args = parts[1:]

    if action == 'help':
        # Documentation
        print("\n**************************")
        print("help - shows this documentation")
        print("book [room] [name] [start_date] [end_date] - Add a reservation")
        print("show rooms - Display all rooms")
        print("show clients - Display all clients")
        print("show reservations - Display all reservations")
        print("add room [room_number] [room_type] [price] - Add a new room")
        print("add client [first_name] [last_name] [birth_date] [phone] - Add a new client")
        print("delete room [room_number] - Remove a room")
        print("delete client [client_id] - Remove a client")
        print("delete reservation [reservation_id] - Remove a reservation")
        print("update room [room_number] [new_room_type] [new_price] - Update room details")
        print("update client [client_id] [new_phone] - Update client's contact information")
        print("exit - Exit the program")
        print("**************************\n")

    elif action == 'book':
        validation = validate_booking_req(args)
        if validation != 'Valid':
            logging.warning(validation)
            print("book [room] [name] [start_date (dd/mm/yyyy)] - [end_date (dd/mm/yyyy)]")
        else:
            room, name, start_date, end_date = args[0], args[1], args[2], args[3]
            print(f"Booking room {room} for {name} from {start_date} to {end_date}...")
            book(room, name, start_date, end_date)

    elif action == 'show':
        if len(args) < 1:
            print('show + "clients", "rooms" or "reservations"')
            print('show room [room number]')
        elif args[0] == 'rooms':
            show_rooms()
        elif args[0] == 'room':
            check_for_show_room(args)
        elif args[0] == 'clients':
            show_clients()
        elif args[0] == 'reservations':
            show_reservations()
        else:
            print('show + "clients", "rooms" or "reservations"')
            print('show room [room number]')

    elif action == 'add':
        if len(args) < 1:
            print('add + "client" or "room"')
        elif args[0] == 'room':
            check_for_add_room(args)
        elif args[0] == 'client':
            check_for_add_client(args)
        else:
            print('add + "client" or "room"')

    elif action == 'delete':
        if len(args) < 1:
            print('delete + "client", "room" or "reservation"')
        elif args[0] == 'room':
            check_for_del_room(args)
        elif args[0] == 'client':
            check_for_del_client(args)
        elif args[0] == 'reservation':
            check_for_del_reservation(args)
        else:
            print('delete + "client", "room" or "reservation"')

    elif action == 'update':
        if args[0] == 'room':
            check_for_update_room(args)
        elif args[0] == 'client':
            check_for_update_client(args)
        else:
            print('add + "client" or "rooms"')

    elif action == 'exit':
        return False  # Signal to exit the program

    else:
        print(f'"{action}" command not found. Try "help" to see the documentation')
    return True


def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False


def validate_phone_number(num):
    # Regex pour un numéro de téléphone français
    pattern = re.compile(r'^(?:\+33\s1|\d{2})\s\d{2}\s\d{2}\s\d{2}\s\d{2}$')

    if pattern.match(num):
        return True
    else:
        return False


def validate_booking_req(args):
    if len(args) != 4:
        return "Invalid number of arguments. Expected 4 arguments."

    room, name, start_date, end_date = args

    if not room.isdigit():
        return "Invalid room number. Room number should be numeric."

    if not re.match("^[A-Za-z ]*$", name):
        return "Invalid name. Name should only contain letters and spaces."

    if not validate_date(start_date) or not validate_date(end_date):
        return "Invalid date format. Use DD/MM/YYYY."

    return "Valid"
