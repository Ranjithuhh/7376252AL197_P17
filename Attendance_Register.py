


print("=========================")
print("   Attendance Register")
print("=========================")
print()

# Loading Students file into list of dictionaries
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
        print("File not found. starting with an empty attendance list")
        return [] 
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
    if len(parts)!=3:
        return False
    
    try:
        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])
    except ValueError:
        return False
    
    if year<1 or month<1 or month>12 or day<1:
        return False
    
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    if(CheckLeap(year)):
        days_in_month[1] = 29

    if day>days_in_month[month-1]:
        return False

    return True

#=====================================================
students = Load_Students("Students.txt")
attendance = Load_Attendance("Attendance.txt")


#Menu 1
def ViewStudentlist():
    print("Showing students list")
    print("---------------------")
    try:
        with open("Students.txt","r") as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found. Check filename or filepath.")

#Menu 2
def MarkAttendance():
    # Validating the entered Date      
    date = input("Enter Date(DD-MM-YYYY):").strip()
    if(not Validate_Date(date)):
        print("Invalid Date!")
        return

    if date in attendance:
        print("Attendance already marked for this date.")
        return

    absent_reg = input("Enter the Absent Reg-Numbers(Comma(,) seperated, '-' if none):").strip()

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
                print(f"Invalid Register number.{reg}")
                return
             
    # Update the attendance file
    attendance[date] = absent_list

    Save_Attendance(attendance, "Attendance.txt")

    present_count = len(students) - len(absent_list)

    print(f"Attendance marked successfully for:{date}")
    print(f"Students present: {present_count}/{len(students)}")

 #============================================================           
    
#Menu 3
def EditAttendance():
    date = input("Enter the date to edit(DD-MM-YYYY):").strip()
    if(not Validate_Date(date)):
        print("Invalid date!")

    if date not in attendance:
        print(f"Attendance havn't marked for this date:{date}")
        return
        
    edit_field = input("Enter which should be edited(date(1)/Reg-numbers(2)):").strip().lower()

    if(edit_field=='1' or edit_field=="date"):
        new_date = input("Enter new date to replace:").strip()
        if(not Validate_Date(new_date)):
            print("Invalid date!")
            return

        if new_date!=date and new_date in attendance:
            print("Attendance already exists for the new date!")
            return

        absent_list = attendance.pop(date)
        attendance[new_date] = absent_list

    elif(edit_field=='2' or edit_field=="reg-numbers"):
        absent_input = input("Enter Reg-number seperated by comma(,) or '-' if none:").strip()

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
                    print(f"Invalid Register number.{reg}")
                    return
        attendance[date] = absent_list
    else:
        print("Invalid editing option!")
        return

    Save_Attendance(attendance, "Attendance.txt")
    print("Attendance updated successfully!")

#Menu 4
def ShowStudentAttendance():
    print("Showing attendance")
    

#Menu 5
def Studentsbelow75():
    print("Listing below 75% students")


#Menu 6
def StudentMonthlyReport():
    print("Showing Monthly Report.")


while True:

    print("1. View Students list")
    print("2. Mark Attendance")
    print("3. Edit Attendance")
    print("4. Show Student Attendance")
    print("5. Students below 75%")
    print("6. Student Monthly report")
    print("7. Exit")
    print()
    option = int(input("Enter Option:"))

    if option==7:
        print("Attendance closing...")
        break
    
    elif option==1:
        ViewStudentlist()
        print()

    elif option==2:
        MarkAttendance()
        print()

    elif option==3:
        EditAttendance()
        print()

    elif option==4:
        ShowStudentAttendance()
        print()

    elif option==5:
        Studentsbelow75()
        print()

    elif option==6:
        StudentMonthlyReport()




    
        










    
