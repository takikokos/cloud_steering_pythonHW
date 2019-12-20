def convert_temerature(x, toCelsius : bool = None, toFahrenheit : bool = None):
    if not (toCelsius or toFahrenheit) or (toCelsius == toFahrenheit):
        print("Укажите в какую шкалу перевести")
        return
    if toCelsius:
        return int((x - 32) * 5/9)
    elif toFahrenheit:
        return int((x * 9/5) + 32)
    

print(f"15 Celsius is {convert_temerature(15, toFahrenheit=True)} Fahrenheit")
print(f"59 Fahrenheit is {convert_temerature(59, toCelsius=True)} Celsius")