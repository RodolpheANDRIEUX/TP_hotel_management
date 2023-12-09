from storage import load_clients, load_rooms, load_reservations

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
