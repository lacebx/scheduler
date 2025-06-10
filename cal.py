import spacy  
from datetime import datetime, timedelta
from icalendar import Calendar, Event
import re

# Load the NLP model
nlp = spacy.load("en_core_web_sm")

# Function to parse user input
def parse_user_input(user_input):
    doc = nlp(user_input)
    tasks = []
    
    # Regex patterns for time extraction
    time_pattern = r'(\d{1,2}:\d{2}|\d{1,2} (?:AM|PM|am|pm)|\b(?:morning|afternoon|evening|night)\b|\bfrom \d{1,2} (?:AM|PM|am|pm) to \d{1,2} (?:AM|PM|am|pm)\b)'
    duration_pattern = r'(\d+)\s*(?:hour|hours|hr|hrs|minute|minutes|min|mins)?'
    
    # Extract sentences and analyze them
    for sent in doc.sents:
        task_text = sent.text
        
        # Extract time
        time_matches = re.findall(time_pattern, task_text)
        duration_matches = re.findall(duration_pattern, task_text)
        
        # Extract task name using dependency parsing
        task_name = None
        for token in sent:
            if token.dep_ in ("ROOT", "dobj"):  # Look for main verbs or direct objects
                task_name = token.lemma_  # Use the base form of the verb as the task name
                break
        
        # Default values
        task_time = time_matches[0] if time_matches else "09:00"  # Default time if none found
        task_duration = int(duration_matches[0]) if duration_matches else 1  # Default duration if none found
        
        # Convert time to 24-hour format if necessary
        if 'AM' in task_time or 'PM' in task_time:
            task_time = datetime.strptime(task_time, '%I %p').strftime('%H:%M')
        elif task_time.lower() == 'morning':
            task_time = '09:00'
        elif task_time.lower() == 'afternoon':
            task_time = '14:00'
        elif task_time.lower() == 'evening':
            task_time = '17:00'
        elif task_time.lower() == 'night':
            task_time = '20:00'
        
        # Handle time ranges (e.g., "from 11 AM to 1 PM")
        if "from" in task_text and "to" in task_text:
            time_range = re.search(r'from (\d{1,2} (?:AM|PM|am|pm)) to (\d{1,2} (?:AM|PM|am|pm))', task_text)
            if time_range:
                start_time = datetime.strptime(time_range.group(1), '%I %p')
                end_time = datetime.strptime(time_range.group(2), '%I %p')
                task_time = start_time.strftime('%H:%M')
                task_duration = (end_time - start_time).seconds // 3600  # Duration in hours
        
        # Create a task entry
        if task_name:  # Only add if a task name was found
            tasks.append({"Task": task_name.capitalize(), "Time": task_time, "Duration": task_duration})

    return tasks

# New function for automated testing
def process_schedule(inputs):
    all_tasks = []  # Initialize all_tasks here
    for user_input in inputs:
        tasks = parse_user_input(user_input)
        all_tasks.extend(tasks)  # Add the new tasks to the overall list
    return all_tasks

# Function for interactive use
def interactive_schedule():
    all_tasks = []
    while True:
        user_input = input("Please describe your schedule for the week: ")
        tasks = parse_user_input(user_input)
        all_tasks.extend(tasks)  # Add the new tasks to the overall list

        more_tasks = input("Would you like to add anything else? (yes/no): ").strip().lower()
        if more_tasks not in ['yes', 'y']:
            break

    # Here you can add code to save the calendar to a file if needed
    return all_tasks

# Main program loop (for interactive use)
if __name__ == "__main__":
    interactive_schedule()
