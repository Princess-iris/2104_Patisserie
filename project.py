# project.py
import tkinter as tk
import webbrowser
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

class PastryShopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pastry Shop Ordering System")
        self.root.geometry("1366x768") 
        self.root.config(bg="#FFB6C1")
        self.cart = []  
        self.logged_in = False
        self.admin_email = "admin@gmail.com"
        self.admin_password = "admin123"

        self.create_navigation_bar()
        self.main_menu_frame = tk.Frame(self.root, bg="#FFB6C1")
        self.main_menu_frame.pack(fill="both", expand=True)
        self.create_main_menu()

    def create_navigation_bar(self):
        """Create the navigation bar (similar to website header)."""
        nav_bar = tk.Frame(self.root, bg="#4D2600", height=50)
        nav_bar.pack(fill="x")
        nav_buttons = [
            ("Home", self.show_home),
            ("Shop", self.open_shop_page),
            ("About Us", self.open_about_us),
            ("Contact", self.open_contact_info),
            ("Login", self.open_login_page),
        ]
        for text, command in nav_buttons:
            btn = tk.Button(nav_bar, text=text, font=("Times New Roman", 14), command=command, bg="#4D2600", fg="#FFFFFF", relief="flat")
            btn.pack(side="left", padx=10)

    def create_main_menu(self):
        """Main menu with title and buttons."""
        label = tk.Label(self.main_menu_frame, text="ALLÉE IRIS PÂTISSERIE", font=("Times New Roman", 75, "bold"), bg="#FFB6C1", fg="#4D2600")
        label.grid(row=0, column=0, pady=(80, 5))
        button = tk.Button(self.main_menu_frame, text="START SHOPPING", font=("Times New Roman", 15), bg="#4D2600", fg="WHITE", command=self.open_shop_page, width=40)
        button.grid(row=1, column=0, pady=(5, 300))
        self.main_menu_frame.grid_rowconfigure(0, weight=1)
        self.main_menu_frame.grid_rowconfigure(1, weight=1)
        self.main_menu_frame.grid_columnconfigure(0, weight=1)

    def show_home(self):
        """Show home page."""
        self.clear_frame(self.main_menu_frame)
        self.create_main_menu()

    def open_about_us(self):
        """Display the About Us page with detailed information."""
        self.clear_frame(self.main_menu_frame)
       

    def open_contact_info(self):
        """Display the Contact Information page."""
        self.clear_frame(self.main_menu_frame)
        contact_info = tk.Label(self.main_menu_frame, text="Contact Us:\nPhone: +63 912 345 6789\nEmail: pastries@example.com", font=("Times New Roman", 18), anchor="center", bg="#FFB6C1")
        contact_info.pack(pady=50)

    def open_shop_page(self):
        """Redirect to login page if not logged in, else open the shop page."""
        if not self.logged_in:
            self.open_login_page()
        else:
            self.show_shop_page()

    def show_shop_page(self):
        """Display the Shop Pastry Products page."""
        self.clear_frame(self.main_menu_frame)
        # (Shop page implementation omitted for brevity)

    def clear_frame(self, frame):
        """Clear all widgets in the current frame."""
        for widget in frame.winfo_children():
            widget.destroy()

    def calculate_total(cart):
        """Calculate the total price of items in the cart."""
        return sum(item["price"] * item["quantity"] for item in cart)

    def add_item_to_cart(cart, product_name, price, quantity):
        """Add an item to the cart."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        for item in cart:
            if item["product"] == product_name:
                item["quantity"] += quantity
                return 
        cart.append({"product": product _name, "price": price, "quantity": quantity})
        return cart

    def clear_cart(cart):
        """Clear all items from the cart."""
        cart.clear()
        return cart

    def start_application():
      """Initialize and start the Tkinter application."""
      root = tk.Tk()
      app = PastryShopApp(root)
      root.mainloop()

    if __name__ == "__main__":
     start_application()