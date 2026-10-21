AIXCELERATE - P17 ATTENDANCE REGISTER
====================================

Name          : RANJITHKUMAR M
Register No.  : 7376252AL197
Project Title : Attendance Register (P17)

1. PROJECT DESCRIPTION
----------------------
A menu-driven Python 3 terminal application for maintaining student attendance.
Student details and daily attendance are stored in text files, so records remain
available after the program is closed and restarted.

2. REQUIREMENTS
---------------
- Python 3
- No database, external library, or framework is required.

3. FILES
--------
Keep these files in the same folder:
- Attendance_Register.py
- Students.txt
- Attendance.txt

Students.txt format:
RegisterNumber|StudentName

Example:
101|Arun
102|Guna

Attendance.txt format:
DD-MM-YYYY|AbsentRegisterNumbers

Absent register numbers are comma-separated. Use '-' when nobody is absent.

Examples:
16-10-2026|101,102
17-10-2026|-

Use the exact filenames expected by main.py. The current program uses
Students.txt and Attendance.txt.

4. HOW TO RUN
-------------
1 Place Attendance_Register.py, Students.txt, and Attendance.txt in the same directory.
2. Open a terminal in that directory.
3. Run:

   python Attendance_Register.py

4. Select a menu option by entering its number.
5. Select option 8 to exit.

5. FEATURES COMPLETED
---------------------
1. View the student list.
2. Mark attendance by entering only absent register numbers; '-' means all
   students are present.
3. Prevent attendance from being marked twice for the same date.
4. Edit an existing attendance record, including its date or absent register
   numbers.
5. View each student's classes attended, classes held, and attendance percentage.
6. List students below 75% attendance and calculate how many consecutive
   additional classes they must attend to reach 75%.
7. Generate a month-wise attendance report for a student.
8. Show the total number of students, absent students, and present students
   for a selected date.
9. Validate date format and calendar validity.
10. Validate user input and handle missing/empty data files without crashing.
11. Save attendance records to a text file for future runs.
12. Keep displaying the menu until the user chooses Exit.

6. KNOWN PROBLEMS
-----------------
No known problems remain from the tests completed for this submission.
The program uses local text files; keep the data files in the same folder as
main.py and make sure they are writable. Always keep a backup before manually
editing the data files.

7. SAMPLE DATA
--------------
Include at least 10 student records in Students.txt for testing.
Attendance examples and a representative terminal session are provided in
sample_run.txt.
