from tkinter import *

windows = Tk()
windows.title("Restaurant billing system")
windows.geometry("1250x700")

Heading_Label = Label(windows,text="Vellvett Grill Lounge & Restaurant Billing System",font=("Arial black",30,"bold"),
                      bg="grey25",fg="gold",bd=12,relief=GROOVE)
Heading_Label.pack(fill=X,pady=4)

Customer_details_frame = LabelFrame(windows,text="Customer Details Section",font=("times new roman,",15,"bold"),bg="gray25"
                               ,fg="gold",bd=8,relief=GROOVE)
Customer_details_frame.pack(fill=X)

Name_label = Label(Customer_details_frame,text="Name",font=("times new roman,",15,"bold"),bg="gray25",fg="white")
Name_label.grid(row=0,column=0,padx=12,pady=1)
Name_Entry = Entry(Customer_details_frame,font=("times new roman,",15,),bd=7,width=20)
Name_Entry.grid(row=0,column=1,padx=12,pady=1)

Phone_label = Label(Customer_details_frame,text="Phone",font=("times new roman,",15,"bold"),bg="gray25",fg="white")
Phone_label.grid(row=0,column=2,padx=12,pady=1)
Phone_Entry = Entry(Customer_details_frame,font=("times new roman,",15,),bd=7,width=20)
Phone_Entry.grid(row=0,column=3,padx=12,pady=1)

Bill_no_label = Label(Customer_details_frame,text="Bill no",font=("times new roman,",15,"bold"),bg="gray25",fg="white")
Bill_no_label.grid(row=0,column=4,padx=12,pady=1)
Bill_no_Entry = Entry(Customer_details_frame,font=("times new roman,",15,),bd=7,width=20)
Bill_no_Entry.grid(row=0,column=5,padx=12,pady=1)

Search_btn = Button(Customer_details_frame,text="SEARCH",font=("arial",14,"bold",),bd=7)
Search_btn.grid(row=0,column=6,padx=20,pady=1)




windows.mainloop()
