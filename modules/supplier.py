from tkinter import *
from tkinter import ttk, messagebox
from db import connect_db 

class Supplier:

    def __init__(self, root):

        self.root = root
        self.root.title("Super Market Billing System - Supplier Management")
        self.root.geometry("1350x700")
        self.root.configure(bg="#ecf0f1")
        self.root.resizable(False, False)

        self.supplier_id =""

        self.name = StringVar()
        self.company = StringVar()
        self.mobile = StringVar()
        self.email = StringVar()
        self.gst_no = StringVar() 
        self.city = StringVar()
        self.state = StringVar()
        self.pincode = StringVar() 
        

        self.search_by = StringVar()
        self.search_txt = StringVar() 

        self.title = Label(
            self.root,
            text="SUPPLIER MANAGEMENT",
            font=("Arial",24,"bold"),
            bg="#2c3e50",
            fg="white",
            pady=10
        )

        self.title.pack(fill=X) 

        left = Frame(
            self.root, 
            bg="white",
            bd=2,
            relief=RIDGE
        )
        
        left.place(
            x=10,
            y=60,
            width=420,
            height=620
        )

        Label(
            left,
            text="Supplier Details",
            font=("Arial",16,"bold"),
            bg="#3498db",
            fg="white",
            pady=5
        ).pack(fill=X)

        form = Frame(
            left,
            bg="White"
        )

        form.pack(
            fill=BOTH,
            expand=True,
            padx=10,
            pady=15 
        )

        Label(
            form,
            text="Supplier name",
            bg="white",
            font=("Arial", 11, "bold")
        ).grid(row=0, column=0, pady=8, sticky=W)

        Entry(
            form,
            textvariable=self.name,
            font=("Arial", 11)
        ).grid(row=0, column=1, padx=10, pady=8)

        Label(
            form,
            text="Company",
            bg="white",
            font=("Arial", 11, "bold")
        ).grid(row=1, column=0, pady=8, sticky=W)

        Entry(
            form,
            textvariable=self.company,
            font=("Arial", 11)
        ).grid(row=1, column=1, padx=10, pady=8)

        Label(
            form,
            text="Mobile",
            bg="white",
            font=("Arial",11,"bold")
        ).grid(row=2, column=0, pady=8, sticky=W)

        Entry(
            form,
            textvariable=self.mobile,
            font=("Arial",11)
        ).grid(row=2, column=1, padx=10, pady=8)

        Label(
            form,
            text="Email",
            bg="white",
            font=("Arial",11,"bold")
        ).grid(row=3, column=0, pady=8, sticky=W)

        Entry(
            form,
            textvariable=self.email,
            font=("Arial",11)
        ).grid(row=3, column=1, padx=10, pady=8)

        Label(
            form,
            text="GST Number",
            bg="white",
            font=("Arial",11,"bold")
        ).grid(row=4, column=0, pady=8, sticky=W)

        Entry(
            form,
            textvariable=self.gst_no,
            font=("Arial",11)
        ).grid(row=4, column=1, padx=10, pady=8)

        Label(
            form,
            text="Address",
            bg="white",
            font=("Arial",11,"bold")
        ).grid(row=5, column=0, sticky=W, pady=8)

        self.txt_address = Text(
            form,
            width=25,
            height=4,
            font=("Arial", 11)
        )

        self.txt_address.grid(
            row=5,
            column=1,
            padx=10,
            pady=8
        )

        Label(
            form,
            text="City",
            bg="white",
            font=("Arial",11,"bold")
        ).grid(row=6, column=0, sticky=W, pady=8)

        Entry(
            form,
            textvariable=self.city,
            font=("Arial",11)
        ).grid(row=6, column=1, padx=10, pady=8)

        Label(
            form,
            text="State",
            bg="white",
            font=("Arial",11,"bold")
        ).grid(row=7, column=0, sticky=W, pady=8)

        Entry(
            form,
            textvariable=self.state,
            font=("Arial",11)
        ).grid(row=7, column=1, padx=10, pady=8)

        Label(
            form,
            text="Pincode",
            bg="white",
            font=("Arial",11,"bold")
        ).grid(row=8, column=0, sticky=W, pady=8)

        Entry(
            form,
            textvariable=self.pincode,
            font=("Arial",11)
        ).grid(row=8, column=1, padx=10, pady=8)


        

        btn_frame = Frame(
            left,
            bg="white"
        )

        btn_frame.pack(
            fill=X,
            pady=10
        )

        Button(
            btn_frame,
            text="Save",
            bg="#27ae60",
            fg="white",
            font=("Arial",11,"bold"),
            width=10,
            command=self.save_supplier
        ).grid(row=0, column=0, padx=5)

        Button(
            btn_frame,
            text="Update",
            bg="#2980b9",
            fg="white",
            font=("Arial",11,"bold"),
            width=10,
            command=self.update_supplier
        ).grid(row=0, column=1, padx=5)


        Button(
            btn_frame,
            text="Delete",
            bg="#c0392b",
            fg="white",
            font=("Arial",11,"bold"),
            width=10,
            command=self.delete_supplier
        ).grid(row=0, column=2, padx=5)

        Button(
            btn_frame,
            text="Clear",
            bg="#7f8c8d",
            fg="white",
            font=("Arial",11,"bold"),
            width=10,
            command=self.clear
        ).grid(row=0, column=3, padx=5)

    def save_supplier(self):
        pass

    def update_supplier(self):
        pass

    def delete_supplier(self):
        pass

    def clear(self):
        pass


if __name__ == "__main__":

    root = Tk()
    obj = Supplier(root) 
    root.mainloop()
