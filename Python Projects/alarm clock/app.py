from flask import Flask, render_template, request, jsonify
import threading
import time
import os
from pygame import mixer

app = Flask(__name__)
alarm_thread = None
alarm_running = False
stop_alarm = False

# Initialize mixer
mixer.init()

def run_alarm(seconds):
    global alarm_running, stop_alarm

    time_elapsed = 0
    alarm_running = True
    stop_alarm = False

    while time_elapsed < seconds and not stop_alarm:
        time.sleep(1)
        time_elapsed += 1

        # We don't need to print to console in web app

    if not stop_alarm:  # If alarm wasn't stopped manually
        play_alarm_sound()

def play_alarm_sound():
    global stop_alarm, alarm_running

    try:
        mixer.music.load("alarm.mp3")
        mixer.music.play(-1)  # Play in a loop until stopped

        # Start with low volume and gradually increase
        volume = 0.1
        mixer.music.set_volume(volume)

        # Calculate the end time (5 minutes from now)
        alarm_end_time = time.time() + 300  # 5 minutes = 300 seconds

        # Increase volume until max
        while mixer.music.get_busy() and volume < 1.0 and not stop_alarm:
            volume = min(volume + 0.01, 1.0)  # Increase volume gradually
            mixer.music.set_volume(volume)
            time.sleep(0.1)  # Adjust speed of volume increase

        # Keep alarm running for at least 5 minutes or until stopped
        while mixer.music.get_busy() and time.time() < alarm_end_time and not stop_alarm:
            time.sleep(0.1)

        # Stop the music if it's still playing
        if mixer.music.get_busy():
            mixer.music.stop()
    except FileNotFoundError:
        print("Error: alarm.mp3 file not found. Please make sure the file exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

    alarm_running = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_alarm', methods=['POST'])
def set_alarm():
    global alarm_thread, alarm_running, stop_alarm

    if alarm_running:
        return jsonify({"status": "error", "message": "An alarm is already running"})

    data = request.get_json()
    mode = data.get('mode')
    value = data.get('value')

    try:
        value = int(value)
        if value <= 0:
            return jsonify({"status": "error", "message": "Please enter a positive number"})

        seconds = value * 60 if mode == 'm' else value

        alarm_thread = threading.Thread(target=run_alarm, args=(seconds,))
        alarm_thread.daemon = True
        alarm_thread.start()

        return jsonify({"status": "success", "message": f"Alarm set for {value} {'minutes' if mode == 'm' else 'seconds'}"})
    except ValueError:
        return jsonify({"status": "error", "message": "Please enter a valid number"})

@app.route('/stop_alarm', methods=['POST'])
def stop_alarm_route():
    global stop_alarm, alarm_running

    if alarm_running:
        stop_alarm = True
        if mixer.music.get_busy():
            mixer.music.stop()
        return jsonify({"status": "success", "message": "Alarm stopped"})
    else:
        return jsonify({"status": "error", "message": "No alarm is currently running"})

@app.route('/alarm_status', methods=['GET'])
def alarm_status():
    global alarm_running
    return jsonify({"running": alarm_running})

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    if not os.path.exists('templates'):
        os.makedirs('templates')

    app.run(debug=True)
