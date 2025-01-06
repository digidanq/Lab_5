import temperatura

# a) 
celsius = 21
fahrenheit = temperatura.c_to_f(celsius)
print(f"{celsius}°C to {fahrenheit}°F")

# b)
fahrenheit = 89
celsius = temperatura.f_to_c(fahrenheit)
print(f"{fahrenheit}°F to {celsius}°C")

# c) 
celsius = 35
kelvin = temperatura.c_to_k(celsius)
print(f"{celsius}°C to {kelvin} K")
