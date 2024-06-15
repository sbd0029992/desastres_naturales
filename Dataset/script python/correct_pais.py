import pandas as pd

# Cargar el archivo CSV
file_path = '/home/diego/Downloads/DESASTRES_NATURALES/Corrected_Cleaned-1900_2021_DISASTERS.csv'
data = pd.read_csv(file_path)

# Truncar los valores en la columna "Country" a 30 caracteres
data['Country'] = data['Country'].astype(str).apply(lambda x: x[:30])

# Truncar los valores en la columna "Location" a 100 caracteres
data['Location'] = data['Location'].astype(str).apply(lambda x: x[:100])

# Guardar el dataframe corregido en un nuevo archivo CSV
corrected_file_path = '/home/diego/Downloads/DESASTRES_NATURALES/pais_Corrected_Cleaned-1900_2021_DISASTERS.csv'
data.to_csv(corrected_file_path, index=False)

print(f"Archivo corregido guardado en: {corrected_file_path}")
