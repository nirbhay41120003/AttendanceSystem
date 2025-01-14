from flask import Flask, jsonify, render_template
import subprocess  # This will allow you to run your Python scripts
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/capture/<name>')
def capture_image(name):
    result = subprocess.run(['python', 'capture.py', name], capture_output=True, text=True)
    return jsonify(message="Image capture complete." if result.returncode == 0 else "Image capture failed.")

@app.route('/train')
def train_model():
    result = subprocess.run(['python', 'train.py'], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    return jsonify(message="Model training complete." if result.returncode == 0 else "Model training failed.")
@app.route('/run')
def run_attendance():
    subprocess.run(['python', 'run.py'])  # Your attendance running script
    return jsonify(message="Attendance system running.")

@app.route('/attendance-log')
def check_attendance():
    attendance_log = []
    with open('attendance_log.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            attendance_log.append(row)  # Add each row to the attendance_log list
    return jsonify(log=attendance_log)  # Return the log as a JSON response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
