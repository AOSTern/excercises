"""Solution to Ellen's Alien Game exercise."""


class Alien:

    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    health = 3

    total_aliens_created = 0

    def __init__(self, *location):
        Alien.total_aliens_created += 1

        self.x_coordinate = location[0]

        self.y_coordinate = location[1]

    def hit(self):
        self.health -= 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, *location):
        self.x_coordinate = location[0]

        self.y_coordinate = location[1]

    def collision_detection(self, *other):
        pass


def new_aliens_collection(args):
    aliens = []

    for arg in args:
        aliens.append(Alien(*arg))

    return aliens


# TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
