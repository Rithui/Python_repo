def convert_celcius(f):
    return(f-32)*5/9
f=float(input("Enter the temprature i farenheit:"))
print("Temprature in celsius is:",convert_celcius(f))
