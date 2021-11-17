# Clock In Managment System Using Face Recognition

from tkinter import * 
import tkinter as tk
from time import strftime
import cv2

def time():
    string = strftime('%H:%M:%S %p \n %x')
    label.config(text=string)
    label.after(1000, time)

def register():
    window = tk.Tk()
    window.geometry("500x400")
    window.resizable(True,False)
    window.title("Registration")

    # Register Frame
    Register_Frame=Frame(window,bd=4,relief=RIDGE, bg="blue")
    Register_Frame.place(x=0, y=0, width=500, height=400)

    reg_title=Label(Register_Frame, text="Registration",font=("times new roman", 30, "bold"),bg="blue", fg="white")
    reg_title.grid(row=0, columnspan=2, pady=10)

    text = Label(Register_Frame, text="Click 'Capture' to take a picture of your face \n Hit 'S' to save the image OR 'Q' to close the program",font=("times new roman", 15, "bold"),bg="blue", fg="white")
    text.place(x=0,y=90)

    # Button 
    RegButton = tk.Button(Register_Frame, text="Capture", command=captureImg, fg="black"  ,bg="white"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
    RegButton.place(x=10, y=180)

    window.mainloop()

def captureImg():
    cap = cv2.VideoCapture(0)

    img_counter = 0

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("failed")
            break
        cv2.imshow("Registration", frame)

        k = cv2.waitKey(1)
        # click 'q' to close the program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Program closing..")
            # closes the webcam
            cap.release()
            # destroys all the windows we created
            cv2.destroyAllWindows()
        # click 's' to save the image
        elif cv2.waitKey(1) & 0xFF == ord('s'):
            # for now it's hardcoded, will be changed for manually entering employee name 
            img_name = "images/krystian.jpg".format(img_counter)
            cv2.imwrite(img_name, frame)
            img_counter += 1
            # closes the webcam
            cap.release()
            # destroys all the windows we created
            cv2.destroyAllWindows()

# User Interface (Menu) 

window = tk.Tk()
window.geometry("1028x520")
window.resizable(True,False)
window.title("Clocking Management System")   

label=Label(window, font=("times new roman", 30, "bold"),bg="grey", fg="white")
label.pack(side=TOP, fill=X)
time()  

# Left Frame 
Left_Frame=Frame(window,bd=4,relief=RIDGE, bg="white")
Left_Frame.place(x=0, y=95, width=520, height=425)

# Right Frame
Right_Frame=Frame(window,bd=4,relief=RIDGE, bg="white")
Right_Frame.place(x=510, y=95, width=520, height=425)

# Buttons 
clockInButton = tk.Button(Left_Frame, text="Clock In" ,fg="white"  ,bg="green"  ,width=11 ,activebackground = "white" ,font=('times', 30, ' bold '))
clockInButton.place(x=100, y=100)

clockOutButton = tk.Button(Left_Frame, text="Clock Out",fg="white"  ,bg="red"  ,width=11 ,activebackground = "white" ,font=('times', 30, ' bold '))
clockOutButton.place(x=100, y=230)

RegButton = tk.Button(Right_Frame, text="Register", command=register ,fg="white"  ,bg="blue"  ,width=11 ,activebackground = "white" ,font=('times', 30, ' bold '))
RegButton.place(x=100, y=160)

window.mainloop()