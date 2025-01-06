import os
import re
from datetime import datetime
from cal import process_schedule  # Import the new function

# Define a function to test the parsing of user input
def test_process_schedule():
    test_cases = [
        {
            "input": [
                "I have a meeting on Monday at 10 AM and then a workout in the evening."
            ],
            "expected": [
                {"Task": "Meet", "Time": "10:00", "Duration": 1},
                {"Task": "Workout", "Time": "17:00", "Duration": 1}
            ]
        },
        {
            "input": [
                "Study from 9 AM to 11 AM and have tea time around 4 PM."
            ],
            "expected": [
                {"Task": "Study", "Time": "09:00", "Duration": 2},
                {"Task": "Tea", "Time": "16:00", "Duration": 1}
            ]
        },
        {
            "input": [
                "I want to go for a run in the morning and then work on my project from 1 PM to 3 PM."
            ],
            "expected": [
                {"Task": "Run", "Time": "09:00", "Duration": 1},
                {"Task": "Work", "Time": "13:00", "Duration": 2}
            ]
        },
        {
            "input": [
                "I will have lunch at noon."
            ],
            "expected": [
                {"Task": "Lunch", "Time": "12:00", "Duration": 1}
            ]
        },
        {
            "input": [
                "From 2 PM to 4 PM, I will study."
            ],
            "expected": [
                {"Task": "Study", "Time": "14:00", "Duration": 2}
            ]
        },
        {
            "input": [
                "Workout at 6 PM and then dinner at 7 PM."
            ],
            "expected": [
                {"Task": "Workout", "Time": "18:00", "Duration": 1},
                {"Task": "Dinner", "Time": "19:00", "Duration": 1}
            ]
        },
        {
            "input": [
                "I have a meeting at 15:00 and a call at 16:30."
            ],
            "expected": [
                {"Task": "Meet", "Time": "15:00", "Duration": 1},
                {"Task": "Call", "Time": "16:30", "Duration": 1}
            ]
        },
        {
            "input": [
                "I will relax in the evening."
            ],
            "expected": [
                {"Task": "Relax", "Time": "17:00", "Duration": 1}
            ]
        },
        {
            "input": [
                "I have nothing planned."
            ],
            "expected": []  # Expecting no tasks
        },
        {
            "input": [
                ""  # Empty input
            ],
            "expected": []  # Expecting no tasks
        },
        {
            "input": [
                "Invalid input without any time or task."
            ],
            "expected": []  # Expecting no tasks
        }
    ]

    for i, case in enumerate(test_cases):
        result = process_schedule(case["input"])
        assert result == case["expected"], f"Test case {i + 1} failed: {result} != {case['expected']}"
        print(f"Test case {i + 1} passed.")

# Run the tests
if __name__ == "__main__":
    test_process_schedule() 