#NAME: RANJITHKUMAR M
#REG NO: 7376252AL197
#TITLE: ATTENDANCE REGISTER
#TITLE NO: P17

print()
print("="*120)
print("ATTENDANCE REGISTER".center(120))
print("="*120)
print()

# Loading Students file into dictionaries
def Load_Students(filename):
    students = {}

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split("|")

                if len(parts) != 2:
                    continue

                reg_no = parts[0].strip()
                name = parts[1].strip()

                if not reg_no or not name:
                    continue

                students[reg_no] = name

    except FileNotFoundError:
        print("Student file not found. Starting with an empty list.")

    return students
#============================================================

# Loading Attendance file into Dictionary
def Load_Attendance(filename):
    try:
        attendance = {}
        with open(filename) as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split("|")

                if len(parts)!=2:
                    continue

                date = parts[0].strip()
                absent_reg = parts[1].strip()

                if not date:
                    continue
                
                if absent_reg == "-":
                    attendance[date] = []
                else:
                    absent_list = absent_reg.split(",")

                    if any(not reg.strip() for reg in absent_list):
                        continue
                    
                    attendance[date] = [reg.strip() for reg in absent_list]
                
        return attendance
    
    except FileNotFoundError:
        print("Attendance File not found. starting with an empty attendance dictionary!")
        return {}
#===================================================

# Updating the Original file
def Save_Attendance(attendance, filename):
    try:
        with open(filename, "w") as file:
            for date, absent_list in attendance.items():
                if not absent_list:
                    line = f"{date}|-\n"
                else:
                    absent_str = ",".join(absent_list)
                    line = f"{date}|{absent_str}\n"

                file.write(line)

        print(f"Attendance successfully saved to {filename}.")

    except OSError:
        print("Error writing to file.")

#=====================================================
# Valid date checker function
def CheckLeap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def Validate_Date(date):
    parts = date.split("-")

    # Check the number of components
    if len(parts) != 3:
        return False

    day, month, year = parts

    # Check exact format: DD-MM-YYYY
    if (len(day) != 2 or len(month) != 2 or len(year) != 4):
        return False

    # Ensure all components contain digits
    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        return False

    day = int(day)
    month = int(month)
    year = int(year)

    # Validate month
    if month < 1 or month > 12:
        return False

    # Days in each month
    days_in_month = [31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]

    # Leap year check
    if CheckLeap(year):
        days_in_month[1] = 29

    # Validate day
    if day < 1 or day > days_in_month[month - 1]:
        return False

    return True

#=====================================================
students = Load_Students("Students.txt")
attendance = Load_Attendance("Attendance.txt")


#Menu 1 
def ViewStudentlist(students):
    print()
    if not students:
        print("No students record available!")
        return
    print("=== STUDENTS LIST ===")
    print(f"{'Reg No':<10} {'Name':<15}")
    print("-"*20)

    for reg,name in students.items():
        print(f"{reg:<10} {name:<15}\n")
    
#Menu 2
def MarkAttendance():
    # Validating the entered Date    
    if not students:
        print("No students record available!")
        return
    print("\n========== MARK ATTENDNACE ==========")
    date = input("Enter Date(DD-MM-YYYY): ").strip()
    if(not Validate_Date(date)):
        print("Invalid Date!\nCheck date and enter valid date.")
        return

    if date in attendance:
        print("Attendance already marked for this date:",date)
        return

    absent_reg = input("Enter Absent Reg-Numbers(',' seperated, '-' if none): ").strip()

    if absent_reg == "-":
        absent_list = []
    else:
        absent_list = [reg.strip() for reg in absent_reg.split(",")]

        if any(not reg for reg in absent_list):
            print("Register numbers cannot be empty!")
            return 

        if len(absent_list)!=len(set((absent_list))):
            print("Duplicate Register numbers entered.")
            return

        for reg in absent_list:
            if reg not in students:
                print(f"No Students belong to this Register number.{reg}")
                return
             
    # Update the attendance file
    attendance[date] = absent_list

    Save_Attendance(attendance, "Attendance.txt")

    present_count = len(students) - len(absent_list)

    print(f"Attendance marked successfully for: {date}")
    print(f"Students present: {present_count}/{len(students)}")

 #============================================================           
    
#Menu 3
def EditAttendance():
    print()
    if not students:
            print("No students record available!")
            return
    
    print("\n========== EDIT ATTENDANCE ==========")
    if not attendance:
        print("No attendance records available.")
        return
    
    date = input("Enter the date to edit(DD-MM-YYYY): ").strip()
    if(not Validate_Date(date)):
        print("Invalid date!\nCheck date and enter valid date.")
        return
    
    if date not in attendance:
        print(f"Attendance havn't marked for this date: {date}")
        return
        
    edit_field = input("Enter which should be edited(date(1)/Reg-numbers(2)): ").strip().lower()

    if(edit_field=='1' or edit_field=="date"):
        new_date = input("Enter new date to replace(DD-MM-YYYY): ").strip()
        if(not Validate_Date(new_date)):
            print("Invalid date!\nCheck date and enter valid date.")
            return

        if new_date!=date and new_date in attendance:
            print("Attendance already exists for the new date!")
            return

        absent_list = attendance.pop(date)
        attendance[new_date] = absent_list

    elif(edit_field=='2' or edit_field=="reg-numbers"):
        absent_input = input("Enter Reg-number seperated by comma(,) or '-' if none: ").strip()

        if absent_input=="-":
            absent_list = []
        else:
            absent_list = [reg.strip() for reg in absent_input.split(",")]

            if any(not reg for reg in absent_list):
                print("Register numbers cannot be empty!")
                return 
            
            if len(absent_list)!=len(set((absent_list))):
                print("Duplicate Register numbers entered.")
                return
            
            for reg in absent_list:
                if reg not in students:
                    print(f"Invalid Register number:{reg}")
                    return
        attendance[date] = absent_list
    else:
        print("Invalid editing option!")
        return

    Save_Attendance(attendance, "Attendance.txt")
    print("Attendance updated successfully!")

#Menu 4
def ShowStudentAttendance(attendance):
    if not students:
            print("No students record available!")
            return
    
    if not attendance:
        print("No attendance records available.")
        return
    #Calculate Classes held
    classes_held = len(attendance)
    
    print("\n====================== STUDENT ATTENDANCE ====================")
    print(f"{'Reg No':<15} {'Name':<15} {'Attended':<10} {'Held':<8} {'Percentage':<12}")
    print("-" * 62)

    for reg,name in students.items():
        classes_absent = 0
        for absent_list in attendance.values():
            if reg in absent_list:
                classes_absent+=1

        classes_attended = classes_held - classes_absent
        attendance_percentage = (classes_attended/classes_held)*100
        attendance_percentage = f"{attendance_percentage:.2f}%"

       
        print(f"{reg:<15} {name:<15} {classes_attended:<10} {classes_held:<8} {attendance_percentage:<11}\n")


#Menu 5
def Studentsbelow75(attendance):
    if not students:
            print("No students record available!")
            return
    
    print("\n==================================== STUDENTS BELOW 75% ======================================")
    print(f"{'Reg No':<15} {'Name':<15} {'Held':<15} {'Attended':<15} {'Percentage':<15} {'Classes Needed':<15}")
    print("-" * 94)

    if not attendance:
        print("No attendance records available")
        return
    found = False
    #Calculate attendance percentage
    classes_held = len(attendance)

    for reg,name in students.items():
        classes_absent = 0
        for absent_list in attendance.values():
            if reg in absent_list:
                classes_absent+=1
        classes_attended = classes_held - classes_absent
        attendance_percentage = (classes_attended/classes_held)*100
        # attendance_percentage = f"{attendance_percentage:.2f}%"

        if attendance_percentage < 75:
            found = True
            attendance_percentage = f"{attendance_percentage:.2f}%"
            classes_needed = 3*classes_held - 4*classes_attended
            print(f"{reg:<15} {name:<15} {classes_held:<15} {classes_attended:<15} {attendance_percentage:<15} {classes_needed:<15}\n")


    if not found:
        print("All students have at least 75% attendance.")

#Menu 6
def MonthWiseReport():
    if not students:
            print("No students record available!")
            return
    if not attendance:
        print("No attendance records available!")
        return
    
    print("\n========== MONTH-WISE ATTENDANCE REPORT ==========")
    print()

    reg_no = input("Enter Student Register number for Monthly Report: ").strip()

    if not reg_no:
        print("Register number cannot be empty!")
        return

    if reg_no not in students:
        print("Register number doesn't exist!")
        return

    month_year = input("Enter the month and year (MM-YYYY): ").strip()
    parts = month_year.split("-")

    if len(parts) != 2 or not all(part.isdigit() for part in parts):
        print("Invalid format! Use MM-YYYY.")
        return

    requested_month = int(parts[0])
    requested_year = int(parts[1])

    if requested_month < 1 or requested_month > 12:
        print("Invalid month or year!")
        return

    classes_held = 0
    classes_absent = 0

    name = students[reg_no]

    for date,absent_list in attendance.items():
        date_parts = date.split("-")
        month = date_parts[1]
        year = date_parts[2]

        if month == f"{requested_month:02d}" and year == str(requested_year):
            classes_held+=1
            if reg_no in absent_list:
                classes_absent+=1

    if classes_held == 0:
        print("No classes held in this month!")
        return

    month_map = {
    '01': "January",
    '02': "February",
    '03': "March",
    '04': "April",
    '05': "May",
    '06': "June",
    '07': "July",
    '08': "August",
    '09': "September",
    '10': "October",
    '11': "November",
    '12': "December"
    }
    classes_attended = classes_held - classes_absent
    attendance_percentage = (classes_attended/classes_held)*100
    print()
    print("========== REPORT =========")
    print("Register Number: ",reg_no)
    print("Student Name: ",name)
    print("Month:", month_map[f"{requested_month:02d}"], requested_year)
    print("Classes Held: ",classes_held)
    print("Classes Attended: ",classes_attended)
    print("Classes Absent: ",classes_absent)
    print(f"Attendance: {attendance_percentage:.2f}%",)

#Menu 7
def PresentCountbyDate():
    if not students:
            print("No students record available!")
            return
    if not attendance:
            print("No attendance records available!")
            return
    
    print("\n========== PRESENT COUNT BY DATE ===========")
    date = input("Enter Date(DD-MM-YYYY): ").strip()

    if(not Validate_Date(date)):
        print("Invalid Date!\nCheck date and enter valid date.")
        return
    
    if date not in attendance:
        print("Attendance has not been marked for this date:", date)
        return

    total_students = len(students)
    students_absent = len(attendance[date])
    students_present = total_students - students_absent

    print("\nDate: ",date)
    print("Total Students: ",total_students)
    print("Students Absent: ",students_absent)
    print("Students Present: ",students_present)


#MAIN FUNCTION
while True:
    print("1. === View-Students-List")
    print("2. === Mark-Attendance")
    print("3. === Edit-Attendance")
    print("4. === View-Student-Attendance")
    print("5. === Students-Below-75%")
    print("6. === Student-Monthly-Report")
    print("7. === Present-Count-by-Date")
    print("8. === Exit")

    try:
        option = int(input("Enter Your Choice: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 8.\n")
        continue

    if option == 1:
        ViewStudentlist(students)
        print()
    elif option == 2:
        MarkAttendance()
        print()
    elif option == 3:
        EditAttendance()
        print()
    elif option == 4:
        ShowStudentAttendance(attendance)
        print()
    elif option == 5:
        Studentsbelow75(attendance)
        print()
    elif option == 6:
        MonthWiseReport()
        print()
    elif option == 7:
        PresentCountbyDate()
        print()
    elif option == 8:
        print("\nATTENDANCE CLOSING...")
        break
    else:
        print("Invalid option! Your valid options are 1 to 8.\n")