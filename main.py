from checker import check_website
from logger import save_log
from reporter import report
import time
import json

# Load the list of sites to monitor from external JSON file
with open("sites.json", "r") as file:
    sites = json.load(file)

def start():
    # Ask the user if they want to begin
    answer = input("Would you like to begin the program? (Y/N): ")
    if answer == "Y":
        next_answer = input("This program runs every 2 minutes until it is stopped. Are you sure? (Y/N): ")
        if next_answer == "Y":
            return run_program()
        elif next_answer == "N":
            return start() # Return to the start prompt
        else:
            print("Invalid input. Please enter Y or N.")
            return start()
    
    if answer == "N":
        return print("No worries, maybe next time!")

def run_program():
    try:
        while True:
            for site in sites:
                result = check_website(site) # Check each site and get result
                save_log(result) # Save result to log
                print(result)
            time.sleep(120) # Wait 2 minutes before the next check
    except KeyboardInterrupt:
        # Gracefully handle CTRL+C to stop the program
        print("Program stopped. Goodbye!")

def entry_message():
    # Top level menu - choose between monitoring and reporting
    print("What would you like to do?")
    print("==========================")
    print("1. Utilise the program")
    print("2. Generate a report")
    print("==========================")
    decision = int(input("Your choice (1-2): "))
    if decision == 1:
        start()
    elif decision == 2:
        report()
    else:
        print("Invalid input. Try again.")
        entry_message()

entry_message() # Run the program