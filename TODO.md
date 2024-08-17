# Features
- [] Create basic task to run batch file.
- [] Edit basic task.
- [] User configurations page.
    - [] Folder focus - folders to focus on instead of displaying all the folders.

- [] implement task event history logs
```python
import win32evtlog

# Specify the log type, for example "System" or "Application"
# Open the event log
log_type = "Microsoft-Windows-TaskScheduler"
h = win32evtlog.OpenEventLog(None, log_type)

# Specify the flags for reading the event log. # Here, EVENTLOG_BACKWARDS_READ reads events in reverse order (newest first), # and EVENTLOG_SEQUENTIAL_READ reads events sequentially.
flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

# Read the events
events = win32evtlog.ReadEventLog(h, flags, 0)

# Loop through the events and filter those from Task Schedulerfor event in events:
    # The event source should be "Microsoft-Windows-TaskScheduler" 
for event in events:
    # if event.SourceName == "Microsoft-Windows-TaskScheduler":
        print("Event ID:", event.EventID)
        print("Record Number:", event.RecordNumber)
        print("Time Generated:", event.TimeGenerated.Format())
        print("Time Written:", event.TimeWritten.Format())
        print("Event Type:", event.EventType)
        print("Event Category:", event.EventCategory)
        print("Source Name:", event.SourceName)
        print("Computer Name:", event.ComputerName)
        print("String Inserts:", event.StringInserts)
        print("-" * 50)

# Close the event log handle
win32evtlog.CloseEventLog(h)
```