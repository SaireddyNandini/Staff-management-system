from flask import Flask, request, jsonify
from config import Config
from models.empl_model import Employee
from models.shift_model import Shift




app = Flask(__name__)
app.config.from_object(Config)
Config.print_env_variables()

@app.route('/add_employee', methods=['POST'])
def add_employee():
    if request.method == 'POST':
        try:
            employee_data = request.json
            if not employee_data:
                return jsonify({"error": "No input data provided"}), 400

            required_fields = ['name', 'position', 'contact_info', 'employee_id', 'salary']
            if not all(field in employee_data for field in required_fields):
                return jsonify({"error": "Missing required fields"}), 400

            Employee.add_employee(employee_data)
            return jsonify({"message": "Employee added successfully"}), 201

        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    else : return jsonify({"error": "Method Not Allowed"}),405

@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.get_all_employees()
    return jsonify(employees), 200

@app.route('/employee/<string:emp_id>', methods=['GET'])
def get_employee(emp_id):
    employee = Employee.get_employee_by_id(emp_id)
    if employee:
        return jsonify(employee), 200
    return jsonify({"error": "Employee not found"}), 404

@app.route('/update_employee/<string:emp_id>', methods=['PUT'])
def update_employee(emp_id):
    try:
        employee_data = request.json
        Employee.update_employee(emp_id, employee_data)
        return jsonify({"message": "Employee updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/delete_employee/<string:emp_id>', methods=['DELETE'])
def delete_employee(emp_id):
    try:
        Employee.delete_employee(emp_id)
        return jsonify({"message": "Employee deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/add_shift', methods=['POST'])
def add_shift():
    shift_data = request.json
    Shift.add_shift(shift_data)
    return jsonify({"message": "Shift added successfully"})

@app.route('/shifts/<employee_id>', methods=['GET'])
def get_shifts(employee_id):
    shifts = Shift.get_shifts_by_employee(employee_id)
    return jsonify(shifts)

@app.route('/update_shift/<shift_id>', methods=['PUT'])
def update_shift(shift_id):
    shift_data = request.json
    Shift.update_shift(shift_id, shift_data)
    return jsonify({"message": "Shift updated successfully"})

@app.route('/delete_shift/<shift_id>', methods=['DELETE'])
def delete_shift(shift_id):
    Shift.delete_shift(shift_id)
    return jsonify({"message": "Shift deleted successfully"})
if __name__ == '__main__':
    app.run(debug=True)
