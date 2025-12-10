from data_ingestion import DataIngestion
from data_cleaning import DataCleaning
from scripts.ai_agent import AIAgent


# Database Configuration

DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "demodb"

DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


#Initialize Components
ingeston = DataIngestion(DB_URL)
cleaner = DataCleaning()
ai_agent = AIAgent()


# Load and clean CSV Data
df_csv = ingeston.load_csv("sample_data.csv")
if df_csv is not None:
    print("Original CSV Data:")
    df_csv = cleaner.clean_data(df_csv)
    df_csv = ai_agent.process_data(df_csv)
    print("\n AI-Cleaned CSV Data:", df_csv)


# Load and clean Excel Data
df_excel = ingeston.load_excel("sample_data1.xlsx")
if df_excel is not None:
    print("Original Excel Data:")
    df_excel = cleaner.clean_data(df_excel)
    df_excel = ai_agent.process_data(df_excel)
    print("\n AI-Cleaned Excel Data:", df_excel)


# Load and clean Data from Database
df_db = ingeston.load_from_database("SELECT * FROM raw_data;")
if df_db is not None:
    print("Original Database Data:")
    df_db = cleaner.clean_data(df_db)
    df_db = ai_agent.process_data(df_db)
    print("\n AI-Cleaned Database Data:", df_db)

# Fetch and clean Data from API
API_URL = "https://jsonplaceholder.typicode.com/posts"
df_api = ingeston.fetch_from_api(API_URL)



if df_api is not None:
        print("Original API Data:")

        df_api = df_api.head(30)

        if "body" in df_api.columns:
            df_api["body"] = df_api["body"].apply(lambda x: x[:100] + "..." if isinstance(x, str) else x)

            df_api = cleaner.clean_data(df_api)
            df_api = ai_agent.process_data(df_api)
            
            print("\n AI-Cleaned API Data:", df_api)