from tkinter import *

windows = Tk()
windows.title("Restaurant billing system")
windows.geometry("1250x700")

Heading_Label = Label(windows,text="BIG WIZZ CAFE AND RESTAURANT BILLING SYSTEM",font=("Arial black",30,"bold"),
                      bg="grey25",fg="yelloW",relief=GROOVE)
Heading_Label.pack(fill=X)

Customer_details_frame = Label(windows,text="Customer Details Section",font=("times new roman,",15,"bold"),bg="gray25"
                               ,fg="yellow",bd=8,relief=GROOVE)
Customer_details_frame.pack()

Name_label = Label(Customer_details_frame,text="Name..",font=("times new roman,",15,"bold"),bg="gray25",fg="white")
Name_label.grid(row=0,column=0)
Name_Entry = Entry(Customer_details_frame)
Name_Entry.grid(row=0,column=1)

Phone_label = Label(Customer_details_frame,text="Phone",font=("times new roman,",15,"bold"),bg="gray25",fg="white")
Phone_label.grid(row=0,column=2)
Phone_Entry = Entry(Customer_details_frame)
Phone_Entry.grid(row=0,column=3)

Bill_no_label = Label(Customer_details_frame,text="Bill no",font=("times new roman,",15,"bold"),bg="gray25",fg="white")
Bill_no_label.grid(row=0,column=4)
Bill_no_Entry = Entry(Customer_details_frame)
Bill_no_Entry.grid(row=0,column=5)

Search_btn = Button(Customer_details_frame,text="search")
Search_btn.grid(row=0,column=6)




windows.mainloop()