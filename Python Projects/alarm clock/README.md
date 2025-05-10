# Alarm Clock Web Application

This is a web-based version of the command-line alarm clock application. The application allows you to set alarms in either minutes or seconds, and plays a sound when the alarm goes off.

## Features

- Set alarms in minutes or seconds
- Real-time countdown display
- Visual alarm status indicators
- Responsive design works on desktop and mobile devices
- Volume gradually increases when alarm sounds

## How to Use

1. Run the web application:

   ```
   python app.py
   ```

2. Open a web browser and navigate to:

   ```
   http://127.0.0.1:5000/
   ```

3. Using the interface:
   - Select either "Minutes" or "Seconds" mode
   - Enter the time value (a positive number)
   - Click "Set Alarm" to start the alarm
   - Use "Stop Alarm" to cancel an active alarm

## Requirements

- Python 3.x
- Flask
- Pygame (for sound playback)
- Web browser with JavaScript enabled
- alarm.mp3 file in the same directory as app.py

## Files

- `main.py` - Original command-line alarm clock implementation
- `app.py` - Flask web application that adapts the alarm clock for web use
- `templates/index.html` - Web interface for the alarm clock
- `static/css/styles.css` - CSS styles for the web interface
- `alarm.mp3` - Sound file played when the alarm goes off

## Notes

- The alarm will play for up to 5 minutes if not stopped manually
- Volume starts low and gradually increases to maximum
- The application uses threading to allow the web interface to remain responsive while the alarm countdown is running
