from read import read
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

pdf_file = os.getenv("PDF_FILE_PATH")
csv_path = os.getenv("CSV_FILE_PATH")

if __name__ == '__main__':
    table = read(pdf_file, 3, 10)
    df = pd.concat(table)
    df.to_csv(csv_path, index=False)