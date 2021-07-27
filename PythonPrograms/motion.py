
SPEED = '1cm/s'
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
