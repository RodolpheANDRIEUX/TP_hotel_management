from models import Room, Client
from storage import load_clients, load_rooms, load_reservations, save_clients

Clients = load_clients()
Rooms = load_rooms()
Reservations = load_reservations()


def book(room, name, start_date, end_date):
    return


def show_clients():
    print(Clients)


def show_reservations():
    print(Reservations)


def show_rooms():
    print(Rooms)


def show_room(room_number):
    for room in Rooms:
        if room['number'] == room_number:
            print(room)
            for reservation in Reservations:
                if reservation['room'] == room_number:
                    print(f'reservation found: {reservation}')
            return
    print(f"No room found with number {room_number}")


def add_room(args):
    room_number, room_type, price_per_night = args

    for room in Rooms:
        if room['number'] == room_number:
            print(f"Room {room_number} already exists.")
            return

    new_room = Room(room_number, room_type, price_per_night)
    print(f"Room {room_number} added successfully.")
    Rooms.append(new_room)


def add_client(args):
    client_id = len(Clients) + 1
    last_name, first_name, birth_date, phone = args

    new_client = Client(client_id, last_name, first_name, birth_date, phone)
    Clients.append(new_client)
    print(f"Client {first_name} {last_name} added successfully.")
    save_clients(Clients)


def del_room(args):
    pass


def del_client(args):
    pass


def del_reservation(args):
    pass


def update_room(args):
    pass


def update_client(args):
    pass
