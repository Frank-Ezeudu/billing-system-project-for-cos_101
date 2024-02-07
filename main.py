from tkinter import *
from tkinter import messagebox
import random
bill_number = random.randint(0,1000)


def bill():
    if Name_Entry.get() == '' or Phone_Entry.get() == '':
        messagebox.showerror('Error','Customer details are required')
    elif food_price_entry.get() == '' and meat_price_entry() == '' and drink_price_entry() == '':
        messagebox.showerror('Error','No selected products')
    elif food_price_entry.get() == '0 ₦' and meat_price_entry() == '0 ₦' and drink_price_entry() == '0 ₦':
        messagebox.showerror('Error','No products selected')
    else:
        Text_area.insert(END,'\t\t*** Welcome Customer***')
        Text_area.insert(END,f'\nBill number: {bill_number}')
        Text_area.insert(END,f'\nName:{Name_Entry.get()}')
        Text_area.insert(END,f'\nPhone Number:{Phone_Entry.get()}')
        Text_area.insert(END,f'\t\t Total GROSS BILL =  ')







def calc_total():
    jellof_rice_price = int(jellof_rice_entry.get()) * 850
    fried_rice_price = int(fried_rice_entry.get()) * 1000
    porridge_price = int(porridge_entry.get()) * 700
    spaghetti_price = int(spaghetti_entry.get()) * 800
    beans_price = int(Beans_entry.get()) * 500

    total_food_price = jellof_rice_price + fried_rice_price + porridge_price + spaghetti_price + beans_price
    food_price_entry.delete(0, END)
    food_price_entry.insert(0, f' ₦{total_food_price} ')

    food_tax = total_food_price * 0.01
    food_tax_entry.delete(0,END)
    food_tax_entry.insert(0,f'₦{food_tax}')

    coke_price = int(coke_entry.get()) * 300
    sprite_price = int(sprite_entry.get()) * 300
    malt_price = int(malt_entry.get()) * 500
    yoghurt_price = int(yoghurt_entry.get()) * 1200
    sosa_price = int(sosa_entry.get()) * 700

    total_drink_price = coke_price + sprite_price + malt_price + yoghurt_price + sosa_price
    drink_price_entry.delete(0, END)
    drink_price_entry.insert(0, f'₦{total_drink_price} ')

    drink_tax = total_drink_price * 0.01
    drink_tax_entry.delete(0,END)
    drink_tax_entry.insert(0,f'₦{drink_tax}')

    beef_price = int(beef_entry.get()) * 200
    chicken_price = int(chicken_entry.get()) * 1000
    pork_price = int(pork_entry.get()) * 400
    meatballs_price = int(meatballs_entry.get()) * 500
    sausage_price = int(sausage_entry.get()) * 250

    total_meat_price = beef_price + chicken_price + pork_price + meatballs_price + sausage_price
    meat_price_entry.delete(0, END)
    meat_price_entry.insert(0, f'₦{total_meat_price}')

    meat_tax = total_meat_price * 0.01
    meat_tax_entry.delete(0,END)
    meat_tax_entry.insert(0,f'₦{meat_tax}')

    meatpie_price = int(meatpie_entry.get()) * 600
    shawarma_price = int(shawarma_entry.get()) * 2500
    spring_rolls_price = int(spring_rolls_entry.get()) * 1000
    brownies_price = int(Brownies_entry.get()) * 2000
    burger_price = int(Burger_entry.get()) * 1500

    total_pastry_price = meatpie_price + shawarma_price + spring_rolls_price + brownies_price + burger_price
    pastries_price_entry.delete(0, END)
    pastries_price_entry.insert(0, f'₦{total_pastry_price}')

    pastry_tax = total_pastry_price * 0.01
    pastries_tax_entry.delete(0,END)
    pastries_tax_entry.insert(0,f'₦{pastry_tax}')







windows = Tk()
windows.title("Restaurant billing system")
windows.geometry("1250x700")

Heading_Label = Label(windows, text="Vellvett Grill Lounge & Restaurant Billing System",
                      font=("Arial black", 30, "bold"),
                      bg="gray25", fg="gold", bd=12, relief=GROOVE)
Heading_Label.pack(fill=X, pady=3)

Customer_details_frame = LabelFrame(windows, text="Customer Details Section", font=("times new roman,", 15, "bold"),
                                    bg="gray25"
                                    , fg="gold", bd=8, relief=GROOVE)
Customer_details_frame.pack(fill=X)

Name_label = Label(Customer_details_frame, text="Name", font=("times new roman,", 15, "bold"), bg="gray25", fg="white")
Name_label.grid(row=0, column=0, padx=12, pady=1)
Name_Entry = Entry(Customer_details_frame, font=("times new roman,", 15,), bd=7, width=20)
Name_Entry.grid(row=0, column=1, padx=12, pady=1)

Phone_label = Label(Customer_details_frame, text="Phone", font=("times new roman,", 15, "bold"), bg="gray25",
                    fg="white")
Phone_label.grid(row=0, column=2, padx=12, pady=1)
Phone_Entry = Entry(Customer_details_frame, font=("times new roman,", 15,), bd=7, width=20)
Phone_Entry.grid(row=0, column=3, padx=12, pady=1)

Bill_no_label = Label(Customer_details_frame, text="Bill no", font=("times new roman,", 15, "bold"), bg="gray25",
                      fg="white")
Bill_no_label.grid(row=0, column=4, padx=12, pady=1)
Bill_no_Entry = Entry(Customer_details_frame, font=("times new roman,", 15,), bd=7, width=20)
Bill_no_Entry.grid(row=0, column=5, padx=12, pady=1)

Search_btn = Button(Customer_details_frame, text="SEARCH", font=("arial", 14, "bold",), bd=7)
Search_btn.grid(row=0, column=6, padx=20, pady=1)

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
jellof_rice_entry.insert(0, 0)

fried_rice_label = Label(foods_frame, text="Fried rice", font=("times new roman,", 10, "bold"), bg="gray25"
                         , fg="white")
fried_rice_label.grid(row=1, column=0, pady=7, padx=7)
fried_rice_entry = Entry(foods_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
fried_rice_entry.grid(row=1, column=1, pady=7, padx=7)
fried_rice_entry.insert(0, 0)

porridge_yam_label = Label(foods_frame, text="Porridge yam", font=("times new roman,", 10, "bold"), bg="gray25"
                           , fg="white")
porridge_yam_label.grid(row=2, column=0, pady=7, padx=7)
porridge_entry = Entry(foods_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
porridge_entry.grid(row=2, column=1, pady=7, padx=7)
porridge_entry.insert(0, 0)

spaghetti_label = Label(foods_frame, text="spaghetti", font=("times new roman,", 10, "bold"), bg="gray25"
                        , fg="white")
spaghetti_label.grid(row=3, column=0, pady=7, padx=7)
spaghetti_entry = Entry(foods_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
spaghetti_entry.grid(row=3, column=1, pady=7, padx=7)
spaghetti_entry.insert(0, 0)

Beans_Label = Label(foods_frame, text="Beans", font=("times new roman,", 10, "bold"), bg="gray25"
                    , fg="white")
Beans_Label.grid(row=4, column=0, pady=7, padx=7)
Beans_entry = Entry(foods_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
Beans_entry.grid(row=4, column=1, pady=7, padx=7)
Beans_entry.insert(0, 0)

drinks_frame = LabelFrame(products_frame, text="Drinks", font=("times new roman,", 15, "bold"), fg="gold"
                          , bd=8, relief=GROOVE, bg="gray25")
drinks_frame.grid(row=0, column=1, padx=5, pady=5)

coke_label = Label(drinks_frame, text="coke", font=("times new roman,", 10, "bold"), bg="gray25"
                   , fg="white")
coke_label.grid(row=0, column=0, pady=7, padx=7)
coke_entry = Entry(drinks_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
coke_entry.grid(row=0, column=1, pady=7, padx=7)
coke_entry.insert(0, 0)

sprite_label = Label(drinks_frame, text="sprite", font=("times new roman,", 10, "bold"), bg="gray25"
                     , fg="white")
sprite_label.grid(row=1, column=0, pady=7, padx=7)
sprite_entry = Entry(drinks_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
sprite_entry.grid(row=1, column=1, pady=7, padx=7)
sprite_entry.insert(0, 0)

malt_label = Label(drinks_frame, text="malt", font=("times new roman,", 10, "bold"), bg="gray25"
                   , fg="white")
malt_label.grid(row=2, column=0, pady=7, padx=7)
malt_entry = Entry(drinks_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
malt_entry.grid(row=2, column=1, pady=7, padx=7)
malt_entry.insert(0, 0)

yoghurt_label = Label(drinks_frame, text="Yoghurt", font=("times new roman,", 10, "bold"), bg="gray25"
                      , fg="white")
yoghurt_label.grid(row=3, column=0, pady=7, padx=7)
yoghurt_entry = Entry(drinks_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
yoghurt_entry.grid(row=3, column=1, pady=7, padx=7)
yoghurt_entry.insert(0, 0)

sosa_Label = Label(drinks_frame, text="Sosa", font=("times new roman,", 10, "bold"), bg="gray25"
                   , fg="white")
sosa_Label.grid(row=4, column=0, pady=7, padx=7)
sosa_entry = Entry(drinks_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
sosa_entry.grid(row=4, column=1, pady=7, padx=7)
sosa_entry.insert(0, 0)

meat_frame = LabelFrame(products_frame, text="Meat", font=("times new roman,", 15, "bold"), fg="gold"
                        , bd=8, relief=GROOVE, bg="gray25")
meat_frame.grid(row=0, column=2, padx=5, pady=5)

beef_label = Label(meat_frame, text="Beef", font=("times new roman,", 10, "bold"), bg="gray25"
                   , fg="white")
beef_label.grid(row=0, column=0, pady=7, padx=7)
beef_entry = Entry(meat_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
beef_entry.grid(row=0, column=1, pady=7, padx=7)
beef_entry.insert(0, 0)

chicken_label = Label(meat_frame, text="chicken", font=("times new roman,", 10, "bold"), bg="gray25"
                      , fg="white")
chicken_label.grid(row=1, column=0, pady=7, padx=7)
chicken_entry = Entry(meat_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
chicken_entry.grid(row=1, column=1, pady=7, padx=7)
chicken_entry.insert(0, 0)

pork_label = Label(meat_frame, text="pork chops", font=("times new roman,", 10, "bold"), bg="gray25"
                   , fg="white")
pork_label.grid(row=2, column=0, pady=7, padx=7)
pork_entry = Entry(meat_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
pork_entry.grid(row=2, column=1, pady=7, padx=7)
pork_entry.insert(0, 0)

meatballs_label = Label(meat_frame, text="Meatballs", font=("times new roman,", 10, "bold"), bg="gray25"
                        , fg="white")
meatballs_label.grid(row=3, column=0, pady=7, padx=7)
meatballs_entry = Entry(meat_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
meatballs_entry.grid(row=3, column=1, pady=7, padx=7)
meatballs_entry.insert(0, 0)

sausage_Label = Label(meat_frame, text="Sausage", font=("times new roman,", 10, "bold"), bg="gray25"
                      , fg="white")
sausage_Label.grid(row=4, column=0, pady=7, padx=7)
sausage_entry = Entry(meat_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
sausage_entry.grid(row=4, column=1, pady=7, padx=7)
sausage_entry.insert(0, 0)

pasteries_frame = LabelFrame(products_frame, text="Pastries", font=("times new roman,", 15, "bold"), fg="gold"
                             , bd=8, relief=GROOVE, bg="gray25")
pasteries_frame.grid(row=0, column=3, padx=5, pady=5)

meatpie_label = Label(pasteries_frame, text="Meat_pie", font=("times new roman,", 10, "bold"), bg="gray25"
                      , fg="white")
meatpie_label.grid(row=0, column=0, pady=7, padx=7)
meatpie_entry = Entry(pasteries_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
meatpie_entry.grid(row=0, column=1, pady=7, padx=7)
meatpie_entry.insert(0, 0)

shawarma_label = Label(pasteries_frame, text="shawarma", font=("times new roman,", 10, "bold"), bg="gray25"
                       , fg="white")
shawarma_label.grid(row=1, column=0, pady=7, padx=7)
shawarma_entry = Entry(pasteries_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
shawarma_entry.grid(row=1, column=1, pady=7, padx=7)
shawarma_entry.insert(0, 0)

spring_rolls_label = Label(pasteries_frame, text="Spring rolls", font=("times new roman,", 10, "bold"), bg="gray25"
                           , fg="white")
spring_rolls_label.grid(row=2, column=0, pady=7, padx=7)
spring_rolls_entry = Entry(pasteries_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
spring_rolls_entry.grid(row=2, column=1, pady=7, padx=7)
spring_rolls_entry.insert(0, 0)

Brownies_label = Label(pasteries_frame, text="Brownies", font=("times new roman,", 10, "bold"), bg="gray25"
                       , fg="white")
Brownies_label.grid(row=3, column=0, pady=7, padx=7)
Brownies_entry = Entry(pasteries_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
Brownies_entry.grid(row=3, column=1, pady=7, padx=7)
Brownies_entry.insert(0, 0)

Burger_Label = Label(pasteries_frame, text="Burger", font=("times new roman,", 10, "bold"), bg="gray25"
                     , fg="white")
Burger_Label.grid(row=4, column=0, pady=7, padx=7)
Burger_entry = Entry(pasteries_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
Burger_entry.grid(row=4, column=1, pady=7, padx=7)
Burger_entry.insert(0, 0)

bill_frame = Frame(products_frame)
bill_frame.grid(row=0, column=4, padx=5, pady=5)

bill_area_label = Label(bill_frame, text="Label Area", font=("times new roman", 15, "bold"), bd=8, relief=GROOVE)
bill_area_label.pack(fill=X)
scroll_bar = Scrollbar(bill_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=Y)

Text_area = Text(bill_frame, height=15, width=55, yscrollcommand=scroll_bar.set)
Text_area.pack()


bill_frame = Frame(products_frame)
bill_frame.grid(row=0, column=4, padx=5, pady=5)

bill_area_label = Label(bill_frame, text="Label Area", font=("times new roman", 15, "bold"), bd=8, relief=GROOVE)
bill_area_label.pack(fill=X)
scroll_bar = Scrollbar(bill_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=Y)

Text_area = Text(bill_frame, height=15, width=55, yscrollcommand=scroll_bar.set)
Text_area.pack()


bill_frame = Frame(products_frame)
bill_frame.grid(row=0, column=4, padx=5, pady=5)

bill_area_label = Label(bill_frame, text="Label Area", font=("times new roman", 15, "bold"), bd=8, relief=GROOVE)
bill_area_label.pack(fill=X)
scroll_bar = Scrollbar(bill_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=Y)

Text_area = Text(bill_frame, height=15, width=55, yscrollcommand=scroll_bar.set)
Text_area.pack()

bill_menu_frame = LabelFrame(windows, text="Total bill menu", font=("times new roman,", 15, "bold"), fg="gold"
                             , bd=8, relief=GROOVE, bg="gray25")
bill_menu_frame.pack(fill=X)

food_price_label = Label(bill_menu_frame, text="food price", font=("times new roman,", 10, "bold"), bg="gray25"
                         , fg="white")
food_price_label.grid(row=0, column=0, pady=7, padx=7)
food_price_entry = Entry(bill_menu_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
food_price_entry.grid(row=0, column=1, pady=7, padx=7)

drink_price_label = Label(bill_menu_frame, text="drink price", font=("times new roman,", 10, "bold"), bg="gray25"
                          , fg="white")
drink_price_label.grid(row=1, column=0, pady=7, padx=7)
drink_price_entry = Entry(bill_menu_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
drink_price_entry.grid(row=1, column=1, pady=7, padx=7)

meat_price_label = Label(bill_menu_frame, text="meat price", font=("times new roman,", 10, "bold"), bg="gray25"
                         , fg="white")
meat_price_label.grid(row=0, column=2, pady=7, padx=7)
meat_price_entry = Entry(bill_menu_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
meat_price_entry.grid(row=0, column=3, pady=7, padx=7)

pastries_price_label = Label(bill_menu_frame, text="pastries price", font=("times new roman,", 10, "bold"), bg="gray25"
                             , fg="white")
pastries_price_label.grid(row=1, column=2, pady=7, padx=7)
pastries_price_entry = Entry(bill_menu_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
pastries_price_entry.grid(row=1, column=3, pady=7, padx=7)

food_tax_label = Label(bill_menu_frame, text="food tax", font=("times new roman,", 10, "bold"), bg="gray25"
                       , fg="white")
food_tax_label.grid(row=0, column=4, pady=7, padx=7)
food_tax_entry = Entry(bill_menu_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
food_tax_entry.grid(row=0, column=5, pady=7, padx=7)

drink_tax_label = Label(bill_menu_frame, text="drink tax", font=("times new roman,", 10, "bold"), bg="gray25"
                        , fg="white")
drink_tax_label.grid(row=1, column=4, pady=7, padx=7)
drink_tax_entry = Entry(bill_menu_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
drink_tax_entry.grid(row=1, column=5, pady=7, padx=7)

meat_tax_label = Label(bill_menu_frame, text="meat tax", font=("times new roman,", 10, "bold"), bg="gray25"
                       , fg="white")
meat_tax_label.grid(row=0, column=6, pady=7, padx=7)
meat_tax_entry = Entry(bill_menu_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
meat_tax_entry.grid(row=0, column=7, pady=7, padx=7)

pastries_tax_label = Label(bill_menu_frame, text="pastries tax", font=("times new roman,", 10, "bold"), bg="gray25"
                           , fg="white")
pastries_tax_label.grid(row=1, column=6, pady=7, padx=7)
pastries_tax_entry = Entry(bill_menu_frame, font=("times new roman", 15, "bold"), width=8, bd=5)
pastries_tax_entry.grid(row=1, column=7, pady=7, padx=7)

button_frame = Frame(bill_menu_frame, bd=10, relief=GROOVE)
button_frame.grid(row=0, column=8)

total_button = Button(button_frame, text="TOTAL..", font=("times new roman", 15, "bold"), bg="gray25", fg="white", bd=10
                      , width=12, pady=10,command=calc_total)
total_button.grid(row=0, column=0)

bill_button = Button(button_frame, text="PRINT BILL..", font=("times new roman", 15, "bold"), bg="gray25", fg="white",
                     bd=10
                     , width=12, pady=10,command=bill)
bill_button.grid(row=0, column=1)

windows.mainloop()
