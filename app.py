from flask import Flask, request, render_template
app = Flask(__name__)

def workflow_calculator(num_clients, num_employees):
    time_intake = 10
    time_preparer = 60
    time_quality_review = 15

    total_time_per_client = time_intake + time_preparer + time_quality_review
    proportion_intake = time_intake / total_time_per_client
    proportion_preparer = time_preparer / total_time_per_client
    proportion_quality_review = time_quality_review / total_time_per_client

    employees_intake = int(num_employees * proportion_intake)
    employees_preparer = int(num_employees * proportion_preparer)
    employees_quality_review = int(num_employees * proportion_quality_review)

    remaining_employees = num_employees - (employees_intake + employees_preparer + employees_quality_review)
    if remaining_employees > 0:
        employees_preparer += remaining_employees

    return {
        "clients": num_clients,
        "employees": num_employees,
        "intake_specialists": employees_intake,
        "preparers": employees_preparer,
        "quality_review_specialists": employees_quality_review
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num_clients = int(request.form['clients'])
        num_employees = int(request.form['employees'])
        result = workflow_calculator(num_clients, num_employees)
        return render_template('result.html', result=result)
    except ValueError:
        return "Please enter valid numbers for clients and employees.", 400

if __name__ == '__main__':
    app.run(debug=True)
