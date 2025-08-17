import tkinter as tk
from tkinter import messagebox, simpledialog


contacts = []


def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()
    address = entry_address.get().strip()
    
    if not name or not phone:
        messagebox.showerror("Error", "Name and Phone are required!")
        return
    
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    messagebox.showinfo("Success", "Contact added successfully!")
    clear_entries()
    refresh_listbox()


def refresh_listbox():
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']}")


def search_contact():
    query = entry_search.get().strip().lower()
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        if query in contact["name"].lower() or query in contact["phone"]:
            listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']}")


def delete_contact():
    selection = listbox_contacts.curselection()
    if not selection:
        messagebox.showerror("Error", "Select a contact to delete!")
        return
    index = selection[0]
    del contacts[index]
    refresh_listbox()


def update_contact():
    selection = listbox_contacts.curselection()
    if not selection:
        messagebox.showerror("Error", "Select a contact to update!")
        return
    index = selection[0]
    contact = contacts[index]
    
    name = simpledialog.askstring("Update Name", "Enter new name:", initialvalue=contact["name"])
    phone = simpledialog.askstring("Update Phone", "Enter new phone:", initialvalue=contact["phone"])
    email = simpledialog.askstring("Update Email", "Enter new email:", initialvalue=contact["email"])
    address = simpledialog.askstring("Update Address", "Enter new address:", initialvalue=contact["address"])
    
    contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
    refresh_listbox()


def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)


root = tk.Tk()
root.title("Contact Management System")
root.geometry("500x500")


tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root, width=40)
entry_name.pack()

tk.Label(root, text="Phone:").pack()
entry_phone = tk.Entry(root, width=40)
entry_phone.pack()

tk.Label(root, text="Email:").pack()
entry_email = tk.Entry(root, width=40)
entry_email.pack()

tk.Label(root, text="Address:").pack()
entry_address = tk.Entry(root, width=40)
entry_address.pack()


tk.Button(root, text="Add Contact", command=add_contact, bg="green", fg="white").pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact, bg="orange", fg="white").pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact, bg="red", fg="white").pack(pady=5)


tk.Label(root, text="Search:").pack()
entry_search = tk.Entry(root, width=30)
entry_search.pack()
tk.Button(root, text="Search", command=search_contact, bg="blue", fg="white").pack(pady=5)


listbox_contacts = tk.Listbox(root, width=50, height=10)
listbox_contacts.pack(pady=10)

refresh_listbox()

root.mainloop()
