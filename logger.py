import json

def load_log():
  try:
    with open("log.json", "r") as file:
      data = json.load(file) # Reads existing log data from file
      return data
  except FileNotFoundError:
    # If no log file exists yet, start with an empty list
    print("Previous data log not found. Starting from a fresh data log.")
    return []
  
def save_log(result):
  data = load_log() # Load existing log before appending
  data.append(result) # Append the new result to the existing log
  with open("log.json", "w") as file:
    json.dump(data, file, indent = 4) # Write updated log back to file