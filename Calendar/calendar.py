from tkinter import *
from tkinter import messagebox
import time


class Alarm:
    def __init__(self, title, alarm_time, snooze, state):
        super(Alarm, self).__init__()
        self.alarm_time = alarm_time
        self.title = title
        self.snooze = snooze
        self.state = state

    def get_alarm_title(self):
        return self.title

    def get_alarm_time(self):
        return self.alarm_time

    def get_alarm_snooze(self):
        return self.snooze

    def get_alarm_state(self):
        return self.state


class AlarmWindow(Tk):
    def __init__(self, alarm):
        super(AlarmWindow, self).__init__()
        self.geometry("400x190")
        self.title('Timer')

        title = Label(self, text=alarm.get_alarm_title(), pady=10, font=('Arial', 25))
        title.pack()

        time_label = Label(self, text=alarm.get_alarm_time(), pady=5, font=('Arial', 15))
        time_label.pack()

        frame_buttons = Frame(self)
        frame_buttons.pack(pady=5)

        stop_button = Button(frame_buttons, text="Stop", font=('Arial', 15), width=20)
        stop_button.pack(pady=(5, 2))
        snooze_button = Button(frame_buttons, text="Snooze", font=('Arial', 15), width=13)
        snooze_button.pack(pady=(2, 5))

    def on_closing(self):
        self.destroy()

    def start(self):
        self.mainloop()


class Clock(Tk):

    def __init__(self):
        super(Clock, self).__init__()

        # Temp
        self.alarm1 = Alarm("Alarm1 Title", "1:10", "00:10", "off")
        self.alarm2 = Alarm("Alarm2 Title", "2:10", "00:20", "off")
        self.alarm3 = Alarm("Alarm3 Title", "3:10", "00:30", "on")

        self.alarm_list = (self.alarm1, self.alarm2, self.alarm3)
        # Temp

        self.timer_status = "stopped"
        self.timer_or_countdown_status = "timer"
        self.time_format = "12-Hour"
        self.hour = 0
        self.minutes = 0
        self.seconds = 0
        self.is_alarm_selected = "no"

        self.hour_countdown_start = 0
        self.minutes_countdown_start = 2
        self.seconds_countdown_start = 0

        def go_to_countdown():
            self.title('Countdown')
            self.geometry("500x200")

            if self.timer_status == 'running':
                stop_timer()

            if self.timer_or_countdown_status == "clock":
                frame_clock_buttons.pack_forget()
                frame_timer_and_countdown_buttons.pack(pady=20)

            if self.timer_or_countdown_status == "alarm":
                frame_time_labels.pack(pady=20)
                frame_timer_and_countdown_buttons.pack(pady=20)
                frame_alarm.pack_forget()

            self.timer_or_countdown_status = "countdown"
            hour_entry.grid(row=0, column=0, padx=(2, 10))
            separator_3.grid(row=0, column=1, padx=(2, 10))
            minutes_entry.grid(row=0, column=2, padx=(2, 10))
            separator_4.grid(row=0, column=3, padx=(2, 10))
            seconds_entry.grid(row=0, column=4, padx=(2, 10))

        def go_to_timer():
            self.title('Timer')
            self.geometry("500x200")

            if self.timer_status == 'running':
                stop_timer()

            if self.timer_or_countdown_status == "countdown":
                hour_entry.grid_forget()
                separator_3.grid_forget()
                minutes_entry.grid_forget()
                separator_4.grid_forget()
                seconds_entry.grid_forget()

            elif self.timer_or_countdown_status == "clock":
                frame_clock_buttons.pack_forget()
                frame_timer_and_countdown_buttons.pack(pady=20)

            elif self.timer_or_countdown_status == "alarm":
                frame_time_labels.pack(pady=20)
                frame_timer_and_countdown_buttons.pack(pady=20)
                frame_alarm.pack_forget()

            self.timer_or_countdown_status = "timer"

        def go_to_clock():
            self.title('Clock')
            if self.timer_status == 'running':
                stop_timer()
            self.geometry("500x200")

            if self.timer_or_countdown_status == "countdown":
                hour_entry.grid_forget()
                separator_3.grid_forget()
                minutes_entry.grid_forget()
                separator_4.grid_forget()
                seconds_entry.grid_forget()

            elif self.timer_or_countdown_status == "alarm":
                frame_time_labels.pack(pady=20)
                frame_clock_buttons.pack(pady=20)
                frame_alarm.pack_forget()

            self.timer_or_countdown_status = "clock"
            frame_timer_and_countdown_buttons.pack_forget()
            frame_clock_buttons.pack(pady=20)
            clock()

        def go_to_alarms():
            self.title('Alarm')
            if self.timer_status == 'running':
                stop_timer()
            self.geometry("500x250")

            if self.timer_or_countdown_status == "timer":
                frame_time_labels.pack_forget()
                frame_timer_and_countdown_buttons.pack_forget()
            elif self.timer_or_countdown_status == "countdown":
                hour_entry.grid_forget()
                separator_3.grid_forget()
                minutes_entry.grid_forget()
                separator_4.grid_forget()
                seconds_entry.grid_forget()
                frame_timer_and_countdown_buttons.pack_forget()
                frame_time_labels.pack_forget()
            elif self.timer_or_countdown_status == "clock":
                frame_time_labels.pack_forget()
                frame_clock_buttons.pack_forget()

            self.timer_or_countdown_status = "alarm"
            frame_alarm.pack(side="top", fill="x")

        def select_alarm(event):
            self.is_alarm_selected = "yes"
            create_edit_alarm_button.config(text="Save")

            selection = event.widget.curselection()
            index = selection[0]

            alarm_title_entry.delete(0, END)
            alarm_title_entry.insert(0, self.alarm_list[index].get_alarm_title())

            alarm_time = self.alarm_list[index].get_alarm_time()
            alarm_time = alarm_time.split(":")
            alarm_hour_entry.delete(0, END)
            alarm_hour_entry.insert(0, alarm_time[0])
            alarm_minutes_entry.delete(0, END)
            alarm_minutes_entry.insert(0, alarm_time[1])

            snooze_time = self.alarm_list[index].get_alarm_snooze()
            snooze_time = snooze_time.split(":")
            alarm_snooze_time_hour_entry.delete(0, END)
            alarm_snooze_time_hour_entry.insert(0, snooze_time[0])
            alarm_snooze_time_minutes_entry.delete(0, END)
            alarm_snooze_time_minutes_entry.insert(0, snooze_time[1])

        def clear_alarm_tile(event):
            if self.is_alarm_selected == "no":
                alarm_title_entry.delete(0, END)
                alarm_title_entry.insert(0, "")

        def alarm_check():
            alarm_tile = alarm_title_entry.get()
            if alarm_tile == "":
                alarm_tile = "Alarm"
            else:
                alarm_hour = alarm_hour_entry.get()
                if int(alarm_hour) < 0 or int(alarm_hour) > 23:
                    messagebox.showerror('Error', 'The field hour must be\nbetween 0 and 23')
                    alarm_hour_entry.focus()
                else:
                    alarm_minutes = alarm_minutes_entry.get()
                    if int(alarm_minutes) < 0 or int(alarm_minutes) > 29:
                        messagebox.showerror('Error', 'The field minutes must be\nbetween 0 and 59')
                        alarm_minutes_entry.focus()
                    else:
                        alarm_snooze_hour = alarm_snooze_time_hour_entry.get()
                        if int(alarm_snooze_hour) < 0 or int(alarm_snooze_hour) > 23:
                            messagebox.showerror('Error', 'The field Snooze hour\nmust be between 0 and 23')
                            alarm_snooze_time_hour_entry.focus()
                        else:
                            alarm_snooze_minutes = alarm_snooze_time_minutes_entry.get()
                            if int(alarm_snooze_minutes) < 0 or int(alarm_snooze_minutes) > 23:
                                messagebox.showerror('Error', 'The field Snooze minutes\nmust be between 0 and 59')
                                alarm_snooze_time_minutes_entry.focus()
                            else:
                                messagebox.showinfo('Complete', 'The alarm is\nsuccessfully created')

        def new_alarm():
            self.is_alarm_selected = "no"
            create_edit_alarm_button.config(text="Create")
            list_of_created_alarms.selection_clear(0, END)

            alarm_title_entry.delete(0, END)
            alarm_title_entry.insert(0, "Alarm Title")

            alarm_hour_entry.delete(0, END)
            alarm_hour_entry.insert(0, "00")
            alarm_minutes_entry.delete(0, END)
            alarm_minutes_entry.insert(0, "00")

            alarm_snooze_time_hour_entry.delete(0, END)
            alarm_snooze_time_hour_entry.insert(0, "00")
            alarm_snooze_time_minutes_entry.delete(0, END)
            alarm_snooze_time_minutes_entry.insert(0, "00")

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
                # 1000 ms -> 1 sec
                self.after(1000, timer)

        def countdown():
            if self.timer_status == "running":
                if self.seconds > 0:
                    self.seconds = self.seconds - 1
                elif self.seconds == 0:
                    self.seconds = 59
                    if self.minutes > 0:
                        self.minutes = self.minutes - 1
                    elif self.minutes == 0:
                        self.minutes = 59
                        if self.hour > 0:
                            self.hour = self.hour - 1
                        elif self.hour == 0:
                            stop_timer()
                            end_message = 'Timer '
                            if self.hour_countdown_start < 10:
                                end_message = end_message + "0" + str(self.hour_countdown_start) + " : "
                            else:
                                end_message = end_message + str(self.hour_countdown_start) + " : "
                            if self.minutes_countdown_start < 10:
                                end_message = end_message + "0" + str(self.minutes_countdown_start) + " : "
                            else:
                                end_message = end_message + str(self.minutes_countdown_start) + " : "
                            if self.seconds_countdown_start < 10:
                                end_message = end_message + "0" + str(self.seconds_countdown_start)
                            else:
                                end_message = end_message + str(self.seconds_countdown_start)

                            messagebox.showwarning('Time is Up', end_message)
                display_time()
                # 1000 ms -> 1 sec
                self.after(1000, countdown)

        def clock():
            self.hour = int(time.strftime("%H", time.localtime()))
            if self.time_format == "12-Hour":
                if self.hour == 0:
                    self.hour = 12
                elif self.hour > 12:
                    self.hour = self.hour - 12
            self.minutes = int(time.strftime("%M", time.localtime()))
            self.seconds = int(time.strftime("%S", time.localtime()))
            self.timer_status = "running"
            timer()

        def start_timer():
            if self.timer_or_countdown_status == "timer":
                self.timer_status = "running"
                timer()
            elif self.timer_or_countdown_status == "countdown":
                if self.timer_status == "stoped":
                    self.seconds_countdown_start = seconds_entry.get()
                    self.seconds_countdown_start = int(self.seconds_countdown_start)
                    self.seconds = self.seconds_countdown_start

                    self.minutes_countdown_start = minutes_entry.get()
                    self.minutes_countdown_start = int(self.minutes_countdown_start)
                    self.minutes = self.minutes_countdown_start

                    self.hour_countdown_start = hour_entry.get()
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
            self.seconds = 0
            display_time()

        def display_time():
            # --hour_label
            if self.hour < 10:
                hour_label.config(text="0" + str(self.hour))
            else:
                hour_label.config(text=str(self.hour))
            # --Minutes
            if self.minutes < 10:
                minutes_label.config(text="0" + str(self.minutes))
            else:
                minutes_label.config(text=str(self.minutes))
            # --Seconds
            if self.seconds < 10:
                seconds_label.config(text="0" + str(self.seconds))
            else:
                seconds_label.config(text=str(self.seconds))

        def change_time_format():
            if self.time_format == "12-Hour":
                self.time_format = "24-Hour"
            elif self.time_format == "24-Hour":
                self.time_format = "12-Hour"
            time_format_button.config(text=self.time_format)
            go_to_clock()

        self.geometry("500x200")
        self.title('Clock')

        # Create Frames
        frame_timer_type = Frame(self)
        frame_time_labels = Frame(self)
        frame_time_entrys = Frame(self)
        frame_timer_and_countdown_buttons = Frame(self)
        frame_clock_buttons = Frame(self)

        # Time Entry
        hour_entry = Entry(frame_time_entrys, width=5)
        hour_entry.insert(0, "00")
        separator_3 = Label(frame_time_entrys, text=':', width=5)
        minutes_entry = Entry(frame_time_entrys, width=5)
        minutes_entry.insert(0, "00")
        separator_4 = Label(frame_time_entrys, text=':', width=5)
        seconds_entry = Entry(frame_time_entrys, width=5)
        seconds_entry.insert(0, "00")
        # Time Labels
        # --hour_label
        hour_label = Label(frame_time_labels, text='00', width=5)
        separator_1 = Label(frame_time_labels, text=':', width=5)
        # --Minutes
        minutes_label = Label(frame_time_labels, text='00', width=5)
        separator_2 = Label(frame_time_labels, text=':', width=5)
        # --Seconds
        seconds_label = Label(frame_time_labels, text='00', width=5)

        # Buttons
        countdown_button = Button(frame_timer_type, text='Countdown', width=10, foreground="red",
                                  command=go_to_countdown)
        timer_button = Button(frame_timer_type, text='Timer', width=10, foreground="red", command=go_to_timer)
        clock_button = Button(frame_timer_type, text='Clock', width=10, foreground="red", command=go_to_clock)
        alarm_button = Button(frame_timer_type, text='Alarms', width=10, foreground="red", command=go_to_alarms)

        start_button = Button(frame_timer_and_countdown_buttons, text='Start', width=10, foreground="red",
                              command=start_timer)
        pause_button = Button(frame_timer_and_countdown_buttons, text='Pause', width=10, foreground="red",
                              command=pause_timer)
        stop_button = Button(frame_timer_and_countdown_buttons, text='Stop', width=10, foreground="red",
                             command=stop_timer)

        time_format_button = Button(frame_clock_buttons, text=self.time_format, width=10, foreground="red",
                                    command=change_time_format)
        time_format_button.grid(row=0, column=10, padx=10)

        #             ALARM
        frame_alarm = Frame(self)
        frame_list_of_alarms = Frame(frame_alarm)
        frame_create_edit_alarm = Frame(frame_alarm)

        frame_list_of_alarms.grid(row=0, column=0, padx=10, sticky='w')
        frame_create_edit_alarm.grid(row=0, column=1, padx=10)

        alarms = []
        for a in self.alarm_list:
            alarms.append(a.get_alarm_title() + "   " + a.get_alarm_time())
        alarms_var = StringVar(value=alarms)

        list_of_created_alarms = Listbox(frame_list_of_alarms, listvariable=alarms_var, selectmode='extended', width=25)
        list_of_created_alarms.bind('<<ListboxSelect>>', select_alarm)
        list_of_created_alarms.pack(pady=5)

        new_alarm_button = Button(frame_list_of_alarms, text="New Alarm", command=new_alarm)
        new_alarm_button.pack(pady=(5, 10))

        alarm_title_entry = Entry(frame_create_edit_alarm)
        alarm_title_entry.bind("<Button-1>",clear_alarm_tile)
        alarm_title_entry.insert(0, 'Alarm Title')
        alarm_title_entry.pack(padx=10)

        frame_create_edit_alarm_time = Frame(frame_create_edit_alarm)
        frame_create_edit_alarm_time.pack(pady=10)

        frame_create_edit_alarm_snooze = Frame(frame_create_edit_alarm)
        frame_create_edit_alarm_snooze.pack(pady=10)

        alarm_hour_entry = Entry(frame_create_edit_alarm_time, width=5)
        alarm_hour_entry.insert(0, "00")
        separator_5 = Label(frame_create_edit_alarm_time, text=':', width=5)
        alarm_minutes_entry = Entry(frame_create_edit_alarm_time, width=5)
        alarm_minutes_entry.insert(0, "00")

        alarm_hour_entry.grid(row=0, column=0)
        separator_5.grid(row=0, column=1)
        alarm_minutes_entry.grid(row=0, column=2)

        alarm_snooze_time_label = Label(frame_create_edit_alarm_snooze, text='Snooze Time : ')
        alarm_snooze_time_hour_entry = Entry(frame_create_edit_alarm_snooze, width=5)
        alarm_snooze_time_hour_entry.insert(0, "00")
        separator_6 = Label(frame_create_edit_alarm_snooze, text=':', width=5)
        alarm_snooze_time_minutes_entry = Entry(frame_create_edit_alarm_snooze, width=5)
        alarm_snooze_time_minutes_entry.insert(0, "00")

        alarm_snooze_time_label.grid(row=0, column=0, padx=(1, 30))
        alarm_snooze_time_hour_entry.grid(row=0, column=1)
        separator_6.grid(row=0, column=2)
        alarm_snooze_time_minutes_entry.grid(row=0, column=3)

        create_edit_alarm_button = Button(frame_create_edit_alarm, text="Create", width=10, command=alarm_check)
        create_edit_alarm_button.pack(pady=10)

        # Place at Window
        frame_timer_type.pack(fill=BOTH, expand=YES)
        countdown_button.grid(row=0, column=0, padx=(2, 10))
        timer_button.grid(row=0, column=1, padx=(2, 10))
        clock_button.grid(row=0, column=2, padx=(2, 10))
        alarm_button.grid(row=0, column=3, padx=(2, 10))

        frame_time_entrys.pack()

        frame_time_labels.pack(pady=20)
        # --Hour
        hour_label.grid(row=0, column=0)
        separator_1.grid(row=0, column=1)
        # --Minutes
        minutes_label.grid(row=0, column=2)
        separator_2.grid(row=0, column=3)
        # --Seconds
        seconds_label.grid(row=0, column=4)

        frame_timer_and_countdown_buttons.pack(pady=20)
        start_button.grid(row=0, column=0, padx=10)
        pause_button.grid(row=0, column=1, padx=10)
        stop_button.grid(row=0, column=2, padx=10)

    def on_closing(self):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = Clock()
    app.start()

    # alarm_window = AlarmWindow(alarm)
    # alarm_window.start()
