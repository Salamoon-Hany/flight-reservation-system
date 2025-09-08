import tkinter as tk
from gui.home import HomePage
from db import init_db

def main():
    init_db()
    
    root = tk.Tk()
    root.title("FlySky Reservations")
    
    try:
        root.iconbitmap(r"D:\VS-Python\Flight_reservation\2530820_airplane_airplane mode_general_office_plane_icon.ico")
    except:
        pass
    
    app = HomePage(root)
    root.mainloop()

if __name__ == "__main__":
    main()