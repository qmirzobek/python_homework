# task1

def convert_cel_to_far(celsius):
    fahrenheit=celsius*9/5+32
    return fahrenheit
def convert_far_to_cel(fahrenheit):
    try:
        celsius=(fahrenheit-32)*5/9
        return celsius
    except:
        print("There is an error.")

try:
    fahrenheit=input("Enter a temperature in degrees F: ")
    fahrenheit=float(fahrenheit)
    celsius=convert_far_to_cel(fahrenheit)
    print(f"{fahrenheit} degrees F = {celsius:.2f} degrees C")
except:
    print('An error happend')

try:
    celsius=input("Enter a temperature in degrees C: ")

    celsius=float(celsius)
    fahrenheit=convert_cel_to_far(celsius)
    print(f"{celsius} degrees C = {fahrenheit:.2f} degrees F")
except:
    print('An error happend')

