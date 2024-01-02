import tkinter as tk
import sqlite3
import mysql.connector
def search_from_database():
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
    

def save_to_database():
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

def Update():
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
    query = 'Update Person set firstname = %s, lastname = %s, address = %s, Phone_number = %s where ID = %s'
    vals = (fname, lname, address, p_num, p_id)
    cursor.execute(query, vals)
    mydb.commit()
    mydb.close()   
def Delete():
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
    
    
def display_from_database():
    # Connect to SQLite database
    conn = sqlite3.connect('userdata.db')
    cursor = conn.cursor()

    # Fetch data from the table
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()

    # Display data in the Tkinter window
    display_text.delete(1.0, tk.END)  # Clear previous content
    print(len(data))
    for row in data:
        display_text.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Email: {row[3]}\n")

    # Close connection
    conn.close()

# Create the Tkinter window
root = tk.Tk()
root.title("User Data Display and Entry")

# Create input fields for adding data
tk.Label(root, text="ID:").pack()
id_entry = tk.Entry(root)
id_entry.pack()

tk.Label(root, text="First name:").pack()
first_name_entry = tk.Entry(root)
first_name_entry.pack()

tk.Label(root, text="Last name:").pack()
last_name_entry = tk.Entry(root)
last_name_entry.pack()

tk.Label(root, text="Address:").pack()
address_entry = tk.Entry(root)
address_entry.pack()

tk.Label(root, text="Phone number:").pack()
phone_number_entry = tk.Entry(root)
phone_number_entry.pack()


# Button to save data
save_button = tk.Button(root, text="Save", command=save_to_database)
save_button.pack()
save_button = tk.Button(root, text="Search", command=search_from_database)
save_button.pack()
save_button = tk.Button(root, text="Delete", command=Delete)
save_button.pack()
save_button = tk.Button(root, text="Update", command=Update)
save_button.pack()


# Display area for showing existing data
display_text = tk.Text(root, height=10, width=50)
display_text.pack()

# Button to display data
display_button = tk.Button(root, text="Display Data", command=display_from_database)
display_button.pack()

# Run the application
root.mainloop()
