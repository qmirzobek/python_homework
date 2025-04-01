import numpy as np
from PIL import Image
from pathlib import Path

current_dir = Path(__file__).resolve().parent

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def convert_temperatures(fahrenheit_values):
    vectorized_f_to_c = np.vectorize(fahrenheit_to_celsius)
    return vectorized_f_to_c(fahrenheit_values)

def power_func(base, exp):
    return base ** exp

def calculate_powers(bases, exponents):
    vectorized_power = np.vectorize(power_func)
    return vectorized_power(bases, exponents)


def solve_linear_system(A, b):
    return np.linalg.solve(A, b)


def flip_image(image_array):
    return np.flipud(np.fliplr(image_array))

def add_noise(image_array):
    noise = np.random.randint(0, 50, image_array.shape, dtype=np.uint8)
    return np.clip(image_array + noise, 0, 255)

def brighten_red_channel(image_array, increase=50):
    brightened_image = image_array.copy()
    brightened_image[:, :, 0] = np.clip(brightened_image[:, :, 0] + increase, 0, 255)
    return brightened_image

def apply_mask(image_array, mask_size=(100, 100)):
    h, w, _ = image_array.shape
    start_x, start_y = (w - mask_size[0]) // 2, (h - mask_size[1]) // 2
    masked_image = image_array.copy()
    masked_image[start_y:start_y+mask_size[1], start_x:start_x+mask_size[0]] = 0
    return masked_image



# Task 1: Convert temperatures
fahrenheit_values = np.array([32, 68, 100, 212, 77])
celsius_values = convert_temperatures(fahrenheit_values)

# Task 2: Power calculations
bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])
power_results = calculate_powers(bases, exponents)

# Task 3: Solve systems of equations
A1 = np.array([[4, 5, 6], [3, -1, 1], [2, 1, -2]])
b1 = np.array([7, 4, 5])
solution1 = solve_linear_system(A1, b1)

A2 = np.array([[10, -2, 3], [-2, 8, -1], [3, -1, 6]])
b2 = np.array([12, -5, 15])
solution2 = solve_linear_system(A2, b2)

# Task 4: Load and process image
image_path = current_dir/"images/birds.jpg"
try:
    image = Image.open(image_path)
    image_array = np.array(image)

    # Apply transformations
    flipped = flip_image(image_array)
    noisy = add_noise(image_array)
    brightened = brighten_red_channel(image_array)
    masked = apply_mask(image_array)

    # Save modified images
    Image.fromarray(flipped).save(current_dir/"images/birds_flipped.jpg")
    Image.fromarray(noisy).save(current_dir/"images/birds_noisy.jpg")
    Image.fromarray(brightened).save(current_dir/"images/birds_brightened.jpg")
    Image.fromarray(masked).save(current_dir/"images/birds_masked.jpg")

    print("Image processing complete.")

except FileNotFoundError:
    print("Error: Image file not found.")

# Print results
celsius_values, power_results, solution1, solution2
