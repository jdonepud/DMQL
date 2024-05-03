import streamlit as st
import psycopg2
import pandas as pd

# Database connection parameters
DB_HOST = "127.0.0.1"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "admin123"

def get_connection():
    return psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

def run_query(query):
    with get_connection() as conn:
        return pd.read_sql_query(query, conn)

def main():
    st.title('SQL Query Interface')

    # Text area for user to enter SQL query
    query = st.text_area("Enter your SQL query here:", height=150)
    
    if st.button("Execute"):
        if query:
            try:
                result = run_query(query)
                st.write(result)
            except Exception as e:
                st.error(f"Error running query: {str(e)}")
        else:
            st.error("Please enter a SQL query to execute.")

if __name__ == "__main__":
    main()
