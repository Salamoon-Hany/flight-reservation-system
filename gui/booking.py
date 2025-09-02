import tkinter as tk
from tkinter import ttk, messagebox
from db import add_reservation
import datetime

class BookingPage(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Book a Flight - FlySky Reservations")
        self.geometry("600x650")
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
        
        tk.Label(header_frame, text="Book a Flight", font=("Arial", 22, "bold"), 
                bg="white", fg=self.primary_color).pack()
        
        
        ttk.Separator(self, orient='horizontal').pack(fill='x', padx=20)
        
        
        form_frame = tk.Frame(self, bg="white", padx=20, pady=20)
        form_frame.pack(fill="both", expand=True)
        
        
        label_style = {"font": ("Arial", 12), "bg": "white", "fg": self.text_color, "anchor": "w"}
        entry_style = {"font": ("Arial", 12), "width": 30}
        
        
        form_row = 0
        
        
        tk.Label(form_frame, text="Passenger Name", **label_style).grid(row=form_row, column=0, sticky="w", pady=(10, 5))
        form_row += 1
        self.entry_name = tk.Entry(form_frame, **entry_style)
        self.entry_name.grid(row=form_row, column=0, sticky="w", pady=(0, 15))
        form_row += 1
        
        
        tk.Label(form_frame, text="Flight Number", **label_style).grid(row=form_row, column=0, sticky="w", pady=(10, 5))
        form_row += 1
        self.entry_flight = tk.Entry(form_frame, **entry_style)
        self.entry_flight.grid(row=form_row, column=0, sticky="w", pady=(0, 15))
        form_row += 1
        
        
        tk.Label(form_frame, text="Date (YYYY-MM-DD)", **label_style).grid(row=form_row, column=0, sticky="w", pady=(10, 5))
        form_row += 1
        self.entry_date = tk.Entry(form_frame, **entry_style)
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        self.entry_date.insert(0, today)
        self.entry_date.grid(row=form_row, column=0, sticky="w", pady=(0, 15))
        form_row += 1
        
        
        tk.Label(form_frame, text="Seat", **label_style).grid(row=form_row, column=0, sticky="w", pady=(10, 5))
        form_row += 1
        self.entry_seat = tk.Entry(form_frame, **entry_style)
        self.entry_seat.grid(row=form_row, column=0, sticky="w", pady=(0, 15))
        form_row += 1
        
        
        tk.Label(form_frame, text="Destination", **label_style).grid(row=form_row, column=0, sticky="w", pady=(10, 5))
        form_row += 1
        self.entry_dest = tk.Entry(form_frame, **entry_style)
        self.entry_dest.grid(row=form_row, column=0, sticky="w", pady=(0, 15))
        form_row += 1
        
        
        tk.Label(form_frame, text="Ticket Class", **label_style).grid(row=form_row, column=0, sticky="w", pady=(10, 5))
        form_row += 1
        
        self.ticket_class = tk.StringVar()
        class_frame = tk.Frame(form_frame, bg="white")
        class_frame.grid(row=form_row, column=0, sticky="w", pady=(0, 15))
        
        class_combo = ttk.Combobox(class_frame, textvariable=self.ticket_class, width=28, font=("Arial", 12))
        class_combo['values'] = ('Economy', 'Business', 'First Class')
        class_combo.current(0)
        class_combo.pack(side="left")
        form_row += 1
        
        
        button_frame = tk.Frame(form_frame, bg="white")
        button_frame.grid(row=form_row, column=0, sticky="w", pady=20)
        
        tk.Button(button_frame, text="Book Flight", command=self.book, bg=self.primary_color, fg="white", 
                font=("Arial", 12), width=15, cursor="hand2").pack(side="left", padx=(0, 10))
        
        tk.Button(button_frame, text="Cancel", command=self.destroy, bg="#e81123", fg="white", 
                font=("Arial", 12), width=15, cursor="hand2").pack(side="left")
        
        
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

    def book(self):
        name = self.entry_name.get()
        flight = self.entry_flight.get()
        date = self.entry_date.get()
        seat = self.entry_seat.get()
        dest = self.entry_dest.get()
        ticket_class = self.ticket_class.get()
        
        if all([name, flight, date, seat, dest, ticket_class]):
            add_reservation(name, flight, date, seat, dest, ticket_class)
            messagebox.showinfo("Success", "Your flight has been booked successfully!")
            self.destroy()
        else:
            messagebox.showwarning("Incomplete Information", "Please fill in all fields to complete your booking.")