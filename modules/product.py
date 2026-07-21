from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk 
from db import connect_db 
from tkcalendar import DateEntry  

import os
import shutil 


class Product:

    def __init__(self, root):

        self.root = root
        self.root.title("Super Market Billing System - Product Management")
        self.root.geometry("1350x700")
        self.root.configure(bg="#ecf0f1")
        self.root.resizable(False, False)

        

        self.product_id = ""

        self.barcode = StringVar()
        self.name = StringVar()
        self.category = StringVar()
        self.brand = StringVar()
        self.purchase = StringVar()
        self.selling = StringVar()
        self.gst = StringVar()
        self.qty = StringVar()
        self.expiry = StringVar()
        self.status = StringVar(value="Available")
        self.image_path = StringVar() 

        

        title = Label(
            self.root,
            text="PRODUCT MANAGEMENT",
            font=("Arial", 22, "bold"),
            bg="#2c3e50",
            fg="white",
            pady=10
        )

        title.pack(fill=X)

        

        left = Frame(
            self.root,
            bg="white",
            bd=2,
            relief=RIDGE
        )

        left.place(x=10, y=60, width=420, height=620)

        Label(
            left,
            text="Product Details",
            bg="#3498db",
            fg="white",
            font=("Arial", 16, "bold"),
            pady=5
        ).pack(fill=X)

        form = Frame(left, bg="white")
        form.pack(fill=BOTH, expand=True, padx=10, pady=15)

        

        Label(form, text="Barcode", bg="white",
              font=("Arial", 11, "bold")).grid(row=0, column=0, sticky=W, pady=8)

        Entry(form, textvariable=self.barcode,
              font=("Arial", 11)).grid(row=0, column=1, pady=8, padx=10)

        Label(form, text="Product Name", bg="white",
              font=("Arial", 11, "bold")).grid(row=1, column=0, sticky=W, pady=8)

        Entry(form, textvariable=self.name,
              font=("Arial", 11)).grid(row=1, column=1, pady=8, padx=10)

        Label(form, text="Category", bg="white",
              font=("Arial", 11, "bold")).grid(row=2, column=0, sticky=W, pady=8)

        Entry(form, textvariable=self.category,
              font=("Arial", 11)).grid(row=2, column=1, pady=8, padx=10)

        Label(form, text="Brand", bg="white",
              font=("Arial", 11, "bold")).grid(row=3, column=0, sticky=W, pady=8)

        Entry(form, textvariable=self.brand,
              font=("Arial", 11)).grid(row=3, column=1, pady=8, padx=10)

        Label(form, text="Purchase Price", bg="white",
              font=("Arial", 11, "bold")).grid(row=4, column=0, sticky=W, pady=8)

        Entry(form, textvariable=self.purchase,
              font=("Arial", 11)).grid(row=4, column=1, pady=8, padx=10)

        Label(form, text="Selling Price", bg="white",
              font=("Arial", 11, "bold")).grid(row=5, column=0, sticky=W, pady=8)

        Entry(form, textvariable=self.selling,
              font=("Arial", 11)).grid(row=5, column=1, pady=8, padx=10)

        Label(form, text="GST %", bg="white",
              font=("Arial", 11, "bold")).grid(row=6, column=0, sticky=W, pady=8)

        Entry(form, textvariable=self.gst,
              font=("Arial", 11)).grid(row=6, column=1, pady=8, padx=10)

        Label(form, text="Quantity", bg="white",
              font=("Arial", 11, "bold")).grid(row=7, column=0, sticky=W, pady=8)

        Entry(form, textvariable=self.qty,
              font=("Arial", 11)).grid(row=7, column=1, pady=8, padx=10)

        Label(form, text="Expiry Date", bg="white",
              font=("Arial", 11, "bold")).grid(row=8, column=0, sticky=W, pady=8)

        Label(form, text="Status", bg="white",
              font=("Arial", 11, "bold")).grid(row=9, column=0, sticky=W, pady=8)

        self.cmb_status = ttk.Combobox(
            form,
            textvariable=self.status,
            values=("Available", "Out of Stock"),
            state="readonly",
            width=22
        )

        self.cmb_status.grid(row=9, column=1, pady=8, padx=10)
        self.cmb_status.current(0)

        

        Label(form, text="Product Image", bg="white",
              font=("Arial", 11, "bold")).grid(row=10, column=0, pady=8, sticky=W)
        
        self.expiry_entry = DateEntry(
            form,
            textvariable=self.expiry,
            width=20,
            date_pattern="yyyy-mm-dd", 
            font=("Arial",11)
        )

        self.expiry_entry.grid(
            row=8,
            column=1,
            padx=10,
            pady=8
        )

        Button(
            form,
            text="Browse",
            command=self.browse_image,
            bg="#8e44ad",
            fg="white",
            font=("Arial", 10, "bold")
        ).grid(row=10, column=2, padx=5)

        

        self.img_label = Label(
            form,
            text="No Image",
            bg="white",
            bd=2,
            relief=RIDGE,
            width=30,
            height=12 
        )

        self.img_label.grid(
            row=11,
            column=1,
            pady=10
        )

        

        btn_frame = Frame(left, bg="white")
        btn_frame.pack(fill=X, pady=10)

        Button(
            btn_frame,
            text="Save",
            bg="#27ae60",
            fg="white",
            font=("Arial", 11, "bold"),
            width=10,
            command=self.save_product
        ).grid(row=0, column=0, padx=5)

        Button(
            btn_frame,
            text="Update",
            bg="#2980b9",
            fg="white",
            font=("Arial", 11, "bold"),
            width=10, 
            command=self.update_product 
        ).grid(row=0, column=1, padx=5)

        Button(
            btn_frame,
            text="Delete",
            bg="#c0392b",
            fg="white",
            font=("Arial", 11, "bold"),
            width=10, 
            command=self.delete_product
        ).grid(row=0, column=2, padx=5)

        Button(
            btn_frame,
            text="Clear",
            bg="#7f8c8d",
            fg="white",
            font=("Arial", 11, "bold"),
            width=10,
            command=self.clear
        ).grid(row=0, column=3, padx=5)

        

        right = Frame(
            self.root,
            bg="white",
            bd=2,
            relief=RIDGE
        )

        right.place(x=440, y=60, width=900, height=620)

        Label(
            right,
            text="Product List",
            bg="#34495e",
            fg="white",
            font=("Arial", 16, "bold"),
            pady=5
        ).pack(fill=X)

        search_frame = Frame(right, bg="white")
        search_frame.pack(fill=X, padx=10, pady=10)

        Label(
            search_frame,
            text="Search By",
            bg="white",
            font=("Arial",11,"bold")
         ).grid(row=0, column=0, padx=5)

        self.search_by = StringVar()

        cmb_search = ttk.Combobox(
            search_frame,
            textvariable=self.search_by,
            values=("Barcode","Product Name","Category"),
            state="readonly",
            width=18
        )

        cmb_search.current(0)
        cmb_search.grid(row=0, column=1, padx=5)

        self.search_txt = StringVar()

        search_entry = Entry(
            search_frame,
            textvariable=self.search_txt,
            font=("Arial",11),
            width=25
        )

        search_entry.grid(row=0, column=2, padx=5)

        search_entry.bind("<KeyRelease>", self.live_search)

        Button(
            search_frame,
            text="Search",
            bg="#2980b9",
            fg="white",
            font=("Arial",10,"bold"),
            command=self.search_product
        ).grid(row=0,column=3,padx=5)

        Button(
            search_frame,
            text="Show All",
            bg="#27ae60",
            fg="white",
            font=("Arial",10,"bold"),
            command=self.fetch_data
        ).grid(row=0,column=4,padx=5)

        table_frame = Frame(right)
        table_frame.pack(fill=BOTH, expand=True)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.product_table = ttk.Treeview(
            table_frame,
            columns=(
                "id",
                "barcode",
                "name",
                "category",
                "brand",
                "purchase",
                "selling",
                "gst",
                "qty",
                "expiry",
                "status",
                "image"
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.product_table.xview)
        scroll_y.config(command=self.product_table.yview)

    

        self.product_table.heading("id", text="ID")
        self.product_table.heading("barcode", text="Barcode")
        self.product_table.heading("name", text="Product Name")
        self.product_table.heading("category", text="Category")
        self.product_table.heading("brand", text="Brand")
        self.product_table.heading("purchase", text="Purchase")
        self.product_table.heading("selling", text="Selling")
        self.product_table.heading("gst", text="GST")
        self.product_table.heading("qty", text="Quantity")
        self.product_table.heading("expiry", text="Expiry")
        self.product_table.heading("status", text="Status")
        self.product_table.heading("image", text="Image")

        self.product_table["show"] = "headings"

        self.product_table.column("id", width=50)
        self.product_table.column("barcode", width=100)
        self.product_table.column("name", width=150)
        self.product_table.column("category", width=120)
        self.product_table.column("brand", width=120)
        self.product_table.column("purchase", width=100)
        self.product_table.column("selling", width=100)
        self.product_table.column("gst", width=80)
        self.product_table.column("qty", width=80)
        self.product_table.column("expiry", width=120)
        self.product_table.column("status", width=120)
        self.product_table.column("image", width=0, stretch=False) 

        self.product_table.pack(fill=BOTH, expand=True)

        self.fetch_data()

        self.product_table.bind("<ButtonRelease-1>", self.get_data)


    def browse_image(self):

        filename = filedialog.askopenfilename(
            title="Select Product Image",
            filetypes=(
                ("Image Files", "*.jpg *.jpeg *.png"),
                ("All Files", "*.*")
            )
        )

        if filename:

            self.selected_image = filename

            self.image_path.set(os.path.basename(filename))

            img = Image.open(filename)
            img.thumbnail((120,120))

            self.photo = ImageTk.PhotoImage(img)

            self.img_label.config(image=self.photo, text="")

    def clear(self):
        """Clear product form fields and reset image."""
        self.product_id = ""

        self.barcode.set("")
        self.name.set("")
        self.category.set("")
        self.brand.set("")
        self.purchase.set("")
        self.selling.set("")
        self.gst.set("")
        self.qty.set("")
        self.expiry.set("")
        self.status.set("Available")

        self.image_path.set("")

        if hasattr(self, "img_label"):
            self.img_label.config(image="", text="No Image")

        if hasattr(self, "selected_image"):
            del self.selected_image


    def save_product(self):

        
        if (
            self.barcode.get() == "" or
            self.name.get() == "" or
            self.purchase.get() == "" or
            self.selling.get() == "" or
            self.qty.get() == ""
        ):
            messagebox.showerror(
                "Error",
                "Please fill all required fields."
            )
            return
        
        
        try:
            float(self.purchase.get())
            float(self.selling.get())
            float(self.gst.get())
            int(self.qty.get())

        except ValueError:
            messagebox.showerror(
                "Error",
                "Purchase Price, Selling Price, GST and Quantity must be numeric."
            )
            return

        print("Save button clicked")

        if self.barcode.get() == "" or self.name.get() == "":
            messagebox.showerror(
                "Error",
                "Barcode and Product Name are required."
            )
            return

        con = connect_db()

        if con is None:
            return

        cur = con.cursor()

        
        cur.execute(
            "SELECT * FROM products WHERE barcode=%s",
            (self.barcode.get(),)
        )

        row = cur.fetchone()

        if row:
            messagebox.showerror(
                "Error",
                "Barcode already exists."
            )

            con.close()
            return
        

        
        image_db_path = "images/no_image.png"

        if hasattr(self, "selected_image"):
            destination_folder = "images/products"
            os.makedirs(destination_folder, exist_ok=True)
            filename = os.path.basename(self.selected_image)
            destination = os.path.join(destination_folder, filename)
            shutil.copy2(self.selected_image, destination)
            image_db_path = destination.replace("\\", "/")

        try:

            sql = """
            INSERT INTO products
            (
                barcode,
                product_name,
                category,
                brand,
                purchase_price,
                selling_price,
                gst,
                quantity,
                expiry_date,
                status,
                image
            )

            VALUES
            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
            """

            values = (

                self.barcode.get(),
                self.name.get(),
                self.category.get(),
                self.brand.get(),
                self.purchase.get(),
                self.selling.get(),
                self.gst.get(),
                self.qty.get(),
                self.expiry.get(),
                self.status.get(), 
                image_db_path 

            )

            print("Image Path:", image_db_path)
            print(values)

            cur.execute(sql, values)

            con.commit()

            messagebox.showinfo(
                "Success",
                "Product Saved Successfully."
            )

            self.fetch_data() 

            self.clear()

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

        finally:

            con.close()

    def fetch_data(self):

        con = connect_db()

        if con is None:
         return

        cur = con.cursor()

        try:

           cur.execute("SELECT * FROM products")

           rows = cur.fetchall()

           self.product_table.delete(*self.product_table.get_children())

           if len(rows) != 0:

               for row in rows:

                   self.product_table.insert("",END,values=row)

           con.commit()

        except Exception as e:

           messagebox.showerror(
            "Database Error",
            str(e)
        )

        finally:

         con.close()

    def get_data(self, ev):

       selected = self.product_table.focus()

       content = self.product_table.item(selected)

       row = content["values"]

       if row:

        self.product_id = row[0]

        self.barcode.set(row[1])
        self.name.set(row[2])
        self.category.set(row[3])
        self.brand.set(row[4])
        self.purchase.set(row[5])
        self.selling.set(row[6])
        self.gst.set(row[7])
        self.qty.set(row[8])
        self.expiry.set(row[9])
        self.status.set(row[10])

        

        image_path = row[11]
        self.image_path.set(image_path)

        try:
            if image_path and os.path.exists(image_path):
                img = Image.open(image_path)
            else:
                img = Image.open("images/no_image.png")
        except Exception:
            img = Image.open("images/no_image.png")

        img = img.resize((220, 220)) 
        self.photo = ImageTk.PhotoImage(img)
        self.img_label.config(image=self.photo, text="")


    def update_product(self):

        if self.product_id == "":
            messagebox.showerror(
                "Error",
                "Please select a product first."
            )
            return

        con = connect_db()

        if con is None:
            return

        cur = con.cursor()

        try:

            sql = """
            UPDATE products
            SET
                barcode=%s,
                product_name=%s,
                category=%s,
                brand=%s,
                purchase_price=%s,
                selling_price=%s,
                gst=%s,
                quantity=%s,
                expiry_date=%s,
                status=%s,
                image=%s
            WHERE id=%s
            """

            values = (
                self.barcode.get(),
                self.name.get(),
                self.category.get(),
                self.brand.get(),
                self.purchase.get(),
                self.selling.get(),
                self.gst.get(),
                self.qty.get(),
                self.expiry.get(),
                self.status.get(),
                self.image_path.get(),
                self.product_id 
            )

            cur.execute(sql, values)

            con.commit()

            messagebox.showinfo(
                "Success",
                "Product Updated Successfully."
            )

            self.fetch_data()
            self.clear()

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

        finally:

            con.close()


    def delete_product(self):

        if self.product_id == "":
            messagebox.showerror(
               "Error",
               "Please select a product first."
           )
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Do you want to delete this product?"
        )

        if not confirm:
            return

        con = connect_db()

        if con is None:
            return

        cur = con.cursor()

        try:

            cur.execute(
                "DELETE FROM products WHERE id=%s",
                (self.product_id,)
            )

            con.commit()

            messagebox.showinfo(
                "Success",
                "Product Deleted Successfully."
            )

            self.fetch_data()
            self.clear()

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

        finally:

            con.close()


    def search_product(self):
        if self.search_txt.get() == "":
            messagebox.showerror(
                "Error",
                "Please enter a value to search."
            )
            return

        con = connect_db()

        if con is None:
            return

        cur = con.cursor()

        try:

            column = ""

            if self.search_by.get() == "Barcode":
                column = "barcode"

            elif self.search_by.get() == "Product Name":
                column = "product_name"

            elif self.search_by.get() == "Category":
                column = "category"

            sql = f"SELECT * FROM products WHERE {column} LIKE %s"

            cur.execute(sql, ('%' + self.search_txt.get() + '%',))

            rows = cur.fetchall()

            self.product_table.delete(*self.product_table.get_children())

            for row in rows:
                self.product_table.insert("", END, values=row)

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

        finally:

            con.close()


    def live_search(self, event):

        if self.search_txt.get() == "":

            self.fetch_data()

            return

        self.search_product()


if __name__ == "__main__":

    root = Tk()

    Product(root)

    root.mainloop() 