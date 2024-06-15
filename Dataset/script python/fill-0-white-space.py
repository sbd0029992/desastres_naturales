import pandas as pd

# Cargar el dataset
file_path = '/home/diego/Downloads/dataset/EDA - Natural Disasters/1900_2021_DISASTERS.xlsx - emdat data.csv'
df = pd.read_csv(file_path)

# Columnas que deben ser rellenadas con 0
columns_to_fill_zero = [
    'Latitude', 'Longitude', 'Local Time',
    'Start Month', 'Start Day', 'End Year', 'End Month', 'End Day',
    'Total Deaths', 'No Injured', 'No Affected', 'No Homeless', 'Total Affected',
    "Insured Damages ('000 US$)", "Total Damages ('000 US$)",'Dis Mag Value'
]

# Rellenar columnas numéricas específicas con 0
df[columns_to_fill_zero] = df[columns_to_fill_zero].fillna(0)

# Rellenar todas las demás columnas de texto con 'No info'
df = df.fillna('Null')

# Guardar el dataset limpio
output_file_path = '/home/diego/Downloads/dataset/EDA - Natural Disasters/Cleaned-1900_2021_DISASTERS.xlsx - emdat data.csv'
df.to_csv(output_file_path, index=False)

print(f"Dataset limpio guardado en: {output_file_path}")

