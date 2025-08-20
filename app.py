import streamlit as st
import pandas as pd
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col

# -------------------------
# Snowflake Connection
# -------------------------
connection_parameters = {
    "account": "eyvjdzp-fy53609",       # e.g. abcd-xy12345
    "user": "AbdulQavi",
    "password": "Qavi@2003_snow",
    "role": "ACCOUNTADMIN",
    "warehouse": "MY_WH",
    "database": "DUMMY_DB",
    "schema": "DUMMY_SCHEMA"
}

session = Session.builder.configs(connection_parameters).create()

# -------------------------
# Ensure table exists
# -------------------------
session.sql("""
    CREATE TABLE IF NOT EXISTS todo_list (
        id INT AUTOINCREMENT,
        task STRING,
        status STRING DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""").collect()

st.title("✅ To-Do List Manager (Snowflake + Streamlit)")

# -------------------------
# Add new task
# -------------------------
new_task = st.text_input("New Task:")
if st.button("Add Task") and new_task.strip() != "":
    session.create_dataframe(
        [[new_task, "pending"]],
        schema=["task", "status"]
    ).write.mode("append").save_as_table("todo_list", column_order="name")
    st.success(f"Task added: {new_task}")
    st.rerun()

# -------------------------
# Show Pending Tasks
# -------------------------
df = session.table("todo_list")
pending = df.filter(col("status") == "pending").to_pandas()

st.subheader("📌 Pending Tasks")
st.table(pending)

# -------------------------
# Mark tasks as done
# -------------------------
if not pending.empty:
    task_ids = pending["ID"].tolist()
    done_task = st.selectbox("Mark task as done:", task_ids)
    if st.button("Complete Task"):
        session.table("todo_list").update(
            assignments={"status": "done"},
            condition=col("id") == done_task
        )
        st.success(f"Task {done_task} marked as done!")
        st.rerun()

# -------------------------
# Show Completed Tasks
# -------------------------
completed = df.filter(col("status") == "done").to_pandas()

st.subheader("✅ Completed Tasks")
st.table(completed)
