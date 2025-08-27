import json
class student:
    def __init__(self , name , student_class , roll_no , physics , chemistry  , maths):
        self.name = name
        self.student_class = student_class
        self.roll_no = roll_no
        self.physics = physics
        self.chemistry = chemistry
        self.maths = maths
        self.average = (physics + chemistry + maths) / 3

    def to_dict(self):
        return{
            "Name": self.name,
            "Class": self.student_class,
            "Roll no.": self.roll_no,
            "Marks of Physics": self.physics,
            "Marks of Chemistry": self.chemistry,
            "Marks of Maths": self.maths,   
            "Average" : self.average       
        }
    
class studentmanager:
    def savedata(self , new_student):
        try:
            with open("data.json" , "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        #Add new student data
        data.append(new_student.to_dict())

        #To save stuednt data
        try:
            with open("data.json" , "w") as f:
                json.dump(data , f , indent = 4)
        except:
            print("Failed")

    def __init__(self):
            self.data = []

    def add_student(self):
        try:
            name = input("Enter Name: ")
            student_class = input("Enter Class: ")
            roll_no = int(input("Enter Roll Number: "))
            physics = int(input("Enter Physics Marks: "))
            chemistry = int(input("Enter Chemistry Marks: "))
            maths = int(input("Enter Maths Marks: "))
        except ValueError:
            print("Invalid input. Please enter correct data.")
            return
        
        new_student = student(name, student_class, roll_no, physics, chemistry, maths) 
        self.savedata(new_student)  # ✅ No parentheses here
        print("Student Added Succesfully")

    def viewdata(self):
        search_name = input("Enter Student Name:")
        try:
            with open("data.json" , "r") as f:
                viewdata = json.load(f)

            found = False
            for student in viewdata:
                if student.get("Name" , "").lower() == search_name.lower():
                    print("\n Student Found \n")
                    for key , values in student.items():
                        print(f"{key} : {values}")
                    found = True
                    break

            if not found:
                print("Student not found")
        except FileNotFoundError:
            print("data.json not Found")
        except json.decoder.JSONDecodeError:
            print("Error decoding JSON. Maybe file is empty or corrupted")
    
    def updatedata(self ):

        print('''
        Which field do you want to update?
        1 = Name
        2 = Class
        3 = Roll No.
        4 = Marks in physics
        5 = Marks in Chemistry
        6 = Marks in Maths
        ''')
        search_name = input("Enter Student Name:") 
        try:
            with open("data.json" , "r") as f:
                viewdata = json.load(f)  
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            print("Error reading data.json")

        found = False

        for to_dict in viewdata:
                if search_name.lower() == to_dict.get("Name", "").lower():
                    found = True
                    UserUpdate = int(input("Enter The Field Number to Change: "))

                    if UserUpdate == 1:
                        to_dict["Name"] = input("Enter New Name: ")
                    elif UserUpdate == 2:
                        to_dict["Class"] = input("Enter New Class: ")
                    elif UserUpdate == 3:
                        to_dict["Roll No."] = int(input("Enter New RollNumber: "))
                    elif UserUpdate == 4:
                        to_dict["Marks of Physics"] = int(input("Enter New Physics Marks: "))
                    elif UserUpdate == 5:
                        to_dict["Marks of Chemistry"] = int(input("Enter New Chemistry Marks: "))
                    elif UserUpdate == 6:
                        to_dict["Marks of Maths"] = int(input("Enter New Maths Marks: "))
                    elif UserUpdate == 7:
                        viewdata.remove(to_dict)
                        print("Student Data deleted")
                    else:
                        print("Enter Valid Field Number")
                    break  

                if UserUpdate in [4, 5, 6]:
                    to_dict["Average"] = (
                    to_dict["Marks of Physics"] +
                    to_dict["Marks of Chemistry"] +
                    to_dict["Marks of Maths"]
                ) / 3

                break
        if not found:
            print("Student not found...")

        try:
            with open("data.json" , "w" )  as f:
                json.dump(viewdata , f , indent=4)  
        except json.decoder.JSONDecodeError:
                print("Error decoding JSON. File may be corrupted.")
                
    def allstudent(self):
        try:
            with open("data.json", "r") as f:
                viewdata = json.load(f)
        except FileNotFoundError:
            print("data.json not found")
        except json.decoder.JSONDecodeError:
            print("Error decoding JSON")

        print("\nList of Students:")
        for studentdata in viewdata:
            print("-", studentdata.get("Name"))
      
def main():
    manager = studentmanager()

    while True:
        print('''
                \n---Student Report System---
              1. Add Student Data
              2. View Student Data
              3. Update Student Data
              4. View All Student Name
              5. Exit
        ''')
        try:
            choice = int(input("Enter Your Choice:"))
        except ValueError:
            print("Please enter appropriate Value...")
            continue

        if choice == 1:
            manager.add_student()
        elif choice == 2 :
            manager.viewdata()
        elif choice == 3 :
            manager.updatedata()
        elif choice == 4 :
            manager.allstudent()
        elif choice == 5 :
            print("Exiting.....")
            break
        else:
            print("Invalid option Try agian..")
    
if __name__ == "__main__":
    main()
        

            