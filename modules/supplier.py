from tkinter import *
from tkinter import ttk, messagebox
from db import connect_db 

class Supplier:

    def __init__(self, root):

        self.root = root
        self.root.title("Super Market Billing System - Supplier Management")
        self.root.geometry("1350x700") 
        self.root.configure(bg="#ecf0f1")
        self.root.resizable(True, True)

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

        self.name_entry = Entry(
            form,
            textvariable=self.name,
            font=("Arial", 11)
        )

        self.name_entry.grid(
            row=0,
            column=1,
            padx=10,
            pady=8
        )

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



        right = Frame(
            self.root,
            bg="white",
            bd=2,
            relief=RIDGE
        )

        right.place(
            x=440,
            y=60,
            width=900,
            height=620
        )

        Label(
            right,
            text="Supplier List",
            bg="#34495e",
            fg="white",
            font=("Arial",16,"bold"),
            pady=5
        ).pack(fill=X)

        search_frame = Frame(
            right,
            bg="white"
        )

        search_frame.pack(
            fill=X,
            padx=10,
            pady=10
        )

        Label(
            search_frame,
            text="Search By",
            bg="white",
            font=("Arial",11,"bold")
        ).grid(row=0, column=0, padx=5)

        cmb_search = ttk.Combobox(
            search_frame,
            textvariable=self.search_by,
            values=("Supplier Name", "Company", "Mobile"),
            state="readonly",
            width=15
        )

        cmb_search.grid(row=0, column=1, padx=5)
        cmb_search.current(0)

        Entry(
            search_frame,
            textvariable=self.search_txt,
            font=("Arial",11),
            width=25
        ).grid(
            row=0,
            column=2,
            padx=5
        )

        Button(
            search_frame,
            text="Search",
            bg="#2980b9",
            fg="white",
            font=("Arial",10,"bold"),
            width=10,
            command=self.search_supplier
        ).grid(row=0, column=3, padx=5)

        Button(
            search_frame,
            text="Show All",
            bg="#27ae60",
            fg="white",
            font=("Arial",10,"bold"),
            width=10,
            command=self.show_all
        ).grid(row=0, column=4, padx=5)

       
        table_frame = Frame(
            right,
            bd=3,
            relief=RIDGE
        )

        table_frame.pack(
            fill=BOTH,
            expand=True,
            padx=10,
            pady=10
        )

        scroll_x = Scrollbar(
            table_frame,
            orient=HORIZONTAL
        )

        scroll_y = Scrollbar(
            table_frame,
            orient=VERTICAL
        )

        self.supplier_table = ttk.Treeview(
            table_frame,
            columns=(
                "id",
                "name",
                "company",
                "mobile",
                "email",
                "gst",
                "address",
                "city",
                "state",
                "pincode"
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(
            side=BOTTOM,
            fill=X
        )

        scroll_y.pack(
            side=RIGHT,
            fill=Y
        )

        scroll_x.config(
            command=self.supplier_table.xview
        )

        scroll_y.config(
            command=self.supplier_table.yview
        )

        self.supplier_table.heading("id", text="ID")
        self.supplier_table.heading("name", text="Supplier Name")
        self.supplier_table.heading("company", text="Company")
        self.supplier_table.heading("mobile", text="Mobile")
        self.supplier_table.heading("email", text="Email")
        self.supplier_table.heading("gst", text="GST Number")
        self.supplier_table.heading("address", text="Address")
        self.supplier_table.heading("city", text="City")
        self.supplier_table.heading("state", text="State")
        self.supplier_table.heading("pincode", text="Pincode")

        self.supplier_table.column("id", width=50)
        self.supplier_table.column("name", width=150)
        self.supplier_table.column("company", width=150)
        self.supplier_table.column("mobile", width=120)
        self.supplier_table.column("email", width=180)
        self.supplier_table.column("gst", width=180)
        self.supplier_table.column("address", width=220)
        self.supplier_table.column("city", width=100)
        self.supplier_table.column("state", width=100)
        self.supplier_table.column("pincode", width=100)

        self.supplier_table["show"] = "headings"

        self.supplier_table.pack(
            fill=BOTH,
            expand=True
        )

        self.supplier_table.bind("<ButtonRelease-1>", self.get_data) 
        self.fetch_data() 

    def save_supplier(self): 
        if self.name.get() == "" or self.mobile.get() == "":
            messagebox.showerror(
                "Error",
                "Supplier Name and Mobile are required."
            )
            return

        con = connect_db()
        if con is None:
            return

        cur = con.cursor()
        address = self.txt_address.get("1.0", END).strip()

        sql = """
        INSERT INTO suppliers
        (
            supplier_name,
            company_name,
            mobile,
            email,
            gst_no,
            address,
            city,
            state,
            pincode
        )
        VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            self.name.get(),
            self.company.get(),
            self.mobile.get(),
            self.email.get(),
            self.gst_no.get(),
            address,
            self.city.get(),
            self.state.get(),
            self.pincode.get()
        )

        try:
            cur.execute(sql, values)
            con.commit()
            messagebox.showinfo(
                "Success",
                "Supplier Saved Successfully."
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
            cur.execute("SELECT * FROM suppliers")

            rows = cur.fetchall()

            if len(rows) != 0:

                self.supplier_table.delete(
                    *self.supplier_table.get_children()
                )

                for row in rows:
                    self.supplier_table.insert(
                        "",
                        END,
                        values=row
                    )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

        finally:

            con.close()

    def get_data(self, ev):

       selected = self.supplier_table.focus()

       content = self.supplier_table.item(selected)

       row = content["values"]

       print(row) 

       if row:
        self.supplier_id = row[0]

        self.name.set(row[1])

        self.company.set(row[2])

        self.mobile.set(row[3])

        self.email.set(row[4])

        self.gst_no.set(row[5])

        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[6])

        self.city.set(row[7])

        self.state.set(row[8])

        self.pincode.set(row[9])
    
    def update_supplier(self):
        if self.supplier_id == "": 
            messagebox.showerror(
                "Error",
                "Please select a supplier first."
            )
            return

        con = connect_db()
        if con is None:
            return

        cur = con.cursor()
        address = self.txt_address.get("1.0", END).strip()

        sql = """
        UPDATE suppliers SET
            supplier_name=%s,
            company_name=%s,
            mobile=%s,
            email=%s,
            gst_no=%s,
            address=%s,
            city=%s,
            state=%s,
            pincode=%s
        WHERE id=%s
        """

        values = (
            self.name.get(),
            self.company.get(),
            self.mobile.get(),
            self.email.get(),
            self.gst_no.get(),
            address,
            self.city.get(),
            self.state.get(),
            self.pincode.get(),
            self.supplier_id
        )

        try:
            cur.execute(sql, values)
            con.commit()
            messagebox.showinfo("Success", "Supplier Updated Successfully.")
            self.fetch_data()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            con.close()

    def delete_supplier(self):
        if self.supplier_id == "":
            messagebox.showerror(
                "Error",
                "Please select a supplier first."
            )
            return
        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Do you really want to delete this supplier?"
        )

        if not confirm:
            return

        con = connect_db()
        if con is None:
            return

        cur = con.cursor()

        try:
            cur.execute("DELETE FROM suppliers WHERE id=%s", (self.supplier_id,))
            con.commit()
            messagebox.showinfo("Success", "Supplier Deleted Successfully.")
            self.fetch_data()
            self.clear()
            self.supplier_id = ""
        except Exception as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            con.close()

    def clear(self):
        self.supplier_id = ""

        self.name.set("")
        self.company.set("")
        self.mobile.set("")
        self.email.set("")
        self.gst_no.set("")

        self.city.set("")
        self.state.set("")
        self.pincode.set("")

        self.txt_address.delete("1.0", END)

        self.fetch_data()

        self.supplier_table.selection_remove(
            self.supplier_table.selection()
        )

        self.name_entry.focus()


    def search_supplier(self):
        if self.search_by.get() == "":
            messagebox.showerror(
                "Error",
                "Please select Search By."
            )
            return

        if self.search_txt.get().strip() == "":
            messagebox.showerror(
                "Error",
                "Please enter something to search."
            )
            return

        con = connect_db()
        if con is None:
            return

        cur = con.cursor()

        field_map = {
            "Supplier Name": "supplier_name",
            "Company": "company_name",
            "Mobile": "mobile"
        }

        column = field_map.get(self.search_by.get())

        try:
            sql = f"SELECT * FROM suppliers WHERE {column} LIKE %s"
            value = f"%{self.search_txt.get().strip()}%"
            cur.execute(sql, (value,))

            rows = cur.fetchall()

            self.supplier_table.delete(
                *self.supplier_table.get_children()
            )

            if len(rows) == 0:
                messagebox.showinfo(
                    "No Record",
                    "No supplier found."
                )
                return 

            for row in rows:
                self.supplier_table.insert("", END, values=row)
        except Exception as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            con.close()

    def show_all(self):
        self.search_txt.set("")
        self.fetch_data()
if __name__ == "__main__":
    root = Tk()
    app = Supplier(root)
    root.mainloop() 


