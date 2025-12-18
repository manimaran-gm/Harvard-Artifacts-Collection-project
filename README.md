# 🏛️ Harvard’s Artifacts Collection
## ETL, SQL Analytics & Streamlit Application

---

## 📌 Project Overview
This project is an end-to-end ETL and data analytics application built using the Harvard Art Museums public API.
It enables users to dynamically collect museum artifact data, store it in a MySQL (TiDB Cloud) database, and explore the data using SQL queries through an interactive Streamlit dashboard.

---

## 🎯 Objectives
- Build a complete ETL pipeline using real-world API data
- Store structured cultural heritage data in a relational database
- Enable SQL-based analysis and exploration through a web interface

---

## 🛠️ Technologies Used
- Python
- Streamlit
- SQLAlchemy
- MySQL (TiDB Cloud)
- Harvard Art Museums API
- Pandas

---

## 🗂️ Project Architecture
```

Streamlit UI
↓
Harvard Art Museums API
↓
ETL (Extract → Transform → Load)
↓
TiDB Cloud (MySQL Database)
↓
SQL Analytics

````

---

## 🗄️ Database Design

### artifact_metadata
Stores general information about each artifact such as title, culture, period, century, classification, and acquisition details.

### artifact_media
Stores media-related information including image count, media count, and creation dates.

### artifact_colors
Stores aggregated color and hue information extracted from artifact images (one row per artifact).

---

## 🔄 ETL Workflow
- **Extraction:** Fetches 2500 artifacts per user-selected classification from the API
- **Transformation:** Cleans JSON data, handles null values, and normalizes nested structures
- **Load:** Inserts data into MySQL using SQLAlchemy with duplicate prevention

  ---

## 🔍 SQL Analytics
- 20 predefined analytical queries
- 5+ custom queries
- Join-based analysis across tables
- All queries are executable directly from the Streamlit UI

---

## 🖥️ Streamlit Application Features
- Classification-based data collection
- Live API data preview
- One-click database insertion
- Interactive SQL query execution
- Tabular result display

---

## 🚀 How to Run the Project

## 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
````

### 2️⃣ Configure Credentials

Create a `config.py` file:

```python
HARVARD_API_KEY = "your_api_key_here"
DATABASE_URL = "your_tidb_cloud_sqlalchemy_url"
```

### 3️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 📊 Expected Outcome

* Structured artifact data stored in a cloud database
* Ready-to-query SQL analytics environment
* Interactive dashboard for data exploration

---

## 👤 Author

**manimaran** - manivsmaran@gmail.com
