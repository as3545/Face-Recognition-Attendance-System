import pandas as pd
import numpy as np
import datetime
import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as ms
from tkinter import simpledialog as tsd
import cv2, os
import csv 
from PIL import Image
import pathlib
from pathlib import Path
import threading
import logging

root=tk.Tk()

def assure_path_exists(path):
    dir_path = Path(path).resolve().parent
    dir_path.mkdir(parents=True, exist_ok=True)
    
def update_clock():
    while True:
        current_time = time.strftime('%H:%M:%S')
        clock.config(text=current_time)
        time.sleep(1)
clock = tk.Label(root, font=('Helvetica', 24), bg='black', fg='white')
clock.pack()

def contact():
    contact_info = "Please contact us at: ahsansultan579@gmail.com"
    contact_label.config(text=contact_info)
root = tk.Tk()
contact_label = tk.Label(root, text="", font=('Helvetica', 12))
contact_label.pack()

def check_haarcascadefile():
    if os.path.isfile("haarcascade_frontalface_default.xml"):
        logging.info("Haarcascade file found.")
    else:
        logging.error("Haarcascade file missing. Please contact us for help.")
        # Optionally, you can exit the program here if desired
        # sys.exit()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def read_password(file_path):
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            return file.read().strip()
    return None

def save_password(file_path, password):
    try:
        with open(file_path, "w") as file:
            file.write(password)
        return True
    except Exception as e:
        ms._show(title='Error', message=f'Failed to save password: {str(e)}')
        return False

def save_pass(master, old, new, nnew):
    file_path = "TrainingImageLabel/psd.txt"
    assure_path_exists(os.path.dirname(file_path))

    old_password = read_password(file_path)
    if old_password is None:
        new_password = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_password is None:
            ms._show(title='No Password Entered', message='Password not set!! Please try again')
            return
        if save_password(file_path, new_password):
            ms._show(title='Password Registered', message='New password was registered successfully!!')
        return

    entered_old_password = old.get()
    new_password = new.get()
    confirm_new_password = nnew.get()

    if entered_old_password != old_password:
        ms._show(title='Wrong Password', message='Please enter correct old password.')
        return

    if new_password != confirm_new_password:
        ms._show(title='Error', message='Confirm new password again!!!')
        return

    if save_password(file_path, new_password):
        ms._show(title='Password Changed', message='Password changed successfully!!')
        master.destroy()
        

class PasswordChangeWindow:
    def __init__(self, parent):
        self.master = tk.Toplevel(parent)
        self.master.geometry("400x160")
        self.master.resizable(False, False)
        self.master.title("Change Password")
        self.master.configure(background="white")

        lbl4 = tk.Label(self.master, text='    Enter Old Password', bg='white', font=('times', 12, ' bold '))
        lbl4.place(x=10, y=10)
        self.old = tk.Entry(self.master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
        self.old.place(x=180, y=10)

        lbl5 = tk.Label(self.master, text='   Enter New Password', bg='white', font=('times', 12, ' bold '))
        lbl5.place(x=10, y=45)
        self.new = tk.Entry(self.master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
        self.new.place(x=180, y=45)

        lbl6 = tk.Label(self.master, text='Confirm New Password', bg='white', font=('times', 12, ' bold '))
        lbl6.place(x=10, y=80)
        self.nnew = tk.Entry(self.master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
        self.nnew.place(x=180, y=80)

        cancel = tk.Button(self.master, text="Cancel", command=self.master.destroy, fg="black", bg="red", height=1,
                           width=25, activebackground="white", font=('times', 10, ' bold '))
        cancel.place(x=200, y=120)

        save1 = tk.Button(self.master, text="Save", command=self.save_pass, fg="black", bg="#3ece48", height=1,
                          width=25, activebackground="white", font=('times', 10, ' bold '))
        save1.place(x=10, y=120)

def save_pass(self):
        # Add your save_pass logic here
        pass

def change_pass():
    root = tk.Tk()
    PasswordChangeWindow(root)
    root.mainloop()
    
def psw():
    file_path = "TrainingImageLabel/psd.txt"
    assure_path_exists(os.path.dirname(file_path))

    password = read_password(file_path)
    if password is None:
        new_password = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_password is None:
            ms._show(title='No Password Entered', message='Password not set!! Please try again')
            return
        if save_password(file_path, new_password):
            ms._show(title='Password Registered', message='New password was registered successfully!!')
        return

    entered_password = tsd.askstring('Password', 'Enter Password', show='*')
    if entered_password == password:
        TrainImages()
    elif entered_password is not None:
        ms._show(title='Wrong Password', message='You have entered the wrong password')

# Example function to be called if password is correct
def TrainImages():
    print("Training Images")

def clear():
    txt.delete(0, tk.END)
    res = "1)Take Images  >>>  2)Save Profile"
    message1.configure(text=res)



window = tk.Tk()
window.geometry("1280x720")
window.resizable(True,False)
window.title("Attendance System")
window.configure(background='#262523')

frame2 = tk.Frame(window, bg="#00aeff")
frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)


txt = tk.Entry(frame2,width=32 ,fg="black",font=('times', 15, ' bold '))
txt.place(x=30, y=88)

message1 = tk.Label(frame2, text="1)Take Images  >>>  2)Save Profile" ,bg="#00aeff" ,fg="black"  ,width=39 ,height=1, activebackground = "yellow" ,font=('times', 15, ' bold '))
message1.place(x=7, y=230)


def clear2():
    txt2.delete(0, tk.END)
    res = "1)Take Images  >>>  2)Save Profile"
    message1.configure(text=res)
    
txt2 = tk.Entry(frame2,width=32 ,fg="black",font=('times', 15, ' bold ')  )
txt2.place(x=30, y=173)

def TakeImages():
    check_haarcascadefile()
    serial = 0
    
    # Define columns for the CSV file
    columns = ['SERIAL NO.', '', 'ID', '', 'NAME']
    
    # Ensure directories exist
    assure_path_exists("StudentDetails/")
    assure_path_exists("TrainingImage/")
    
    # Determine the next serial number
    exists = os.path.isfile("StudentDetails\StudentDetails.csv")
    if exists:
        with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            serial = sum(1 for _ in reader1) // 2
    else:
        with open("StudentDetails\StudentDetails.csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(columns)
            serial = 1

    # Read ID and name from text fields
    Id = txt.get()
    name = txt2.get()
    
    if name.replace(' ', '').isalpha():
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        
        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                sampleNum += 1
                img_path = f"TrainingImage\ {name}.{serial}.{Id}.{sampleNum}.jpg"
                cv2.imwrite(img_path, gray[y:y + h, x:x + w])
                cv2.imshow('Taking Images', img)
                
            if cv2.waitKey(100) & 0xFF == ord('q') or sampleNum > 100:
                break
        
        cam.release()
        cv2.destroyAllWindows()
        
        res = f"Images Taken for ID: {Id}"
        row = [serial, '', Id, '', name]
        
        with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        
        ms.showinfo(title="Success", message=res)
        message1.configure(text=res)
    
    else:
        ms.showerror(title="Error", message="Enter Correct name")
def getImagesAndLabels(path):
    # Get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    
    # Create empty lists for faces and IDs
    faces = []
    Ids = []

    # Loop through all the image paths and load the IDs and the images
    for imagePath in imagePaths:
        try:
            # Load the image and convert it to grayscale
            pilImage = Image.open(imagePath).convert('L')
            # Convert the PIL image into a numpy array
            imageNp = np.array(pilImage, dtype=np.uint8)
            # Get the ID from the image filename
            ID = int(os.path.basename(imagePath).split(".")[1])
            # Extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(ID)
        except Exception as e:
            print(f"Error processing image {imagePath}: {e}")

    return faces, Ids

frame1 = tk.Frame(window, bg="#00aeff")
frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

tv= ttk.Treeview(frame1,height =13,columns = ('name','date','time'))
tv.column('#0',width=82)
tv.column('name',width=130)
tv.column('date',width=133)
tv.column('time',width=133)
tv.grid(row=2,column=0,padx=(0,0),pady=(150,0),columnspan=4)
tv.heading('#0',text ='ID')
tv.heading('name',text ='NAME')
tv.heading('date',text ='DATE')
tv.heading('time',text ='TIME')

def TrackImages():
    check_haarcascadefile()
    assure_path_exists("Attendance/")
    assure_path_exists("StudentDetails/")
    
    for k in tv.get_children():
        tv.delete(k)
    
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    trainner_path = "TrainingImageLabel/Trainner.yml"
    
    if os.path.isfile(trainner_path):
        recognizer.read(trainner_path)
    else:
        ms._show(title='Data Missing', message='Please click on Save Profile to reset data!!')
        return
    
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    
    df_path = "StudentDetails/StudentDetails.csv"
    if os.path.isfile(df_path):
        df = pd.read_csv(df_path)
    else:
        ms._show(title='Details Missing', message='Students details are missing, please check!')
        return
    
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']
    attendance = []
    
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
            
            if conf < 50:
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                name = df.loc[df['SERIAL NO.'] == serial, 'NAME'].values[0]
                ID = df.loc[df['SERIAL NO.'] == serial, 'ID'].values[0]
                attendance = [str(ID), '', name, '', str(date), '', str(timeStamp)]
            else:
                name = 'Unknown'
            
            cv2.putText(im, str(name), (x, y + h), font, 1, (255, 255, 255), 2)
        
        cv2.imshow('Taking Attendance', im)
        if cv2.waitKey(1) == ord('q'):
            break
    
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    attendance_file = f"Attendance/Attendance_{date}.csv"
    
    if not os.path.isfile(attendance_file):
        with open(attendance_file, 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(col_names)
            writer.writerow(attendance)
    else:
        with open(attendance_file, 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(attendance)
    
    with open(attendance_file, 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for i, lines in enumerate(reader1, 1):
            if i > 1 and i % 2 != 0:
                tv.insert('', 0, text=str(lines[0]), values=(str(lines[2]), str(lines[4]), str(lines[6])))
    
    cam.release()
    cv2.destroyAllWindows()
global key
key = ''

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day,month,year=date.split("-")

mont = {str(i).zfill(2): month for i, month in enumerate(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], start=1)}

message3 = tk.Label(window, text="Face Recognition Based Attendance System" ,fg="white",bg="#262523" ,width=55 ,height=1,font=('times', 29, ' bold '))
message3.place(x=10, y=10)


frame3 = tk.Frame(window, bg="#c4c6ce")
frame3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)

frame4 = tk.Frame(window, bg="#c4c6ce")
frame4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)

datef = tk.Label(frame4, text = day+"-"+mont[month]+"-"+year+"  |  ", fg="orange",bg="#262523" ,width=55 ,height=1,font=('times', 22, ' bold '))
datef.pack(fill='both',expand=1)

clock = tk.Label(frame3,fg="orange",bg="#262523" ,width=55 ,height=1,font=('times', 22, ' bold '))
clock.pack(fill='both',expand=1)


head2 = tk.Label(frame2, text="                       For New Registrations                       ", fg="black",bg="#3ece48" ,font=('times', 17, ' bold ') )
head2.grid(row=0,column=0)

head1 = tk.Label(frame1, text="For Already Registered ", fg="black",bg="#3ece48" ,font=('times', 17, ' bold ') )
head1.place(x=0,y=0)

lbl = tk.Label(frame2, text="Enter ID",width=20  ,height=1  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold ') )
lbl.place(x=80, y=55)

txt = tk.Entry(frame2,width=32 ,fg="black",font=('times', 15, ' bold '))
txt.place(x=30, y=88)

lbl2 = tk.Label(frame2, text="Enter Name",width=20  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold '))
lbl2.place(x=80, y=140)

txt2 = tk.Entry(frame2,width=32 ,fg="black",font=('times', 15, ' bold ')  )
txt2.place(x=30, y=173)

message = tk.Label(frame2, text="" ,bg="#00aeff" ,fg="black"  ,width=39,height=1, activebackground = "yellow" ,font=('times', 16, ' bold '))
message.place(x=7, y=450)

lbl3 = tk.Label(frame1, text="Attendance",width=20  ,fg="black"  ,bg="#00aeff"  ,height=1 ,font=('times', 17, ' bold '))
lbl3.place(x=100, y=115)

res=0
exists = os.path.isfile("StudentDetails\StudentDetails.csv")
if exists:
    with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for l in reader1:
            res = res + 1
    res = (res // 2) - 1
    csvFile1.close()
else:
    res = 0
message.configure(text='Total Registrations till now  : '+str(res))


menubar = tk.Menu(window,relief='ridge')
filemenu = tk.Menu(menubar,tearoff=0)
filemenu.add_command(label='Change Password', command = change_pass)
filemenu.add_command(label='Contact Us', command = contact)
filemenu.add_command(label='Exit',command = window.destroy)
menubar.add_cascade(label='Help',font=('times', 29, ' bold '),menu=filemenu)


scroll=ttk.Scrollbar(frame1,orient='vertical',command=tv.yview)
scroll.grid(row=2,column=4,padx=(0,100),pady=(150,0),sticky='ns')
tv.configure(yscrollcommand=scroll.set)

###################### BUTTONS ##################################

clearButton = tk.Button(frame2, text="Clear", command=clear  ,fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
clearButton.place(x=335, y=86)
clearButton2 = tk.Button(frame2, text="Clear", command=clear2  ,fg="black"  ,bg="#ea2a2a"  ,width=11 , activebackground = "white" ,font=('times', 11, ' bold '))
clearButton2.place(x=335, y=172)    
takeImg = tk.Button(frame2, text="Take Images", command=TakeImages  ,fg="white"  ,bg="blue"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
takeImg.place(x=30, y=300)
trainImg = tk.Button(frame2, text="Save Profile", command=psw ,fg="white"  ,bg="blue"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
trainImg.place(x=30, y=380)
trackImg = tk.Button(frame1, text="Take Attendance", command=TrackImages  ,fg="black"  ,bg="yellow"  ,width=35  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
trackImg.place(x=30,y=50)
quitWindow = tk.Button(frame1, text="Quit", command=window.destroy  ,fg="black"  ,bg="red"  ,width=35 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
quitWindow.place(x=30, y=450)

window.configure(menu=menubar)
window.mainloop()
