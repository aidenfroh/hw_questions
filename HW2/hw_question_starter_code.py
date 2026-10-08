import math

def calculate_volume(radius):
    volume = 4 / 3 * math.pi * radius ^ 3
    return volume

def calculate_density(mass, volume):
    density = mass / volume
    print(density)

radius = input("Enter the radius in meters: ")
mass = input("Enter the mass in kg: ")

volume = calculate_volume(radius)
density = calculate_density(mass, volume)

print("The density is " + density + " kg per cubic meter")