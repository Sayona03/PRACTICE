import tkinter
from tkinter import ttk
from tkinter import messagebox


root=tkinter.Tk()
root.title("Data Entry Form")

frame=tkinter.Frame(root)
frame.pack()

def retrieve():
   accept=termvar.get()
   reg=regvar.get()

   if accept=="Accepted" and reg=="Registered":
    
      fname=first_name_entry.get()
      lname=last_name_entry.get()

      if fname!="" and lname!="":
          
        age=user_age_spinbox.get()
        nationality=user_nationality_combobox.get()
        course=user_course_spinbox.get()
        sem=user_sem_spinbox.get()

        print(f"Name: {fname} Last Name: {lname} Age: {age} Nationality: {nationality} Course: {course} Semester: {sem} Registeration Status {reg} Termas and Conditions {accept}")

      else:
         tkinter.messagebox.showwarning(title="Error",message="please fill first name and last name")
   else:
       tkinter.messagebox.showwarning(message="check registration status and terms and condition",title="Error")
   
   
    

user_information_frame=tkinter.LabelFrame(frame,text="User Information")
user_information_frame.grid(row=0,column=0,padx=20,pady=20)
first_name=tkinter.Label(user_information_frame,text="First Name")
first_name.grid(row=0,column=0)
last_name=tkinter.Label(user_information_frame,text="Last Name")
last_name.grid(row=0,column=1)
first_name_entry=tkinter.Entry(user_information_frame)
first_name_entry.grid(row=1,column=0)
last_name_entry=tkinter.Entry(user_information_frame)
last_name_entry.grid(row=1,column=1)
user_title=tkinter.Label(user_information_frame,text="Title")
user_title.grid(row=0,column=2)
user_title_combobox=ttk.Combobox(user_information_frame,values=["","Mr.","Mrs.","Miss"])
user_title_combobox.grid(row=1,column=2)
user_age=tkinter.Label(user_information_frame,text="Age")
user_age.grid(row=2,column=0)
user_age_spinbox=tkinter.Spinbox(user_information_frame,from_=18,to=100)
user_age_spinbox.grid(row=3,column=0)
user_nationality=tkinter.Label(user_information_frame,text="Nationality")
user_nationality.grid(row=2,column=1)
user_nationality_combobox=ttk.Combobox(user_information_frame,values=["Asia","Antartica","Ocenia","North America","Africa"])
user_nationality_combobox.grid(row=3,column=1)

for widget in user_information_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)



user_info_frame=tkinter.LabelFrame(frame)
user_info_frame.grid(row=1,column=0,sticky="news",padx=20,pady=20)
reg_status=tkinter.Label(user_info_frame,text="Registration status")

regvar=tkinter.StringVar(value="Not registered")
reg_status_check=tkinter.Checkbutton(user_info_frame,text="Currently registered",variable=regvar,onvalue="Registered",offvalue="Not registered")


reg_status.grid(row=0,column=0)
reg_status_check.grid(row=1,column=0)
user_course=tkinter.Label(user_info_frame,text="#Completed Courses")
user_course.grid(row=0,column=1)
user_course_spinbox=tkinter.Spinbox(user_info_frame,from_=0,to="infinity")
user_course_spinbox.grid(row=1,column=1)
user_sem=tkinter.Label(user_info_frame,text="Semester completed")
user_sem.grid(row=0,column=2)
user_sem_spinbox=tkinter.Spinbox(user_info_frame,from_=0,to="infinity")
user_sem_spinbox.grid(row=1,column=2)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)



termsandcondition=tkinter.LabelFrame(frame,text="Terms & conditions")
termsandcondition.grid(row=2,column=0,sticky="news",padx=20,pady=20)
termvar=tkinter.StringVar(value="Not accepted")
last_step=tkinter.Checkbutton(termsandcondition,text="I have accepted the terms and conditions",variable=termvar,onvalue="Accepted",offvalue="Not accepted")
last_step.grid(row=0,column=0,padx=10,pady=5)




bt=tkinter.Button(frame,text="Enter data",command=lambda:retrieve())
bt.grid(row=3,column=0)

    
                            
root.mainloop()
