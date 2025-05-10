from pygame import mixer
import time

def alarm(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"Alarm will go off in {minutes_left:02d}:{seconds_left:02d}", end="\r")
    print("Time's up! Alarm ringing...")

    mixer.init()
    try:
        mixer.music.load("alarm.mp3")
        mixer.music.play()

        # Start with low volume and gradually increase
        volume = 0.1
        mixer.music.set_volume(volume)

        # Increase volume in a separate thread to not block the main thread
        start_time = time.time()
        while mixer.music.get_busy() and volume < 1.0:
            volume = min(volume + 0.01, 1.0)  # Increase volume gradually
            mixer.music.set_volume(volume)
            time.sleep(0.1)  # Adjust speed of volume increase

        while mixer.music.get_busy():
            time.sleep(1)
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
