# Automated Testing and Fixing System for Python Code

## Project Overview

This project provides an Automated Testing and Fixing System for Python code, designed to streamline the process of scheduling tasks and running tests. The main components of this project are `cal.py`, which handles user input and task scheduling, and `test_cal.py`, which contains automated tests to ensure the functionality of the scheduling system.

## Key Components

### 1. `cal.py`

`cal.py` is the main program that allows users to input their schedules in natural language. It parses the input to extract tasks, times, and durations, and can also run interactively to gather user input.

#### Features:
- **Natural Language Processing**: Utilizes the spaCy library to parse user input.
- **Task Parsing**: Extracts tasks, times, and durations from user input.
- **Interactive Mode**: Allows users to input their schedule and add multiple tasks.

#### How to Run `cal.py`:
1. Ensure you have the required dependencies installed (see Installation section).
2. Run the program using the following command:
   ```bash
   python cal.py
   ```
3. Follow the prompts to describe your schedule for the week.

### 2. `test_cal.py`

`test_cal.py` contains automated tests for the functionality of `cal.py`. It verifies that the task parsing and scheduling work as expected by running a series of predefined test cases.

#### Features:
- **Automated Testing**: Tests various scenarios to ensure the correctness of the task parsing logic.
- **Error Reporting**: Provides detailed output on which test cases passed or failed.

#### How to Run `test_cal.py`:
1. Ensure you have the required dependencies installed (see Installation section).
2. Run the test script using the following command:
   ```bash
   python test_cal.py
   ```
3. Review the output to see the results of the test cases.

## Installation

To get started with this project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/lacebx/scheduler.git
   cd scheduler
   ```

2. **Install dependencies**:
   Make sure you have Python installed. You can create a virtual environment and install the required packages:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

## Future Improvements

While the current implementation provides a solid foundation for task scheduling and testing, there is potential for further development. One idea is to create a more advanced automated testing and fixing system that can analyze errors, suggest fixes, and apply them automatically until all tests pass successfully. This would significantly enhance the debugging process and improve code quality. You can find more info on this in the `Automated Testing and Fixing System for cal.md` located in improvements folder

## Contributing 

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the open-source community for their contributions and support.
- Special thanks to the developers of spaCy and icalendar for their excellent libraries.
