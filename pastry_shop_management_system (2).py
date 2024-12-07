import tkinter as tk
import webbrowser
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
from tkinter import messagebox


class PastryShopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pastry Shop Management System")
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

     canvas = tk.Canvas(self.main_menu_frame, bg="#FFB6C1")
     scrollable_frame = tk.Frame(canvas, bg="#FFB6C1")
    
     scrollbar = tk.Scrollbar(self.main_menu_frame, orient="vertical", command=canvas.yview)
     canvas.configure(yscrollcommand=scrollbar.set)

     scrollbar.pack(side="right", fill="y")
     canvas.pack(side="left", fill="both", expand=True)

     canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

     title_label = tk.Label(scrollable_frame, text="About Allée Iris Pâtisserie", font=("Georgia", 40, "bold"), fg="#4D2600", bg="#FFB6C1")
     title_label.pack(pady=40, anchor="center")

     intro_text = """
Welcome to Allée Iris Pâtisserie, where passion for baking and love for pastry come together!
Our pastry store, founded in 2024, is dedicated to making original, handcrafted desserts that 
honor the great traditions of baking. Allee Iris Patisserie values quality.
That is why we utilize only the best, locally sourced ingredients to produce our pastries fresh every day.
"""
     intro_label = tk.Label(scrollable_frame, text=intro_text, font=("Times New Roman", 16), fg="#4D2600", bg="#FFB6C1", justify="center", wraplength=1250)
     intro_label.pack(pady=20, padx=40, anchor="center")

     specialties_text = """
At Allée Iris Pâtisserie, we offer a variety of exquisite treats that are sure to delight. Our Artisan Cakes are perfect for any occasion, whether it's a birthday, wedding, or just because, each one is baked, decorated, and filled with fresh, high-quality ingredients. Our Fresh Pastries, including flaky croissants and creamy éclairs, are made daily with love and care. We also offer beautifully decorated Cupcakes and Tarts, available in a variety of fun, seasonal flavors, with rich fillings from fruity to decadent chocolate. To complete your experience, our Artisan Breads, from soft, rustic loaves to crispy baguettes, are made with passion and attention to detail. We pride ourselves on exceptional customer service and aim to make every visit special—whether you're a first-timer or a regular, we want you to feel welcome and satisfied each time you indulge in our baked goods.
"""
     specialties_label = tk.Label(scrollable_frame, text=specialties_text, font=("Times New Roman", 16), fg="#4D2600", bg="#FFB6C1", justify="center", wraplength=1250)
     specialties_label.pack(pady=20, padx=40, anchor="center")

     mission_text = """
Our mission is straightforward: to spread the art of baking across our community. We want every customer who enters through our doors to feel as if they're in a Classic patisserie. We take pleasure in providing a great experience, whether you're enjoying a morning croissant with a cup of coffee or buying an adapted cake for a special occasion.
"""
     mission_label = tk.Label(scrollable_frame, text=mission_text, font=("Times New Roman", 16), fg="#4D2600", bg="#FFB6C1", justify="center", wraplength=1250)
     mission_label.pack(pady=20, padx=40, anchor="center")

     unique_text = """
What makes Allée Iris Pâtisserieunique is our dedication to quality and passion for baking. We pride ourselves on making all our pastries fresh daily, ensuring that every bite is a true delight. We offer personalized cakes and pastries to enhance special occasions, adding a personal touch to every celebration. Our commitment to using high-quality ingredients from local farmers and producers means that each creation is crafted with the finest products. Above all, we are passionate about baking, and we put our heart and soul into every pastry we make, ensuring that each visit to our bakery is a memorable one.
"""
     unique_label = tk.Label(scrollable_frame, text=unique_text, font=("Times New Roman", 16), fg="#4D2600", bg="#FFB6C1", justify="center", wraplength=1250)
     unique_label.pack(pady=20, padx=40, anchor="center")

     story_text = """
Our Story:
Alessandra and Iris have always shared a love for pastries and a dream of opening their bakery. 
During their time in college, they envisioned a place to combine their passion for baking and their close friendship into something meaningful for the community. 

After years of dedication and hard work, they opened Allée Iris Pâtisserie to bring their dream to life. Their mission has always been to create more than just a bakery—a cozy, friendly space where everyone feels welcome and can enjoy delightful pastries.
"""
     story_label = tk.Label(scrollable_frame, text=story_text, font=("Brush Script MT", 18, "italic"), fg="#4D2600", bg="#FFEBEB", justify="center", wraplength=800, relief="solid", padx=20, pady=20)
     story_label.pack(pady=100, padx=40, anchor="center")

     join_text = """
JOIN US: 
      Experience the warmth, tradition, and sweetness that define Allée Iris Pâtisserie. Whether you’re stopping by for a quick treat, placing an order for a custom cake, or just looking for a cozy spot to enjoy a coffee, we can’t wait to welcome you. See you soon!
"""
     join_label = tk.Label(scrollable_frame, text=join_text, font=("Times New Roman", 16), fg="#4D2600", bg="#FFB6C1", justify="center", wraplength=1250)
     join_label.pack(pady=20, padx=40, anchor="center")

     scrollable_frame.update_idletasks()
     canvas.config(scrollregion=canvas.bbox("all"))


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
        shop_label = tk.Label(self.main_menu_frame, text="SHOP PASTRY PRODUCTS", font=("Times New Roman", 45, "bold"), fg="#4D2600", bg="#FFB6C1")
        shop_label.pack(pady=20)

        view_cart_button = tk.Button(self.main_menu_frame, text="View Cart", font=("Times New Roman", 14), fg="#4D2600", command=self.view_cart)
        view_cart_button.place(relx=1.0, y=10, anchor="ne") 

        categories = [
            ("Cakes", self.show_cakes),
            ("Pastries", self.show_pastries),
            ("Cupcakes", self.show_cupcakes),
            ("Tarts", self.show_tarts),
            ("Breads", self.show_breads),
        ]

        for category_name, category_function in categories:
            tk.Button(self.main_menu_frame, text=category_name, font=("Times New Roman", 14), 
              bg="#4D2600", fg="WHITE", command=category_function, width=40, height=2 ).pack(pady=10, padx=20)

    def show_products(self, category_name, products):
     """Display products in a given category in a grid layout."""
     self.clear_frame(self.main_menu_frame)
     tk.Label(self.main_menu_frame, text=f"Available {category_name}", font=("Times New Roman", 40, "bold"), fg="#4D2600", bg="#FFB6C1").pack(pady=20, anchor="center")

     center_frame = tk.Frame(self.main_menu_frame, bg="#FFB6C1")
     center_frame.pack(fill="both", expand=True)

     product_frame = tk.Frame(center_frame, bg="#FFB6C1")
     product_frame.pack(pady=20)

     self.quantities = [] 

     for index, (product_name, price, img_path) in enumerate(products):
        product_panel = tk.Frame(product_frame, bg="#FFB6C1", bd=2, relief="groove")
        product_panel.grid(row=index // 3, column=index % 3, padx=10, pady=10, sticky="nsew")

        tk.Label(product_panel, text=product_name, font=("Times New Roman", 14, "bold"), fg="#4D2600", bg="#FFB6C1").pack(pady=(5, 5))

        tk.Label(product_panel, text="Quantity:", font=("Times New Roman", 12), fg="#4D2600", bg="#FFB6C1").pack(pady=(5, 0))
        quantity_entry = tk.Entry(product_panel, font=("Times New Roman", 12), width=10)
        quantity_entry.pack(pady=(0, 5))
        self.quantities.append((product_name, quantity_entry))

        add_button = tk.Button(product_panel, text=f"Add to Cart - PHP {price}", font=("Times New Roman", 12), command=lambda p=product_name, pr=price, qty_entry=quantity_entry: self.add_to_cart(p, pr, qty_entry), width=30)
        add_button.pack(pady=(5, 10))

     for i in range(3):
        product_frame.grid_columnconfigure(i, weight=1)

     for i in range((len(products) + 2) // 3):
        product_frame.grid_rowconfigure(i, weight=1)

    def add_to_cart(self, product_name, price, quantity_entry):
      """Add products to the cart with specified quantity."""
      try:
        quantity = int(quantity_entry.get())
        if quantity < 0:
            messagebox.showwarning("Invalid Quantity", "0 and negative values are not allowed.")
            return
        elif quantity == 0:
            messagebox.showwarning("Invalid Quantity", "0 is not a valid quantity.")
            return
      except ValueError:
        messagebox.showwarning("Invalid Quantity", "Please enter a valid number.")
        return

    # Check if the product already exists in the cart
      for item in self.cart:
        if item["product"] == product_name:
            item["quantity"] += quantity
            messagebox.showinfo("Updated Cart", f"Another {quantity} {product_name}(s) added to your cart!")
            return

    # Add the product to the cart if it doesn't exist
      self.cart.append({"product": product_name, "price": price, "quantity": quantity})
      messagebox.showinfo("Added to Cart", f"{quantity} {product_name}(s) have been added to your cart!")

    def view_cart(self):
     """Display the cart page."""
     self.clear_frame(self.main_menu_frame)

     if not self.cart:
        tk.Label(self.main_menu_frame, text="Your Cart is Empty", font=("Times New Roman", 18), bg="#FFB6C1").pack(pady=50)
        return

     cart_frame = tk.Frame(self.main_menu_frame, bg="#FFB6C1")
     cart_frame.pack(fill="both", expand=True)

     total_price = 0
     for item in self.cart:
        product_name = item["product"]
        price = item["price"]
        quantity = item["quantity"]
        total_price += price * quantity

        cart_item_label = tk.Label(cart_frame, text=f"{product_name} x {quantity} - PHP {price * quantity}", font=("Times New Roman", 14), bg="#FFB6C1")
        cart_item_label.pack(pady=5)

     checkout_button = tk.Button(cart_frame, text=f"Checkout - Total: PHP {total_price}", font=("Times New Roman", 14), command=lambda: self.checkout(), bg="#4D2600", fg="white")
     checkout_button.pack(pady=20)

     cart_frame.update_idletasks()

    def open_login_page(self):
        """Open the login page for admin access."""
        self.clear_frame(self.main_menu_frame)

        login_label = tk.Label(self.main_menu_frame, text="LOGIN", font=("Times New Roman", 55, "bold"), fg="#4D2600", bg="#FFB6C1")
        login_label.pack(pady=30)

        email_label = tk.Label(self.main_menu_frame, text="Email", font=("Times New Roman", 14), fg="#4D2600", bg="#FFB6C1")
        email_label.pack(pady=5, anchor="center")

        email_entry = tk.Entry(self.main_menu_frame, font=("Times New Roman", 14), width=50, relief="solid")
        email_entry.pack(pady=10, anchor="center")

        password_label = tk.Label(self.main_menu_frame, text="Password", font=("Times New Roman", 14), fg="#4D2600", bg="#FFB6C1")
        password_label.pack(pady=5, anchor="center")

        password_entry = tk.Entry(self.main_menu_frame, font=("Times New Roman", 14), width=50, show="*", relief="solid")
        password_entry.pack(pady=10, anchor="center")

        def login_action():
            email = email_entry.get()
            password = password_entry.get()

            if email == self.admin_email and password == self.admin_password:
                self.logged_in = True
                self.show_shop_page()
                messagebox.showinfo("Login Successful", "You are logged in as an admin.")
            else:
                messagebox.showerror("Login Failed", "Invalid email or password.")

        login_button = tk.Button(self.main_menu_frame, text="Login", font=("Times New Roman", 14), fg="WHITE", bg="#4D2600", command=login_action, width=20)
        login_button.pack(pady=20, anchor="center")

    def clear_frame(self, frame):
        """Clear all widgets in the current frame."""
        for widget in frame.winfo_children():
            widget.destroy()

    def show_cakes(self):
        """Display cakes category."""
        products = [
             ("Chocolate Cake", 250, "images/chocolate_cake.jpg"),
             ("Vanilla Cake", 200, "images/vanilla_cake.jpg"),
             ("Red Velvet Cake", 300, "images/red_velvet_cake.jpg"),
        ]
        self.show_products("Cakes", products)

    def show_pastries(self):
        """Display pastries category."""
        products = [
            ("Croissant", 80, "images/croissant.jpg"),
            ("Danish Pastry", 90, "images/danish_pastry.jpg"),
            ("Eclair", 100, "images/eclair.jpg"),
        ]
        self.show_products("Pastries", products)

    def show_cupcakes(self):
        """Display cupcakes category."""
        products = [
            ("Chocolate Cupcake", 50, "images/chocolate_cupcake.jpg"),
            ("Vanilla Cupcake", 60, "images/vanilla_cupcake.jpg"),
            ("Stawberry Cupcake", 70, "images/strawberry_cupcake.jpg"),
        ]
        self.show_products("Cupcakes", products)

   
    def show_tarts(self):
        """Display tarts category."""
        products = [
            ("Lemon Tart", 120, "images/lemon_tart.jpg"),
            ("Fruit Tart", 150, "images/fruit_tart.jpg"),
            ("Chocolate Tart", 180, "images/chocolate_tart.jpg"),
        ]
        self.show_products("Tarts", products)

    def show_breads(self):
        """Display breads category."""
        products = [
            ("Sourdough", 40, "images/sourdough.jpg"),
            ("Baguette", 30, "images/baguette.jpg"),
            ("Ciabatta", 50, "images/ciabatta.jpg"),
        ]
        self.show_products("Breads", products)
    
    def checkout(self):
     """Simulate the checkout process, generate a PDF receipt, and show details in a new frame."""
     customer_name = simpledialog.askstring("Customer Name", "Enter your name:")
     if not customer_name:
        messagebox.showwarning("Invalid Input", "Please enter your name to complete the checkout.")
        return

     total_price = sum(item["price"] * item["quantity"] for item in self.cart)

     filename = f"receipt_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
     c = canvas.Canvas(filename, pagesize=letter)

     c.setFont("Helvetica", 12)

     width, height = letter

     title = f"Receipt - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
     title_width = c.stringWidth(title, "Helvetica", 12)
     c.drawString((width - title_width) / 2, height - 30, title)

     name_label = f"Customer: {customer_name}"
     name_width = c.stringWidth(name_label, "Helvetica", 12)
     c.drawString((width - name_width) / 2, height - 50, name_label)

     c.drawString(30, height - 70, "----------------------------------------")

     y_position = height - 90
     receipt_details = ""  
     for item in self.cart:
        product_name = item["product"]
        quantity = item["quantity"]
        price = item["price"]
        total_item_price = price * quantity
        c.drawString(30, y_position, f"{product_name} x {quantity} - PHP {total_item_price}")
        receipt_details += f"{product_name} x {quantity} - PHP {total_item_price}\n"
        y_position -= 20

     c.drawString(30, y_position, "----------------------------------------")
     c.drawString(30, y_position - 20, f"Total Price: PHP {total_price}")
     c.save()
    
     webbrowser.open(filename)
     self.show_receipt(receipt_details, total_price, customer_name)

     self.cart.clear()

    def show_receipt(self, receipt_details, total_price, customer_name):
        """Display the receipt details in a new frame."""
        receipt_frame = tk.Frame(self.main_menu_frame, bg="#FFB6C1")
        receipt_frame.pack(fill="both", expand=True)

        tk.Label(receipt_frame, text="Receipt", font=("Times New Roman", 30, "bold"), bg="#FFB6C1", fg="#4D2600").pack(pady=20)
        tk.Label(receipt_frame, text=f"Customer: {customer_name}", font=("Times New Roman", 16), bg="#FFB6C1").pack(pady=5)
        tk.Label(receipt_frame, text="----------------------------------------", font=("Times New Roman", 14), bg="#FFB6C1").pack(pady=5)
        
        receipt_text = tk.Text(receipt_frame, font=("Times New Roman", 14), bg="#FFB6C1", fg="#4D2600", height=10, width=50)
        receipt_text.insert(tk.END, receipt_details)
        receipt_text.config(state=tk.DISABLED)
        receipt_text.pack(pady=10)

        tk.Label(receipt_frame, text="----------------------------------------", font=("Times New Roman", 14), bg="#FFB6C1").pack(pady=5)
        tk.Label(receipt_frame, text=f"Total Price: PHP {total_price}", font=("Times New Roman", 16), bg="#FFB6C1").pack(pady=5)

def ask_customer_name(self):
        """Prompt the user to enter the customer name."""
        name = simpledialog.askstring("Customer Name", "Please enter your name:", parent=self.root)
        return name if name else "Anonymous"

if __name__ == "__main__":
    root = tk.Tk()
    app = PastryShopApp(root)
    root.mainloop()
