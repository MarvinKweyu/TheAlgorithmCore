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

import enum
import itertools
from typing import List


class Direction(enum.Enum):
    RIGHT = 0
    LEFT = 1


class Particle:
    def __init__(self, position: int, direction: Direction):
        self.position = position
        self.direction = direction


class Pole:
    def __init__(self, length: int, particles: List[Particle]):
        self.length = length
        self.particles = particles
        self.removed_particles = []
        self.times_of_particles_removal = [None for _ in particles]

    def move_particles(self, current_time: int, steps: int = 1):
        for _ in range(steps):
            for particle in self.particles:
                if self.length >= particle.position >= 0:
                    particle.position = particle.position + 1 if particle.direction == Direction.RIGHT \
                        else particle.position - 1
                    if particle.position > self.length or particle.position < 0:
                        idx = self.particles.index(particle)
                        self.removed_particles.append(particle)
                        self.times_of_particles_removal[idx] = current_time


class World:
    def __init__(self, poles: List[Pole]):
        self.poles = poles
        self.removed_poles = {}
        self.current_time = 0

    def simulate(self):
        while len(self.poles) > len(self.removed_poles.keys()):
            yield self.current_time
            self.current_time += 1
            for i, pole in enumerate(self.poles):
                if i not in self.removed_poles.keys():
                    pole.move_particles(self.current_time)
                    if len(pole.particles) == len(pole.removed_particles):
                        idx = self.poles.index(pole)
                        self.removed_poles[idx] = pole
        yield self.current_time


def get_direction_permutations(number_of_particles: int):
    directions = [Direction.RIGHT, Direction.LEFT]
    permutations = [i for i in itertools.product(
        directions, repeat=number_of_particles)]
    return permutations


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
    length_of_pole = 5
    starting_positions = [2, 3, 1]

    direction_permutations = get_direction_permutations(
        len(starting_positions))
    poles = []

    for permutation in direction_permutations:
        particles = []
        for idx, starting_position in enumerate(starting_positions):
            particles.append(Particle(starting_position, permutation[idx]))
        poles.append(Pole(length_of_pole, particles))

    world = World(poles)
    _ = [t for t in world.simulate()]

    times = []
    starting_times = []
    stopping_times = []
    for pole in poles:
        t = pole.times_of_particles_removal
        times.append(t)
        starting_times.append(min(t))
        stopping_times.append(max(t))

    first = starting_times.index(min(starting_times))
    last = stopping_times.index(max(stopping_times))

    direction_permutations_char = [
        ["R" if j == Direction.RIGHT else "L" for j in i] for i in direction_permutations]
    print(
        f"First to drop off: {direction_permutations_char[first]} at time {min(starting_times)}")
    print(
        f"Last to drop off: {direction_permutations_char[last]} at time {max(stopping_times)}")


if __name__ == "__main__":
    main()
