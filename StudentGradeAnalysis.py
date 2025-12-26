import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import arabic_reshaper
from bidi.algorithm import get_display

def arabic_text(text):
    return get_display(arabic_reshaper.reshape(text))

class OldSystemStudent:
    def __init__(self, student_data):
        self.name=student_data["اسم الطالب بالعربيه"]
        self.seat_number=student_data["رقم الجلوس"]
        self.total=student_data["المجموع الكلى"]
        self.percentage=(self.total/410)*100
class NewSystemStudent:
    def __init__(self, student_data):
        self.name=student_data['arabic_name']
        self.seat_number=student_data['seating_no']
        self.total=student_data['total_degree']
        self.percentage=(self.total/320)*100

def assign_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

def rows(r,num):
    start=0
    step=4
    while start<len(r):
        for i in range(len(r.iloc[start:start+num,0])):
            print(f"{i+1} - {arabic_text(r.iloc[start+i,1])}")
        choose=int(input("If your name is in the above list, type its number--otherwise type '0' to see more: "))
        if choose == 1:
            return r.iloc[start]
        elif choose == 2:
            return r.iloc[start+1]
        elif choose==0:
            start+=step
        else:
            print("Invalid input. Please try again.")
            continue
def OLDSCHOOL():
    while True:
        op=input("Do you want to search by name or seat number? (Enter name or seat number): ")
        if op=='name':
            name=input("Enter your name: ")
            student_row = data[data['اسم الطالب بالعربيه'].str.split().str[0] == name]
            if len(student_row)>0:
                student_row=rows(student_row,2)
                name_old_obj=OldSystemStudent(student_row)
                print(f"Name: {arabic_text(name_old_obj.name)}")
                print(f"Seat Number: {name_old_obj.seat_number}")
                print(f"Total Marks: {name_old_obj.total}")
                print(f"Percentage: {name_old_obj.percentage:.2f}%")
                print(f"Grade: {assign_grade(name_old_obj.percentage)}")
                break
            else:
                print("Name not found.")
        elif op=='seat number':
            seat_number=input("Enter your seat number: ")
            if len(seat_number)!=7:
                print("InValid seat number")
            else:
                seat_number=int(seat_number)
                student_raw=data[data['رقم الجلوس']==(seat_number)]
                if len(student_raw)>0:
                    student_raw=student_raw.iloc[0]
                    seat_number_old_obj=OldSystemStudent(student_raw) 
                    print(f"Name: {arabic_text(seat_number_old_obj.name)}")
                    print(f"Seat Number: {seat_number_old_obj.seat_number}")
                    print(f"Total Marks: {seat_number_old_obj.total}")
                    print(f"Percentage: {seat_number_old_obj.percentage:.2f}%")
                    print(f"Grade: {assign_grade(seat_number_old_obj.percentage)}")
                    break
                else:
                    print("Seat number not found.")
        else:
            print("Invalid input. Please enter 'name' or 'seat number'.")

def NewSCHOOL():
    while True:
        op=input("Do you want to search by name or seat number? (Enter name or seat number): ")
        if op=='name':
            name=input("Enter your name: ")
            student_row=data[data['arabic_name'].str.split().str[0] == name]
            if len(student_row)>0:
                student_row=rows(student_row,2)
                name_new_obj=NewSystemStudent(student_row)
                print(f"Name: {arabic_text(name_new_obj.name)}")
                print(f"Seat Number: {name_new_obj.seat_number}")
                print(f"Total Marks: {name_new_obj.total}")
                print(f"Percentage: {name_new_obj.percentage:.2f}%")
                print(f"Grade: {assign_grade(name_new_obj.percentage)}")
                break
            else:
                print("Name not found.")
        elif op=='seat number':
            seat_number=input("Enter your seat number: ")
            if len(seat_number)!=7:
                print("InValid seat number")
            else:
                seat_number=int(seat_number)
                student_row=data[data['seating_no']==(seat_number)]
                if len(student_row)>0:
                    student_row=student_row.iloc[0]
                    seat_number_new_obj=NewSystemStudent(student_row)
                    print(f"Name: {arabic_text(seat_number_new_obj.name)}")
                    print(f"Seat Number: {seat_number_new_obj.seat_number}")
                    print(f"Total Marks: {seat_number_new_obj.total}")
                    print(f"Percentage: {seat_number_new_obj.percentage:.2f}%")
                    print(f"Grade: {assign_grade(seat_number_new_obj.percentage)}")
                    break
                else:
                    print("Seat number not found.")
        else:
            print("Invalid input. Please enter 'name' or 'seat number'.")







data_old = pd.read_excel("OldSystem_NotReal.xlsx")
data_new = pd.read_excel("NewSystem_NotReal.xlsx")
while True:
    choice=input("Are you a old system student or a new system student? (Enter old or new) :")
    if choice.lower()=='old':
        data = data_old
        data['percentage'] = (data['المجموع الكلى'] / 410) * 100
        OLDSCHOOL()
        break
    elif choice.lower()=='new':
        data = data_new
        data['percentage'] = (data['total_degree'] / 320) * 100
        NewSCHOOL()
        break
    else:
        print("Invalid input. Please enter 'old' or 'new")


#--------------------------------------------------------------------------------#

data['Grade'] = data['percentage'].apply(assign_grade)
print()
print("The pie chart below shows the distribution of grades among the students")
grade_counts = data['Grade'].value_counts()
plt.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%')
plt.title('Grade Distribution')
plt.show()


x=data[['percentage']]
y=data['Grade']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)   
model=LogisticRegression(max_iter=1000)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
accuracy=accuracy_score(y_test,y_pred)*100
print(f"The accuracy of the model is {accuracy:.2f}%")
