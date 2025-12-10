import streamlit as st
import requests
import pandas as pd
from io import StringIO
import json


#FastAPI backend URL
FASTAPI_URL = "http://127.0.0.1:8000"

#Streamlit UI Configuration
st.set_page_config(page_title="AI-Powered Data Cleaning", layout="wide")


#Sidebar - Data Source Selection
st.sidebar.title("Data Source Selection")
data_source = st.sidebar.radio("Choose Data Source", (" CSV/Excel", "Database", "API"))


#Main Title
st.markdown("# AI-Powered Data Cleaning Application")

#Handling CSV/Excel Upload
if data_source == " CSV/Excel":
    st.subheader("Upload File for cleaning")
    uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=['csv', 'xlsx'])

    if uploaded_file is not None:
        file_extension = uploaded_file.name.split('.')[-1]
        if file_extension == "csv":
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.write("### Original Data")
        st.dataframe(df)

        if st.button("Clean Data"):
            files = {'file': (uploaded_file.name, uploaded_file.getvalue())}
            response = requests.post(f"{FASTAPI_URL}/clean-data/", files=files)

            if response.status_code == 200:
                st.subheader("Raw API Response(Debugging)")
                st.json(response.json())

                #parse cleaned data properly
                try:
                    cleaned_data_raw = response.json().get("cleaned_data")
                    if isinstance(cleaned_data_raw, str):
                        cleaned_data = pd.DataFrame(json.loads(cleaned_data_raw))
                    else:
                        cleaned_data = pd.DataFrame(cleaned_data_raw)

                        st.subheader("Cleaned Data")
                        st.dataframe(cleaned_data)
                except Exception as e:
                    st.error(f"Error parsing cleaned data: {e}")
            else:
                st.error(f"Error from backend")

#Handling Database Input
elif data_source == "Database":
    st.subheader("Database Connection Details")
    db_url = st.text_input("Enter Database URL", "postgresql://user:password@localhost:5432/dbname")
    query = st.text_area("Enter SQL Query", "SELECT * FROM table_name;")

    if st.button("Clean Data from Database"):
        response = requests.post(f"{FASTAPI_URL}/clean-db/", json={"db_url": db_url, "query": query})

        if response.status_code == 200:
            st.subheader("Raw API Response(Debugging)")
            st.json(response.json())

            #parse cleaned data properly
            try:
                cleaned_data_raw = response.json().get("cleaned_data")
                if isinstance(cleaned_data_raw, str):
                    cleaned_data = pd.DataFrame(json.loads(cleaned_data_raw))
                else:
                    cleaned_data = pd.DataFrame(cleaned_data_raw)

                    st.subheader("Cleaned Data")
                    st.dataframe(cleaned_data)
            except Exception as e:
                st.error(f"Error parsing cleaned data: {e}")
        else:
            st.error(f"Error from backend:")

#Handling API Input
elif data_source == "API":
    st.subheader("API Endpoint Details")
    api_url = st.text_input("Enter API URL", "https://jsonplaceholder.typicode.com/posts")

    if st.button("Clean Data from API"):
        response = requests.post(f"{FASTAPI_URL}/clean-api/", json={"api_url": api_url})

        if response.status_code == 200:
            st.subheader("Raw API Response(Debugging)")
            st.json(response.json())

            #parse cleaned data properly
            try:
                cleaned_data_raw = response.json().get("cleaned_data")
                if isinstance(cleaned_data_raw, str):
                    cleaned_data = pd.DataFrame(json.loads(cleaned_data_raw))
                else:
                    cleaned_data = pd.DataFrame(cleaned_data_raw)

                    st.subheader("Cleaned Data")
                    st.dataframe(cleaned_data)
            except Exception as e:
                st.error(f"Error parsing cleaned data: {e}")
        else:
            st.error(f"Error from backend: {response.text}")

#Footer
st.markdown("---")
st.markdown("Developed by AI Data Cleaning Team")