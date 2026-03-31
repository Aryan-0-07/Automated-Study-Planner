# Automated-Study-Planner
This structured document outlines the development of an Automated Study Planner, focusing on the journey from identifying student-related productivity gaps to implementing an AI-driven solution.
<br>
<br>
Features:
Dynamic Sorting: Automatically reorders tasks so the most urgent deadlines appear first using tasks.sort().
Live Countdown: Uses the datetime library to calculate exactly how many days remain from "today" until the deadline.
Urgency Tagging: Uses logic to auto-label tasks as "OVERDUE", "DO THIS NOW", or "Relax" based on the remaining days.
Error Handling: Includes a try-except block to prevent the program from crashing if a user enters an invalid date format.
Bulk Entry: Features an infinite loop (while True) allowing users to input multiple subjects at once until they type "done.
"Categorized Summary: Generates a clean, prioritized report showing the status of every assignment in one view.
<br>
<br>
Prerequisites
Python 3.x installed on your system.
Datetime libraries are required (uses standard Python functionality).
<br>
<br>
Code Structure
import datetime: Provides the classes for manipulating dates and times.
Error Handling: Uses a try-except block to prevent the program from crashing if the user types the date incorrectly.
Creates an empty list (tasks = []) to act as a temporary database.
Uses a "sentinel value" ('done') to allow the user to enter as many items as they want.
Uses a Lambda Function (key=lambda x: x['days']) to tell Python exactly how to reorder the list (from smallest number of days to largest).
Conditional Logic (if/elif/else): Categorizes each task based on urgency (Overdue, Now, or Relax).
run_planner(): The final line that actually starts the program when the file is opened.
<br>
<br>
Author: [Aryan Raj]
<br>
Registration number:25BAI10693
<br>
<br>
<img width="1920" height="1080" alt="CODE(1)" src="https://github.com/user-attachments/assets/a2adb5ea-d505-41ff-a668-277cfb23f3d2" />
<br>
<br>
<img width="1920" height="1080" alt="CODE(2)" src="https://github.com/user-attachments/assets/319ebe6f-b7e7-429e-9f4e-4ae3dc904f1a" />
<br>
<br>
<img width="1920" height="1080" alt="CODE(3)" src="https://github.com/user-attachments/assets/915f097a-1a89-4e09-b887-d86b8c1fc1fd" />


