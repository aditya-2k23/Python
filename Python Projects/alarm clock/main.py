from pygame import mixer
import time
import msvcrt  # For Windows keyboard input

def check_for_keypress():
    while True:
        if msvcrt.kbhit():  # Check if a key has been pressed
            return True
        time.sleep(0.1)

def alarm(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"Alarm will go off in {minutes_left:02d}:{seconds_left:02d}", end="\r")
    print("Time's up! Alarm ringing... (Press any key to stop)")

    mixer.init()
    try:
        mixer.music.load("alarm.mp3")
        mixer.music.play(-1)  # Play in a loop until stopped

        # Start with low volume and gradually increase
        volume = 0.1
        mixer.music.set_volume(volume)

        # Calculate the end time (5 minutes from now)
        alarm_end_time = time.time() + 300  # 5 minutes = 300 seconds

        # Increase volume until max
        while mixer.music.get_busy() and volume < 1.0:
            if msvcrt.kbhit():
                msvcrt.getch()  # Clear the key buffer
                break
            volume = min(volume + 0.01, 1.0)  # Increase volume gradually
            mixer.music.set_volume(volume)
            time.sleep(0.1)  # Adjust speed of volume increase

        # Keep alarm running for at least 5 minutes or until key press
        while mixer.music.get_busy() and time.time() < alarm_end_time:
            if msvcrt.kbhit():
                msvcrt.getch()  # Clear the key buffer
                break
            time.sleep(0.1)

        # Stop the music if it's still playing
        if mixer.music.get_busy():
            mixer.music.stop()
            print("Alarm stopped.")
    except FileNotFoundError:
        print("Error: alarm.mp3 file not found. Please make sure the file exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

while True:
    choice = input("You want to set an alarm in minutes? or seconds? (m/s): ")

    if choice == 'm':
        try:
            minutes = int(input("Enter the number of minutes: "))
            seconds = minutes * 60
            alarm(seconds)
            break
        except ValueError:
            print("Please enter a valid number for minutes.")
    elif choice == 's':
        try:
            seconds = int(input("Enter the number of seconds: "))
            alarm(seconds)
            break
        except ValueError:
            print("Please enter a valid number for seconds.")
    else:
        print("Invalid choice. Please enter 'm' for minutes or 's' for seconds.")
        print("Try again!")
