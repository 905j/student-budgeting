import os
import json
import sqlite3
from chatgpt_api import get_budget_advice
from bank_inputs import get_user_input

def create_db_and_table(username, budget_data):
    db = "student_budgeting.db"
    # making connection and cursor for sqlite integration
    connection = sqlite3.connect(db)
    cursor = connection.cursor()

    username = username.replace(' ', '_')
    table_name = f"{username}s_budgeting_plan"

    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        category TEXT PRIMARY KEY,
        amount INTEGER
    )""")

    #inserting budget_data from api into the table_name
    for category, amount in budget_data.items():
        cursor.execute(f"""
            INSERT OR REPLACE INTO {table_name} (category, amount)
            VALUES (?, ?)
        """, (category, amount))

    
    # Commit the changes and close the connection
    connection.commit()
    connection.close()
    print(f"Great! Data has been inserted into table {table_name} in {db} database.")

student_info = get_user_input()
budget_advice = get_budget_advice(student_info)
budget_data = json.loads(budget_advice)
create_db_and_table(student_info["name"], budget_data)
