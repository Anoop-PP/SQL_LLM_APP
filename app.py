from dotenv import load_dotenv
load_dotenv()   ## Load all the environment variables

import streamlit as st
import sqlite3
import os


import google.generativeai as genai

## Configure our API Key..aistudio,google
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



#Function to load Google Gemini Model and provide sql query as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text


## Function to retrieve query from the sql database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


## Define Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query !
    The SQL database has the name  EMPLOYEE and has the following columns - NAME, DESIGNATION, LOCATION and SALARY
    For example
    Example 1 - How many entries of records are present?, the SQL command will be something like this SELECT COUNT(*) FROM EMPLOYEE;
    EXAMPLE 2 - Tell me all employees as  Data Scientist  ?, the SQL command will be something like this SELECT * FROM EMPLOYEE
    where DESIGNATION="Data Scientist";
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]


## STREAMLIT APP

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")


# If submit is clicked 
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response= read_sql_query(response,"employee.db")
    st.subheader("The Response is ")
    for row in response:
        print(row)
        st.header(row)
