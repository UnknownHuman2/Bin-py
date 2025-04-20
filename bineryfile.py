import pickle
import os
def creat():
            print("----------- Creating/Appending Data Entries -------------")
            emp_no=int(input("Enter Employee ID : "))
            emp_name=input("Enter Employee name : ")
            emp_dep=input("Enter Employee Department : ")
            emp_sal=int(input("Enter Employee Salary : "))
            emp={"Emp.ID":emp_no,"Emp.Name":emp_name,"Emp.Dep":emp_dep,"Salary":emp_sal}
            with open("employee.dat","ab") as o:
                pickle.dump(emp,o)
            print("Creation or append was Sucessfull")

def fetch():
      with open("employee.dat","rb") as o1:
        print("-------- Featching Data from BITS File -------------")
        while True:
            try:
                       ram=pickle.load(o1)
                       print("Emoployee no :",ram["Emp.ID"])
                       print("Employee Name :",ram["Emp.Name"])
                       print("Employee Department :",ram["Emp.Dep"])
                       print("Emp. Salary :",ram["Salary"])
                       print("-------------------------------------")
            except EOFError:
                    break

def search():
    with open ("employee.dat","rb") as o2:
        emp_no=int(input("Provide Employee ID for location : "))
        found=0
        while True:
            try:
                ram1=pickle.load(o2)
                if ram1["Emp.ID"]==emp_no:
                    print("Emoployee no :",ram1["Emp.ID"])
                    print("Employee Name :",ram1["Emp.Name"])
                    print("Employee Department :",ram1["Emp.Dep"])
                    print("Emp. Salary :",ram1["Salary"])
                    print("-------- Above Data was found ---------")
                    found=1
                    break
            except EOFError:
                break
        if found==0:
                print("XXXXXX  No data is associated with given Emp. ID XXXXXXX")

def delete():
    conf_var = 0
    temp_file = 'temp_employee.dat'
    with open('employee.dat', 'rb') as o3, open(temp_file, 'wb') as o4:
        warn=input("Do you really want to delete Data? Yes or No?")
        if warn!="Yes":
            return
        emp_no = int(input("Provide Employee ID for Deletion : "))
        while True:
            try:
                ram = pickle.load(o3)
                if ram["Emp.ID"] != emp_no:
                    pickle.dump(ram, o4)
                else:
                    conf_var = 1
            except EOFError:
                break
    os.remove('employee.dat')
    os.rename(temp_file, 'employee.dat')
    if conf_var == 1:
        print("Employee ID :",emp_no," has been deleted.")
    else:
        print("XXXXXX  No data is associated with given Emp. ID XXXXXXX")

def update():
    conf_var = 0
    temp_file = 'temp_employee.dat'
    with open('employee.dat', 'rb') as o5, open(temp_file, 'wb') as o6:
        warn=input("Do you really want to Update Data? Yes or No?")
        if warn!="Yes":
            return
        upid = int(input("Provide Employee ID For Data Location : "))
        while True:
            try:
                ram1 = pickle.load(o5)
                if ram1["Emp.ID"] == upid:
                    conf_var = 1
                    print("Current Details:")
                    print(f"Name: {ram1['Emp.Name']}, Department: {ram1['Emp.Dep']}, Salary: {ram1['Salary']}")
                    ram1["Emp.Name"] = input("Enter new name: ")
                    ram1["Emp.Dep"] = input("Enter new department: ")
                    ram1["Salary"] = int(input("Enter new salary: "))
                pickle.dump(ram1, o6)
            except EOFError:
                break
    os.remove('employee.dat')
    os.rename(temp_file, 'employee.dat')
    if conf_var == 1:
        print("Employee ID : ",upid," has been updated.")
    else:
        print("XXXXXX  No data is associated with Emp. ID XXXXXXX")


def shred():
    with open('employee.dat', 'rb') as o5:
        warn=input('''WARNING: THIS ACTION IS IRREVERSIBLE\nDo you really want to shred Data?\n"Yes" or "No" ? : ''')
        if warn=="Yes":
            os.remove('employee.dat')
            print("BITS File Has Been Successfully Shredded")
        else:
            print("NO ACTION HAVE BEEN TAKEN")

#Main program

print('''
      __     __ __     ___    _
     / /    / / \\ \\   / _ \\  | |
    / /    / /   \\ \\ | | | | | |     Enterprise BITS Data Supervision Framework
    \\ \\   / /    / / | |_| | | |
     \\_\\ /_/    /_/   \\___/  |_|


      1. Create/Append Enteries
      2. Fetch all Data
      3. Search Data via Emp. ID
      4. Delete Data Point
      5. Update Data Point
      6. Shred the BITS File
      7. Exit ''')

while True:
    try:
        inval=int(input("\nSelect the appropriate option : "))
        if inval==1:
            creat()
        elif inval==2:
            fetch()
        elif inval==3:
            search()
        elif inval==4:
            delete()
        elif inval==5:
            update()
        elif inval==6:
            shred()
        elif inval==7:
            exit()
        else:
             print("XXXXXXXXXX  Invalid Selection  XXXXXXXXXX")

    except FileNotFoundError:
        print("XXXXXXXX Error:Data structure donot exist XXXXXXXX")
    except ValueError:
        print("XXXXXXXX Error:Only Integer values are alowwed XXXXXXXX")