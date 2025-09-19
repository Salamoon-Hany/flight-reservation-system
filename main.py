import tkinter as tk
from gui.home import HomePage
from db import init_db

def main():
    init_db()
    
    root = tk.Tk()
    root.title("FlySky Reservations")
    
    try:
        root.iconbitmap(r"D:\VS-Python\New folder\Palne Icon.ico")
    except Exception as e:
        print(f"Icon load failed: {e}")
    
    app = HomePage(root)
    root.mainloop()

if __name__ == "__main__":
    main()