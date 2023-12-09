import getpass
import re
from datetime import datetime
from controller import book, show_rooms, show_clients, show_reservations

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
        return input(f"\n{green}hotel reservation manager{client_color} @{username} {reset}"
                     f"(try '{input_color}help{reset}')\n$ ")
    return input(f"\n{green}hotel reservation manager{client_color} @{username} {reset}\n$ ")


def process_command(command):
    """Process the user's command"""
    parts = command.split()
    action = parts[0]
    args = parts[1:]

    if action == 'help':
        # Documentation
        print("\n**************************")
        print("help - shows documentation")
        print("book [room] [name] [start_date] - [end_date] - Add a reservation")
        print("**************************\n")
    elif action == 'book':
        if validate_booking_req(args) == 'Valid':
            room, name, start_date, end_date = args[0], args[1], args[2], args[3]
            # Appeler la fonction de réservation
            print(f"Booking room {room} for {name} from {start_date} to {end_date}...")
            book(room, name, start_date, end_date)
        else:
            print("book [room] [name] [start_date (dd/mm/yyyy)] - [end_date (dd/mm/yyyy)]")
    elif action == 'show':
        if args[0] == 'rooms':
            show_rooms()
        elif args[0] == 'clients':
            show_clients()
        elif args[0] == 'reservations':
            show_reservations()
        else:
            print('show + "clients", "rooms" or "reservations"')
    elif action == 'exit':
        return False  # Signal to exit the program
    return True


def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False


def validate_booking_req(args):
    if len(args) != 4:
        return "Invalid number of arguments. Expected 4 arguments."

    room, name, start_date, end_date = args

    # Vérifier si le numéro de chambre est un nombre
    if not room.isdigit():
        return "Invalid room number. Room number should be numeric."

    # Vérifier le format des noms (pas de caractères spéciaux)
    if not re.match("^[A-Za-z ]*$", name):
        return "Invalid name. Name should only contain letters and spaces."

    # Valider les dates
    if not validate_date(start_date) or not validate_date(end_date):
        return "Invalid date format. Use DD/MM/YYYY."

    # Vous pouvez ajouter d'autres validations ici si nécessaire

    return "Valid"
