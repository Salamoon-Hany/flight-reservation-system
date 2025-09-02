import tkinter as tk
from tkinter import ttk, messagebox
from db import get_reservations, delete_reservation
from gui.edit_reservation import EditReservationPage
import datetime

class ReservationListPage(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Reservations - FlySky Reservations")
        self.geometry("900x650")
        self.configure(bg="white")
        
        self.primary_color = "#0078D4"
        self.secondary_color = "#f0f5f9"
        self.text_color = "#333333"
        
        try:
            self.iconbitmap("assets/favicon.ico")
        except:
            pass
            
        nav_bar = tk.Frame(self, bg=self.primary_color, height=60)
        nav_bar.pack(fill="x")
        
        tk.Label(nav_bar, text="FlySky Reservations", font=("Arial", 16, "bold"), 
                bg=self.primary_color, fg="white").pack(side="left", padx=20, pady=10)
        
        header_frame = tk.Frame(self, bg="white")
        header_frame.pack(fill="x", pady=20)
        
        tk.Label(header_frame, text="Your Reservations", font=("Arial", 22, "bold"), 
                bg="white", fg=self.primary_color).pack()
        
        ttk.Separator(self, orient='horizontal').pack(fill='x', padx=20)
        
        content_frame = tk.Frame(self, bg="white", padx=20, pady=20)
        content_frame.pack(fill="both", expand=True)
        
        columns = ("id", "name", "flight", "date", "seat", "destination", "class")
        self.tree = ttk.Treeview(content_frame, columns=columns, show="headings", height=15)
        
        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 11), rowheight=25)
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#f0f0f0")
        
        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="Passenger Name")
        self.tree.heading("flight", text="Flight")
        self.tree.heading("date", text="Date")
        self.tree.heading("seat", text="Seat")
        self.tree.heading("destination", text="Destination") 
        self.tree.heading("class", text="Class")
        
        self.tree.column("id", width=50, anchor="center")
        self.tree.column("name", width=150)
        self.tree.column("flight", width=100, anchor="center")
        self.tree.column("date", width=100, anchor="center")
        self.tree.column("seat", width=80, anchor="center")
        self.tree.column("destination", width=140)
        self.tree.column("class", width=100)
        
        scrollbar = ttk.Scrollbar(content_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        self.refresh()

        button_frame = tk.Frame(self, bg="white", pady=15)
        button_frame.pack(fill="x", padx=20)
        
        button_style = {"font": ("Arial", 12), "width": 12, "cursor": "hand2"}
        tk.Button(button_frame, text="Edit", command=self.edit, bg=self.primary_color, fg="white", 
                **button_style).pack(side="left", padx=10)
        tk.Button(button_frame, text="Delete", command=self.delete, bg="#e81123", fg="white", 
                **button_style).pack(side="left", padx=10)
        tk.Button(button_frame, text="Back", command=self.destroy, bg="#333", fg="white", 
                **button_style).pack(side="right", padx=10)
        
        status_frame = tk.Frame(self, bg="#f5f5f5", height=30)
        status_frame.pack(side="bottom", fill="x")
        
        username = "Salamoon-Hany"
        username_label = tk.Label(status_frame, text=f"Current User's Login: {username}", 
                               font=("Arial", 9), bg="#f5f5f5", fg=self.text_color)
        username_label.pack(side="left", padx=10, pady=5)
        
        self.clock_label = tk.Label(status_frame, font=("Arial", 9), bg="#f5f5f5", 
                                  fg=self.text_color)
        self.clock_label.pack(side="right", padx=10, pady=5)
        self.update_clock()
        
    def update_clock(self):
        current_time = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        self.clock_label.config(text=f"Current Date and Time (UTC - YYYY-MM-DD HH:MM:SS formatted): {current_time}")
        self.after(1000, self.update_clock)

    def refresh(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
            
        for res in get_reservations():
            self.tree.insert("", "end", values=res)

    def get_selected(self):
        sel = self.tree.selection()
        if sel:
            return self.tree.item(sel[0])["values"]
        messagebox.showwarning("Selection Required", "Please select a reservation first.")
        return None

    def edit(self):
        row = self.get_selected()
        if row:
            EditReservationPage(self, row, self.refresh)

    def delete(self):
        row = self.get_selected()
        if row:
            if messagebox.askyesno("Delete Confirmation", "Are you sure you want to delete this reservation?"):
                delete_reservation(row[0])
                self.refresh()
                messagebox.showinfo("Success", "Reservation deleted successfully!")