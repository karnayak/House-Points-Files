from tkinter import *
import os
import time
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from collections import defaultdict
from collections import deque





# Define
def hello():
    message = Label(root, text="You have successfully entered the current points.")
    message.pack()
now = datetime.datetime.now()
Date = now.strftime("%Y-%m-%d")




# Front-End View
root = Tk()
root.config(bg="pink")
root.geometry("1000x1500")

# Clock
def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    watch.config(text=hour + ":" + minute + ":" + second)
    watch.after(1000, clock)

watch = Label(root, text="", fg="green", bg="black", font=("Helvetica, 20"))
watch.pack(pady=20)

now = datetime.datetime.now()
Date = now.strftime("%Y-%m-%d")


clock()


# Reset

def resetpts():
    os.remove("house points data.txt")
    file = open('house points data.txt')
    successremove = Label(root, text="POINTS SUCCESSFULLY RESET!", bg="pink", fg="black")
    successremove.pack()
    file.close()


reset = Button(root, text="RESET ALL POINTS", bg="black", fg="blue", command=resetpts)
reset.pack()

space1 = Label(root, text="              "
                          "              "
                          "              ", bg="pink")
space1.pack()

## Welcome Scripts


welcomeText = Label(root, text="Welcome to this house points counter.", bg="pink")
welcomeText.pack()
notice = Label(root,
               text="This is a program which will ease the calculation of the house points. Created by Kartik Nayak (Secondary 2)",
               bg="pink")
notice.pack()

space = Label(root, text="          "
                         ""
                         "           ", bg="pink")
space.pack()

## Points Retrieval
asgard_pts_message = Label(root, text="Input the number of points which Asgard got today", bg="light green")
asgard_pts_message.pack()
space_2 = Label(root, text="          ", bg="pink")

space_2.pack()
asgard_pts_enter = Entry(root, fg="green")
asgard_pts_enter.pack()

space_3 = Label(root, text="          ", bg="pink")
space_3.pack()

wakanda_pts_message = Label(root, text="Input the number of points which Wakanda got today", bg="light blue")
wakanda_pts_message.pack()
space_4 = Label(root, text="          ", bg="pink")
space_4.pack()
wakanda_pts_enter = Entry(root, fg="blue")
wakanda_pts_enter.pack()
space_5 = Label(root, text="          ", bg="pink")
space_5.pack()

xandar_pts_message = Label(root, text="Input the number of points which Xandar got today", bg="red")
xandar_pts_message.pack()
space_6 = Label(root, text="          ", bg="pink")
space_6.pack()
xandar_pts_enter = Entry(root, fg="red")
xandar_pts_enter.pack()
space_7 = Label(root, text="          ", bg="pink")
space_7.pack()

valhalla_pts_message = Label(root, text="Input the number of points which Valhalla got today", bg="orange")
valhalla_pts_message.pack()
space_8 = Label(root, text="          ", bg="pink")
space_8.pack()
valhalla_pts_enter = Entry(root, fg="orange")
valhalla_pts_enter.pack()
space_9 = Label(root, text="          ", bg="pink")
space_9.pack()

## Information Scripts

points = Label(root, text="Click on the button below to submit these current points.", bg="pink")
points.pack()

# Houses

teams = ['Asgard: ', "Valhalla:", "Wakanda:", "Xandar:"]
totaltxt = "Asgard: " + str(asgard_pts_enter.get()) + "\n" + "Wakanda: " + str(wakanda_pts_enter.get()) + "\n" + "Xandar: " + str(xandar_pts_enter.get()) + "\n" + "Valhalla: " + str(valhalla_pts_enter.get())


# Email Part of Program

def email():
    contacts = ["kartik.nayak@sis-semarang.org"]
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.starttls()
    mailserver.login("publicbetaprogram@gmail.com", "publicbeta")

    msg = MIMEMultipart()
    msg["From"] = "publicbetprogram@gmail.com"
    msg["To"] = ",".join(contacts)
    msg["Subject"] = f"House Points Info at {Date}"

    file = open("house points data.txt", "r")
    data = file.read()
    file.close()

    msg.attach(MIMEText(data, 'plain'))


    mailserver.sendmail("publicbetaprogram@gmail.com", contacts, msg.as_string())

    successemail = Label(root, text="EMAIL SUCCESSSFULLY SENT!", bg="pink")
    successemail.pack()

## Buttons and Data Retrieval

currentmoment = time.strftime("%H:%M:%S")
def show_data():
    labela = Label(root, text="\n Asgard: " + str(asgard_pts_enter.get()), bg="green", fg="white")
    labela.pack(pady=5)
    labelw = Label(root, text="\nWakanda: " + str(wakanda_pts_enter.get()), bg="blue", fg="white")
    labelw.pack(pady=5)
    labelx = Label(root, text="\nXandar: " + str(xandar_pts_enter.get()), bg="red", fg="white")
    labelx.pack(pady=5)
    labelv = Label(root, text="\nValhalla: " + str(valhalla_pts_enter.get()), bg="#ffa500", fg="white")
    labelv.pack(pady=5)
    currentmomenttxt=Label(root, text="Last updated on: " + currentmoment + "              "
                                                                            "   " + "\n", font="20")
    currentmomenttxt.pack(pady=5)


# Adding Points
def addpts():
    addedpoints = []
    readpoints = []

    file = open("house points data.txt", "r")
    for line in file:
        m = line.strip()
        readpoints.append(m)
    file.close()

    addedpoints.append(str(asgard_pts_enter.get()))
    addedpoints.append(str(xandar_pts_enter.get()))
    addedpoints.append(str(wakanda_pts_enter.get()))
    addedpoints.append(str(valhalla_pts_enter.get()))



    asgard = int(addedpoints [0]) + int(readpoints [1])
    xandar = int(addedpoints [1]) + int(readpoints [3])
    wakanda = int(addedpoints [2]) + int(str(readpoints [5]))
    valhalla = int(addedpoints [3]) + int(readpoints [7])


    file = open('house points data.txt', 'w')
    file.write('Asgard: ')
    file.write('\n')
    file.write(str(asgard))
    file.write('\n')
    file.write('Xandar: ')
    file.write('\n')
    file.write(str(xandar))
    file.write('\n')
    file.write('Wakanda: ')
    file.write('\n')
    file.write(str(wakanda))
    file.write('\n')
    file.write('Valhalla: ')
    file.write('\n')
    file.write(str(valhalla))
    file.close()

    successdata = Label(root, text="DATA SUCCESSFULLY STORED!", bg="pink")
    successdata.pack()

    # Rankings

    overall = [str(asgard), str(xandar), str(wakanda), str(valhalla)]

    d = defaultdict(deque)
    for i, x in enumerate(sorted(overall, reverse=True), start=1):
        d[x].append(i)

    result = [d[x].popleft() for x in overall]

    rank = (
        f"\n The rank of Asgard: {result[0]} \n The rank of Valhalla: {result[1]} \n The rank of Wakanda: {result[2]} \n The rank of Xandar: {result[3]}")

    file = open('house points data.txt', 'a')

    file.write('\n')
    file.write(rank)
    file.close()





def viewdata():
    file = open("house points data.txt", "r")
    readdata = Label(root, text=file.read())
    readdata.pack()


enter2 = Button(root, text="STORE DATA", fg="blue", bg="black")
enter2.config(command=addpts)
enter2.pack()

space_10 = Label(root, text="                     "
                            "        ", bg="pink")
space_10.pack()

enter3 = Button(root, text="SEND EMAIL", fg="blue", bg="black")
enter3.config(command=email)
enter3.pack()

space_11 = Label(root, text="                     "
                            "        ", bg="pink")
space_11.pack()

enter4 = Button(root, text="VIEW CURRENT POINTS", fg="blue", bg="black")
enter4.config(command=viewdata)
enter4.pack()

root.mainloop()

