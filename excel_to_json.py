import pandas as pd

def convert_excel_to_json(excel_file_path, json_file_path):
    df = pd.read_excel(excel_file_path)
    df.to_json(json_file_path, orient='records', indent=4)
    print(f" Excel converted to JSON successfully: {json_file_path}")

# Your file name and location
convert_excel_to_json(
    "C:/Users/ahmed/OneDrive/Desktop/QuickFix Vehicles Case Study Data.xlsx",
    "C:/Users/ahmed/OneDrive/Desktop/QuickFix_Vehicles.json"
)
