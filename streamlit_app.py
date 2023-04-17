import streamlit as st
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

@st.cache_data(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

# Create a text input for filtering the data
filter_text = st.text_input("Filter", "")

sheet_url = st.secrets["private_gsheets_url"]
rows = conn.execute(f'SELECT * FROM "{sheet_url}" WHERE tag LIKE "%%{filter_text}%%" OR content LIKE "%%{filter_text}%%"', headers=1)
rows_all = rows.fetchall()

table_data = [['date', 'tag', 'content']]

for row in rows_all:
    table_data.append([row.date, row.tag, row.content])

st.table(table_data)
