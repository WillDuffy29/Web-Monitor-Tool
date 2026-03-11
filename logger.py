import json

def load_log():
  try:
    with open("log.json", "r") as file:
      data = json.load(file)
      return data
  except FileNotFoundError:
    print("Previous data log not found. Starting from a fresh data log.")
    return []
  
def save_log(result):
  data = load_log()
  data.append(result)
  with open("log.json", "w") as file:
    json.dump(data, file, indent = 4)