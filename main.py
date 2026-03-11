from checker import check_website
from logger import save_log
from reporter import report
import time
import json

with open("sites.json", "r") as file:
    sites = json.load(file)

def start():
    answer = input("Would you like to begin the program? (Y/N): ")
    if answer == "Y":
        next_answer = input("This program runs every 2 minutes until it is stopped. Are you sure? (Y/N): ")
        if next_answer == "Y":
            return run_program()
        elif next_answer == "N":
            return start()
        else:
            print("Invalid input. Please enter Y or N.")
            return start()
    
    if answer == "N":
        return print("No worries, maybe next time!")

def run_program():
    try:
        while True:
            for site in sites:
                result = check_website(site)
                save_log(result)
                print(result)
            time.sleep(120)
    except KeyboardInterrupt:
        print("Program stopped. Goodbye!")

def entry_message():
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

entry_message()