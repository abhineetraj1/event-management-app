import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv

# Create the main window
root = tk.Tk()
root.title("Event Management App")
root.geometry("800x400")
root.configure(bg="#000000")  # Set background color to black

# Create style for ttk elements
style = ttk.Style()
style.theme_create(
    "dark",
    settings={
        "TLabel": {
            "configure": {
                "foreground": "#C0C0C0",  # Set label foreground color to silver
                "background": "#000000",  # Set label background color to black
                "font": ("Helvetica", 12),
            }
        },
        "TButton": {
            "configure": {
                "foreground": "#000000",  # Set button foreground color to black
                "background": "#C0C0C0",  # Set button background color to silver
                "font": ("Helvetica", 12, "bold"),
            }
        },
        "TEntry": {
            "configure": {
                "foreground": "#C0C0C0",  # Set entry foreground color to silver
                "background": "#000000",  # Set entry background color to black
                "font": ("Helvetica", 12),
            }
        },
        "TListbox": {
            "configure": {
                "foreground": "#C0C0C0",  # Set listbox foreground color to silver
                "background": "#000000",  # Set listbox background color to black
                "font": ("Helvetica", 12),
            }
        },
    },
)
style.theme_use("dark")

# Create customer information list
customer_info = []

# Function to save customer information to a CSV file
def save_customer_info():
    place_of_visit = txt_place_of_visit.get()
    home_place = txt_home_place.get()
    email = txt_email.get()
    phone_number = txt_phone_number.get()
    customer_name = txt_customer_name.get()
    if place_of_visit and home_place and email and phone_number and customer_name:
        customer_info.append({"Place of Visit": place_of_visit,"Home Place": home_place,"Email": email,"Phone Number": phone_number,"Customer Name": customer_name,})
        with open("customer_info.csv", mode="a", newline="") as file:
            writer = csv.DictWriter(file,fieldnames=["Place of Visit","Home Place","Email","Phone Number","Customer Name",],)
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(customer_info[-1])
        messagebox.showinfo("Success", "Customer information saved successfully.")
        clear_fields()
    else:
        messagebox.showwarning("Error", "Please fill in all the fields.")

# Function to clear input fields
def clear_fields():
    txt_place_of_visit.delete(0, tk.END)
    txt_home_place.delete(0, tk.END)
    txt_email.delete(0, tk.END)
    txt_phone_number.delete(0, tk.END)
    txt_customer_name.delete(0, tk.END)

# Function to open the Add Travel Information window
def open_add_travel_window():
    add_travel_window = tk.Toplevel(root)
    add_travel_window.title("Add Travel Information")
    add_travel_window.geometry("400x500")
    add_travel_window.configure(bg="#000000")  # Set background color to black
    lbl_place_of_visit = ttk.Label(add_travel_window, text="Place of Visit:", style="TLabel")
    lbl_place_of_visit.pack(pady=10)
    txt_place_of_visit = ttk.Entry(add_travel_window, width=30)
    txt_place_of_visit.pack()
    lbl_home_place = ttk.Label(add_travel_window, text="Home Place:", style="TLabel")
    lbl_home_place.pack(pady=10)
    txt_home_place = ttk.Entry(add_travel_window, width=30)
    txt_home_place.pack()
    lbl_email = ttk.Label(add_travel_window, text="Email:", style="TLabel")
    lbl_email.pack(pady=10)
    txt_email = ttk.Entry(add_travel_window, width=30)
    txt_email.pack()
    lbl_phone_number = ttk.Label(add_travel_window, text="Phone Number:", style="TLabel")
    lbl_phone_number.pack(pady=10)
    txt_phone_number = ttk.Entry(add_travel_window, width=30)
    txt_phone_number.pack()
    lbl_customer_name = ttk.Label(add_travel_window, text="Customer Name:", style="TLabel")
    lbl_customer_name.pack(pady=10)
    txt_customer_name = ttk.Entry(add_travel_window, width=30)
    txt_customer_name.pack()
    btn_save_customer_info = ttk.Button(add_travel_window, text="Save", command=save_customer_info, style="TButton")
    btn_save_customer_info.pack(pady=10)

# Function to search for customer information
def search_customer_info():
    keyword = txt_search.get().lower()
    if keyword:
        found_info = []
        for info in customer_info:
            if (keyword in info["Place of Visit"].lower() or keyword in info["Home Place"].lower() or keyword in info["Email"].lower() or keyword in info["Phone Number"].lower() or keyword in info["Customer Name"].lower() ):
                found_info.append(info)
        if found_info:
            display_search_results(found_info)
        else:
            messagebox.showinfo("Search Results", "No matching records found.")
    else:
        messagebox.showwarning("Error", "Please enter a keyword to search.")

# Function to display search results
def display_search_results(results):
    result_window = tk.Toplevel(root)
    result_window.title("Search Results")
    result_window.geometry("600x400")
    result_window.configure(bg="#000000")  # Set background color to black
    lbl_results = ttk.Label(result_window, text="Search Results:", style="TLabel")
    lbl_results.pack(pady=10)
    results_listbox = tk.Listbox(result_window, width=50, height=10, bg="#000000", fg="#C0C0C0", font=("Helvetica", 12))
    results_listbox.pack(padx=20, pady=10)
    for info in results:
        results_listbox.insert(tk.END, f"Place of Visit: {info['Place of Visit']}\n"
            f"Home Place: {info['Home Place']}\n"
            f"Email: {info['Email']}\n"
            f"Phone Number: {info['Phone Number']}\n"
            f"Customer Name: {info['Customer Name']}\n"
            "-------------------------------",)

# Create Add Travel Information Button
btn_add_travel_info = ttk.Button(root, text="Add Travel Information", command=open_add_travel_window, style="TButton")
btn_add_travel_info.place(x=20, y=20)

# Create Search Entry Field and Button
lbl_search = ttk.Label(root, text="Search:", style="TLabel")
lbl_search.place(x=20, y=60)
txt_search = ttk.Entry(root, width=30)
txt_search.place(x=80, y=60)

btn_search = ttk.Button(root, text="Search", command=search_customer_info, style="TButton")
btn_search.place(x=320, y=60)

# Start the main event loop
root.mainloop()
