import pandas as pd
import json


def read_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        print("CSV file loaded successfully!")
        return df
    except FileNotFoundError:
        print("Error: File not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: File not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}")
