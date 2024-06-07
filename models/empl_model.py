import snowflake.connector
from flask import current_app

def get_db_connection():
    return snowflake.connector.connect(
        user=current_app.config['SNOWFLAKE_USER'],
        password=current_app.config['SNOWFLAKE_PASSWORD'],
        account=current_app.config['SNOWFLAKE_ACCOUNT'],
        database=current_app.config['SNOWFLAKE_DATABASE'],
        schema=current_app.config['SNOWFLAKE_SCHEMA']
    )

class Employee:

    @staticmethod
    def add_employee(data):
        query = (
            "INSERT INTO EMPLOYEE (name, position, contact_info, employee_id, salary) "
            "VALUES (%s, %s, %s, %s, %s)"
        )
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, (data['name'], data['position'], data['contact_info'], data['employee_id'], data['salary']))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_all_employees():
        query = "SELECT * FROM EMPLOYEE"
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            print(rows)
            print("Rows fetched from database:", rows)  # Debug statement
            employees = [
                {
                    "id": row[0],
                    "name": row[1],
                    "position": row[2],
                    "contact_info": row[3],
                    "employee_id": row[4],
                    "salary": row[5]
                }
                for row in list(rows)
            ]
            return employees
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_employee_by_id(emp_id):
        query = "SELECT id, name, position, contact_info, employee_id, salary FROM EMPLOYEE WHERE employee_id = %s"
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, (emp_id,))
            row = cursor.fetchone()
            if row:
                return {
                    "id": row[0],
                    "name": row[1],
                    "position": row[2],
                    "contact_info": row[3],
                    "employee_id": row[4],
                    "salary": row[5]
                }
            return None
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def update_employee(emp_id, data):
        query = (
            "UPDATE EMPLOYEE SET name = %s, position = %s, contact_info = %s, salary = %s "
            "WHERE employee_id = %s"
        )
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, (data['name'], data['position'], data['contact_info'], data['salary'], emp_id))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete_employee(emp_id):
        query = "DELETE FROM EMPLOYEE WHERE employee_id = %s"
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, (emp_id,))
            conn.commit()
        finally:
            cursor.close()
            conn.close()
