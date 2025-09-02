import tkinter as tk
from tkinter import ttk, PhotoImage
from gui.booking import BookingPage
from gui.reservation_list import ReservationListPage
import datetime

class HomePage(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.geometry("900x650")
        self.master.minsize(800, 600)
        
        self.primary_color = "#0078D4"  
        self.secondary_color = "#f0f5f9"
        self.text_color = "#333333"
        
        nav_bar = tk.Frame(self, bg=self.primary_color, height=60)
        nav_bar.pack(fill="x")
        
        try:
            self.logo_img = PhotoImage(file="assets/plane_icon.png").subsample(15, 15)
            logo_label = tk.Label(nav_bar, image=self.logo_img, bg=self.primary_color)
            logo_label.pack(side="left", padx=(20, 5), pady=10)
        except:
            pass
            
        tk.Label(nav_bar, text="FlySky Reservations", font=("Arial", 16, "bold"), 
                bg=self.primary_color, fg="white").pack(side="left", padx=5, pady=10)
        
        nav_btn_style = {"font": ("Arial", 12), "bg": self.primary_color, 
                         "fg": "white", "bd": 0, "cursor": "hand2"}
        
        tk.Button(nav_bar, text="View Reservations", command=self.open_res_list, 
                 **nav_btn_style).pack(side="right", padx=10, pady=10)
        
        tk.Button(nav_bar, text="Book Flight", command=self.open_booking, 
                 **nav_btn_style).pack(side="right", padx=10, pady=10)
                
        tk.Button(nav_bar, text="Home", **nav_btn_style).pack(side="right", padx=20, pady=10)
        
        content_frame = tk.Frame(self, bg="white")
        content_frame.pack(fill="both", expand=True)
        
        tk.Label(content_frame, text="Welcome to FlySky Reservations", 
                font=("Arial", 24, "bold"), fg=self.primary_color, 
                bg="white").pack(pady=(40, 10))
        
        tk.Label(content_frame, text="Book your flights and manage your reservations with our simple and intuitive system.", 
                font=("Arial", 12), fg=self.text_color, bg="white", 
                wraplength=600).pack(pady=(0, 40))
        
        cards_frame = tk.Frame(content_frame, bg="white")
        cards_frame.pack(pady=20, expand=True)
        
        book_card = tk.Frame(cards_frame, bg="white", bd=1, relief="solid", 
                            highlightbackground="#ddd", highlightthickness=1)
        book_card.pack(side="left", padx=20, pady=20, ipadx=20, ipady=20)
        
        icon_frame = tk.Canvas(book_card, width=80, height=80, bg="white", highlightthickness=0)
        icon_frame.create_oval(5, 5, 75, 75, fill="#e6f3fa", outline="")
        icon_frame.create_text(40, 40, text="✈️", font=("Arial", 24), fill=self.primary_color)
        icon_frame.pack(pady=15)
        
        tk.Label(book_card, text="Book a Flight", font=("Arial", 16, "bold"), 
                fg=self.primary_color, bg="white").pack(pady=5)
        
        tk.Label(book_card, text="Reserve your next flight by providing your details and flight information.", 
                font=("Arial", 10), fg=self.text_color, bg="white", 
                wraplength=300).pack(pady=10)
        
        book_btn = tk.Button(book_card, text="Book Flight", bg=self.primary_color, fg="white", 
                            font=("Arial", 12), width=25, cursor="hand2", 
                            command=self.open_booking)
        book_btn.pack(pady=15)
        
        view_card = tk.Frame(cards_frame, bg="white", bd=1, relief="solid", 
                            highlightbackground="#ddd", highlightthickness=1)
        view_card.pack(side="left", padx=20, pady=20, ipadx=20, ipady=20)
        
        icon_frame = tk.Canvas(view_card, width=80, height=80, bg="white", highlightthickness=0)
        icon_frame.create_oval(5, 5, 75, 75, fill="#e6f3fa", outline="")
        icon_frame.create_text(40, 40, text="≡", font=("Arial", 24), fill=self.primary_color)
        icon_frame.pack(pady=15)
        
        tk.Label(view_card, text="View Reservations", font=("Arial", 16, "bold"), 
                fg=self.primary_color, bg="white").pack(pady=5)
        
        tk.Label(view_card, text="Manage your existing reservations, view details, edit or cancel if needed.", 
                font=("Arial", 10), fg=self.text_color, bg="white", 
                wraplength=300).pack(pady=10)
        
        view_btn = tk.Button(view_card, text="View Reservations", bg=self.primary_color, fg="white", 
                            font=("Arial", 12), width=25, cursor="hand2", 
                            command=self.open_res_list)
        view_btn.pack(pady=15)
        
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
        
        self.pack(fill="both", expand=True)

    def update_clock(self):
        current_time = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        self.clock_label.config(text=f"Current Date and Time (UTC - YYYY-MM-DD HH:MM:SS formatted): {current_time}")
        self.after(1000, self.update_clock)

    def open_booking(self):
        booking_window = BookingPage(self.master)
        
    def open_res_list(self):
        list_window = ReservationListPage(self.master)