import math


class Vector:
    # __coordinates=list()

    def __init__(self, *args):
        self.coordinates = list(args)
    
    def __str__(self):
        """
        String representation of the vector
        """
        return f"Vector: {tuple(self.coordinates)}"
    
    def __add__(self, other):
        """
        Add two vectors
        """
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Vectors must have the same length")
        new_coordinates = [x + y for x, y in zip(self.coordinates, other.coordinates)]
        return Vector(*new_coordinates)
    def __sub__(self, other):
        """
        Subtraction
        """
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Vectors must have the same length")
        new_coordinates = [x - y for x, y in zip(self.coordinates, other.coordinates)]
        return Vector(*new_coordinates)
    def __mul__(self, other):
        """
        Dot product
        """
        if(type(other) == int or type(other) == float):
            new_coordinates = [x * other for x in self.coordinates]
            return Vector(*new_coordinates)
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Vectors must have the same length")
        
        new_coordinates = [x * y for x, y in zip(self.coordinates, other.coordinates)]
        return sum(new_coordinates)
    
    def magnitude(self):
        """
        Calculate the magnitude of the vector
        """
        return math.sqrt(sum([x**2 for x in self.coordinates]))
    def normalize(self):
        """
        Normalize the vector
        """
        return Vector(*[x/self.magnitude() for x in self.coordinates])
    


# Create vectors
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Print the vector
print(v1)          # Output: Vector(1, 2, 3)

# Addition
v3 = v1 + v2
print(v3)          # Output: Vector(5, 7, 9)

# Subtraction
v4 = v2 - v1
print(v4)          # Output: Vector(3, 3, 3)

# Dot product
dot_product = v1 * v2
print(dot_product) # Output: 32

# Scalar multiplication
v5 =  v1 * 3
print(v5)          # Output: Vector(3, 6, 9)

# Magnitude
print(v1.magnitude())  # Output: 3.7416573867739413

# Normalization
v_unit = v1.normalize()
print(v_unit)      # Output: Vector(0.267, 0.534, 0.801)

