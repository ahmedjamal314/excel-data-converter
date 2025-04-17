import pandas as pd

def convert_excel_to_csv(excel_file_path, csv_file_path):
    df = pd.read_excel(excel_file_path)
    df.to_csv(csv_file_path, index=False)
    print(f"✅ Excel converted to CSV successfully: {csv_file_path}")

convert_excel_to_csv(
    "C:/Users/ahmed/OneDrive/Desktop/QuickFix Vehicles Case Study Data.xlsx",
    "C:/Users/ahmed/OneDrive/Desktop/QuickFix_Vehicles.csv"
)
