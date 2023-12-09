import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s: %(levelname)s: %(message)s',
    filename='hotel_logs.log',
)

from ui import display_menu, process_command


def main():
    logging.info('launching main')

    while True:
        # get input
        choice = display_menu()

        # Process the user's command
        continue_program = process_command(choice)

        # Check if the user chose to exit the application
        if not continue_program:
            break

    print("Thank you for using our hotel reservation manager!")


if __name__ == "__main__":
    main()
