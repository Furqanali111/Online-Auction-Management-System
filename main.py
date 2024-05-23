import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

# starting GUI
root = tk.Tk()
# giving name to application and setting its height and width
root.title("Online Auction")
root.geometry("400x400")

# setting min and max size of the root window
root.minsize(450, 400)
root.maxsize(450, 400)
# creating frames
startwindow = tk.Frame(root)
adminlogin = tk.Frame(root)
admin_page = tk.Frame(root)
check_auction_page=tk.Frame(root)
add_to_auction_page=tk.Frame(root)
final_bid_page=tk.Frame(root)


customerlogin = tk.Frame(root)
customer_page = tk.Frame(root)
register_page = tk.Frame(root)
your_profile_page=tk.Frame(root)
check_cat=tk.Frame(root)
view_bid=tk.Frame(root)
add_item_user=tk.Frame(root)

# database
db_file = 'Auction.db'
#global variables
font=("Arial",10)
global customer_username

def startwindowfun():
    adminbut = tk.Button(startwindow, text="Admin Login", fg="black", height=2, width=20,
                         command=lambda: goto_admin_login(adminlogin))
    adminbut.pack(pady=10)
    customerbut = tk.Button(startwindow, text="Customer Login", fg="black", height=2, width=20,
                            command=lambda: goto_customer_login(customerlogin))
    customerbut.pack()

def goback_start(frame):
    if frame.winfo_ismapped():
        frame.pack_forget()
        for wid in frame.winfo_children():
            wid.destroy()
        startwindow.pack(pady=130)
    pass

def goto_customer_login(frame):
    if startwindow.winfo_ismapped():  # if frame 1 is visible
        startwindow.pack_forget()  # hide frame 1
        customer_login_fun()
        frame.pack(pady=55 )  # show frame 2
    pass

def customer_login_fun():
    label_username = tk.Label(customerlogin, text='User Name:           ', font=("Arial", 11), justify='left', )
    label_username.grid(row=1, column=1)
    entry_username = tk.Entry(customerlogin)
    entry_username.grid(row=2, column=1, pady=(5, 15))

    label_password = tk.Label(customerlogin, text='Password:             ', font=("Arial", 11), justify='left')
    label_password.grid(row=3, column=1)
    entry_password = tk.Entry(customerlogin)
    entry_password.grid(row=4, column=1, pady=5)

    submit_button = tk.Button(customerlogin, text="Login", font=("Arial", 11), width=13, height=1,
                              command=lambda: login_customer(entry_username, entry_password))
    submit_button.grid(row=5, column=1, pady=10)

    register_button = tk.Button(customerlogin, text="Register", font=("Arial", 11), width=13, height=1,
                                command=goto_register_customer)
    register_button.grid(row=6, column=1, pady=10)

    goback_button = tk.Button(customerlogin, text="Go Back", font=("Arial", 11), width=13, height=1,
                                command=lambda: goback_start(customerlogin))
    goback_button.grid(row=7, column=1, pady=10)

def goto_register_customer():
    # loading the registration form
    if customerlogin.winfo_ismapped():
        customerlogin.pack_forget()
        register_customer()
        register_page.pack(pady=10)

def register_customer():
    # creating label and entries boxes to register user
    label_name = tk.Label(register_page, text='Registration Form   ', font=("Arial", 11), justify='left')
    label_name.pack(anchor='center')

    label_name = tk.Label(register_page, text='Name:                     ', font=("Arial", 11), justify='left')
    label_name.pack()
    entry_name = tk.Entry(register_page)
    entry_name.pack(pady=5)

    label_phone = tk.Label(register_page, text='Phone Number:     ', font=("Arial", 11), justify='left')
    label_phone.pack()
    entry_phone = tk.Entry(register_page)
    entry_phone.pack(pady=5)

    label_email = tk.Label(register_page, text='Email Address:      ', font=("Arial", 11), justify='left')
    label_email.pack()
    entry_email = tk.Entry(register_page)
    entry_email.pack(pady=5)

    label_username = tk.Label(register_page, text='User Name:           ', font=("Arial", 11), justify='left', )
    label_username.pack()
    entry_username = tk.Entry(register_page)
    entry_username.pack(pady=(5, 15))

    label_password = tk.Label(register_page, text='Password:             ', font=("Arial", 11), justify='left')
    label_password.pack()
    entry_password = tk.Entry(register_page)
    entry_password.pack(pady=5)

    submit_but=tk.Button(register_page,text='Submit',font=("Arial",11),justify='left',width=15,height=1,
                         command=lambda :register(entry_name,entry_username,entry_phone,entry_password,entry_email))
    submit_but.pack(pady=5)
    submit_but=tk.Button(register_page,text='Go Back',font=("Arial",11),justify='left',width=15,height=1,command=go_back_to_customer_login)
    submit_but.pack(pady=5)

def register(name_en,username_en,phone_en,password_en,email_en):
    #getting values from the entry field
    name=name_en.get()
    username=username_en.get()
    phone=phone_en.get()
    password=password_en.get()
    email=email_en.get()
    # adding the login information of the user to the database
    if len(name) !=0 and len(username)!=0 and len(phone)!=0 and len(password)!=0 and len(email)!=0:
        phone=int(phone)
        conn.execute(
            "INSERT INTO customerlogin (name, phone_number, Email,user_name,password) VALUES (?,? ,? ,?,?)",(name,phone,email,username,password))
        go_back_to_customer_login()
    else:
        messagebox.showinfo("Error","Account not created try again")

def go_back_to_customer_login():
    if register_page.winfo_ismapped():
        register_page.pack_forget()
        for widget in register_page.winfo_children():
            widget.destroy()
        customer_login_fun()
        customerlogin.pack(pady=60)

def login_customer(username_en, password_en):
    global customer_username
    username = username_en.get()
    password = password_en.get()
    check = conn.execute('Select * FROM customerlogin WHERE user_name = ? And password = ?', (username, password))
    check12 = 0
    for x in check:
        check12 = x

    if check12:
        if customerlogin.winfo_ismapped():  # if frame 1 is visible
            customerlogin.pack_forget()  # hide frame 1
            customer_username = username
            customer_page_fun()
            customer_page.pack(pady=80)  # show frame 2
        pass
    else:
        messagebox.showinfo("Error", "Wrong username or password entered!")
    pass

def customer_page_fun():
    global customer_username,chkitem,Statment
    chkitem=conn.execute("SELECT * FROM bid WHERE customer_username=?",(customer_username,))
    Statment="You have won the bid for item ID "
    y=True
    z=False
    for i in chkitem:
        if y:
            Statment=Statment+f'{i[1]}'
            y=False
            z=True
        else:
            Statment=Statment+f' and {i[1]}'
            y=True


    Check_auction = tk.Button(customer_page, text="View Auction List", width=23, height=2,command=goto_check)
    Check_auction.pack(pady=10)
    add_bidding = tk.Button(customer_page, text="Add item", width=23, height=2,command=gotoadd)
    add_bidding.pack()

    View_bidding = tk.Button(customer_page, text="View your bidding", width=23, height=2,command=goto_view_bid)
    View_bidding.pack(pady=10)

    profile = tk.Button(customer_page, text="Your Profile", width=23, height=2,command=goto_your_profile)
    profile.pack()

    if z:
        customer_page.pack(pady=80)
        messagebox.showinfo("Congratulations",f"{Statment}")
        conn.execute("DELETE FROM bid WHERE customer_username = ?",(customer_username,))

def gotoadd():
    if customer_page.winfo_ismapped():
        customer_page.pack_forget()
        add_item_user_fun()
        add_item_user.pack()

def add_item_user_fun():
    # creating label
    Head = tk.Label(add_item_user, text="ADD Item To auction", font=("Arial", 11))
    Head.pack(pady=5, anchor="center")

    # creating label and entry field
    label_name = tk.Label(add_item_user, text="Enter Item Name:", font=("Arial", 11), justify='right')
    label_name.pack(pady=5, padx=9, anchor="w")
    name_entry = tk.Entry(add_item_user)
    name_entry.pack(pady=3, padx=10, anchor="w")

    # creating label and entry field
    label_Type = tk.Label(add_item_user, text="Enter Item Type:", font=("Arial", 11), justify='right')
    label_Type.pack(pady=5, padx=9, anchor="w")
    Type_entry = tk.Entry(add_item_user)
    Type_entry.pack(pady=3, padx=10, anchor="w")

    # creating label and entry field
    label_Price = tk.Label(add_item_user, text="Enter starting bid:", font=("Arial", 11), justify='right')
    label_Price.pack(pady=5, padx=9, anchor="w")
    Price_entry = tk.Entry(add_item_user)
    Price_entry.pack(pady=3, padx=10, anchor="w")

    # creating Buttons
    submit_button = tk.Button(add_item_user, text="Add item", font=("Arial", 10), width=15, height=1,
                              command=lambda: Add_item_to_auction_user(name_entry, Type_entry, Price_entry))
    submit_button.pack(pady=5, padx=10, anchor="w")
    goback = tk.Button(add_item_user, text="Go Back", font=("Arial", 10), width=15, height=1,
                       command=lambda: go_back_to_customer_page(add_item_user))
    goback.pack(pady=5, padx=10, anchor="w")

def Add_item_to_auction_user(name_en, type_en, price_en):
    # getting the value from the entry field
    name = name_en.get()
    type = type_en.get()
    bid = price_en.get()
    # checking if the user have written something or not
    if len(name) != 0 and len(type) != 0 and len(bid) != 0:
        # inserting data into the database
        conn.execute(
            "INSERT INTO auction (name, Type, bid) "
            "VALUES (?, ?, ?)",
            (name, type, bid)
        )
    # going back to admin page
    go_back_to_customer_page(add_item_user)

def goto_view_bid():
    if customer_page.winfo_ismapped():
        customer_page.pack_forget()
        viw_bid_fun()
        view_bid.pack(fill="both",expand=True,padx=10)

def viw_bid_fun():
    global customer_username
    # getting items from the auction table from the database
    auction_items = conn.execute('SELECT * FROM orders WHERE customer_username= ?',(customer_username,))

    # initializing the Canvas variable
    canvas = tk.Canvas(view_bid)
    canvas.pack(side="left", fill="both", expand=True)
    # initializing the Scrollbar variable
    scrollbar = tk.Scrollbar(view_bid, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # configuring the Canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # initializing the inner frame variable
    inner_frame = tk.Frame(canvas)
    inner_frame.pack(fill="both", expand=True, padx=15)

    # creating the Canvas window
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    # creating a label
    label_menu = tk.Label(inner_frame, text='Auction Categories')
    label_menu.pack(pady=2, anchor="center")
    # displaying data from the database on the screen

    for item in auction_items:
        label = tk.Label(inner_frame, text=f'{item[0]}. {item[1]} - ${item[2]} - {item[3]} - {item[4]}')
        label.pack(pady=2, anchor="nw")

    # creating a go back fucntion
    goback = tk.Button(inner_frame, text="GoBack", fg="black", height=1, width=20,
                       command=lambda: go_back_to_customer_page(view_bid))
    goback.pack(pady=8, anchor="nw")

def goto_check():
    if customer_page.winfo_ismapped():
        customer_page.pack_forget()
        check_cat_fun()
        check_cat.pack(fill="both",expand=True,padx=10,pady=5)

def check_cat_fun():

    # getting items from the auction table from the database
    auction_items = conn.execute('SELECT id, name,Type, bid FROM auction')

    # initializing the Canvas variable
    canvas = tk.Canvas(check_cat)
    canvas.pack(side="left", fill="both", expand=True)
    # initializing the Scrollbar variable
    scrollbar = tk.Scrollbar(check_cat, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # configuring the Canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # initializing the inner frame variable
    inner_frame = tk.Frame(canvas)
    inner_frame.pack(fill="both", expand=True, padx=15)

    # creating the Canvas window
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    # creating a label
    label_menu = tk.Label(inner_frame, text='Auction Categories')
    label_menu.pack(pady=2, anchor="center")
    # displaying data from the database on the screen
    cat_list=[]
    i=0
    for item in auction_items:
        if item[2] in cat_list:
            continue
        else:
            label = tk.Label(inner_frame, text=f'{i}.  {item[2]}')
            label.pack(pady=2, anchor="nw")
            cat_list.append(item[2])
        i+=1

    label = tk.Label(inner_frame, text="Enter id of category you want to bid in: ")
    label.pack(pady=2, anchor="nw")

    cat_entry=tk.Entry(inner_frame)
    cat_entry.pack(pady=2, anchor="nw",padx=8)



    submit = tk.Button(inner_frame, text="Select", fg="black", height=1, width=20,
                       command=lambda: chose(cat_list,cat_entry.get()))
    submit.pack(pady=8, anchor="nw")

    # creating a go back fucntion
    goback = tk.Button(inner_frame, text="GoBack", fg="black", height=1, width=20,
                       command=lambda: go_back_to_customer_page(check_cat))
    goback.pack(pady=8, anchor="nw")

def chose(cat_li,index):
    chosen_cat=cat_li[int(index)]
    for wid in check_cat.winfo_children():
        wid.destroy()
    # getting items from the auction table from the database
    auction_items = conn.execute('SELECT id, name,Type, bid FROM auction WHERE Type= ?',(chosen_cat,))

    # initializing the Canvas variable
    canvas = tk.Canvas(check_cat)
    canvas.pack(side="left", fill="both", expand=True)
    # initializing the Scrollbar variable
    scrollbar = tk.Scrollbar(check_cat, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # configuring the Canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # initializing the inner frame variable
    inner_frame = tk.Frame(canvas)
    inner_frame.pack(fill="both", expand=True, padx=15)

    # creating the Canvas window
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    # creating a label
    label_menu = tk.Label(inner_frame, text='Auction')
    label_menu.pack(pady=2, anchor="center")
    # displaying data from the database on the screen

    for item in auction_items:
        label = tk.Label(inner_frame, text=f'{item[0]}. {item[1]} - {item[2]} - ${item[3]}')
        label.pack(pady=2, anchor="nw")

    label = tk.Label(inner_frame, text="Enter id of item you want to bid on: ")
    label.pack(pady=2, anchor="nw")

    id_entry=tk.Entry(inner_frame)
    id_entry.pack(pady=2, anchor="nw",padx=8)

    label = tk.Label(inner_frame, text="Enter your bid for the item: ")
    label.pack(pady=2, anchor="nw")

    bid_entry=tk.Entry(inner_frame)
    bid_entry.pack(pady=2, anchor="nw",padx=8)

    submit = tk.Button(inner_frame, text="Select", fg="black", height=1, width=20,
                       command=lambda: order(id_entry.get(),bid_entry.get(),chosen_cat))
    submit.pack(pady=8, anchor="nw")

    # creating a go back fucntion
    goback = tk.Button(inner_frame, text="GoBack", fg="black", height=1, width=20,
                       command=lambda: go_back_to_customer_page(check_cat))
    goback.pack(pady=8, anchor="nw")

def order(id,bid,chosen_cat):
    global customer_username
    Item_info=conn.execute('SELECT name,Type, bid FROM auction WHERE id = ? AND Type = ?',(id,chosen_cat))

    item_name="d"
    for i in Item_info:
        item_name=i[0]

    if item_name=="d":
        messagebox.showinfo("Error","Please Enter a valid id")
        return

    customer_info=conn.execute('SELECT phone_number FROM customerlogin WHERE user_name = ?',(str(customer_username),))
    phone_number=0
    for x in customer_info:
        phone_number=x[0]

    conn.execute(
        "INSERT INTO orders (item_id, cus_bit, customer_username,customer_phone) VALUES (?,?,?,?)",(id,bid,customer_username,phone_number))

    print(id,bid,customer_username,phone_number)
    go_back_to_customer_page(check_cat)
    pass

def goto_your_profile():
    if customer_page.winfo_ismapped():
        customer_page.pack_forget()
        your_profile_fun()
        your_profile_page.pack(fill="both",expand=True)

def your_profile_fun():
    global customer_username
    head=tk.Label(your_profile_page,text="Profile",font=font)
    head.grid(row=0, column=0, padx=180, pady=(25,7), sticky='w')
    check = conn.execute('Select * FROM customerlogin WHERE user_name = ?', (customer_username,))
    for item in check:
        name=item[1]
        phone=item[2]
        email=item[3]
        username=item[4]

    pad=160
    name_label = tk.Label(your_profile_page, text=f"Name: {name}", font=font)
    name_label.grid(row=1, column=0, padx=pad, pady=5, sticky='w')

    phone_label = tk.Label(your_profile_page, text=f"Phone No: {phone}", font=font)
    phone_label.grid(row=2, column=0, padx=pad, pady=5, sticky='w')

    email_label = tk.Label(your_profile_page, text=f"Email Address: {email}", font=font)
    email_label.grid(row=3, column=0, padx=pad, pady=5, sticky='w')

    username_label=tk.Label(your_profile_page,text=f"Username: {username}",font=font)
    username_label.grid(row=4, column=0, padx=pad, pady=5, sticky='w')

    gobac=tk.Button(your_profile_page,text="Go Back",width=13,command=lambda:go_back_to_customer_page(your_profile_page))
    gobac.grid(row=5, column=0, padx=pad+10, pady=5, sticky='w')

def go_back_to_customer_page(frame):
    if frame.winfo_ismapped():
        frame.pack_forget()
        for wid in frame.winfo_children():
            wid.destroy()

        customer_page.pack(fill="both",expand=True,pady=80)
def goto_admin_login(frame):
    if startwindow.winfo_ismapped():  # if frame 1 is visible
        startwindow.pack_forget()  # hide frame 1
        admin_login_fun()
        frame.pack(pady=80)  # show frame 2

def admin_login_fun():
    label_username = tk.Label(adminlogin, text='User Name:           ', font=("Arial", 11), justify='left', )
    label_username.grid(row=1, column=1)
    entry_username = tk.Entry(adminlogin)
    entry_username.grid(row=2, column=1, pady=(5, 15))

    label_password = tk.Label(adminlogin, text='Password:             ', font=("Arial", 11), justify='left')
    label_password.grid(row=3, column=1)
    entry_password = tk.Entry(adminlogin)
    entry_password.grid(row=4, column=1, pady=5)

    submit_button = tk.Button(adminlogin, text="Login", font=("Arial", 11), width=13, height=1,
                              command=lambda: login_admin(entry_username, entry_password))
    submit_button.grid(row=5, column=1, pady=10)

    goback_button = tk.Button(adminlogin, text="Go Back", font=("Arial", 11), width=13, height=1,
                                command=lambda: goback_start(adminlogin))
    goback_button.grid(row=6, column=1, pady=10)

def login_admin(username_en, password_en):
    username = username_en.get()
    password = password_en.get()
    check = conn.execute('Select * FROM adminlogin WHERE user_name = ? And password = ?', (username, password))
    check12 = 0
    for x in check:
        check12 = x

    if check12:
        if adminlogin.winfo_ismapped():  # if frame 1 is visible
            adminlogin.pack_forget()  # hide frame 1
            admin_page_fun()
            admin_page.pack(pady=80)  # show frame 2
        pass
    else:
        messagebox.showinfo("Error", "Wrong username or password entered!")

def admin_page_fun():
    Check_Auction = tk.Button(admin_page, text="View Auction list", width=23, height=2,command=lambda :goto_check_auction())
    Check_Auction.pack(pady=15)
    Add_to_Auction = tk.Button(admin_page, text="Add to Auction list", width=23, height=2,command=goto_add_to)
    Add_to_Auction.pack()

    Finalize_bid = tk.Button(admin_page, text="Finalize bidding", width=23, height=2,command=goto_final_bid)
    Finalize_bid.pack(pady=15)

def goto_final_bid():
    dict_key={}
    auction_items = conn.execute('SELECT id,item_id,cus_bit,customer_username,customer_phone FROM orders')
    templist=[]
    for item in auction_items:
        tple=(item[1],item[2],item[3])
        templist.append(tple)

    temlist2=[]
    temdic={}
    for i in templist:
        if i[0] in temlist2:
            x=temdic[i[0]]
            prev_bid=x[0]
            if prev_bid>i[1]:
                continue
            else:
                temdic[i[0]] = [i[1], i[2]]

        else:
            temlist2.append(i[0])
            temdic[i[0]]=[i[1],i[2]]
    print(temdic)

    # # creating final bid table
    # conn.execute('''CREATE TABLE IF NOT EXISTS bid
    #                  (id INTEGER PRIMARY KEY,
    #                   item_id INTEGER NOT NULL,
    #                   cus_bit REAL NOT NULL,
    #                   customer_username TEXT NOT NULL,
    #                   customer_phone TEXT NOT NULL
    #                   )''')
    for x in temdic.keys():
        val=temdic[x]
        phone_infor=conn.execute('SELECT customer_phone FROM orders WHERE customer_username=?',(val[1],))
        phon_num=0
        for yu in phone_infor:
            phon_num=yu[0]
        bid=val[0]
        username=val[1]
        conn.execute(
            "INSERT INTO bid (item_id, cus_bit, customer_username,customer_phone) VALUES (?,?,?,?)",(int(x),float(bid),username,phon_num))
        conn.execute("DELETE FROM orders")
    messagebox.showinfo("BIDS FINALIZED","You have accepted the highest bidder for all items")

def goto_add_to():
    if admin_page.winfo_ismapped():
        admin_page.pack_forget()
        for wid in admin_page.winfo_children():
            wid.destroy()
        add_to_fun()
        add_to_auction_page.pack()

def add_to_fun():
    # creating label
    Head = tk.Label(add_to_auction_page, text="ADD Item To auction", font=("Arial", 11))
    Head.pack(pady=5, anchor="center")

    # creating label and entry field
    label_name = tk.Label(add_to_auction_page, text="Enter Item Name:", font=("Arial", 11), justify='right')
    label_name.pack(pady=5, padx=9, anchor="w")
    name_entry = tk.Entry(add_to_auction_page)
    name_entry.pack(pady=3, padx=10, anchor="w")

    # creating label and entry field
    label_Type = tk.Label(add_to_auction_page, text="Enter Item Type:", font=("Arial", 11), justify='right')
    label_Type.pack(pady=5, padx=9, anchor="w")
    Type_entry = tk.Entry(add_to_auction_page)
    Type_entry.pack(pady=3, padx=10, anchor="w")

    # creating label and entry field
    label_Price = tk.Label(add_to_auction_page, text="Enter Starting bid:", font=("Arial", 11), justify='right')
    label_Price.pack(pady=5, padx=9, anchor="w")
    Price_entry = tk.Entry(add_to_auction_page)
    Price_entry.pack(pady=3, padx=10, anchor="w")

    # creating Buttons
    submit_button = tk.Button(add_to_auction_page, text="Add item", font=("Arial", 10), width=15, height=1,
                              command=lambda: Add_item_to_auction(name_entry, Type_entry, Price_entry))
    submit_button.pack(pady=5, padx=10, anchor="w")
    goback = tk.Button(add_to_auction_page, text="Go Back", font=("Arial", 10), width=15, height=1,
                       command=lambda: go_back_adminpage(add_to_auction_page))
    goback.pack(pady=5, padx=10, anchor="w")

def Add_item_to_auction(name_en, type_en, price_en):
    # getting the value from the entry field
    name = name_en.get()
    type = type_en.get()
    bid = price_en.get()
    # checking if the user have written something or not
    if len(name) != 0 and len(type) != 0 and len(bid) != 0:
        # inserting data into the database
        conn.execute(
            "INSERT INTO auction (name, Type, bid) "
            "VALUES (?, ?, ?)",
            (name, type, bid)
        )
    # going back to admin page
    go_back_adminpage(add_to_auction_page)

def goto_check_auction():
    # loading view Auction page
    if admin_page.winfo_ismapped():
        admin_page.pack_forget()
        for wid in admin_page.winfo_children():
            wid.destroy()
        check_all_auction()
        check_auction_page.pack(fill="both",expand=True,padx=10)

def check_all_auction():
    # getting items from the auction table from the database
    Auction_items = conn.execute('SELECT id, name,Type, bid FROM auction')

    # initializing the Canvas variable
    canvas = tk.Canvas(check_auction_page)
    canvas.pack(side="left", fill="both", expand=True)
    # initializing the Scrollbar variable
    scrollbar = tk.Scrollbar(check_auction_page, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # configuring the Canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # initializing the inner frame variable
    inner_frame = tk.Frame(canvas)
    inner_frame.pack(fill="both", expand=True, padx=15)

    # creating the Canvas window
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    # creating a label
    label_menu = tk.Label(inner_frame, text='Auction List')
    label_menu.pack(pady=2, anchor="center")
    # displaying data from the database on the screen
    for item in Auction_items:
        label = tk.Label(inner_frame, text=f'{item[0]}. {item[1]} - {item[2]} - ${item[3]}')
        label.pack(pady=2, anchor="nw")

    # creating a go back fucntion
    goback = tk.Button(inner_frame, text="GoBack", fg="black", height=1, width=20,
                       command=lambda: go_back_adminpage(check_auction_page))
    goback.pack(pady=10, anchor="nw")

def go_back_adminpage(Frame):
    # loading the admin page and deleting the widget of the previous frame
    if Frame.winfo_ismapped():
        for widget in Frame.winfo_children():
            widget.destroy()
        Frame.pack_forget()
        admin_page_fun()
        admin_page.pack(pady=80)

def createdatabase():
    # Create a table for the amdin login
    conn.execute('''CREATE TABLE IF NOT EXISTS adminlogin
                     (id INTEGER PRIMARY KEY,
                      user_name TEXT NOT NULL,
                      name Text,
                      phone_number REAL,
                      password TEXT)''')
    # Insert data into the Adminlogin table
    conn.execute(
        "INSERT INTO adminlogin (user_name, name, phone_number,password) VALUES ('admin', 'Tester', +945852682,'123')")

    # creating customerlogin table
    conn.execute('''CREATE TABLE IF NOT EXISTS customerlogin
                     (id INTEGER PRIMARY KEY,
                      name Text,
                      phone_number INT,
                      Email Text,
                      user_name TEXT NOT NULL,
                      password TEXT)''')

    # creating auction table
    conn.execute('''CREATE TABLE IF NOT EXISTS auction
                     (id INTEGER PRIMARY KEY,
                      name TEXT NOT NULL,
                      Type TEXT,
                      bid REAL NOT NULL)''')

    # Insert data into the auction table
    conn.execute(
        "INSERT INTO auction (name, Type, bid)VALUES ('BMW M140i', 'vehicle', 7000)")
    conn.execute(
        "INSERT INTO auction (name, Type, bid) VALUES ('Bugatti Royal Kellner Coupe', 'vehicle',5000)")
    conn.execute(
        "INSERT INTO auction (name, Type, bid) VALUES ('Lamborghini Veneno Roadster ', 'vehicle',6000)")
    conn.execute(
        "INSERT INTO auction (name, Type, bid) VALUES ('Neuschwanstein Castle', 'property', 80000)")
    conn.execute("INSERT INTO auction (name, Type, bid) VALUES ('The Playboy Mansion', 'property', 90000)")
    conn.execute("INSERT INTO auction (name, Type, bid) VALUES ('Hearst Castle', 'property', 100000)")

    # creating order table
    conn.execute('''CREATE TABLE IF NOT EXISTS orders
                     (id INTEGER PRIMARY KEY,
                      item_id INTEGER NOT NULL,
                      cus_bit REAL NOT NULL,
                      customer_username TEXT NOT NULL,
                      customer_phone TEXT NOT NULL
                      )''')

    # creating final bid table
    conn.execute('''CREATE TABLE IF NOT EXISTS bid
                     (id INTEGER PRIMARY KEY,
                      item_id INTEGER NOT NULL,
                      cus_bit REAL NOT NULL,
                      customer_username TEXT NOT NULL,
                      customer_phone TEXT NOT NULL
                      )''')



if __name__ == "__main__":
    startwindowfun()
    if not os.path.isfile(db_file):
        conn = sqlite3.connect(db_file)
        createdatabase()
    else:
        conn = sqlite3.connect(db_file)

    startwindow.pack(pady=130)
    root.mainloop()
    conn.commit()
    conn.close()
