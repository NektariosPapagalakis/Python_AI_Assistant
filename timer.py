from tkinter import *
from tkinter import messagebox
import time

class Timer(Tk):

    def __init__(self):
        super(Timer,self).__init__()

        self.timer_status = "stoped"
        self.timer_or_countdown_status = "timer"
        self.time_format = "12-Hour"
        self.hour = 0
        self.minutes = 0
        self.seconds =0

        self.hour_countdown_start = 0
        self.minutes_countdown_start = 2
        self.seconds_countdown_start =0

        def go_to_countdown():
            if self.timer_or_countdown_status == "timer":
                self.title('Countdown')
                self.timer_or_countdown_status = "countdown"
                hour_entery.grid(row=0, column=0,padx=(2,10))
                separator_3.grid(row=0, column=1,padx=(2,10))
                minutes_entery.grid(row=0, column=2,padx=(2,10))
                separator_4.grid(row=0, column=3,padx=(2,10))
                seconds_entery.grid(row=0, column=4,padx=(2,10))
                stop_timer()

        def go_to_timer():
            if self.timer_or_countdown_status == "countdown":
                self.title('Timer')
                self.timer_or_countdown_status = "timer"
                hour_entery.grid_forget()
                separator_3.grid_forget()
                minutes_entery.grid_forget()
                separator_4.grid_forget()
                seconds_entery.grid_forget()
                stop_timer()

        def go_to_clock():
            start_button.grid_forget()
            pause_button.grid_forget()
            stop_button.grid_forget()
            time_format_button.grid(row=0, column=10,padx=10)
            start_timer()

        def timer():
            if self.timer_status == "running":
                self.seconds = self.seconds + 1
                if self.seconds == 60:
                    self.seconds = 0
                    self.minutes = self.minutes + 1
                    if self.minutes == 60:
                        self.minutes = 0
                        self.hour = self.hour + 1
                display_time()
                #1000 ms -> 1 sec
                self.after(1000,timer)
            
        def countdown():
            if self.timer_status == "running":
                if self.seconds > 0:
                    self.seconds = self.seconds - 1
                elif self.seconds == 0:
                    self.seconds = 59
                    if self.minutes > 0 :
                        self.minutes = self.minutes - 1
                    elif self.minutes == 0:
                        self.minutes = 59
                        if self.hour > 0:
                            self.hour = self.hour -1
                        elif self.hour == 0:
                            stop_timer()
                            end_message = 'Timer '
                            if self.hour_countdown_start <10:
                                end_message = end_message + "0"+str(self.hour_countdown_start)+" : "
                            else:
                                end_message = end_message +str(self.hour_countdown_start)+" : "
                            if self.minutes_countdown_start <10:
                                end_message = end_message + "0"+str(self.minutes_countdown_start)+" : "
                            else:
                                end_message = end_message +str(self.minutes_countdown_start)+" : "
                            if self.seconds_countdown_start <10:
                                end_message = end_message + "0"+str(self.seconds_countdown_start)
                            else:
                                end_message = end_message +str(self.seconds_countdown_start)

                            messagebox.showwarning('Time is Up', end_message)
                display_time()
                #1000 ms -> 1 sec
                self.after(1000,countdown)

        def start_timer():                
            if self.timer_or_countdown_status == "timer":
                self.timer_status = "running"
                timer()
            elif self.timer_or_countdown_status == "countdown":
                if self.timer_status == "stoped":
                    self.seconds_countdown_start = seconds_entery.get()
                    self.seconds_countdown_start = int(self.seconds_countdown_start)
                    self.seconds = self.seconds_countdown_start

                    self.minutes_countdown_start = minutes_entery.get()
                    self.minutes_countdown_start = int(self.minutes_countdown_start)
                    self.minutes = self.minutes_countdown_start
                    
                    self.hour_countdown_start = hour_entery.get()
                    self.hour_countdown_start = int(self.hour_countdown_start)
                    self.hour = self.hour_countdown_start
                self.timer_status = "running"
                countdown()
            
        def pause_timer():
                self.timer_status = "paused"

        def stop_timer():
                self.timer_status = "stoped"
                self.hour = 0
                self.minutes = 0
                self.seconds =0
                display_time()

        def display_time():
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

        def change_time_format():
            if self.time_format == "12-Hour":
                self.time_format = "24-Hour"
            elif self.time_format == "24-Hour":
                self.time_format = "12-Hour"
            time_format_button.config(text=self.time_format)
        
        self.geometry("500x200")
        self.title('Timer')

        #Create Frames
        frame_timer_type = Frame(self)
        frame_time_labels = Frame(self)
        frame_time_enterys = Frame(self)
        frame_buttons = Frame(self)

        #Time Enterys
        hour_entery = Entry(frame_time_enterys, width=5)
        hour_entery.insert(0, "00")
        separator_3= Label(frame_time_labels,text=':', width=5)
        minutes_entery = Entry(frame_time_enterys, width=5)
        minutes_entery.insert(0, "00")
        separator_4= Label(frame_time_labels,text=':', width=5)
        seconds_entery = Entry(frame_time_enterys, width=5)
        seconds_entery.insert(0, "00")
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
        countdown_button = Button(frame_timer_type,text='Countdown', width=10,foreground="red",command=go_to_countdown)
        timer_button = Button(frame_timer_type,text='Timer', width=10,foreground="red",command=go_to_timer)
        clock_button = Button(frame_timer_type,text='Clock', width=10,foreground="red",command=go_to_clock)
        
        start_button = Button(frame_buttons,text='Start', width=10,foreground="red",command=start_timer)
        pause_button = Button(frame_buttons,text='Pause', width=10,foreground="red",command=pause_timer)
        stop_button = Button(frame_buttons,text='Stop', width=10,foreground="red",command=stop_timer)

        time_format_button = Button(frame_buttons,text=self.time_format, width=10,foreground="red",command=change_time_format)


        #Plece at Window
        frame_timer_type.pack(fill=BOTH, expand=YES)
        countdown_button.grid(row=0, column=0,padx=(2,10))
        timer_button.grid(row=0, column=1,padx=(2,10))
        clock_button.grid(row=0, column=2,padx=(2,10))

        frame_time_enterys.pack()

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
