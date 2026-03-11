import json

def report():
    # Load all entries from the log file
    with open("log.json", "r") as file:
        log = json.load(file)
    
    # Group log entries by URL into a dictionary
    sites = {}
    for entry in log:
        if entry["url"] not in sites:
            sites[entry["url"]] = [] # Create a new list for this URL if not seen before
        sites[entry["url"]].append(entry)

    # Calculate statistics for each site
    results = {}
    for site in sites:
        entries = sites[site]
        total = len(entries) # Total number of checks for this site
        
        # Count online entries
        online_entries = []
        for e in entries:
            if e["status"] == "Online":
                online_entries.append(e)
        
        online = len(online_entries)
        offline = total - online # Offline count derived from total minus online

        # Collect valid response times, excluding None values from unreachable sites
        times = []
        for e in entries:
            if e["response_time_ms"] is not None:
                times.append(e["response_time_ms"])
        
        # Calculate average, best and worst response times
        if times:
            average_time = sum(times) / len(times)
        else:
            average_time = None
        
        best_time = min(times) if times else None
        worst_time = max(times) if times else None

        # Store calculated stats for this site
        results[site] = {
            "total": total,
            "online": online,
            "offline": offline,
            "average_time": average_time,
            "best_time": best_time,
            "worst_time": worst_time
        }

    # Display interactive menu
    print("What would you like to see?")
    print("===========================")
    print("1. Total Entries")
    print("2. Online Entries")
    print("3. Offline Entries")
    print("4. Average response time")
    print("5. Best response time")
    print("6. Worst response time")
    print("===========================")

    answer = int(input("Your selection (1-6): "))

    if answer == 1:
        for site in results:
            print(f"{site} | Total entries: {results[site]['total']}")
        response = input("Would you like more information? (Y/N)): ")
        if response == "Y":
            report() # Restart the report menu
        else:
            print("Have a great day!")
            return
    elif answer == 2:
        for site in results:
            print(f"{site} | Online entries: {results[site]['online']}")
        response = input("Would you like more information? (Y/N)): ")
        if response == "Y":
            report()
        else:
            print("Have a great day!")
            return
    elif answer == 3:
        for site in results:
            print(f"{site} | Offline entries: {results[site]['offline']}")
        response = input("Would you like more information? (Y/N)): ")
        if response == "Y":
            report()
        else:
            print("Have a great day!")
            return
    elif answer == 4:
        for site in results:
            print(f"{site} | Average response time: {results[site]['average_time']}ms")
        response = input("Would you like more information? (Y/N)): ")
        if response == "Y":
            report()
        else:
            print("Have a great day!")
            return
    elif answer == 5:
        for site in results:
            print(f"{site} | Best response time: {results[site]['best_time']}ms")
        response = input("Would you like more information? (Y/N)): ")
        if response == "Y":
            report()
        else:
            print("Have a great day!")
            return
    elif answer == 6:
        for site in results:
            print(f"{site} | Worst response time: {results[site]['worst_time']}ms")
        response = input("Would you like more information? (Y/N)): ")
        if response == "Y":
            report()
        else:
            print("Have a great day!")
            return
    else:
        print("Invalid input. Please try again.")
        report()