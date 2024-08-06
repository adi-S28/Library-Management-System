import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector # type: ignore

# Connect to the MySQL database
conn = mysql.connector.connect(
    user='Aaryan',
    password='admin',
    host='localhost',
    database='library'
)
cursor = conn.cursor()

# Functions for handling user authentication and functionalities
def admin_login():
    ad_name = ad_name_entry.get()
    ad_pass = ad_pass_entry.get()

    # Query the Admin table to authenticate the admin user
    query = "SELECT * FROM Admin WHERE Ad_name = %s AND Ad_pass = %s"
    cursor.execute(query, (ad_name, ad_pass))
    result = cursor.fetchone()

    if result:
        # Admin authenticated, display the admin functionalities
        display_admin_functionalities()
    else:
        # Display an error message for invalid credentials
        error_label.config(text="Invalid admin credentials")

def staff_login():
    staff_name = staff_name_entry.get()
    staff_email = staff_email_entry.get()

    # Query the Staff table to authenticate the staff user
    query = "SELECT * FROM Staff WHERE S_name = %s AND S_email = %s"
    cursor.execute(query, (staff_name, staff_email))
    result = cursor.fetchone()

    if result:
        # Staff authenticated, display the staff functionalities
        display_staff_functionalities()
    else:
        # Display an error message for invalid credentials
        error_label.config(text="Invalid staff credentials")

def member_login():
    member_name = member_name_entry.get()
    member_email = member_email_entry.get()

    # Query the Members table to authenticate the member user
    query = "SELECT * FROM Members WHERE M_name = %s AND M_email = %s"
    cursor.execute(query, (member_name, member_email))
    result = cursor.fetchone()

    if result:
        # Member authenticated, display the member functionalities
        display_member_functionalities()
    else:
        # Display an error message for invalid credentials
        error_label.config(text="Invalid member credentials")

def display_admin_functionalities():
    # Clear the login frame
    for widget in login_frame.winfo_children():
        widget.destroy()

    # Create a new frame for admin functionalities
    admin_frame = ttk.Frame(root, padding="20")
    admin_frame.grid(row=0, column=0, sticky="nsew")

    # Add functionalities for managing staff
    staff_label = ttk.Label(admin_frame, text="Manage Staff", font=("Arial", 14, "bold"))
    staff_label.grid(row=0, column=0, columnspan=2, pady=10)

    add_staff_button = ttk.Button(admin_frame, text="Add Staff", command=add_staff)
    add_staff_button.grid(row=1, column=0, padx=5, pady=5)

    update_staff_button = ttk.Button(admin_frame, text="Update Staff", command=update_staff)
    update_staff_button.grid(row=1, column=1, padx=5, pady=5)

    delete_staff_button = ttk.Button(admin_frame, text="Delete Staff", command=delete_staff)
    delete_staff_button.grid(row=2, column=0, padx=5, pady=5)

    view_staff_button = ttk.Button(admin_frame, text="View Staff List", command=view_staff_list)
    view_staff_button.grid(row=2, column=1, padx=5, pady=5)

    # Add functionalities for managing books and e-resources
    book_label = ttk.Label(admin_frame, text="Manage Books and E-Resources", font=("Arial", 14, "bold"))
    book_label.grid(row=3, column=0, columnspan=2, pady=10)

    add_book_button = ttk.Button(admin_frame, text="Add Book/E-Resource", command=add_book)
    add_book_button.grid(row=4, column=0, padx=5, pady=5)

    update_book_button = ttk.Button(admin_frame, text="Update Book/E-Resource", command=update_book)
    update_book_button.grid(row=4, column=1, padx=5, pady=5)

    delete_book_button = ttk.Button(admin_frame, text="Delete Book/E-Resource", command=delete_book)
    delete_book_button.grid(row=5, column=0, padx=5, pady=5)

    view_book_button = ttk.Button(admin_frame, text="View Books/E-Resources List", command=view_book_list)
    view_book_button.grid(row=5, column=1, padx=5, pady=5)
    # Add functionalities for managing publishers
    publisher_label = ttk.Label(admin_frame, text="Manage Publishers", font=("Arial", 14, "bold"))
    publisher_label.grid(row=6, column=0, columnspan=2, pady=10)

    add_publisher_button = ttk.Button(admin_frame, text="Add Publisher", command=add_publisher)
    add_publisher_button.grid(row=7, column=0, padx=5, pady=5)

    update_publisher_button = ttk.Button(admin_frame, text="Update Publisher", command=update_publisher)
    update_publisher_button.grid(row=7, column=1, padx=5, pady=5)

    delete_publisher_button = ttk.Button(admin_frame, text="Delete Publisher", command=delete_publisher)
    delete_publisher_button.grid(row=8, column=0, padx=5, pady=5)

    view_publisher_button = ttk.Button(admin_frame, text="View Publishers List", command=view_publisher_list)
    view_publisher_button.grid(row=8, column=1, padx=5, pady=5)

    # Add functionalities for managing reports
    report_label = ttk.Label(admin_frame, text="Manage Reports", font=("Arial", 14, "bold"))
    report_label.grid(row=9, column=0, columnspan=2, pady=10)

    view_report_button = ttk.Button(admin_frame, text="View Reports List", command=view_report_list)
    view_report_button.grid(row=10, column=0, padx=5, pady=5)

    update_report_button = ttk.Button(admin_frame, text="Update Report Status", command=update_report_status)
    update_report_button.grid(row=10, column=1, padx=5, pady=5)

    # Add functionalities for managing fines
    fine_label = ttk.Label(admin_frame, text="Manage Fines", font=("Arial", 14, "bold"))
    fine_label.grid(row=11, column=0, columnspan=2, pady=10)

    view_fine_button = ttk.Button(admin_frame, text="View Fines List", command=view_fine_list)
    view_fine_button.grid(row=12, column=0, padx=5, pady=5)

    update_fine_button = ttk.Button(admin_frame, text="Update Fine Amounts", command=update_fine_amounts)
    update_fine_button.grid(row=12, column=1, padx=5, pady=5)

# Functions for admin functionalities
def add_staff():
    add_staff_window = tk.Toplevel(root)
    add_staff_window.title("Add Staff")

    id_label = ttk.Label(add_staff_window, text="ID:")
    id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    id_entry = ttk.Entry(add_staff_window)
    id_entry.grid(row=0, column=1, padx=5, pady=5)

    name_label = ttk.Label(add_staff_window, text="Name:")
    name_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    name_entry = ttk.Entry(add_staff_window)
    name_entry.grid(row=1, column=1, padx=5, pady=5)

    email_label = ttk.Label(add_staff_window, text="Email:")
    email_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    email_entry = ttk.Entry(add_staff_window)
    email_entry.grid(row=2, column=1, padx=5, pady=5)

    phone_label = ttk.Label(add_staff_window, text="Phone:")
    phone_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    phone_entry = ttk.Entry(add_staff_window)
    phone_entry.grid(row=3, column=1, padx=5, pady=5)

    type_label = ttk.Label(add_staff_window, text="Type:")
    type_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
    type_entry = ttk.Entry(add_staff_window)
    type_entry.grid(row=4, column=1, padx=5, pady=5)

    def add_staff_to_db():
        id = id_entry.get()
        name = name_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        staff_type = type_entry.get()

        # Query to insert new staff into the Staff table
        query = "INSERT INTO Staff (S_id, S_name, S_email, S_phone, S_type) VALUES (%s, %s, %s, %s, %s)"
        try:
            cursor.execute(query, (id, name, email, phone, staff_type))
            conn.commit()
            messagebox.showinfo("Success", "Staff member added successfully.")
            add_staff_window.destroy()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error occurred: {e}")

    add_button = ttk.Button(add_staff_window, text="Add Staff", command=add_staff_to_db)
    add_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)


def update_staff():
    update_staff_window = tk.Toplevel(root)
    update_staff_window.title("Update Staff")

    staff_id_label = ttk.Label(update_staff_window, text="Staff ID:")
    staff_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    staff_id_entry = ttk.Entry(update_staff_window)
    staff_id_entry.grid(row=0, column=1, padx=5, pady=5)

    name_label = ttk.Label(update_staff_window, text="Name:")
    name_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    name_entry = ttk.Entry(update_staff_window)
    name_entry.grid(row=1, column=1, padx=5, pady=5)

    email_label = ttk.Label(update_staff_window, text="Email:")
    email_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    email_entry = ttk.Entry(update_staff_window)
    email_entry.grid(row=2, column=1, padx=5, pady=5)

    phone_label = ttk.Label(update_staff_window, text="Phone:")
    phone_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    phone_entry = ttk.Entry(update_staff_window)
    phone_entry.grid(row=3, column=1, padx=5, pady=5)

    type_label = ttk.Label(update_staff_window, text="Type:")
    type_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
    type_entry = ttk.Entry(update_staff_window)
    type_entry.grid(row=4, column=1, padx=5, pady=5)

    def update_staff_in_db():
        staff_id = staff_id_entry.get()
        name = name_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        staff_type = type_entry.get()

        # Query to update staff information in the Staff table
        query = "UPDATE Staff SET S_name = %s, S_email = %s, S_phone = %s, S_type = %s WHERE S_id = %s"
        try:
            cursor.execute(query, (name, email, phone, staff_type, staff_id))
            conn.commit()
            messagebox.showinfo("Success", "Staff member updated successfully.")
            update_staff_window.destroy()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error occurred: {e}")

    update_button = ttk.Button(update_staff_window, text="Update Staff", command=update_staff_in_db)
    update_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

def delete_staff():
    delete_staff_window = tk.Toplevel(root)
    delete_staff_window.title("Delete Staff")

    staff_id_label = ttk.Label(delete_staff_window, text="Staff ID:")
    staff_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    staff_id_entry = ttk.Entry(delete_staff_window)
    staff_id_entry.grid(row=0, column=1, padx=5, pady=5)

    def delete_staff_from_db():
        staff_id = staff_id_entry.get()

        # Query to delete staff from the Staff table
        query = "DELETE FROM Staff WHERE S_id = %s"
        try:
            cursor.execute(query, (staff_id,))
            conn.commit()
            messagebox.showinfo("Success", "Staff member deleted successfully.")
            delete_staff_window.destroy()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error occurred: {e}")

    delete_button = ttk.Button(delete_staff_window, text="Delete Staff", command=delete_staff_from_db)
    delete_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

def view_staff_list():
    view_staff_window = tk.Toplevel(root)
    view_staff_window.title("Staff List")

    staff_tree = ttk.Treeview(view_staff_window, columns=("ID", "Name", "Email", "Phone", "Type"), show="headings")
    staff_tree.heading("ID", text="ID")
    staff_tree.heading("Name", text="Name")
    staff_tree.heading("Email", text="Email")
    staff_tree.heading("Phone", text="Phone")
    staff_tree.heading("Type", text="Type")
    staff_tree.pack(fill="both", expand=True)

    # Query to fetch staff data from the Staff table
    query = "SELECT S_id, S_name, S_email, S_phone, S_type FROM Staff"
    cursor.execute(query)
    staff_data = cursor.fetchall()

    for staff in staff_data:
        staff_tree.insert("", "end", values=staff)

def add_book():
    add_book_window = tk.Toplevel(root)
    add_book_window.title("Add Book/E-Resource")

    id_label = ttk.Label(add_book_window, text="ID:")
    id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    id_entry = ttk.Entry(add_book_window)
    id_entry.grid(row=0, column=1, padx=5, pady=5)

    title_label = ttk.Label(add_book_window, text="Title:")
    title_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    title_entry = ttk.Entry(add_book_window)
    title_entry.grid(row=1, column=1, padx=5, pady=5)

    author_label = ttk.Label(add_book_window, text="Author:")
    author_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    author_entry = ttk.Entry(add_book_window)
    author_entry.grid(row=2, column=1, padx=5, pady=5)

    isbn_label = ttk.Label(add_book_window, text="ISBN:")
    isbn_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    isbn_entry = ttk.Entry(add_book_window)
    isbn_entry.grid(row=3, column=1, padx=5, pady=5)

    category_label = ttk.Label(add_book_window, text="Category:")
    category_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
    category_entry = ttk.Entry(add_book_window)
    category_entry.grid(row=4, column=1, padx=5, pady=5)

    price_label = ttk.Label(add_book_window, text="Price:")
    price_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
    price_entry = ttk.Entry(add_book_window)
    price_entry.grid(row=5, column=1, padx=5, pady=5)

    publisher_label = ttk.Label(add_book_window, text="Publisher ID:")
    publisher_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
    publisher_entry = ttk.Entry(add_book_window)
    publisher_entry.grid(row=6, column=1, padx=5, pady=5)

    def add_book_to_db():
        id = id_entry.get()
        title = title_entry.get()
        author = author_entry.get()
        isbn = isbn_entry.get()
        category = category_entry.get()
        price = price_entry.get()
        publisher_id = publisher_entry.get()

        # Query to insert new book into the Books table
        query = "INSERT INTO Books (B_id, Title, Author, ISBN, Category, Price, P_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        try:
            cursor.execute(query, (id, title, author, isbn, category, price, publisher_id))
            conn.commit()
            messagebox.showinfo("Success", "Book/E-Resource added successfully.")
            add_book_window.destroy()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error occurred: {e}")

    add_button = ttk.Button(add_book_window, text="Add Book/E-Resource", command=add_book_to_db)
    add_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

def update_book():
    update_book_window = tk.Toplevel(root)
    update_book_window.title("Update Book/E-Resource")

    book_id_label = ttk.Label(update_book_window, text="Book ID:")
    book_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    book_id_entry = ttk.Entry(update_book_window)
    book_id_entry.grid(row=0, column=1, padx=5, pady=5)

    title_label = ttk.Label(update_book_window, text="Title:")
    title_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    title_entry = ttk.Entry(update_book_window)
    title_entry.grid(row=1, column=1, padx=5, pady=5)

    author_label = ttk.Label(update_book_window, text="Author:")
    author_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    author_entry = ttk.Entry(update_book_window)
    author_entry.grid(row=2, column=1, padx=5, pady=5)

    isbn_label = ttk.Label(update_book_window, text="ISBN:")
    isbn_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    isbn_entry = ttk.Entry(update_book_window)
    isbn_entry.grid(row=3, column=1, padx=5, pady=5)

    category_label = ttk.Label(update_book_window, text="Category:")
    category_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
    category_entry = ttk.Entry(update_book_window)
    category_entry.grid(row=4, column=1, padx=5, pady=5)

    price_label = ttk.Label(update_book_window, text="Price:")
    price_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
    price_entry = ttk.Entry(update_book_window)
    price_entry.grid(row=5, column=1, padx=5, pady=5)

    publisher_label = ttk.Label(update_book_window, text="Publisher ID:")
    publisher_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
    publisher_entry = ttk.Entry(update_book_window)
    publisher_entry.grid(row=6, column=1, padx=5, pady=5)

    def update_book_in_db():
        book_id = book_id_entry.get()
        title = title_entry.get()
        author = author_entry.get()
        isbn = isbn_entry.get()
        category = category_entry.get()
        price = price_entry.get()
        publisher_id = publisher_entry.get()

        # Query to update book information in the Books table
        query = "UPDATE Books SET Title = %s, Author = %s, ISBN = %s, Category = %s, Price = %s, P_id = %s WHERE Book_id = %s"
        try:
            cursor.execute(query, (title, author, isbn, category, price, publisher_id, book_id))
            conn.commit()
            messagebox.showinfo("Success", "Book/E-Resource updated successfully.")
            update_book_window.destroy()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error occurred: {e}")

    update_button = ttk.Button(update_book_window, text="Update Book/E-Resource", command=update_book_in_db)
    update_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

def delete_book():
    delete_book_window = tk.Toplevel(root)
    delete_book_window.title("Delete Book/E-Resource")

    book_id_label = ttk.Label(delete_book_window, text="Book ID:")
    book_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    book_id_entry = ttk.Entry(delete_book_window)
    book_id_entry.grid(row=0, column=1, padx=5, pady=5)

    def delete_book_from_db():
        book_id = book_id_entry.get()

        # Query to delete book from the Books table
        query = "DELETE FROM Books WHERE Book_id = %s"
        try:
            cursor.execute(query, (book_id,))
            conn.commit()
            messagebox.showinfo("Success", "Book/E-Resource deleted successfully.")
            delete_book_window.destroy()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error occurred: {e}")

    delete_button = ttk.Button(delete_book_window, text="Delete Book/E-Resource", command=delete_book_from_db)
    delete_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

def view_book_list():
    view_book_window = tk.Toplevel(root)
    view_book_window.title("Books and E-Resources List")

    book_tree = ttk.Treeview(view_book_window, columns=("ID", "Title", "Author", "ISBN", "Category", "Price", "Publisher"), show="headings")
    book_tree.heading("ID", text="ID")
    book_tree.heading("Title", text="Title")
    book_tree.heading("Author", text="Author")
    book_tree.heading("ISBN", text="ISBN")
    book_tree.heading("Category", text="Category")
    book_tree.heading("Price", text="Price")
    book_tree.heading("Publisher", text="Publisher")
    book_tree.pack(fill="both", expand=True)

    # Query to fetch book data from the Books table
    query = """
        SELECT b.Book_id, b.Title, b.Author, b.ISBN, b.Category, b.Price, p.P_name
        FROM Books b
        JOIN Publisher p ON b.P_id = p.P_id
    """
    cursor.execute(query)
    book_data = cursor.fetchall()

    for book in book_data:
        book_tree.insert("", "end", values=book)

def add_publisher():
    add_publisher_window = tk.Toplevel(root)
    add_publisher_window.title("Add Publisher")

    id_label = ttk.Label(add_publisher_window, text="ID:")
    id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    id_entry = ttk.Entry(add_publisher_window)
    id_entry.grid(row=0, column=1, padx=5, pady=5)

    name_label = ttk.Label(add_publisher_window, text="Name:")
    name_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    name_entry = ttk.Entry(add_publisher_window)
    name_entry.grid(row=1, column=1, padx=5, pady=5)

    address_label = ttk.Label(add_publisher_window, text="Address:")
    address_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    address_entry = ttk.Entry(add_publisher_window)
    address_entry.grid(row=2, column=1, padx=5, pady=5)

    def add_publisher_to_db():
        id = id_entry.get()
        name = name_entry.get()
        address = address_entry.get()

        # Query to insert new publisher into the Publisher table
        query = "INSERT INTO Publisher (P_id, P_name, P_address) VALUES (%s, %s, %s)"
        try:
            cursor.execute(query, (id, name, address))
            conn.commit()
            messagebox.showinfo("Success", "Publisher added successfully.")
            add_publisher_window.destroy()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error occurred: {e}")

    add_button = ttk.Button(add_publisher_window, text="Add Publisher", command=add_publisher_to_db)
    add_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

def update_publisher():
    update_publisher_window = tk.Toplevel(root)
    update_publisher_window.title("Update Publisher")

    publisher_id_label = ttk.Label(update_publisher_window, text="Publisher ID:")
    publisher_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    publisher_id_entry = ttk.Entry(update_publisher_window)
    publisher_id_entry.grid(row=0, column=1, padx=5, pady=5)

    name_label = ttk.Label(update_publisher_window, text="Name:")
    name_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    name_entry = ttk.Entry(update_publisher_window)
    name_entry.grid(row=1, column=1, padx=5, pady=5)

    address_label = ttk.Label(update_publisher_window, text="Address:")
    address_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    address_entry = ttk.Entry(update_publisher_window)
    address_entry.grid(row=2, column=1, padx=5, pady=5)

    def update_publisher_in_db():
        publisher_id = publisher_id_entry.get()
        name = name_entry.get()
        address = address_entry.get()

        # Query to update publisher information in the Publisher table
        query = "UPDATE Publisher SET P_name = %s, P_address = %s WHERE P_id = %s"
        try:
            cursor.execute(query, (name, address, publisher_id))
            conn.commit()
            messagebox.showinfo("Success", "Publisher updated successfully.")
            update_publisher_window.destroy()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error occurred: {e}")

    update_button = ttk.Button(update_publisher_window, text="Update Publisher", command=update_publisher_in_db)
    update_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

def delete_publisher():
    delete_publisher_window = tk.Toplevel(root)
    delete_publisher_window.title("Delete Publisher")

    publisher_id_label = ttk.Label(delete_publisher_window, text="Publisher ID:")
    publisher_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    publisher_id_entry = ttk.Entry(delete_publisher_window)
    publisher_id_entry.grid(row=0, column=1, padx=5, pady=5)

    def delete_publisher_from_db():
        publisher_id = publisher_id_entry.get()

        # Query to delete publisher from the Publisher table
        query = "DELETE FROM Publisher WHERE P_id = %s"
        try:
            cursor.execute(query, (publisher_id,))
            conn.commit()
            messagebox.showinfo("Success", "Publisher deleted successfully.")
            delete_publisher_window.destroy()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error occurred: {e}")

    delete_button = ttk.Button(delete_publisher_window, text="Delete Publisher", command=delete_publisher_from_db)
    delete_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

def view_publisher_list():
    view_publisher_window = tk.Toplevel(root)
    view_publisher_window.title("Publishers List")

    publisher_tree = ttk.Treeview(view_publisher_window, columns=("ID", "Name", "Address"), show="headings")
    publisher_tree.heading("ID", text="ID")
    publisher_tree.heading("Name", text="Name")
    publisher_tree.heading("Address", text="Address")
    publisher_tree.pack(fill="both", expand=True)

    # Query to fetch publisher data from the Publisher table
    query = "SELECT P_id, P_name, P_address FROM Publisher"
    cursor.execute(query)
    publisher_data = cursor.fetchall()

    for publisher in publisher_data:
        publisher_tree.insert("", "end", values=publisher)

def view_report_list():
    view_report_window = tk.Toplevel(root)
    view_report_window.title("Reports List")

    report_tree = ttk.Treeview(view_report_window, columns=("Report ID", "User ID", "Book ID", "Issue Date", "Due Date", "Status"), show="headings")
    report_tree.heading("Report ID", text="Report ID")
    report_tree.heading("User ID", text="User ID")
    report_tree.heading("Book ID", text="Book ID")
    report_tree.heading("Issue Date", text="Issue Date")
    report_tree.heading("Due Date", text="Due Date")
    report_tree.heading("Status", text="Status")
    report_tree.pack(fill="both", expand=True)

    # Query to fetch report data from the Report table
    query = "SELECT Rp_id, U_id, Book_id, Issue_date, Due_date, Book_status FROM Report"
    cursor.execute(query)
    report_data = cursor.fetchall()

    for report in report_data:
        report_tree.insert("", "end", values=report)

def update_report_status():
    update_report_window = tk.Toplevel(root)
    update_report_window.title("Update Report Status")

    report_id_label = ttk.Label(update_report_window, text="Report ID:")
    report_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    report_id_entry = ttk.Entry(update_report_window)
    report_id_entry.grid(row=0, column=1, padx=5, pady=5)

    status_label = ttk.Label(update_report_window, text="New Status:")
    status_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    status_entry = ttk.Entry(update_report_window)
    status_entry.grid(row=1, column=1, padx=5, pady=5)

    def update_report_status_in_db():
        report_id = report_id_entry.get()
        new_status = status_entry.get()

        # Query to update report status in the Report table
        query = "UPDATE Report SET Book_status = %s WHERE Rp_id = %s"
        try:
            cursor.execute(query, (new_status, report_id))
            conn.commit()
            messagebox.showinfo("Success", "Report status updated successfully.")
            update_report_window.destroy()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error occurred: {e}")

    update_button = ttk.Button(update_report_window, text="Update Report Status", command=update_report_status_in_db)
    update_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

def view_fine_list():
    view_fine_window = tk.Toplevel(root)
    view_fine_window.title("Fines List")

    fine_tree = ttk.Treeview(view_fine_window, columns=("Account ID", "User ID", "Fine Amount", "Balance"), show="headings")
    fine_tree.heading("Account ID", text="Account ID")
    fine_tree.heading("User ID", text="User ID")
    fine_tree.heading("Fine Amount", text="Fine Amount")
    fine_tree.heading("Balance", text="Balance")
    fine_tree.pack(fill="both", expand=True)

    # Query to fetch fine data from the Account table
    query = "SELECT A_id, U_id, A_fine, A_bal FROM Account"
    cursor.execute(query)
    fine_data = cursor.fetchall()

    for fine in fine_data:
        fine_tree.insert("", "end", values=fine)

def update_fine_amounts():
    update_fine_window = tk.Toplevel(root)
    update_fine_window.title("Update Fine Amounts")

    account_id_label = ttk.Label(update_fine_window, text="Account ID:")
    account_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    account_id_entry = ttk.Entry(update_fine_window)
    account_id_entry.grid(row=0, column=1, padx=5, pady=5)

    fine_amount_label = ttk.Label(update_fine_window, text="New Fine Amount:")
    fine_amount_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    fine_amount_entry = ttk.Entry(update_fine_window)
    fine_amount_entry.grid(row=1, column=1, padx=5, pady=5)

    def update_fine_amount_in_db():
        account_id = account_id_entry.get()
        new_fine_amount = fine_amount_entry.get()

        # Query to update fine amount in the Account table
        query = "UPDATE Account SET A_fine = %s WHERE A_id = %s"
        try:
            cursor.execute(query, (new_fine_amount, account_id))
            conn.commit()
            messagebox.showinfo("Success", "Fine amount updated successfully.")
            update_fine_window.destroy()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error occurred: {e}")

    update_button = ttk.Button(update_fine_window, text="Update Fine Amount", command=update_fine_amount_in_db)
    update_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Helper function to fetch members from the database
def fetch_members():
    query = "SELECT M_id, M_name, M_email, M_phone, M_add FROM Members"
    cursor.execute(query)
    return cursor.fetchall()

# Helper function to fetch books from the database
def fetch_books():
    query = "SELECT Book_id, Title, Author, ISBN, Category, Price FROM Books"
    cursor.execute(query)
    return cursor.fetchall()

# Helper function to fetch reports from the database
def fetch_reports():
    query = "SELECT Rp_id, U_id, Book_id, Issue_date, Due_date, Book_status FROM Report"
    cursor.execute(query)
    return cursor.fetchall()

# Helper function to fetch e-resources from the database
def fetch_eresources():
    query = "SELECT Er_id, Er_Title, url, Er_access FROM E_Resources"
    cursor.execute(query)
    return cursor.fetchall()

def fetch_account_details(member_id):
    query = "SELECT A_id, A_fine, A_bal FROM Account WHERE U_id = %s"
    cursor.execute(query, (member_id,))
    return cursor.fetchone()

def fetch_fines():
    query = "SELECT A_id, U_id, A_fine, A_bal FROM Account"
    cursor.execute(query)
    return cursor.fetchall()

# Add a new member
def add_member():
    add_member_window = tk.Toplevel(root)
    add_member_window.title("Add Member")

    # Create form fields for member details
    id_label = ttk.Label(add_member_window, text="ID:")
    id_label.grid(row=0, column=0, padx=5, pady=5)
    id_entry = ttk.Entry(add_member_window)
    id_entry.grid(row=0, column=1, padx=5, pady=5)

    name_label = ttk.Label(add_member_window, text="Name:")
    name_label.grid(row=1, column=0, padx=5, pady=5)
    name_entry = ttk.Entry(add_member_window)
    name_entry.grid(row=1, column=1, padx=5, pady=5)

    email_label = ttk.Label(add_member_window, text="Email:")
    email_label.grid(row=2, column=0, padx=5, pady=5)
    email_entry = ttk.Entry(add_member_window)
    email_entry.grid(row=2, column=1, padx=5, pady=5)

    phone_label = ttk.Label(add_member_window, text="Phone:")
    phone_label.grid(row=3, column=0, padx=5, pady=5)
    phone_entry = ttk.Entry(add_member_window)
    phone_entry.grid(row=3, column=1, padx=5, pady=5)

    address_label = ttk.Label(add_member_window, text="Address:")
    address_label.grid(row=4, column=0, padx=5, pady=5)
    address_entry = ttk.Entry(add_member_window)
    address_entry.grid(row=4, column=1, padx=5, pady=5)

    def save_member():
        id = id_entry.get()
        name = name_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        address = address_entry.get()

        query = "INSERT INTO Members (M_id, M_name, M_email, M_phone, M_add) VALUES (%s, %s, %s, %s, %s)"
        values = (id, name, email, phone, address)
        cursor.execute(query, values)
        conn.commit()
        messagebox.showinfo("Success", "Member added successfully.")
        add_member_window.destroy()

    save_button = ttk.Button(add_member_window, text="Save", command=save_member)
    save_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Update an existing member
def update_member():
    update_member_window = tk.Toplevel(root)
    update_member_window.title("Update Member")

    # Create a combobox to select the member
    member_label = ttk.Label(update_member_window, text="Select Member:")
    member_label.grid(row=0, column=0, padx=5, pady=5)
    member_combobox = ttk.Combobox(update_member_window, values=[f"{m[0]} - {m[1]}" for m in fetch_members()])
    member_combobox.grid(row=0, column=1, padx=5, pady=5)

    # Create form fields for member details
    name_label = ttk.Label(update_member_window, text="Name:")
    name_label.grid(row=1, column=0, padx=5, pady=5)
    name_entry = ttk.Entry(update_member_window)
    name_entry.grid(row=1, column=1, padx=5, pady=5)

    email_label = ttk.Label(update_member_window, text="Email:")
    email_label.grid(row=2, column=0, padx=5, pady=5)
    email_entry = ttk.Entry(update_member_window)
    email_entry.grid(row=2, column=1, padx=5, pady=5)

    phone_label = ttk.Label(update_member_window, text="Phone:")
    phone_label.grid(row=3, column=0, padx=5, pady=5)
    phone_entry = ttk.Entry(update_member_window)
    phone_entry.grid(row=3, column=1, padx=5, pady=5)

    address_label = ttk.Label(update_member_window, text="Address:")
    address_label.grid(row=4, column=0, padx=5, pady=5)
    address_entry = ttk.Entry(update_member_window)
    address_entry.grid(row=4, column=1, padx=5, pady=5)

    def update_member_details():
        selected_member = member_combobox.get().split(" - ")[0]
        name = name_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        address = address_entry.get()

        query = "UPDATE Members SET M_name = %s, M_email = %s, M_phone = %s, M_add = %s WHERE M_id = %s"
        values = (name, email, phone, address, selected_member)
        cursor.execute(query, values)
        conn.commit()
        messagebox.showinfo("Success", "Member updated successfully.")
        update_member_window.destroy()

    update_button = ttk.Button(update_member_window, text="Update", command=update_member_details)
    update_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Delete a member
def delete_member():
    delete_member_window = tk.Toplevel(root)
    delete_member_window.title("Delete Member")

    # Create a combobox to select the member
    member_label = ttk.Label(delete_member_window, text="Select Member:")
    member_label.grid(row=0, column=0, padx=5, pady=5)
    member_combobox = ttk.Combobox(delete_member_window, values=[f"{m[0]} - {m[1]}" for m in fetch_members()])
    member_combobox.grid(row=0, column=1, padx=5, pady=5)

    def delete_member_details():
        selected_member = member_combobox.get().split(" - ")[0]

        query = "DELETE FROM Members WHERE M_id = %s"
        cursor.execute(query, (selected_member,))
        conn.commit()
        messagebox.showinfo("Success", "Member deleted successfully.")
        delete_member_window.destroy()

    delete_button = ttk.Button(delete_member_window, text="Delete", command=delete_member_details)
    delete_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

def view_member_list():
    view_members_window = tk.Toplevel(root)
    view_members_window.title("Members List")

    # Create a Treeview widget to display members
    members_treeview = ttk.Treeview(view_members_window, columns=("ID", "Name", "Email", "Phone", "Address"))
    members_treeview.heading("#0", text="")
    members_treeview.heading("ID", text="ID")
    members_treeview.heading("Name", text="Name")
    members_treeview.heading("Email", text="Email")
    members_treeview.heading("Phone", text="Phone")
    members_treeview.heading("Address", text="Address")
    members_treeview.pack(fill="both", expand=True)

# Fetch members from the database and populate the Treeview
    members = fetch_members()
    for member in members:
        members_treeview.insert("", "end", text="", values=member)

# Issue a book
def issue_book():
    issue_book_window = tk.Toplevel(root)
    issue_book_window.title("Issue Book")

    # Create a combobox to select the member
    member_label = ttk.Label(issue_book_window, text="Select Member:")
    member_label.grid(row=0, column=0, padx=5, pady=5)
    member_combobox = ttk.Combobox(issue_book_window, values=[f"{m[0]} - {m[1]}" for m in fetch_members()])
    member_combobox.grid(row=0, column=1, padx=5, pady=5)

    # Create a combobox to select the book
    book_label = ttk.Label(issue_book_window, text="Select Book:")
    book_label.grid(row=1, column=0, padx=5, pady=5)
    book_combobox = ttk.Combobox(issue_book_window, values=[f"{b[0]} - {b[1]}" for b in fetch_books()])
    book_combobox.grid(row=1, column=1, padx=5, pady=5)

    def issue_book_details():
        selected_member = member_combobox.get().split(" - ")[0]
        selected_book = book_combobox.get().split(" - ")[0]

        # Insert a new record into the Report table
        query = "INSERT INTO Report (U_id, Book_id, Issue_date, Due_date, Book_status) VALUES (%s, %s, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 14 DAY), 'issued')"
        values = (selected_member, selected_book)
        cursor.execute(query, values)
        conn.commit()

        messagebox.showinfo("Success", "Book issued successfully.")
        issue_book_window.destroy()

    issue_button = ttk.Button(issue_book_window, text="Issue", command=issue_book_details)
    issue_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Return a book
def return_book():
   return_book_window = tk.Toplevel(root)
   return_book_window.title("Return Book")

   # Create a combobox to select the report
   report_label = ttk.Label(return_book_window, text="Select Report:")
   report_label.grid(row=0, column=0, padx=5, pady=5)
   report_combobox = ttk.Combobox(return_book_window, values=[f"{r[0]} - Book ID: {r[2]} - Member ID: {r[1]}" for r in fetch_reports() if r[5] == 'issued'])
   report_combobox.grid(row=0, column=1, padx=5, pady=5)

   def return_book_details():
       selected_report = report_combobox.get().split(" - ")[0]

       # Update the Book_status in the Report table
       query = "UPDATE Report SET Book_status = 'returned' WHERE Rp_id = %s"
       cursor.execute(query, (selected_report,))
       conn.commit()

       messagebox.showinfo("Success", "Book returned successfully.")
       return_book_window.destroy()

   return_button = ttk.Button(return_book_window, text="Return", command=return_book_details)
   return_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# View books list
def view_book_list():
   view_books_window = tk.Toplevel(root)
   view_books_window.title("Books List")

   # Create a Treeview widget to display books
   books_treeview = ttk.Treeview(view_books_window, columns=("ID", "Title", "Author", "ISBN", "Category", "Price"))
   books_treeview.heading("#0", text="")
   books_treeview.heading("ID", text="ID")
   books_treeview.heading("Title", text="Title")
   books_treeview.heading("Author", text="Author")
   books_treeview.heading("ISBN", text="ISBN")
   books_treeview.heading("Category", text="Category")
   books_treeview.heading("Price", text="Price")
   books_treeview.pack(fill="both", expand=True)

   # Fetch books from the database and populate the Treeview
   books = fetch_books()
   for book in books:
       books_treeview.insert("", "end", text="", values=book)

# View fines list
def view_fine_list():
   view_fines_window = tk.Toplevel(root)
   view_fines_window.title("Fines List")

   # Create a Treeview widget to display fines
   fines_treeview = ttk.Treeview(view_fines_window, columns=("Account ID", "Member ID", "Fine Amount", "Balance"))
   fines_treeview.heading("#0", text="")
   fines_treeview.heading("Account ID", text="Account ID")
   fines_treeview.heading("Member ID", text="Member ID")
   fines_treeview.heading("Fine Amount", text="Fine Amount")
   fines_treeview.heading("Balance", text="Balance")
   fines_treeview.pack(fill="both", expand=True)

   # Fetch fines from the database and populate the Treeview
   query = "SELECT A_id, U_id, A_fine, A_bal FROM Account"
   cursor.execute(query)
   fines = cursor.fetchall()
   for fine in fines:
       fines_treeview.insert("", "end", text="", values=fine)

# Update fine amounts
def update_fine_amounts():
   update_fines_window = tk.Toplevel(root)
   update_fines_window.title("Update Fine Amounts")

   # Create a combobox to select the account
   account_label = ttk.Label(update_fines_window, text="Select Account:")
   account_label.grid(row=0, column=0, padx=5, pady=5)
   account_combobox = ttk.Combobox(update_fines_window, values=[f"{f[0]} - Member ID: {f[1]}" for f in fetch_fines()])
   account_combobox.grid(row=0, column=1, padx=5, pady=5)

   # Create an entry field for the new fine amount
   fine_label = ttk.Label(update_fines_window, text="New Fine Amount:")
   fine_label.grid(row=1, column=0, padx=5, pady=5)
   fine_entry = ttk.Entry(update_fines_window)
   fine_entry.grid(row=1, column=1, padx=5, pady=5)

   def update_fine_details():
       selected_account = account_combobox.get().split(" - ")[0]
       new_fine_amount = fine_entry.get()

       # Update the A_fine in the Account table
       query = "UPDATE Account SET A_fine = %s WHERE A_id = %s"
       cursor.execute(query, (new_fine_amount, selected_account))
       conn.commit()

       messagebox.showinfo("Success", "Fine amount updated successfully.")
       update_fines_window.destroy()

   update_button = ttk.Button(update_fines_window, text="Update", command=update_fine_details)
   update_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Display staff functionalities
def display_staff_functionalities():
   # Clear the login frame
   for widget in login_frame.winfo_children():
       widget.destroy()

   # Create a new frame for staff functionalities
   staff_frame = ttk.Frame(root, padding="20")
   staff_frame.grid(row=0, column=0, sticky="nsew")

   # Add functionalities for managing members
   member_label = ttk.Label(staff_frame, text="Manage Members", font=("Arial", 14, "bold"))
   member_label.grid(row=0, column=0, columnspan=2, pady=10)

   add_member_button = ttk.Button(staff_frame, text="Add Member", command=add_member)
   add_member_button.grid(row=1, column=0, padx=5, pady=5)

   update_member_button = ttk.Button(staff_frame, text="Update Member", command=update_member)
   update_member_button.grid(row=1, column=1, padx=5, pady=5)

   delete_member_button = ttk.Button(staff_frame, text="Delete Member", command=delete_member)
   delete_member_button.grid(row=2, column=0, padx=5, pady=5)

   view_member_button = ttk.Button(staff_frame, text="View Members List", command=view_member_list)
   view_member_button.grid(row=2, column=1, padx=5, pady=5)

   # Add functionalities for managing books
   book_label = ttk.Label(staff_frame, text="Manage Books", font=("Arial", 14, "bold"))
   book_label.grid(row=3, column=0, columnspan=2, pady=10)

   issue_book_button = ttk.Button(staff_frame, text="Issue Book", command=issue_book)
   issue_book_button.grid(row=4, column=0, padx=5, pady=5)

   return_book_button = ttk.Button(staff_frame, text="Return Book", command=return_book)
   return_book_button.grid(row=4, column=1, padx=5, pady=5)

   view_book_button = ttk.Button(staff_frame, text="View Books List", command=view_book_list)
   view_book_button.grid(row=5, column=0, padx=5, pady=5)

   # Add functionalities for managing fines
   fine_label = ttk.Label(staff_frame, text="Manage Fines", font=("Arial", 14, "bold"))
   fine_label.grid(row=6, column=0, columnspan=2, pady=10)

   view_fine_button = ttk.Button(staff_frame, text="View Fines List", command=view_fine_list)
   view_fine_button.grid(row=7, column=0, padx=5, pady=5)

   update_fine_button = ttk.Button(staff_frame, text="Update Fine Amounts", command=update_fine_amounts)
   update_fine_button.grid(row=7, column=1, padx=5, pady=5)


# Assuming you have a global variable to store the logged-in member's ID
logged_in_member_id = None

# View account balance
def view_account_balance():
    view_balance_window = tk.Toplevel(root)
    view_balance_window.title("View Account Balance")

    # Get the member ID from the logged-in member's ID
    member_id = logged_in_member_id

    account_details = fetch_account_details(member_id)
    if account_details:
        account_id, fine_amount, balance = account_details
        message = f"Account ID: {account_id}\nFine Amount: {fine_amount}\nBalance: {balance}"
    else:
        message = "No account found for the logged-in member."

    balance_label = ttk.Label(view_balance_window, text=message)
    balance_label.pack(padx=20, pady=20)

# Pay fines
def pay_fines():
    pay_fines_window = tk.Toplevel(root)
    pay_fines_window.title("Pay Fines")

    # Get the member ID from the logged-in member's ID
    member_id = logged_in_member_id

    account_details = fetch_account_details(member_id)
    if account_details:
        account_id, fine_amount, balance = account_details
        message = f"Account ID: {account_id}\nFine Amount: {fine_amount}\nBalance: {balance}"
    else:
        message = "No account found for the logged-in member."

    fine_label = ttk.Label(pay_fines_window, text=message)
    fine_label.pack(padx=20, pady=20)

    # Add functionality to pay the fine amount here

# View available books
def view_available_books():
    view_books_window = tk.Toplevel(root)
    view_books_window.title("Available Books")

    # Create a Treeview widget to display books
    books_treeview = ttk.Treeview(view_books_window, columns=("ID", "Title", "Author", "ISBN", "Category", "Price"))
    books_treeview.heading("#0", text="")
    books_treeview.heading("ID", text="ID")
    books_treeview.heading("Title", text="Title")
    books_treeview.heading("Author", text="Author")
    books_treeview.heading("ISBN", text="ISBN")
    books_treeview.heading("Category", text="Category")
    books_treeview.heading("Price", text="Price")
    books_treeview.pack(fill="both", expand=True)

    # Fetch books from the database and populate the Treeview
    books = fetch_books()
    for book in books:
        books_treeview.insert("", "end", text="", values=book)

# Request a book
def request_book():
    request_book_window = tk.Toplevel(root)
    request_book_window.title("Request Book")

    # Create a combobox to select the book
    book_label = ttk.Label(request_book_window, text="Select Book:")
    book_label.grid(row=0, column=0, padx=5, pady=5)
    book_combobox = ttk.Combobox(request_book_window, values=[f"{b[0]} - {b[1]}" for b in fetch_books()])
    book_combobox.grid(row=0, column=1, padx=5, pady=5)

    def request_book_details():
        selected_book = book_combobox.get().split(" - ")[0]

        # Get the member ID from the logged-in member's ID
        member_id = logged_in_member_id

        # Add a new record to the Request table
        query = "INSERT INTO Request (U_id, Book_id, Request_date) VALUES (%s, %s, CURDATE())"
        values = (member_id, selected_book)
        cursor.execute(query, values)
        conn.commit()

        messagebox.showinfo("Success", "Book request submitted successfully.")
        request_book_window.destroy()

    request_button = ttk.Button(request_book_window, text="Request", command=request_book_details)
    request_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
# View available e-resources
def view_available_eresources():
    view_eresources_window = tk.Toplevel(root)
    view_eresources_window.title("Available E-Resources")

    # Create a Treeview widget to display e-resources
    eresources_treeview = ttk.Treeview(view_eresources_window, columns=("ID", "Title", "URL", "Access"))
    eresources_treeview.heading("#0", text="")
    eresources_treeview.heading("ID", text="ID")
    eresources_treeview.heading("Title", text="Title")
    eresources_treeview.heading("URL", text="URL")
    eresources_treeview.heading("Access", text="Access")
    eresources_treeview.pack(fill="both", expand=True)

    # Fetch e-resources from the database and populate the Treeview
    eresources = fetch_eresources()
    for eresource in eresources:
        eresources_treeview.insert("", "end", text="", values=eresource)

# Access e-resources
def access_eresources():
    access_eresources_window = tk.Toplevel(root)
    access_eresources_window.title("Access E-Resources")

    # Create a combobox to select the e-resource
    eresource_label = ttk.Label(access_eresources_window, text="Select E-Resource:")
    eresource_label.grid(row=0, column=0, padx=5, pady=5)
    eresource_combobox = ttk.Combobox(access_eresources_window, values=[f"{er[0]} - {er[1]}" for er in fetch_eresources()])
    eresource_combobox.grid(row=0, column=1, padx=5, pady=5)

    def access_eresource_details():
        selected_eresource = eresource_combobox.get().split(" - ")[0]

        # Get the URL and access type of the selected e-resource
        query = "SELECT url, Er_access FROM E_Resources WHERE Er_id = %s"
        cursor.execute(query, (selected_eresource,))
        result = cursor.fetchone()

        if result:
            url, access_type = result
            message = f"URL: {url}\nAccess Type: {access_type}"
            messagebox.showinfo("E-Resource Access", message)
        else:
            messagebox.showerror("Error", "E-Resource not found.")

    access_button = ttk.Button(access_eresources_window, text="Access", command=access_eresource_details)
    access_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Display member functionalities
def display_member_functionalities():
    # Clear the login frame
    for widget in login_frame.winfo_children():
        widget.destroy()

    # Create a new frame for member functionalities
    member_frame = ttk.Frame(root, padding="20")
    member_frame.grid(row=0, column=0, sticky="nsew")

    # Add functionalities for managing account
    account_label = ttk.Label(member_frame, text="Manage Account", font=("Arial", 14, "bold"))
    account_label.grid(row=0, column=0, columnspan=2, pady=10)

    view_balance_button = ttk.Button(member_frame, text="View Account Balance", command=view_account_balance)
    view_balance_button.grid(row=1, column=0, padx=5, pady=5)

    pay_fine_button = ttk.Button(member_frame, text="Pay Fines", command=pay_fines)
    pay_fine_button.grid(row=1, column=1, padx=5, pady=5)

    # Add functionalities for managing books
    book_label = ttk.Label(member_frame, text="Manage Books", font=("Arial", 14, "bold"))
    book_label.grid(row=2, column=0, columnspan=2, pady=10)

    view_book_button = ttk.Button(member_frame, text="View Available Books", command=view_available_books)
    view_book_button.grid(row=3, column=0, padx=5, pady=5)

    request_book_button = ttk.Button(member_frame, text="Request Book", command=request_book)
    request_book_button.grid(row=3, column=1, padx=5, pady=5)

    # return_book_button = ttk.Button(member_frame, text="Return Book", command=return_book)
    # return_book_button.grid(row=4, column=0, padx=5, pady=5)

    # Add functionalities for managing e-resources
    eresource_label = ttk.Label(member_frame, text="Manage E-Resources", font=("Arial", 14, "bold"))
    eresource_label.grid(row=5, column=0, columnspan=2, pady=10)

    view_eresource_button = ttk.Button(member_frame, text="View Available E-Resources", command=view_available_eresources)
    view_eresource_button.grid(row=6, column=0, padx=5, pady=5)

    access_eresource_button = ttk.Button(member_frame, text="Access E-Resources", command=access_eresources)
    access_eresource_button.grid(row=6, column=1, padx=5, pady=5)

# Create the main window
root = tk.Tk()
root.title("Library Management System")

# Create a frame for the login options
login_frame = ttk.Frame(root, padding="20")
login_frame.grid(row=0, column=0, sticky="nsew")

# Create labels and entry fields for admin login
ad_name_label = ttk.Label(login_frame, text="Admin Name:")
ad_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
ad_name_entry = ttk.Entry(login_frame)
ad_name_entry.grid(row=0, column=1, padx=5, pady=5)

ad_pass_label = ttk.Label(login_frame, text="Admin Password:")
ad_pass_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
ad_pass_entry = ttk.Entry(login_frame, show="*")
ad_pass_entry.grid(row=1, column=1, padx=5, pady=5)

# Create a button for admin login
admin_login_button = ttk.Button(login_frame, text="Admin Login", command=admin_login)
admin_login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Create labels and entry fields for staff login
staff_name_label = ttk.Label(login_frame, text="Staff Name:")
staff_name_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
staff_name_entry = ttk.Entry(login_frame)
staff_name_entry.grid(row=3, column=1, padx=5, pady=5)

staff_email_label = ttk.Label(login_frame, text="Staff Email:")
staff_email_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
staff_email_entry = ttk.Entry(login_frame)
staff_email_entry.grid(row=4, column=1, padx=5, pady=5)

# Create a button for staff login
staff_login_button = ttk.Button(login_frame, text="Staff Login", command=staff_login)
staff_login_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Create labels and entry fields for member login
member_name_label = ttk.Label(login_frame, text="Member Name:")
member_name_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
member_name_entry = ttk.Entry(login_frame)
member_name_entry.grid(row=6, column=1, padx=5, pady=5)

member_email_label = ttk.Label(login_frame, text="Member Email:")
member_email_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")
member_email_entry = ttk.Entry(login_frame)
member_email_entry.grid(row=7, column=1, padx=5, pady=5)

# Create a button for member login
member_login_button = ttk.Button(login_frame, text="Member Login", command=member_login)
member_login_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

# Create an error label
error_label = ttk.Label(login_frame, text="", foreground="red")
error_label.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

# Add similar login options for staff and members

root.mainloop()