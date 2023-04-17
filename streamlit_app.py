from google.oauth2 import service_account
from gsheetsdb import connect

# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ],
)
conn = connect(credentials=credentials) 

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
