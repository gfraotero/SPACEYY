from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

# Datos de 2024: meses del año y valores de los KPI
months = np.arange(1, 13).reshape(-1, 1)  # Meses de enero a diciembre
dso_2024 = np.array([32, 30, 31, 29, 28, 27, 30, 31, 33, 32, 30, 29])
dio_2024 = np.array([25, 24, 26, 27, 28, 30, 29, 30, 28, 27, 26, 25])
dpo_2024 = np.array([35, 36, 37, 38, 36, 35, 34, 33, 34, 35, 36, 37])
ccc_2024 = dso_2024 + dio_2024 - dpo_2024  # Calcular CCC

# Modelo de regresión lineal
model = LinearRegression()

# Predicciones para 2025
months_2025 = np.arange(13, 25).reshape(-1, 1)  # Meses de enero a diciembre de 2025

# Ajustar y predecir para cada KPI
predictions = {}
for kpi_name, kpi_data in zip(["DSO", "DIO", "DPO", "CCC"], [dso_2024, dio_2024, dpo_2024, ccc_2024]):
    model.fit(months, kpi_data)  # Entrenar el modelo
    predictions[kpi_name] = model.predict(months_2025)  # Predecir para 2025

# Crear un DataFrame con las predicciones
df_predictions = pd.DataFrame({
    "Month": np.arange(1, 13),
    "DSO_2025": predictions["DSO"],
    "DIO_2025": predictions["DIO"],
    "DPO_2025": predictions["DPO"],
    "CCC_2025": predictions["CCC"]
})

# Guardar en un archivo Excel
output_path_predictions = "C:/ANALYST-LABS/Working_Capital_2025_Predictions.xlsx"
df_predictions.to_excel(output_path_predictions, index=False, sheet_name="2025 Predictions")

output_path_predictions
