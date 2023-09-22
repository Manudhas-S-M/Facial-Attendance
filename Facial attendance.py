from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import os
from gtts import gTTS
from playsound import playsound

dbase=sqlite3.connect("attendance.db")

dbase.execute('''CREATE TABLE IF NOT EXISTS
                 TABLE1(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        NAME TEXT NOT NULL,
                        REGNO TEXT UNIQUE,
                        USERNAME TEXT UNIQUE,
                        PASSWORD TEXT NOT NULL)
                        ''')

dbase.execute('''CREATE TABLE IF NOT EXISTS
                 TABLE2(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        NAME TEXT NOT NULL,
                        REGNO TEXT NOT NULL,
                        DATE TEXT NOT NULL,
                        TIME TEXT NOT NULL)
                        ''')

dbase.commit()
app = Tk()

app.title("Login Page")
app.geometry("550x330")

def signup():
    signapp = Toplevel(app)

    signapp.title("Signup")

    signapp.geometry("600x360")
    signapp.configure(background = "#f5bce2")
    

    username=StringVar()
    password=StringVar()
    name = StringVar()
    conpass = StringVar()
    regno = StringVar()
    def submit():
       
        usernameval=username.get()
        print("user",usernameval)
        passwordval=password.get()
        print("passsword",passwordval)
        nameval = name.get()
        regnoval = regno.get()
        print(nameval)
        conpassval = conpass.get()
        print(conpassval)
        if conpassval == passwordval:
            dbase.execute("INSERT INTO TABLE1(NAME, REGNO, USERNAME,PASSWORD)VALUES(?,?,?,?)",(nameval,regnoval,usernameval,passwordval))
            dbase.commit()
            print("The data added database successfully")
            
        else:
            print("password and confirm password didn't match")
        en1.delete(first=0,last=END)
        en2.delete(first=0,last=END)
        en3.delete(first=0,last=END)
        en4.delete(first=0,last=END)
        en5.delete(first=0,last=END)
        signapp.destroy()
        


    lab1 = Label(signapp,text = "Enter your name : ", bg = "#f5bce2", fg = "black", font = ("Arial black",12,))
    lab2 = Label(signapp,text = "Enter your Regno : ", bg = "#f5bce2", fg = "black", font = ("Arial black",12,))     
    lab3 = Label(signapp,text = "Enter your  username : ", bg = "#f5bce2", fg = "black", font = ("Arial black",12,))
    lab4 = Label(signapp,text = "Enter your password : ", bg = "#f5bce2", fg = "black", font = ("Arial black",12,))
    
    lab5 = Label(signapp,text = "Enter confirm password : ", bg = "#f5bce2", fg = "black", font = ("Arial black",12,))
    

    lab1.grid(row = 0, column = 0, padx = (15,20), pady = (10))
    lab2.grid(row = 1, column = 0, padx = (10,20), pady = (10))
    lab3.grid(row = 2, column = 0, padx = (10,20), pady = (10))    
    lab4.grid(row = 3, column = 0, padx = (30,20), pady = (10))
    lab5.grid(row = 4, column = 0, padx = (10,20), pady = (10))
    
    en1 = Entry(signapp, textvariable = name, bg = "#f5bce2", fg = "black", font = ("Arial black",12,))     
    en2 = Entry(signapp, textvariable = regno, bg = "#f5bce2", fg = "black", font = ("Arial black",12,))
    
    en3 = Entry(signapp, textvariable = username, bg = "#f5bce2", fg = "black", font = ("Arial black",12,))
    en4 = Entry(signapp, textvariable = password, bg = "#f5bce2", show = "*",fg = "black", font = ("Arial black",12,))
    
    en5 = Entry(signapp, textvariable = conpass, bg = "#f5bce2", show = "*",fg = "black", font = ("Arial black",12,))
    

    en1.grid(row = 0, column = 1, padx = (10,20), pady = (10))
    en2.grid(row = 1, column = 1, padx = (10,20), pady = (10))
    
    en3.grid(row = 2, column = 1, padx = (10,20), pady = (10))
    en4.grid(row = 3, column = 1, padx = (10,20), pady = (10))
    en5.grid(row = 4, column = 1, padx = (10,20), pady = (10))
    

    btn1 = Button(signapp,command = submit, text = "Signup", bg = "#f5bce2", fg = "black", font = ("Arial black",12,))
    btn1.place(x = 250, y = 250)


    app.mainloop()


def login():

    loginapp = Toplevel(app)

    loginapp.title("Login")

    loginapp.geometry("600x360")
    loginapp.configure(background = "#f5bce2")


    username=StringVar()
    password=StringVar()
    
    def submit():
        usernameval=username.get()
        en1.delete(first=0,last=END)
        
        
        passwordval=password.get()
        en2.delete(first=0,last=END)
        con = dbase.cursor()
        con.execute("SELECT*FROM TABLE1 WHERE USERNAME = ?  and PASSWORD = ? " ,(usernameval,passwordval))
        
        dbase.commit()
        
        value = con.fetchone()
        if value:

            subapp1 = Toplevel(loginapp)

            subapp1.title("Attendance")

            subapp1.geometry("600x360")
            subapp1.configure(background = "#f5bce2")
            lab1 = Label(subapp1,text = "Login sucessfully ", bg = "#f5bce2", fg = "black", font = ("Arial black",26,))
            lab1.grid(row = 0, column = 0, padx = (100,20), pady = (150))
            
            print("Login successfully")
            v = gTTS(text="Login successfully",lang='en',slow=False,tld='ie')

            v.save("voice.mp3")
            playsound("voice.mp3")
            os.remove("voice.mp3")
            name = StringVar()
            
            def capture_image():
                
                import cv2
                import os
                con = dbase.cursor()
                nameval = con.execute("SELECT * FROM TABLE1 WHERE USERNAME = ? AND PASSWORD = ?",(usernameval,passwordval,))
                value=con.fetchone()
                dbase.commit()
                    
                regval = value[2]
                
                print("hai", regval)
                if os.path.exists(regval):
                    print(regval + " folder already exists")
                else:
                    try:
                        os.mkdir(regval)
                    except Exception as e:
                        print(e)
                        
                    print(regval + " folder created ")



                font=cv2.FONT_HERSHEY_SIMPLEX

                face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                video=cv2.VideoCapture(0)
                a=1
                nameval=StringVar()
                
                ideval=StringVar()
                
                con = dbase.cursor()
                nameval = con.execute("SELECT * FROM TABLE1 WHERE USERNAME = ? AND PASSWORD = ?",(usernameval,passwordval,))
                value=con.fetchone()
                dbase.commit()
                
                nameval = value[1]
                regnoval = value[2]
                while True:
                    check,frame=video.read()
                   
                    faces=face_cascade.detectMultiScale(frame,scaleFactor=1.05, minNeighbors=5,minSize=(70,70))
                    
                    imageop2=frame
                    cropimage=frame
                    for x,y,w,h in faces:
                        imageop=cv2.rectangle(frame, (x, y), (x+w,y+h), (99, 255, 3), 2)
                        #imageop2=cv2.putText(imageop, str("detected face"),(x+w//3,y+h+15),font,w/250,(125, 255, 255),2)
                        cropimage = imageop2[y + 2:y + h - 2, x + 2:x + w - 2]
                    resizeimg = cv2.resize(cropimage, (400, 400))
                    
                    if cropimage is frame:
                        pass
                    else:
                        a+=1
                        print(a)
                        cv2.imwrite(regval+"/"+nameval+str('.')+str(regnoval) +str('.')+ str(a)+ ".jpg", cropimage)
                    
                    cv2.imshow("vid", imageop2)
                    key=cv2.waitKey(10)
                    if key==ord("q") or key==27:
                        break
                    elif a>=61:
                        break
                    
                video.release()
                cv2.destroyAllWindows()
                import cv2
                from PIL import Image
                import os
                import numpy as np
                def getImagesAndLabels(path):
                    imagePaths=[os.path.join(path,f)for f in os.listdir(path)] 
                    faces=[]
                    Ids=[]
                    for imagePath in imagePaths:
                        img=cv2.imread(imagePath)
                        
                        cv2.imshow('',img)
                        cv2.waitKey(100)
                        cv2.destroyAllWindows()
                        pilImage=Image.open(imagePath).convert('L')
                        imageNp=np.array(pilImage,'uint8')
                        I=str(os.path.split(imagePath)[-1].split(".")[1])
                        if 'URK' or 'urk' in I:
                            I=str(os.path.split(imagePath)[-1].split(".")[1][7:])
                        else:
                            pass
                        
                        faces.append(imageNp)
                        Id = int(I)
                        #print(type(Id))
                        #print(Id)
                        Ids.append(Id)        
                    return faces,Ids

                def trainimage():
                    recognizer=cv2.face.LBPHFaceRecognizer_create()    
                    faces,Id = getImagesAndLabels(regval)
                    
                    sav = recognizer.train(faces, np.array(Id))
                    recognizer.save("Trainner.yml")
                    


                trainimage()

            def attendance():
                import cv2
                from PIL import Image
                import os
                import numpy as np
                from gtts import gTTS
                from playsound import playsound
                from datetime import datetime

                def TrackImages():
                    nameval=StringVar()
                
                    ideval=StringVar()
                    
                    con = dbase.cursor()
                    nameval = con.execute("SELECT * FROM TABLE1 WHERE USERNAME = ? AND PASSWORD = ?",(usernameval,passwordval,))
                    value=con.fetchone()
                    dbase.commit()
                    
                    nameval = value[1]
                    regnoval = value[2]
                
                    recognizer = cv2.face.LBPHFaceRecognizer_create()
                    recognizer.read("Trainner.yml")
                    
                    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                    cam = cv2.VideoCapture(0)
                    
                    font = cv2.FONT_HERSHEY_SIMPLEX

                    tt='' 
                    while True:
                        ret,im =cam.read()
                        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
                        faces=faceCascade.detectMultiScale(gray, 1.2,5)    
                        for(x,y,w,h) in faces:
                            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
                            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                            
                            conf=int(conf)
                            Id=int(Id)
                            print(Id, conf)
                            if(30< conf <90):
                                                               
                                if str(Id)== str(regnoval[7:]) or str(Id)== str(regnoval):
                                    nam=nameval
                                    tt=str(regnoval)+"-"+nam
                                
                                else:
                                    tt='unknown'                             
                            elif(conf>90 or conf<30):
                                Id='Unknown'                
                          
                            cv2.putText(im,str(tt),(x,y+h), font, w/250,(255,255,255),2)        
                            
                        cv2.imshow('image Detected',im)
    
                        key=cv2.waitKey(1)
                        try:
                            if str(Id) == str(regnoval[7:]) or str(Id) == str(regnoval):
                                print(nameval,"Attendance marked")
                                
                                

                                Time = datetime.now()
                                timeval = Time.strftime("%H:%M:%S")
                                dateval = Time.strftime("%d-%b-%y")


                                dbase.execute("INSERT INTO TABLE2(NAME, REGNO, DATE, TIME)VALUES(?,?,?,?)",(nameval,regnoval,dateval,timeval))
                                dbase.commit()
                                

                                mytext=nameval+" Attendance marked"

                                language = 'en'

                                v = gTTS(text=mytext,lang=language,slow=False,tld='ie')

                                v.save("voice.mp3")
                                playsound("voice.mp3")
                                os.remove("voice.mp3")
                                

                                break
                        
                                
                        except Exception as e:
                            print("face not recognized")
                            mytext="face not recognized"

                            language = 'en'

                            v = gTTS(text=mytext,lang=language,slow=False,tld='ie')

                            v.save("voice.mp3")
                            playsound("voice.mp3")
                            os.remove("voice.mp3")
                            break
                        
                        
                        if key==ord('q') or key==27:
                            break
                        
                            
                            
                    cam.release()
                    cv2.destroyAllWindows()
                

                TrackImages()

     
            btn1 = Button(subapp1,command = capture_image, text = "Capture Image", bg = "#f5bce2", fg = "black", font = ("Arial black",12,))
            btn1.place(x = 250, y = 250)
            btn2 = Button(subapp1,command = attendance, text = "Mark Attendance", bg = "#f5bce2", fg = "black", font = ("Arial black",12,))
            btn2.place(x = 50, y = 250)
        else:
            subapp2 = Toplevel(loginapp)

            subapp2.title("Manu")

            subapp2.geometry("800x360")
            subapp2.configure(background = "#f5bce2")
            lab1 = Label(subapp2,text = "username and password wrong  ", bg = "#f5bce2", fg = "black", font = ("Arial black",26,))
            lab1.grid(row = 0, column = 0, padx = (100,20), pady = (150))
            print("Username and password wrong")
            v = gTTS(text="Username and password is wrong please enter correct username and password",lang='en',slow=False,tld='ie')

            v.save("voice.mp3")
            playsound("voice.mp3")
            os.remove("voice.mp3")

        
    lab1 = Label(loginapp,text = "Enter your  username : ", bg = "#f5bce2", fg = "black", font = ("Arial black",12,))
    lab2 = Label(loginapp,text = "Enter your password : ", bg = "#f5bce2", fg = "black", font = ("Arial black",12,))
    
    
    lab1.grid(row = 1, column = 0, padx = (10,20), pady = (10))
    lab2.grid(row = 2, column = 0, padx = (60,20), pady = (10))
     

    en1 = Entry(loginapp, textvariable = username, bg = "#f5bce2", fg = "black", font = ("Arial black",12,))
    en2 = Entry(loginapp, textvariable = password, bg = "#f5bce2", show = "*",fg = "black", font = ("Arial black",12,))

    
    en1.grid(row = 1, column = 1, padx = (10,20), pady = (10))
    en2.grid(row = 2, column = 1, padx = (10,20), pady = (10))


    btn1 = Button(loginapp,command = submit, text = "Login", bg = "#f5bce2", fg = "black", font = ("Arial black",12,))
    btn1.place(x = 250, y = 250)


    app.mainloop()
        


img = Image.open('background.jpg')
bg = ImageTk.PhotoImage(img)
label = Label(app, image=bg)
label.place(x = 0,y = 0)


lab1 = Label(app,text = "Do you want to login or register : ", bg = "#f5bce2", fg = "black", font = ("Arial black",12,))
lab1.place(x=100,y=50)

btn1 = Button(app,command = signup, text = "Signup", bg = "#f5bce2", fg = "black", font = ("Arial black",12,))
btn1.place(x = 150, y = 150)

btn1 = Button(app,command = login, text = "Login", bg = "#f5bce2", fg = "black", font = ("Arial black",12,))
btn1.place(x = 250, y = 150)


app.mainloop()



