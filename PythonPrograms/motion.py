"""
Imagine we are simulating a system containing a number of particles constrained to move along a 1D line
of length N cm. Each particle moves in a particular direction (left or right) with a constant speed of 1
cm/s. When a particle reaches either end of the line, it is immediately removed from the system. If two
particles meet at the same point, they both turn around (i.e. reverse their directions) and begin moving in
the opposite directions. At the start of the simulation, we know the original positions of the particles on the
line, but we do not know the direction they are facing! Given only the starting positions, write a program
that will compute the earliest and the latest possible times needed for all particles to be removed from the
system, given that every particle can be facing either left or right to begin with.
Your program should accept the following input. The first input is a single integer N, the length of the
pole. The next is an integer K, specifying the number of particles. K integers follow, where each integer
specifies the starting location of a particle.
Your program should then output

? first particle to get off
a) the earliest possible time when all the particles fall off the pole, and
? last particle to get off
b) the latest possible such time.

Sample input: 214 7 11 12 7 13 176 23 191
Sample output: 38 207
"""

SPEED = '1cm/s'
EARLIEST_TIME = None
LATEST_TIME = None

# N
length_of_pole = int(input("Please enter the length of the pole (cm): "))

# K
num_of_particles = int(input("\nPlease enter the number of particles: "))

starting_points = []

while len(starting_points) < num_of_particles:
    point = int(
        input(f"\nPlease enter the starting point for particle {len(starting_points) + 1}: "))
    starting_points.append(point)

print(f"You entered: {starting_points} as the starting points")


for particle_start in starting_points:
    motion_to_right = length_of_pole - particle_start
    motion_to_left = particle_start

    if motion_to_right > motion_to_left:
        latest_time = motion_to_right
        earliest_time = motion_to_left

    elif motion_to_right == motion_to_left:
        earliest_time = motion_to_right
        latest_time = motion_to_right

    else:
        # motion_to_left is greater than to right
        latest_time = motion_to_left
        earliest_time = motion_to_right


def check_prev_early_time(new_early_time: int):
    """
    Check if previous set earliest time is smaller than new suggested value
    """
    if EARLIEST_TIME:
        if new_early_time < EARLIEST_TIME:
            EARLIEST_TIME = new_early_time


def check_prev_late_time(new_late_time: int):
    """
    Check if previous set latest time is greater than new suggested value
    """
    if LATEST_TIME:
        if new_late_time > LATEST_TIME:
            LATEST_TIME = new_late_time


print(f"Earliest time: {earliest_time}")
print(f"Latest time: {latest_time}")
