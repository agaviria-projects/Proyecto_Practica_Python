import pandas as pd

# Leer clientes.csv
clientes = pd.read_csv('../data/clientes.csv')
print("Clientes:")
print(clientes.head())

# Leer ventas.xlsx
ventas = pd.read_excel('../data/ventas.xlsx')
print("\nVentas:")
print(ventas.head())

#Obtener informacion basica del dataframe
print(clientes.info())
print(ventas.info())

print(clientes.tail())