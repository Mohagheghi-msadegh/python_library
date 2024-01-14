import mysql.connector

import tkinter as tk
root = tk.Tk()
root.title("library")
# Setting background color for the window
root.configure(bg="lightblue")
person_list = ["  id  "," first_name "," last_name ","address","phone_number"]
book_list = ["ISBN","Title","Author","publisher","publish_year","numberof instance","number of avalable"]
Button_dict = {0:"person",1:"Book",2:"Employee",3:"reserve",4:"loan"}
employer_list = ["ID-e","name","familyname","employment_year"]
reserve_list = ["ID","ISBN","reserve_date","expire_date"]
loan_list = ["ISBN","ID_e","ID","browing_date","Delivery_date_set","Actual_Delivery_date","Penalty"]
text_boxes = []
lable_list=[]
library_list=["Person","Book","Employee","Reserve","Book_loan"]    

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("300x200")
    label = tk.Label(new_window, text="This is a window for %s" %library_list[0])
    label.pack()
    global id_entry
    global first_name_entry
    global last_name_entry
    global phone_number_entry
    global address_entry
    
    tk.Label(new_window, text="ID:").pack()
    id_entry = tk.Entry(new_window)
    id_entry.pack(padx=20, pady=20)
    
    tk.Label(new_window, text="First name:").pack()
    first_name_entry = tk.Entry(new_window)
    first_name_entry.pack(padx=20, pady=20)

    tk.Label(new_window, text="Last name:").pack()
    last_name_entry = tk.Entry(new_window)
    last_name_entry.pack(padx=20, pady=20)

    tk.Label(new_window, text="Address:").pack()
    address_entry = tk.Entry(new_window)
    address_entry.pack(padx=20, pady=20)

    tk.Label(new_window, text="Phone number:").pack()
    phone_number_entry = tk.Entry(new_window)
    phone_number_entry.pack(padx=20, pady=20)
    
    
   # for i in range(5):
   #     l1=tk.Label(new_window,text = person_list[i])
   #     l1.pack()
    #    lable_list.append(l1)
     #   text_box = tk.Entry(new_window)
      #  text_box.pack()
       # text_boxes.append(text_box)
    insert = tk.Button(new_window, text="Save", width=15, height=5,bg="lightblue",command=Person_save_to_database)
    insert.pack(side=tk.LEFT, padx=80, pady=10)    
    search = tk.Button(new_window, text="Search", width=15, height=5,bg="lightblue",command=Person_search_from_database)
    search.pack(side=tk.LEFT, padx=80, pady=10)

    update = tk.Button(new_window, text="Update", width=15, height=5,bg="lightblue",command=Person_Update)    
    update.pack(side=tk.LEFT, padx=80, pady=10)

    delete = tk.Button(new_window, text="Delete", width=15, height=5, bg="lightblue",command=Person_Delete)
    delete.pack(side=tk.LEFT, padx=80, pady=10)  


       
def button_clicked(button_number):
    print(f"Button {button_number} clicked")

def open_new_window1():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("300x200")
    label = tk.Label(new_window, text="This is a window for %s"%library_list[1])
    label.pack()
    global ISBN_entry
    global title_entry
    global Author_entry
    global publisher_entry
    global year_entry
    global instance_entry
    global avalable_entry
    
    tk.Label(new_window, text="ISBN:").pack()
    ISBN_entry = tk.Entry(new_window)
    ISBN_entry.pack()
    
    tk.Label(new_window, text="Title:").pack()
    title_entry = tk.Entry(new_window)
    title_entry.pack()

    tk.Label(new_window, text="Author:").pack()
    Author_entry = tk.Entry(new_window)
    Author_entry.pack()

    tk.Label(new_window, text="publisher:").pack()
    publisher_entry = tk.Entry(new_window)
    publisher_entry.pack()

    tk.Label(new_window, text="Publish_year:").pack()
    year_entry = tk.Entry(new_window)
    year_entry.pack()
    tk.Label(new_window, text="number of instance:").pack()
    instance_entry = tk.Entry(new_window)
    instance_entry.pack()
    tk.Label(new_window, text="number of availble:").pack()
    avalable_entry = tk.Entry(new_window)
    avalable_entry.pack()
    
    insert = tk.Button(new_window, text="Save", width=15, height=5,bg="lightblue",command = Book_save_to_database)
    insert.pack(side=tk.LEFT, padx=80, pady=10)
    search = tk.Button(new_window, text="Search", width=15, height=5,bg="lightblue",command = Book_search_from_database)
    search.pack(side=tk.LEFT, padx=80, pady=10)
    Update = tk.Button(new_window, text="Update", width=15, height=5,bg="lightblue" ,command = Book_Update)
    Update.pack(side=tk.LEFT, padx=80, pady=10)
    Delete = tk.Button(new_window, text="Delete", width=15, height=5, bg="lightblue",command = Book_Delete)
    Delete.pack(side=tk.LEFT, padx=80, pady=10)
def open_new_window2():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("300x200")
    label = tk.Label(new_window, text="DEMO")
    label.pack()
    for i in range(len(employer_list)):
        l1=tk.Label(new_window,text = employer_list[i])
        l1.pack()
        lable_list.append(l1)
        text_box = tk.Entry(new_window)
        text_box.pack()
        text_boxes.append(text_box)
    search = tk.Button(new_window, text="Search", width=15, height=5,bg="lightblue",command=lambda: button_clicked(1))
    search.pack(side=tk.TOP, padx=130, pady=10)  
def open_new_window3():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("300x200")
    label = tk.Label(new_window, text="DEMO")
    label.pack()
    for i in range(len(reserve_list)):
        label1 = tk.Label(new_window, text=reserve_list[i])
        label1.pack()

        entry1 = tk.Entry(new_window)
        entry1.pack()
    search = tk.Button(new_window, text="Search", width=15, height=5,bg="purple",command=lambda: button_clicked(1))
    search.pack(side=tk.LEFT, padx=130, pady=10)

    Update = tk.Button(new_window, text="Update", width=15, height=5,bg="red" ,command=lambda: button_clicked(2))
    Update.pack(side=tk.LEFT, padx=130, pady=10)

    Delete = tk.Button(new_window, text="Delete", width=15, height=5, bg="darkblue",command=lambda: button_clicked(3))
    Delete.pack(side=tk.LEFT, padx=130, pady=10)
def open_new_window4():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("300x200")
    label = tk.Label(new_window, text="Demo")
    label.pack()
    for i in range(len(loan_list)):          
        label1 = tk.Label(new_window, text=loan_list[i])
        label1.pack()

        entry1 = tk.Entry(new_window)
        entry1.pack()
    search = tk.Button(new_window, text="Search", width=15, height=5,bg="bluesky",command=lambda: button_clicked(1))
    search.pack(side=tk.LEFT, padx=90, pady=10)

    Update = tk.Button(new_window, text="Update", width=15, height=5,bg="bluesky" ,command=lambda: button_clicked(2))
    Update.pack(side=tk.LEFT, padx=90, pady=10)

    Delete = tk.Button(new_window, text="Delete", width=15, height=5, bg="bluesky",command=lambda: button_clicked(3))
    Delete.pack(side=tk.LEFT, padx=90, pady=10)
    
def Person_save_to_database():
    # Get values from entry fields
    p_id = id_entry.get()
    fname = first_name_entry.get()
    lname = last_name_entry.get()
    address = address_entry.get()
    p_num = phone_number_entry.get()
    
    # Connect to SQLite database
    mydb = mysql.connector.connect(
    user="root",
    password="Irannl1404!",
    database="library")
    cursor = mydb.cursor()
    query = 'Insert into Person values(%s, %s, %s, %s, %s);'
    vals = (p_id, fname, lname, address, p_num)
    cursor.execute(query, vals)
    mydb.commit()
    mydb.close()
    # Clear the entry fields after saving
    id_entry.delete(0, tk.END) 
def Book_save_to_database():
    # Get values from entry fields
    isbn= ISBN_entry.get()
    title = title_entry.get()
    author = Author_entry.get()
    year = year_entry.get()
    pub = publisher_entry.get()
    instance = instance_entry.get()
    avalable = avalable_entry.get()
    # Connect to SQLite database
    mydb = mysql.connector.connect(
    user="root",
    password="Irannl1404!",
    database="library")
    cursor = mydb.cursor()
    query = 'Insert into Book values(%s, %s, %s, %s, %s,%s,%s);'
    vals = (isbn,title,author,pub,year,instance,avalable)
    cursor.execute(query, vals)
    mydb.commit()
    mydb.close()
    # Clear the entry fields after saving
    ISBN_entry.delete(0, tk.END)    
    
def Person_search_from_database():
    
    p_id = id_entry.get()

    mydb = mysql.connector.connect(
    user="root",
    password="Irannl1404!",
    database="library")
    cursor = mydb.cursor()
    query = 'select * from Person where ID = ' + p_id
    #vals = (p_id)
    cursor.execute(query)
    data = cursor.fetchall()
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    phone_number_entry.delete(0, tk.END)
    if len(data) == 0:
        first_name_entry.insert(tk.END, "No record found!")
    for row in data:
        first_name_entry.insert(tk.END, f"{row[1]}")
        last_name_entry.insert(tk.END, f"{row[2]}")
        address_entry.insert(tk.END, f"{row[3]}")
        phone_number_entry.insert(tk.END, f"{row[4]}")
        break
        
    mydb.commit()
    mydb.close()
def Book_search_from_database():
    
    
    isbn_id = ISBN_entry.get()

    mydb = mysql.connector.connect(
    user="root",
    password="Irannl1404!",
    database="library")
    cursor = mydb.cursor()
    query1 = 'select * from Book where ISBN = ' + isbn_id
    #vals = (p_id)
    cursor.execute(query1)
    data = cursor.fetchall()
    """"
    title_entry.delete(0, tk.END)
    Author_entry.delete(0, tk.END)
    publisher_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    instance_entry.delete(0, tk.END)
    avalable_entry.delete(0, tk.END)
    """
    if len(data) == 0:
        first_name_entry.insert(tk.END, "No record found!")
    for row in data:
        
        title_entry.insert(tk.END, f"{row[1]}")
        Author_entry.insert(tk.END, f"{row[2]}")
        publisher_entry.insert(tk.END, f"{row[3]}")
        year_entry.insert(tk.END, f"{row[4]}")
        instance_entry.insert(tk.END, f"{row[5]}")
        avalable_entry.insert(tk.END, f"{row[6]}")
        break
        
        
    mydb.commit()
    mydb.close()
    
def Person_Update():
    p_id = id_entry.get()
    fname = first_name_entry.get()
    lname = last_name_entry.get()
    address = address_entry.get()
    p_num = phone_number_entry.get()
    mydb = mysql.connector.connect(
    user="root",
    password="Irannl1404!",
    database="library")
    cursor = mydb.cursor()
    query ='Update Person set firstname = %s, lastname = %s, address = %s, Phone_number = %s where ID = %s'
    vals = (fname, lname, address, p_num, p_id)
    cursor.execute(query, vals)
    mydb.commit()
    mydb.close() 
def Book_Update():
    isbn= ISBN_entry.get()
    title = title_entry.get()
    author = Author_entry.get()
    year = year_entry.get()
    pub = publisher_entry.get()
    instance = instance_entry.get()
    available = avalable_entry.get()

    mydb = mysql.connector.connect(
    user="root",
    password="Irannl1404!",
    database="library")
    cursor = mydb.cursor()
    query = 'Update Book set title = %s, Author = %s, publisher = %s, publication_year = %s, number_of_instance = %s, number_of_availible = %s where ISBN = %s'
    vals = (title, author, pub, year, instance, available, isbn)
    cursor.execute(query, vals)
    mydb.commit()
    mydb.close() 
    ISBN_entry.delete(0, tk.END)    

#this is a function that get id's person and delete that person from database    
    
def Person_Delete():
    p_id = id_entry.get()
    mydb = mysql.connector.connect(
    user="root",
    password="Irannl1404!",
    database="library")
    cursor = mydb.cursor()
    query = 'delete  from Person where ID = ' + p_id
    cursor.execute(query)
    mydb.commit()
    mydb.close()
    
#this is a function that get isbn's book and delete that book from database    
def Book_Delete():
    isbn = ISBN_entry.get()
    mydb = mysql.connector.connect(
    user="root",
    password="Irannl1404!",
    database="library")
    cursor = mydb.cursor()
    query = 'delete  from Book where ISBN = ' + isbn
    cursor.execute(query)
    mydb.commit()
    mydb.close()    
    ISBN_entry.delete(0, tk.END)    

    
    
for s in range(5):
    if s==0:  
        button = tk.Button(root, width=10, height=2,bg="lightgray",text=library_list[s], command=open_new_window)
        button.pack(padx=20, pady=20)
    elif s==1:
        button = tk.Button(root, width=10, height=2,bg="lightgray",text=library_list[s], command=open_new_window1)
        button.pack(padx=20, pady=20)
    elif s==2:
        button = tk.Button(root, width=10, height=2,bg="lightgray",text=library_list[s], command=open_new_window2)
        button.pack(padx=20, pady=20) 
    elif s==3:
        button = tk.Button(root, width=10, height=2,bg="lightgray",text=library_list[s], command=open_new_window3)
        button.pack(padx=20, pady=20)   
    elif s==4:
        button = tk.Button(root, width=10, height=2,bg="lightgray",text=library_list[s], command=open_new_window4)
        button.pack(padx=20, pady=20)     
root.mainloop()
