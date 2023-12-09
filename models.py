class Client:
    def __init__(self, client_id, last_name, first_name, birth_date, phone):
        self.client_id = client_id
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.phone = phone

    def update_contact_info(self, new_phone):
        self.phone = new_phone

    def display_client_info(self):
        return (f"Client ID: {self.client_id}, Name: {self.first_name} {self.last_name}, Birth Date: {self.birth_date}"
                f", Phone: {self.phone}")


class Room:
    def __init__(self, number, room_type, price_per_night):
        self.number = number
        self.room_type = room_type
        self.price_per_night = price_per_night

    def update_price(self, new_price):
        self.price_per_night = new_price

    def display_room_info(self):
        return f"Room Number: {self.number}, Type: {self.room_type}, Price per Night: {self.price_per_night}"


class Reservation:
    def __init__(self, client, room, start_date, end_date):
        self.client = client
        self.room = room
        self.start_date = start_date
        self.end_date = end_date

    def extend_reservation(self, new_end_date):
        self.end_date = new_end_date

    def display_reservation_info(self):
        return (f"Reservation for {self.client.first_name} {self.client.last_name} in Room {self.room.number} "
                f"from {self.start_date} to {self.end_date}")
