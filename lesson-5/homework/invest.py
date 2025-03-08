# task2

def invest(amount, rate, years):
    if(years==0):
        return
    newAmount=amount*((1+rate)**years)
    invest(amount,rate,(years-1))
    print(f"year {years}: ${newAmount:.2f}")

try:
    amount=float(input("Enter the initual amount: "))
    percentageRate=float(input("Enter the percentage rate (e.g. .05 = 5%): "))
    years=int(input("Enter a number of years: "))
    invest(amount,percentageRate,years)
except:
    print("An error occured")

# invest(100,.05,4)

