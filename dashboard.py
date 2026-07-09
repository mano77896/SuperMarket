from tkinter import *
from tkinter import ttk
from datetime import datetime

class Dashboard:

    def __init__(self, root):

        self.root = root
        self.root.title("Super Market Billing System")
        self.root.geometry("1350x700")
        self.root.state("zoomed")
        self.root.configure(bg="#ecf0f1")

        # ================= HEADER =================
        title = Label(
            self.root,
            text="SUPER MARKET BILLING SYSTEM",
            bg="#2c3e50",
            fg="white",
            font=("Arial", 24, "bold"),
            pady=12
        )
        title.pack(fill=X)

        # ================= DATE & TIME =================
        self.time_lbl = Label(
            self.root,
            font=("Arial", 12, "bold"),
            bg="#34495e",
            fg="white",
            pady=5
        )
        self.time_lbl.pack(fill=X)

        self.update_time()

        # ================= SIDEBAR =================
        sidebar = Frame(self.root, bg="#34495e", width=220)
        sidebar.pack(side=LEFT, fill=Y)

        Label(
            sidebar,
            text="MENU",
            bg="#34495e",
            fg="white",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

        self.menu_button(sidebar, "🏠 Dashboard")
        self.menu_button(sidebar, "📦 Products")
        self.menu_button(sidebar, "👥 Customers")
        self.menu_button(sidebar, "🚚 Suppliers")
        self.menu_button(sidebar, "🛒 Billing")
        self.menu_button(sidebar, "📊 Reports")
        self.menu_button(sidebar, "⚙ Settings")
        self.menu_button(sidebar, "🚪 Logout")

        # ================= CONTENT =================
        self.content = Frame(self.root, bg="#ecf0f1")
        self.content.pack(side=LEFT, fill=BOTH, expand=True)

        Label(
            self.content,
            text="Dashboard",
            bg="#ecf0f1",
            fg="#2c3e50",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

        # ================= CARDS =================
        card_frame = Frame(self.content, bg="#ecf0f1")
        card_frame.pack(pady=20)

        self.create_card(card_frame, "Products", "0", "#3498db", 0, 0)
        self.create_card(card_frame, "Customers", "0", "#27ae60", 0, 1)
        self.create_card(card_frame, "Suppliers", "0", "#9b59b6", 1, 0)
        self.create_card(card_frame, "Today's Sales", "₹0", "#e67e22", 1, 1)

    # ================= MENU BUTTON =================

    def menu_button(self, parent, text):
        Button(
            parent,
            text=text,
            font=("Arial", 12, "bold"),
            bg="#2c3e50",
            fg="white",
            activebackground="#1abc9c",
            width=20,
            pady=10,
            relief=FLAT
        ).pack(pady=5)

    # ================= CARD =================

    def create_card(self, parent, title, value, color, row, col):

        card = Frame(
            parent,
            bg=color,
            width=260,
            height=150
        )

        card.grid(row=row, column=col, padx=30, pady=20)
        card.grid_propagate(False)

        Label(
            card,
            text=title,
            bg=color,
            fg="white",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

        Label(
            card,
            text=value,
            bg=color,
            fg="white",
            font=("Arial", 26, "bold")
        ).pack()

    # ================= CLOCK =================

    def update_time(self):

        now = datetime.now()

        current = now.strftime("%d-%m-%Y    %I:%M:%S %p")

        self.time_lbl.config(text=current)

        self.root.after(1000, self.update_time)


root = Tk()

Dashboard(root)

root.mainloop()