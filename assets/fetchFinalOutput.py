import pandas as pd
import requests
import os
from dotenv import load_dotenv
load_dotenv()


def fetchFinalOutput(): 
    if os.getenv('SCRIPT_ENV') == "DEV": 
        url = 'http://79.137.87.52/final_output.xlsx'
        response = requests.get(url)
        with open('final_output.xlsx', 'wb') as f:
            f.write(response.content)
    else :
        os.system('sudo scp -r /var/www/html/final_output.xlsx  /')

    # Read the Excel file using pandas
    df = pd.read_excel('final_output.xlsx', header=None, engine='openpyxl')

    # Convert DataFrame to dictionary with desired format
    key_value_dict = df.set_index(0)[1].to_dict()

    return key_value_dict