# Python Website Monitor
A Python automation tool that monitors website uptime, logs response times, 
and generates interactive summary reports. Built independently as a 
self-directed project to demonstrate real-world Python and IT automation skills.

## File Structure
- **checker.py** — Sends HTTP requests to each URL and returns a result dictionary containing the site status, status code, response time and timestamp.
- **logger.py** — Handles all data persistence. Loads the existing log from log.json and appends each new result, saving it back after every check.
- **reporter.py** — Reads the log and presents an interactive menu allowing the user to query total checks, online/offline counts, and response times per site.
- **main.py** — Entry point for the program. Loads sites from sites.json and provides a top-level menu to either run the monitor or generate a report.
- **sites.json** — A JSON list of URLs to monitor. Add or remove sites here without touching any code.
- **log.json** — Stores all check results. Starts empty and builds over time.

## Setup & Installation
1. Clone the repository
2. Install the required dependency: pip3 install requests
3. Add the URLs you want to monitor to sites.json (some are pre-installed, feel free to remove)
4. Run the program: python3 main.py

## Concepts Demonstrated
- Modular program structure across multiple files
- HTTP requests and status code handling
- JSON data persistence and file I/O
- Exception handling for network errors and missing files
- Automation with timed loop execution
- Interactive CLI menus with input validation

## Known Limitations
- Some sites return a 403 Forbidden status code when requests come from a Python script rather than a browser. The server is reachable but blocks automated requests. These sites are incorrectly marked as Offline as a result.
- The reporter generates statistics across all available log data rather than filtering to a specific time window.

## Future Improvements
- Add a User-Agent header to checker.py to avoid 403 responses from sites that block automated requests
- Add a 24 hour time filter to the reporter for true daily summaries
- Email alerts when a site goes offline
- Export reports to a .txt or .csv file
