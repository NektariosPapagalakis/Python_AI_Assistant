from tkinter import *
import time
from threading import *

class Timer(Tk):

    #BACKGROUND_COLOR = "#2C2C2C"
    #SECOND_COLOR = "#5B5B5B"
    def __init__(self):
        super(Timer,self).__init__()

        self.timer_status = "stoped"
        self.hour = 0
        self.minutes = 0
        self.seconds =0

        def timer():
            if self.timer_status == "running":
                self.seconds = self.seconds + 1
                if self.seconds == 60:
                    self.seconds = 0
                    self.minutes = self.minutes + 1
                    if self.minutes == 60:
                        self.minutes = 0
                        self.hour = self.hour + 1
                desplay_time()
                #1000 ms -> 1 sec
                self.after(1,timer)


        def start_timer():
            self.timer_status = "running"
            timer()

        def pause_timer():
                self.timer_status = "paused"

        def stop_timer():
                self.timer_status = "stoped"
                self.hour = 0
                self.minutes = 0
                self.seconds =0
                desplay_time()

        def desplay_time():
            #--hour_label
            if self.hour <10:
                hour_label.config(text = "0"+str(self.hour))
            else:
                hour_label.config(text = str(self.hour))
            #--Minutes
            if self.minutes <10:
                minutes_label.config(text = "0"+str(self.minutes))
            else:
                minutes_label.config(text = str(self.minutes))
            #--Seconds
            if self.seconds <10:
                seconds_label.config(text = "0"+str(self.seconds))
            else:
                seconds_label.config(text = str(self.seconds))

        
        self.geometry("500x200")
        self.title('Find Wifi Password')
        #window.configure(background=BACKGROUND_COLOR)

        #Create Frames
        frame_timer_type = Frame(self)
        frame_time_labels = Frame(self)
        frame_time_enterys = Frame(self)
        frame_buttons = Frame(self)

        #Time Enterys
        hour_entery = En(frame_time_enterys,text='00', width=5)
        #Time Labels
        #--hour_label
        hour_label = Label(frame_time_labels,text='00', width=5)
        separator_1= Label(frame_time_labels,text=':', width=5)
        #--Minutes
        minutes_label = Label(frame_time_labels,text='00', width=5)
        separator_2= Label(frame_time_labels,text=':', width=5)
        #--Seconds
        seconds_label = Label(frame_time_labels,text='00', width=5)

        #Buttons
        countdown_button = Button(frame_timer_type,text='Countdown', width=10,foreground="red")
        timer_button = Button(frame_timer_type,text='Timer', width=10,foreground="red")
        
        start_button = Button(frame_buttons,text='Start', width=10,foreground="red",command=start_timer)
        pause_button = Button(frame_buttons,text='Pause', width=10,foreground="red",command=pause_timer)
        stop_button = Button(frame_buttons,text='Stop', width=10,foreground="red",command=stop_timer)


        #Plece at Window
        frame_timer_type.pack(fill=BOTH, expand=YES)
        countdown_button.grid(row=0, column=0,padx=(2,10))
        timer_button.grid(row=0, column=1)

        frame_time_labels.pack(pady=20)
        #--Hour
        hour_label.grid(row=0, column=0)
        separator_1.grid(row=0, column=1)
        #--Minutes
        minutes_label.grid(row=0, column=2)
        separator_2.grid(row=0, column=3)
        #--Seconds
        seconds_label.grid(row=0, column=4)

        frame_buttons.pack(pady=20)
        start_button.grid(row=0, column=9,padx=10)
        pause_button.grid(row=0, column=10,padx=10)
        stop_button.grid(row=0, column=11,padx=10)

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = Timer()
    app.start()
