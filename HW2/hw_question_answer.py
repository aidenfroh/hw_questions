import math

def calculate_volume(radius):
    """
    Calculate the volume of a sphere.

    Inputs:
    radius; float, the radius of the sphere in meters

    Output:
    Volume of the sphere in cubic meters.
    """
    volume = 4 / 3 * math.pi * radius ** 3
    return volume

def calculate_density(mass, volume):
    """
    Calculate the density of a body.

    Inputs:
    mass; float, the mass of the body in kg
    volume; float, the volume of the body in cubic meters

    Output:
    Density of the body in kg per cubic meter.
    """
    density = mass / volume
    return density

def calculate_surface_area(radius):
    """
    Calculate the surface area of a sphere.

    Inputs:
    radius; float, the radius of the sphere in meters

    Output:
    Surface area of the sphere in square meters.
    """
    area = 4 * math.pi * radius ** 2
    return area

radius = float(input("Enter the radius in meters: "))
mass = float(input("Enter the mass in kg: "))

volume = calculate_volume(radius)
density = calculate_density(mass, volume)
area = calculate_surface_area(radius)

print(f"The density is {round(density, 2)} kg per cubic meter")
print(f"The surface area is {round(area, 2)} square meters")


"""
Answer key:
Input() returns text, not a number, so the code outputs a TypeError. Wrap each input in a float to properly
flow through. Radius ^3 is not the correct formatting. I actually struggled with this when working on the
Roche limit problem for longer than I care to admit. Simple things that you forget can often trip you up. 
Calculate_density uses print(density) instead of return. This makes the density variable end up as None 
since it is not stored within the function when called upon later. “The density is “ + density + … tries to
add text to a number, raising a TypeError. A simple f-string fixes this. 
"""