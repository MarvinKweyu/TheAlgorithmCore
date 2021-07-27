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

SPEED = 1  # in cm/s
EARLIEST_TIME = 0
LATEST_TIME = 0


def check_prev_times(new_early_time: int, new_late_time: int):
    """
    Check if previous set earliest time is smaller than new suggested value
    """
    early_time = 0
    late_time = 0

    if new_early_time < EARLIEST_TIME:
        early_time = new_early_time
    else:
        early_time = new_early_time

    if new_late_time > LATEST_TIME:
        late_time = new_late_time
    else:
        late_time = new_late_time

    return early_time, late_time


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

    # print(f"You entered: {starting_points} as the starting points")
    calc_particle_motion(starting_points, length_of_pole)

    print(f"Earliest time: {EARLIEST_TIME}")
    print(f"Latest time: {LATEST_TIME}")


if __name__ == "__main__":
    main()
