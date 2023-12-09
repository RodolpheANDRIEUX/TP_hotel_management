import logging
import json


def save_data(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4, default=lambda o: o.__dict__)
        logging.info(f"Data successfully saved to {filename}")
    except IOError as e:
        logging.error(f"Error saving data to {filename}: {e}")


def load_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            logging.info(f"Data successfully loaded from {filename}")
            return data
    except FileNotFoundError:
        logging.warning(f"No data found at {filename}, starting with empty data.")
        return []
    except json.JSONDecodeError as e:
        logging.error(f"Error reading {filename}: {e}")
        return []


def save_clients(clients):
    save_data(clients, 'clients.json')


def load_clients():
    return load_data('clients.json')


def save_rooms(rooms):
    save_data(rooms, 'data/rooms.json')


def load_rooms():
    return load_data('data/rooms.json')


def save_reservations(reservations):
    save_data(reservations, 'reservations.json')


def load_reservations():
    return load_data('reservations.json')
