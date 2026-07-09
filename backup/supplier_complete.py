from tkinter import *
from tkinter import ttk, messagebox
from db import connect_db 

class supplier:

    def __init__(self, root):

        self.root = root
        self.root.title("Supper Market Billing System - Supplier Management")
        self.root.geometry("1350x700")
        self.root.configure(bg="#ecf0f1")
        self.root.resizable(False, False)

        self.supplier_id =""

        self.name = StringVar()
        self.company = StringVar()
        self.mobile = StringVar()
        self.email = StringVar()
        self.gst = StringVar()
        self.city = StringVar()
        self.state = StringVar()
        self.pincode = StringVar()