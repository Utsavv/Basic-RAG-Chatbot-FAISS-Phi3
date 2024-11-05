import os
import csv
import pdfplumber

# Path to the folder containing PDF files
folder_path = "./ChatWithSwiggy/Orders"

# Get a list of all PDF files in the folder
pdf_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.pdf')]

for pdf_path in pdf_files:
    # Define the CSV file path for each PDF
    csv_file_path = pdf_path.replace('.pdf', '.csv')

    # Open the CSV file in write mode
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Open each PDF file
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    for row in table:
                        # Write the extracted table rows to the CSV file
                        csv_writer.writerow(row)

    print(f"CSV file created for {pdf_path}: {csv_file_path}")