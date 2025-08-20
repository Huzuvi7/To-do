# To-Do List App with Snowflake

A simple Streamlit application that helps you manage your tasks using Snowflake as the database backend.

## What This App Does

- ➕ Add new tasks to your to-do list
- 📝 View all pending tasks in a clean interface
- ✅ Mark tasks as completed with one click
- 💾 Automatically saves all data in Snowflake
- 🔄 Real-time updates when you make changes

## How to Run the App Locally

1. **Install Python dependencies**
   ```bash
   pip install streamlit snowflake-snowpark-python
   ```

2. **Save the code**
   Create a file called `app.py` and paste the application code into it

3. **Configure credentials**
   Make sure you have your Snowflake account credentials ready (will be prompted when running)

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   The app will automatically open at `http://localhost:8501`

## Features

- Simple and intuitive interface
- Persistent storage in Snowflake cloud database
- Real-time task management
- No data loss between sessions
- Direct integration with Snowflake's secure platform

The app asks you for Snowflake connection details (account, username, password, warehouse, database, and schema) when first run. These credentials are used to establish a secure connection to your Snowflake instance where the tasks are stored.
