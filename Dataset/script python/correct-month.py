import pandas as pd

# Cargar el dataset con el delimitador correcto
file_path = '/home/diego/Downloads/DESASTRES_NATURALES/datasetDanios.csv'
df = pd.read_csv(file_path, delimiter=';')

# Rellenar los valores vacíos de 'Start Month' con 1
df['Start Month'].fillna(1, inplace=True)

# Convertir 'Start Year' y 'Start Month' a strings
df['Start Year'] = df['Start Year'].astype(str)
df['Start Month'] = df['Start Month'].astype(int).astype(str)

# Guardar el dataframe actualizado de nuevo a un archivo CSV
output_file_path = '/home/diego/Downloads/DESASTRES_NATURALES/Fixed-datasetDanios_updated.csv'
df.to_csv(output_file_path, index=False, sep=';')

print("El archivo actualizado ha sido guardado como 'Fixed-datasetDanios_updated.csv'.")

