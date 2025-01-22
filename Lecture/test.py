import subprocess
import sys
import os

def test_practice():
    # Prepare the input data for 60 students with 5 subjects each
    input_data = "\n".join([" ".join(["75", "80", "85", "90", "95"]) for _ in range(60)])

    # Run the practice.py script with the prepared input data
    result = subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), 'practice.py')],
                            input=input_data, text=True, capture_output=True)

    # Check the output
    output_lines = result.stdout.strip().split('\n')

    # Calculate expected average
    expected_average = sum([75, 80, 85, 90, 95]) / 5

    # Check the average grade
    assert output_lines[0] == f"Average Grade: {expected_average}"

    # Check the letter grade
    assert output_lines[1] == "Letter Grade: B"

# Run the test
if __name__ == "__main__":
    test_practice()
    print("All tests passed.")
