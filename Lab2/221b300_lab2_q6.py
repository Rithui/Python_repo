def convert_faren(C):
    return (C
            *(9/5)+32)

c=int(input("Enter the tempraure in celcius:"))
print("Temprature in farenheit is:",convert_faren(c))
