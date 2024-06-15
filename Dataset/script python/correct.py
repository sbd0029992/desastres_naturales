import pandas as pd

# Cargar el archivo CSV
file_path = '/home/diego/Downloads/DESASTRES_NATURALES/datasetDanios.csv'
data = pd.read_csv(file_path)

# Filtrar las entradas inválidas en la columna "Month"
valid_months = data['Start Month'].apply(lambda x: str(x).isdigit() and 1 <= int(x) <= 12)
data.loc[~valid_months, 'Start Month'] = '00'  # Establecer meses inválidos a '00'

# Asegurar que todos los valores de los meses tengan dos caracteres
data['Start Month'] = data['Start Month'].apply(lambda x: str(x).zfill(2))

# Guardar el dataframe corregido en un nuevo archivo CSV
corrected_file_path = '/home/diego/Downloads/DESASTRES_NATURALES/correct-datasetDanios.csv'
data.to_csv(corrected_file_path, index=False)

