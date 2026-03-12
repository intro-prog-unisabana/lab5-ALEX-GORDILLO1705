import os
import math

# Directorio actual
cwd = os.getcwd()
print(f"Current working directory: {cwd}")

# Entrada usuario
num = int(input("Enter an integer: "))

log_value = math.log2(num)
print(f"Log base 2 of {num} is: {log_value}")

print(f"Floor: {math.floor(log_value)}")
print(f"Ceiling: {math.ceil(log_value)}")