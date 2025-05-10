/**
 * Alarm Clock Application - Main JavaScript
 *
 * This file contains all the JavaScript functionality for the alarm clock web app.
 * It handles clock updates, setting alarms, and communicating with the Flask backend.
 */

// Wait until the document is fully loaded before running any code
document.addEventListener("DOMContentLoaded", function () {
  // =============== ELEMENT SELECTORS ===============
  // Get references to all the HTML elements we need to interact with
  const currentTimeElement = document.getElementById("currentTime"); // The element that displays the current time
  const timeInput = document.getElementById("timeInput"); // Input field for alarm time value
  const setButton = document.getElementById("setButton"); // Button to set the alarm
  const stopButton = document.getElementById("stopButton"); // Button to stop the alarm
  const statusElement = document.getElementById("status"); // Element to show status messages
  const countdownContainer = document.getElementById("countdownContainer"); // Container for countdown display
  const countdownElement = document.getElementById("countdown"); // Element that shows the countdown time
  const themeToggle = document.getElementById("themeToggle"); // Theme toggle button
  const themeToggleIcon = themeToggle.querySelector(".theme-toggle-icon"); // Theme toggle icon
  const themeToggleText = themeToggle.querySelector(".theme-toggle-text"); // Theme toggle text

  // =============== STATE VARIABLES ===============
  // Variables to keep track of the alarm state
  let countdownInterval = null; // Stores the interval ID for the countdown timer
  let alarmEndTime = null; // Stores when the alarm should go off
  let isDarkMode = true; // Default to dark mode

  // =============== CLOCK FUNCTIONS ===============
  /**
   * Updates the digital clock display with the current time
   */
  function updateClock() {
    // Get the current date and time
    const now = new Date();

    // Format hours, minutes, and seconds with leading zeros if needed
    const hours = String(now.getHours()).padStart(2, "0");
    const minutes = String(now.getMinutes()).padStart(2, "0");
    const seconds = String(now.getSeconds()).padStart(2, "0");

    // Update the clock display
    currentTimeElement.textContent = `${hours}:${minutes}:${seconds}`;
  }

  // Update the clock immediately and then every second
  updateClock();
  setInterval(updateClock, 1000);

  // =============== ALARM STATUS FUNCTIONS ===============
  /**
   * Checks with the server if an alarm is currently running
   * and updates the UI accordingly
   */
  function checkAlarmStatus() {
    // Make a request to the server to check alarm status
    fetch("/alarm_status")
      .then((response) => response.json())
      .then((data) => {
        if (data.running) {
          // If alarm is running, disable set button and enable stop button
          setButton.disabled = true;
          stopButton.disabled = false;
        } else {
          // If no alarm is running, enable set button and disable stop button
          setButton.disabled = false;
          stopButton.disabled = true;

          // Hide countdown if alarm is not running and no end time is set
          if (!alarmEndTime) {
            countdownContainer.classList.add("hidden");
          }
        }
      })
      .catch((error) => console.error("Error checking alarm status:", error));
  }

  // Check alarm status every 2 seconds
  setInterval(checkAlarmStatus, 2000);
  checkAlarmStatus(); // Also check immediately

  // =============== COUNTDOWN FUNCTIONS ===============
  /**
   * Updates the countdown display showing time remaining until alarm
   */
  function updateCountdown() {
    // If no alarm end time is set, don't do anything
    if (!alarmEndTime) return;

    // Calculate time remaining
    const now = new Date().getTime();
    const timeLeft = alarmEndTime - now;

    // If countdown is finished
    if (timeLeft <= 0) {
      clearInterval(countdownInterval);
      countdownElement.textContent = "00:00";
      return;
    }

    // Calculate minutes and seconds from milliseconds
    const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

    // Update the countdown display with formatted time
    countdownElement.textContent = `${String(minutes).padStart(
      2,
      "0"
    )}:${String(seconds).padStart(2, "0")}`;
  }

  // =============== EVENT HANDLERS ===============
  /**
   * Handle setting the alarm when the Set Alarm button is clicked
   */
  setButton.addEventListener("click", function () {
    // Get the time value the user entered
    const value = timeInput.value;

    // Validate the input value
    if (!value || value <= 0) {
      showStatus("Please enter a valid positive number", "error");
      return;
    }

    // Get which mode is selected (minutes or seconds)
    const mode = document.querySelector('input[name="mode"]:checked').value;

    // Send a request to the server to set the alarm
    fetch("/set_alarm", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ mode, value }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.status === "success") {
          // Show success message
          showStatus(data.message, "success");

          // Calculate when the alarm will end
          const seconds = mode === "m" ? parseInt(value) * 60 : parseInt(value);
          alarmEndTime = new Date().getTime() + seconds * 1000;

          // Show the countdown display
          countdownContainer.classList.remove("hidden");

          // Clear any existing countdown interval
          if (countdownInterval) {
            clearInterval(countdownInterval);
          }

          // Start the countdown timer
          updateCountdown();
          countdownInterval = setInterval(updateCountdown, 1000);
        } else {
          // Show error message
          showStatus(data.message, "error");
        }
      })
      .catch((error) => {
        console.error("Error setting alarm:", error);
        showStatus("An error occurred while setting the alarm", "error");
      });
  });

  /**
   * Handle stopping the alarm when the Stop Alarm button is clicked
   */
  stopButton.addEventListener("click", function () {
    // Send a request to the server to stop the alarm
    fetch("/stop_alarm", {
      method: "POST",
    })
      .then((response) => response.json())
      .then((data) => {
        // Show status message
        showStatus(
          data.message,
          data.status === "success" ? "success" : "error"
        );

        if (data.status === "success") {
          // Clear countdown timer
          if (countdownInterval) {
            clearInterval(countdownInterval);
            countdownInterval = null;
          }
          alarmEndTime = null;
        }
      })
      .catch((error) => {
        console.error("Error stopping alarm:", error);
        showStatus("An error occurred while stopping the alarm", "error");
      });
  });
  // =============== UTILITY FUNCTIONS ===============
  /**
   * Display a status message to the user
   * @param {string} message - The message to display
   * @param {string} type - The type of message ('success' or 'error')
   */
  function showStatus(message, type) {
    // Set the message text and appropriate styling class
    statusElement.textContent = message;
    statusElement.className = "status " + type;

    // Automatically clear the status message after 5 seconds
    setTimeout(() => {
      statusElement.textContent = "";
      statusElement.className = "status";
    }, 5000);
  }

  // =============== THEME FUNCTIONS ===============
  /**
   * Toggle between light and dark mode
   */
  function toggleTheme() {
    isDarkMode = !isDarkMode;

    if (isDarkMode) {
      // Switch to dark mode
      document.documentElement.classList.add("dark-mode");
      themeToggleIcon.textContent = "☀️";
      themeToggleText.textContent = "Light Mode";
    } else {
      // Switch to light mode
      document.documentElement.classList.remove("dark-mode");
      themeToggleIcon.textContent = "🌙";
      themeToggleText.textContent = "Dark Mode";
    }

    // Save user preference to local storage
    localStorage.setItem("darkMode", isDarkMode);
  }

  // Add click event listener to theme toggle button
  themeToggle.addEventListener("click", toggleTheme);

  // Initialize theme based on saved preference or default to dark mode
  if (localStorage.getItem("darkMode") === "false") {
    isDarkMode = true; // Set to true so that toggleTheme will switch to light mode
    toggleTheme();
  }
});
