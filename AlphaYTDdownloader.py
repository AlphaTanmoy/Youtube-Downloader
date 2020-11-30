from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import ttk
from threading import *

file_size = 0

def Start_Download():
    global file_size
    try:
        url = urlField.get()
        choice = ytdchoices.get()
        #changing Button Text!
        dbtn.config(text="Please wait...")
        dbtn.config(state=DISABLED)
        path_of_video = askdirectory()
        print(url)
        print(path_of_video)
        #ob = YouTube(url)
        ob = YouTube(url)
        
        if(len(url)>1):
            if(choice == choices[0]):
                strm_video = ob.streams.filter(progressive=True).first()
                dbtn1.config(text="Downloading Your Video")
                print("Downloading Video")
            #elif(choice == choices[1]):
            #    strm_video = ob.streams.filter(progressive=True).last()
            #    dbtn1.config(text="Downloading Your Video")
            #    print("Downloading Video")
            elif(choice == choices[2]):
                strm_video = ob.streams.filter(only_audio=True).first()
                #strm_video = ob.streams.filter(file_extension='mp3').first()
                dbtn1.config(text="Downloading Your Audio")
                print("Downloading Audio")

        print(file_size) 
        vtitle.config(text=strm_video.title)
        num1 = round((strm_video.filesize/1024/1024))
        num2 = str(num1)+" Mb"
        dbtn2.config(text=num2)
        #Creating Youtube Object With URL
        #printing all possible streams
        #strm_main_video = ob.streams.all()
        #strm_video = ob.streams.filter(progressive=True).first()
        #strm_audio = ob.streams.filter(only_audio=True).first()
        #print(strm_video) # showing the actualla stream
        #print(strm_video.filesize) #showing size of the Downloadable file
        #print(strm_video.title) # Showing Title of the Downloadable file
        #print(strm_video.resolution) #Showing Resolution of the Downloadable file
        #For Downloading Audio And Video
        strm_video.download(path_of_video)
        print("done.....!")
        dbtn.config(text="Start Another One!")
        urlField.delete(0,END)
        dbtn.config(state=NORMAL)
        showinfo("Download Completed", "Downloaded Successfully!")
        dbtn1.config(text="Progress of ...!")
        dbtn2.config(text="Size will be")

    except Exception as e:
        print(e)
        print("Error !!")
        #showinfo("Re-Stat the Application!","You did't paste a workable URL in the field!")
        showinfo("Error!! <_>","Sorry an Error Occure,Please Close The Application And Restart It.")

def Start_Download_Thread():
    #creating thread
    thread = Thread(target=Start_Download)
    thread.start()



#User Interface
main = Tk()
#setting Title
main.title("Alpha Youtube Downloader")   
#setting icon
main.iconbitmap(r'C:\\Users\\TANMOY DAS\\Desktop\\Folders\\AlphaYtd\\logo.ico')
main.geometry("500x600")
#heading Icon
file = PhotoImage(file=r'C:\\Users\\TANMOY DAS\\Desktop\\Folders\\AlphaYtd\\logo.png')
headingIcon = Label(main,image=file)
headingIcon.pack(side=TOP, pady=5)
#instruction
instLabel = Label(main,text="Enter the URL of the Video",font=("Calibri",15))
instLabel.pack(side=TOP, pady=5)
#url Holder
urlField = Entry(main,justify=CENTER, font="Century")
urlField.pack(side=TOP, fill = X, padx=30, pady=5)

#combobox Holder Section
comboxLabel = Label(main,text="What will You Download?",font=("Calibri",15))
comboxLabel.pack(side=TOP, pady=5)
#choices = ["Possible Best Video Quality","Possible 2nd Best Video Quality","Possible Best Audio Quality"]
choices = ["Possible Best Video Quality","Possible Best Audio Quality"]
ytdchoices = ttk.Combobox(main,values=choices)
ytdchoices.pack(side=TOP, fill=X, padx=145, pady=5)
#download Button
dbtn = Button(main, width=19, bd=4, font="Century", text="Start Download", bg="Light Blue", fg="Black", command=Start_Download_Thread)
dbtn.pack(side=TOP, pady=5)
#video Title
vtitle = Label(main,text="Video Title", bg="Light Green", fg="black", font=("Century",10))
vtitle.pack(side=TOP, pady=5)
#dbtn1 = Button(main, width=19, bd=4, font="Century", text="Downloading Progress", bg="Light Green", fg="Black")
#dbtn1.pack(side=TOP, pady=90)
#Secondary heading Icon for Audio to video Convertion
#file1 = PhotoImage(file='Logo2.png')
#secondaryIcon = Label(main,image=file1)
#secondaryIcon.pack(side=TOP, pady=5)
#Convertion & Download Button to Audio
dbtn1 = Button(main, width=25, bd=4, font="Century", text="Progress of ...", bg="pink", fg="black")
dbtn1.pack(side=TOP, pady=5)
dbtn1.config(state=DISABLED)
dbtn2 = Button(main, width=25, bd=4, font="Century", text="Size will be in MB", bg="Orange", fg="black")
dbtn2.pack(side=TOP, pady=45)
dbtn2.config(state=DISABLED)
#developer Label
developerlabel = Label(main,text="Created By AlphaTanmoy",font=("Broadway",10))
developerlabel.pack()
main.mainloop()