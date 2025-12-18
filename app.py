# app.py

import streamlit as st
import pandas as pd
from sqlalchemy import text

from api_client import fetch_artifacts_by_classification, CLASSIFICATIONS
from transformer import transform_artifacts
from loader import load_data
from schema import create_tables
from connection import get_engine
from sql_queries import SQL_QUERIES

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(page_title="Harvard Artifacts Collection", layout="wide")

st.title("🏛️ Harvard’s Artifacts Collection")
st.write("""
This Streamlit application allows you to:
- Collect artifact data from the Harvard Art Museums API
- Store the data in TiDB Cloud (MySQL)
- Run analytical SQL queries on the collected data
""")

# -------------------------------------------------
# Initialize Database Tables
# -------------------------------------------------
create_tables()

# -------------------------------------------------
# Session State
# -------------------------------------------------
if "raw_data" not in st.session_state:
    st.session_state.raw_data = None

if "selected_classification" not in st.session_state:
    st.session_state.selected_classification = None

# -------------------------------------------------
# Classification Selection
# -------------------------------------------------
st.subheader("📂 Select Classification")

selected_classification = st.selectbox(
    "Choose a classification",
    CLASSIFICATIONS
)

st.session_state.selected_classification = selected_classification

# -------------------------------------------------
# Collect Data
# -------------------------------------------------
if st.button("📥 Collect Data from API"):
    with st.spinner("Fetching data from Harvard API..."):
        raw_data = fetch_artifacts_by_classification(selected_classification)
        st.session_state.raw_data = raw_data

    st.success(f"Collected {len(raw_data)} records for '{selected_classification}'")

# -------------------------------------------------
# Show Sample Data
# -------------------------------------------------
if st.button("👀 Show Sample Data"):
    if st.session_state.raw_data:
        df = pd.json_normalize(st.session_state.raw_data[:20])
        st.dataframe(df)
    else:
        st.warning("No data collected yet.")

# -------------------------------------------------
# Insert into SQL
# -------------------------------------------------
if st.button("🗄️ Insert into SQL"):
    if st.session_state.raw_data:
        with st.spinner("Transforming and inserting data into database..."):
            meta, media, colors = transform_artifacts(
                st.session_state.raw_data,
                st.session_state.selected_classification
            )
            inserted_count = load_data(meta, media, colors)

        st.success(f"Inserted {inserted_count} new artifacts into the database.")
    else:
        st.warning("Please collect data before inserting into SQL.")

# -------------------------------------------------
# SQL Query Section
# -------------------------------------------------
st.divider()
st.subheader("🔍 SQL Queries & Analysis")

query_name = st.selectbox(
    "Select a query to run",
    list(SQL_QUERIES.keys())
)

if st.button("▶️ Run Query"):
    engine = get_engine()
    query = SQL_QUERIES[query_name]

    with engine.connect() as connection:
        result = connection.execute(query)
        df = pd.DataFrame(result.fetchall(), columns=result.keys())

    st.dataframe(df)
