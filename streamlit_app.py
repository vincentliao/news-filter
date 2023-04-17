import gspread
from google.oauth2.service_account import Credentials
import streamlit as st


scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = Credentials.from_service_account_file('key.json', scopes=scopes)

# Authenticate with the Google Sheets API
client = gspread.authorize(creds)

# Open the Google Sheet by name
sheet_name = "俄烏戰爭表_精簡版 的副本"
sheet = client.open(sheet_name).sheet1

# Get all the values from the sheet
all_values = sheet.get_all_values()
headers = all_values[0]

# Create a text input for filtering the data
filter_text = st.text_input("Filter", "")

# Filter the data based on the filter text
filtered_values = [headers]  # start with headers
for row in all_values[1:]:
    if filter_text.lower() in " ".join(row).lower():  # case-insensitive search
        filtered_values.append(row)

# Display the values in a Streamlit table
st.table(filtered_values)
