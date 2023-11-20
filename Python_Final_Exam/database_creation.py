import sqlite3
def db_create():
    connection = sqlite3.connect("university_database.db")
    cursor = connection.cursor()
    connection.execute("""
    create table students
    (
        id int,
        name text,
        college_name text,
        department text,
        join_date date
    )
    """)
    connection.execute('''
    create table instructors
    (
        id int,
        name text,
        college_name text,
        department text,
        join_date date
    )
    '''
    )
    connection.execute('''
    create table employees
    (
        id int,
        name text,
        college_name text,
        department text,
        join_date date
    )
    '''
    )
    connection.commit()
    connection.close()