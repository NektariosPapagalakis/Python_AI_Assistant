from tkinter import *
import datetime

class Timer(Tk):

    def __init__(self):
        super(Timer,self).__init__()

        self.month_name = datetime.datetime.now().strftime("%B")
        self.year = datetime.datetime.now().strftime("%Y")

        def put_numbers_on_grid():
            print("ff")

        
        self.geometry("750x500")
        self.title('Calendar')
        put_numbers_on_grid()
        #Create Frames
        frame_month_navigation = Frame(self)
        frame_days = Frame(self)
        

        #Month Navigation
        button_previous_month = Button(frame_month_navigation,text="Prev", width=10)
        button_next_month = Button(frame_month_navigation,text="Next", width=10)
        label_month_name = Label(frame_month_navigation,text=self.month_name + "  "+self.year, width=15,font=('Arial',30))

        #Days Labels
        label_monday = Label(frame_days,text="Monday", width=9,font=('Arial',15))
        label_tuesday = Label(frame_days,text="Tuesday", width=9,font=('Arial',15))
        label_Wednesday = Label(frame_days,text="Wednesday", width=9,font=('Arial',15))
        label_Thursday = Label(frame_days,text="Thursday", width=9,font=('Arial',15))
        label_Friday = Label(frame_days,text="Friday", width=9,font=('Arial',15))
        label_Saturday = Label(frame_days,text="Saturday", width=9,font=('Arial',15))
        label_Sunday = Label(frame_days,text="Sunday", width=9,font=('Arial',15))

        #Number Days Labels
        label_1 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_2 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_3 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_4 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_5 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_6 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_7 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_8 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_9 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_10 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_11 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_12 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_13 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_14 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_15 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_16 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_17 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_18 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_19 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_20 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_21 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_22 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_23 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_24 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_25 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_26 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_27 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_28 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_29 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_30 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_31 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_32= Label(frame_days,text=".", width=9,font=('Arial',10))
        label_33 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_34 = Label(frame_days,text=".", width=9,font=('Arial',10))
        label_35 = Label(frame_days,text=".", width=9,font=('Arial',10))

        #Place on Window
        #Place Frames
        frame_month_navigation.pack(pady=10)
        frame_days.pack(pady=10)

        #Put on frame_month_navigation
        button_previous_month.grid(row=0,column=0,padx=5)
        label_month_name.grid(row=0,column=1,padx=5)
        button_next_month.grid(row=0,column=2,padx=5)

        #Place days Labels on frame_days
        label_monday.grid(row=0,column=0)
        label_tuesday.grid(row=0,column=1)
        label_Wednesday.grid(row=0,column=2)
        label_Thursday.grid(row=0,column=3)
        label_Friday.grid(row=0,column=4)
        label_Saturday.grid(row=0,column=5)
        label_Sunday.grid(row=0,column=6)

        #Place Number on frame_days
        #line 1
        label_1.grid(row=1,column=0)
        label_2.grid(row=1,column=1)
        label_3.grid(row=1,column=2)
        label_4.grid(row=1,column=3)
        label_5.grid(row=1,column=4)
        label_6.grid(row=1,column=5)
        label_7.grid(row=1,column=6)
        #line 2
        label_8.grid(row=2,column=0)
        label_9.grid(row=2,column=1)
        label_10.grid(row=2,column=2)
        label_11.grid(row=2,column=3)
        label_12.grid(row=2,column=4)
        label_13.grid(row=2,column=5)
        label_14.grid(row=2,column=6)
        #line 3
        label_15.grid(row=3,column=0)
        label_16.grid(row=3,column=1)
        label_17.grid(row=3,column=2)
        label_18.grid(row=3,column=3)
        label_19.grid(row=3,column=4)
        label_20.grid(row=3,column=5)
        label_21.grid(row=3,column=6)
        #line 4
        label_22.grid(row=4,column=0)
        label_23.grid(row=4,column=1)
        label_24.grid(row=4,column=2)
        label_25.grid(row=4,column=3)
        label_26.grid(row=4,column=4)
        label_27.grid(row=4,column=5)
        label_28.grid(row=4,column=6)
        #line 5
        label_29.grid(row=5,column=0)
        label_30.grid(row=5,column=1)
        label_31.grid(row=5,column=2)
        label_32.grid(row=5,column=3)
        label_33.grid(row=5,column=4)
        label_34.grid(row=5,column=5)
        label_35.grid(row=5,column=6)

        



        

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()

if __name__ == "__main__":
    app = Timer()
    app.start()