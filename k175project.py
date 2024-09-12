import tkinter as tk
import sqlite3
# Function to insert data into the SQLite database
def insert_data():
    Name = Name_entry.get()
    Rollno = Rollno_entry.get()
    Age = Age_entry.get()
    M1 = M1_entry.get()
    M2 = M2_entry.get()

    # Insert data into the database
    cursor.execute("INSERT INTO student2 (Name, Rollno , Age  , M1 , M2) VALUES (?, ? ,? ,? ,?)",
                   (Name, Rollno, Age, M1, M2))
    conn.commit()
    # cursor.execute("ALTER TABLE student2 ADD COLUMN (Name, Rollno , Age  , M1 , M2) VALUES (?, ? ,? ,? ,?)",(Name, Rollno , Age , M1 , M2))
    # conn.commit()
    # Clear the input fields
    Name_entry.delete(0, tk.END)
    Rollno_entry.delete(0, tk.END)
    Age_entry.delete(0, tk.END)
    M1_entry.delete(0, tk.END)
    M2_entry.delete(0, tk.END)

    # Update the data displayed in the GUI
    update_data()


# Function to fetch data from the SQLite database and display it in the GUI
def update_data():
    cursor.execute("SELECT * FROM student2")
    data = cursor.fetchall()

    # Clear the data text widget
    data_text.delete(1.0, tk.END)

    # Display the data in the text widget
    for row in data:
        data_text.insert(tk.END, f"Name: {row[1]}, Rollno: {row[2]} ,Age: {row[3]} ,M1: {row[4]} ,M2: {row[5]}\n")

# Create a Tkinter window
root = tk.Tk()
root.title("SQLite Database GUI")

# Create a database connection and cursor
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# Create a table to store data
cursor.execute("CREATE TABLE IF NOT EXISTS student2 (Name TEXT, Rollno INTEGER, Age INTEGER , M1 INTEGER , M2 INTEGER)")
conn.commit()

# Create a table to store data
# cursor.execute("CREATE TABLE student2 (Name TEXT, Rollno INTEGER, age INTEGER , M1 INTEGER , M2 INTEGER)")
# conn.commit()


# Create and place widgets in the window
Name_label = tk.Label(root, text="Name:")
Name_label.pack()

Name_entry = tk.Entry(root)
Name_entry.pack()

Rollno_label = tk.Label(root, text="Rollno:")
Rollno_label.pack()

Rollno_entry = tk.Entry(root)
Rollno_entry.pack()

Age_label = tk.Label(root, text="Age:")
Age_label.pack()

Age_entry = tk.Entry(root)
Age_entry.pack()

M1_label = tk.Label(root, text="M1:")
M1_label.pack()

M1_entry = tk.Entry(root)
M1_entry.pack()

M2_label = tk.Label(root, text="M2:")
M2_label.pack()

M2_entry = tk.Entry(root)
M2_entry.pack()

add_button = tk.Button(root, text="Add Data", command=insert_data)
add_button.pack()

data_text = tk.Text(root, height=10, width=30)
data_text.pack()

update_button = tk.Button(root, text="Show Data", command=update_data)
update_button.pack()

# Start the Tkinter main loop
root.mainloop()