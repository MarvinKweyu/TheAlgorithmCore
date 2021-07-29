"""
Imagine we are simulating a system containing a number of particles
constrained to move along a 1D line of length N cm.
Each particle moves in a particular direction (left or right) with a constant speed of 1cm/s.
When a particle reaches either end of the line, it is immediately removed from the system.
If two particles meet at the same point, they both turn around (i.e. reverse their directions)
and begin moving in the opposite directions.
At the start of the simulation, we know the original positions of the particles on the line,
but we do not know the direction they are facing! Given only the starting positions, write a program
that will compute the earliest and the latest possible times needed for all particles
to be removed from the system, given that every particle can be facing either left or right to begin with.
Your program should accept the following input.
The first input is a single integer N, the length of the pole.
The next is an integer K, specifying the number of particles. K integers follow, where each integer
specifies the starting location of a particle.
Your program should then output

? first particle to get off
a) the earliest possible time when all the particles fall off the pole, and
? last particle to get off
b) the latest possible such time.

Sample input: 214 7 11 12 7 13 176 23 191
Sample output: 38 207
"""

import random
import itertools

SPEED = 1  # in cm/s
length_of_path = 214  # cm
num_of_particles = 7  # number of particles
EARLIEST_TIME = 0
LATEST_TIME = 0


class Particle:
    """An object on the 1D plane"""

    def __init__(self, position: int, direction: str):
        self.position = position
        self.direction = direction

    def change_direction(self, new_direction: str):
        """change direction of a particle"""
        self.direction = new_direction

    def change_position(self, new_position: int):
        """Change position of particle"""
        self.position = new_position

    def move(self):
        """Move in a specified direction"""
        if self.direction == "left":
            self.position -= SPEED
        elif self.direction == "right":
            self.position += SPEED

    def remove(self):
        """Remove particle from collection of particles"""
        pass


def calc_particle_motion(starting_points: list, length_of_pole: int):
    """
    Calculate length of a single particle
    """
    for starting_point in starting_points:
        time_to_right = (length_of_pole - starting_point) / SPEED
        time_to_left = starting_point / SPEED

        if time_to_right > time_to_left:
            EARLIEST_TIME, LATEST_TIME = check_prev_times(
                time_to_left, time_to_right)

        elif time_to_right == time_to_left:
            EARLIEST_TIME, LATEST_TIME = check_prev_times(
                time_to_right, time_to_right)

        else:
            # time_to_left is greater than to right
            EARLIEST_TIME, LATEST_TIME = check_prev_times(
                time_to_right, time_to_left)


def find_closest_two(all_particles: list, particle: Particle):
    """
    Parameters
    ----------
    all_particles: list
    A list of particle objects

    particle: Particle
    A single particle object

    Take a particle and find the closest item in a position higher than it and in a
    position less than it
    """

    pass


def get_number_of_possible_directions(all_particles: list) -> list:
    """
    Given an array of particles, get possible directions they can go

    Parameters
    ----------
    all_particles: list
    A list of all particles

    Returns a list of tuples with possible directions
    """
    p_s = ['L', 'R']
    possible_directions = [
        p for p in itertools.product(p_s, repeat=len(all_particles))]
    return possible_directions


def main():
    """
    main program entry
    """
    # N
    length_of_pole = int(input("Please enter the length of the pole (cm): "))

    # K
    num_of_particles = int(input("\nPlease enter the number of particles: "))

    starting_points = []

    while len(starting_points) < num_of_particles:
        point = int(
            input(f"\nPlease enter the starting point for particle {len(starting_points) + 1}: "))
        starting_points.append(point)

    print(f"Earliest time: {EARLIEST_TIME}")
    print(f"Latest time: {LATEST_TIME}")


def dummy_input():
    """
    Use dummy data as particles
    Note: this acts as the main of this program until the algorith words and
    is ready to accept input. Values here(starting points, length of 1D plane) are hard-coded
    """

    starting_points = [11, 12, 7, 13, 176, 23, 191]

    # create an object for each particle
    earliest_time_to_fall = []
    latest_time_to_fall = []

    directions = get_number_of_possible_directions(starting_points)

    #  create particles for each possible direction
    for possible_direction in directions:
        particles_for_direction = []  # eg tuple (L,L,L,L, L)
        for position, starting_point in enumerate(starting_points):
            # We give each particle a direction.
            particles_for_direction.append(
                Particle(starting_point, possible_direction[position]))

        # for particles taking a particular sequence of directions, find the times to fall off
        # particles_moving_right = []
        # particles_moving_left = []
        directions_of_particles = [
            particle.direction for particle in particles_for_direction]
        """
            if all particles have same direction, time is the same.
            get the item at the furthest end(right or left) and calc the time it takes to leave the opposite
            i.e left or right respectively
            """
        result = all(
            element == directions_of_particles[0] for element in directions_of_particles)

        if (result):
            print("All the elements are Equal")
        else:
            print("All Elements are not equal")

        # for particle in particles_for_direction:
        #     # group all the particles according to direction
        #     # if the particle is moving right, add it to the list
        #     if particle.direction == "right":
        #         particles_moving_right.append(particle)
        #     else:
        #         particles_moving_left.append(particle)

        # print(
        # f"Possible directions: {get_number_of_possible_directions(starting_points)}")


if __name__ == "__main__":
    dummy_input()
