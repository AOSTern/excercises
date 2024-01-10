"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    counter = 1
    if int(number) <= 0:
        return ""
    while counter <= number:
        if counter == 1 or counter % 4 == 1:
            seat = "A"
        if counter == 2 or counter % 4 == 2:
            seat = "B"
        if counter == 3 or counter % 4 == 3:
            seat = "C"
        if counter == 4 or counter % 4 == 0:
            seat = "D"
        counter += 1
        yield seat


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    counter = 1
    if int(number) <= 0:
        return ""
    while counter <= number:
        if ((counter + 4) // 4) == 13:
            counter += 1
            number += 1
            continue
        if counter == 1 or counter % 4 == 1:
            seat = str((counter + 4) // 4) + "A"
        if counter == 2 or counter % 4 == 2:
            seat = str((counter + 4) // 4) + "B"
        if counter == 3 or counter % 4 == 3:
            seat = str((counter + 4) // 4) + "C"
        if counter == 4 or counter % 4 == 0:
            if (((counter + 4) // 4) - 1) == 13:
                seat = str(((counter + 4) // 4) - 2) + "D"
            else:
                seat = str(((counter + 4) // 4) - 1) + "D"
        counter += 1
        yield seat


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    manifiesto = {}
    seats = generate_seats(len(passengers))
    for passenger in passengers:
        manifiesto[passenger] = next(seats)
    return manifiesto


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    codes = []
    for seats in seat_numbers:
        code = seats + flight_id
        while len(code) < 12:
            code = code + "0"
        yield code
