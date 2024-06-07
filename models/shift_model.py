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

    # Existing Employee methods...

class Shift:

    @staticmethod
    def add_shift(data):
        query = (
            "INSERT INTO SHIFTS (employee_id, start_time, end_time) "
            "VALUES (%s, %s, %s)"
        )
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, (data['employee_id'], data['start_time'], data['end_time']))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_shifts_by_employee(employee_id):
        query = "SELECT shift_id, employee_id, start_time, end_time FROM SHIFTS WHERE employee_id = %s"
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, (employee_id,))
            rows = cursor.fetchall()
            shifts = [
                {
                    "shift_id": row[0],
                    "employee_id": row[1],
                    "start_time": row[2],
                    "end_time": row[3]
                }
                for row in rows
            ]
            return shifts
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def update_shift(shift_id, data):
        query = (
            "UPDATE SHIFTS SET start_time = %s, end_time = %s "
            "WHERE shift_id = %s"
        )
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, (data['start_time'], data['end_time'], shift_id))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete_shift(shift_id):
        query = "DELETE FROM SHIFTS WHERE shift_id = %s"
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, (shift_id,))
            conn.commit()
        finally:
            cursor.close()
            conn.close()
