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

products_frame = Frame(windows)
products_frame.pack()

foods_frame = LabelFrame(products_frame, text="Main dishes", font=("times new roman,", 15, "bold"), fg="gold"
                         , bd=8, relief=GROOVE, bg="gray25")
foods_frame.grid(row=0, column=0, pady=5, padx=5)

jollof_rice_label = Label(foods_frame, text="jollof rice", font=("times new roman,", 10, "bold"), bg="gray25"
                          , fg="white")
jollof_rice_label.grid(row=0, column=0, pady=7, padx=7)
jellof_rice_entry = Entry(foods_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
jellof_rice_entry.grid(row=0, column=1, pady=7, padx=7)

fried_rice_label = Label(foods_frame, text="Fried rice", font=("times new roman,", 10, "bold"), bg="gray25"
                         , fg="white")
fried_rice_label.grid(row=1, column=0, pady=7, padx=7)
fried_rice_entry = Entry(foods_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
fried_rice_entry.grid(row=1, column=1, pady=7, padx=7)

porridge_yam_label = Label(foods_frame, text="Porridge yam", font=("times new roman,", 10, "bold"), bg="gray25"
                           , fg="white")
porridge_yam_label.grid(row=2, column=0, pady=7, padx=7)
porridge_entry = Entry(foods_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
porridge_entry.grid(row=2, column=1, pady=7, padx=7)

spaghetti_label = Label(foods_frame, text="spaghetti", font=("times new roman,", 10, "bold"), bg="gray25"
                        , fg="white")
spaghetti_label.grid(row=3, column=0, pady=7, padx=7)
spaghetti_entry = Entry(foods_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
spaghetti_entry.grid(row=3, column=1, pady=7, padx=7)

Beans_Label = Label(foods_frame, text="Beans", font=("times new roman,", 10, "bold"), bg="gray25"
                    , fg="white")
Beans_Label.grid(row=4, column=0, pady=7, padx=7)
Beans_entry = Entry(foods_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
Beans_entry.grid(row=4, column=1, pady=7, padx=7)

drinks_frame = LabelFrame(products_frame, text="Drinks", font=("times new roman,", 15, "bold"), fg="gold"
                          , bd=8, relief=GROOVE, bg="gray25")
drinks_frame.grid(row=0, column=1, padx=5, pady=5)

coke_label = Label(drinks_frame, text="coke", font=("times new roman,", 10, "bold"), bg="gray25"
                   , fg="white")
coke_label.grid(row=0, column=0, pady=7, padx=7)
coke_entry = Entry(drinks_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
coke_entry.grid(row=0, column=1, pady=7, padx=7)

sprite_label = Label(drinks_frame, text="sprite", font=("times new roman,", 10, "bold"), bg="gray25"
                     , fg="white")
sprite_label.grid(row=1, column=0, pady=7, padx=7)
sprite_entry = Entry(drinks_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
sprite_entry.grid(row=1, column=1, pady=7, padx=7)

malt_label = Label(drinks_frame, text="malt", font=("times new roman,", 10, "bold"), bg="gray25"
                   , fg="white")
malt_label.grid(row=2, column=0, pady=7, padx=7)
malt_entry = Entry(drinks_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
malt_entry.grid(row=2, column=1, pady=7, padx=7)

yoghurt_label = Label(drinks_frame, text="Yoghurt", font=("times new roman,", 10, "bold"), bg="gray25"
                      , fg="white")
yoghurt_label.grid(row=3, column=0, pady=7, padx=7)
yoghurt_entry = Entry(drinks_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
yoghurt_entry.grid(row=3, column=1, pady=7, padx=7)

sosa_Label = Label(drinks_frame, text="Sosa", font=("times new roman,", 10, "bold"), bg="gray25"
                   , fg="white")
sosa_Label.grid(row=4, column=0, pady=7, padx=7)
sosa_entry = Entry(drinks_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
sosa_entry.grid(row=4, column=1, pady=7, padx=7)




windows.mainloop()
