from tkinter import *
from tkinter import ttk, messagebox
from db import connect_db 

class Customer:

    def __init__(self, root):

        self.root = root
        self.root.title("Super Market Billing System - Customer Management")
        self.root.geometry("1350x700")
        self.root.configure(bg="#ecf0f1")
        self.root.resizable(False, False)

        self.customer_id = ""

        self.name = StringVar()
        self.mobile = StringVar()
        self.email = StringVar()
        self.city = StringVar()
        self.state = StringVar()
        self.pincode = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        title = Label(
            self.root,
            text="CUSTOMER MANAGEMENT",
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

        left.place(
            x=10,
            y=60,
            width=420,
            height=620
        )

        Label(
            left,
            text="Customer Details",
            bg="#3498db",
            fg="white",
            font=("Arial", 16, "bold"),
            pady=5
        ).pack(fill=X)

        form = Frame(
            left,
            bg="white"
        )

        form.pack(
            fill=BOTH,
            expand=True,
            padx=10,
            pady=15
        )

        Label(
            form,
            text="Customer Name",
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
            text="Mobile",
            bg="white",
            font=("Arial", 11, "bold")
        ).grid(row=1, column=0, pady=8, sticky=W)

        Entry(
            form,
            textvariable=self.mobile,
            font=("Arial", 11)
        ).grid(row=1, column=1, padx=10, pady=8)

        Label(
            form,
            text="Email",
            bg="white",
            font=("Arial", 11, "bold")
        ).grid(row=2, column=0, pady=8, sticky=W)

        Entry(
            form,
            textvariable=self.email,
            font=("Arial", 11)
        ).grid(row=2, column=1, padx=10, pady=8)

        Label(
            form,
            text="Address",
            bg="white",
            font=("Arial", 11, "bold")
        ).grid(row=3, column=0, sticky=NW, pady=8)

        self.txt_address = Text(
            form,
            width=25,
            height=4,
            font=("Arial", 11)
        )
        self.txt_address.grid(
            row=3,
            column=1,
            padx=10,
            pady=8
        )

        Label(
            form,
            text="City",
            bg="white",
            font=("Arial", 11, "bold")
        ).grid(row=4, column=0, pady=8, sticky=W)

        Entry(
            form,
            textvariable=self.city,
            font=("Arial", 11)
        ).grid(row=4, column=1, padx=10, pady=8)

        Label(
            form,
            text="State",
            bg="white",
            font=("Arial", 11, "bold")
        ).grid(row=5, column=0, pady=8, sticky=W)

        Entry(
            form,
            textvariable=self.state,
            font=("Arial", 11)
        ).grid(row=5, column=1, padx=10, pady=8)

        Label(
            form,
            text="Pincode",
            bg="white",
            font=("Arial", 11, "bold")
        ).grid(row=6, column=0, pady=8, sticky=W)

        Entry(
            form,
            textvariable=self.pincode,
            font=("Arial", 11)
        ).grid(row=6, column=1, padx=10, pady=8)

        btn_frame = Frame(left, bg="white")
        btn_frame.pack(fill=X, pady=10)

        Button(
            btn_frame,
            text="Save",
            bg="#27ae60",
            fg="white",
            font=("Arial", 11, "bold"),
            width=10,
            command=self.save_customer
        ).grid(row=0, column=0, padx=5)

        Button(
            btn_frame,
            text="Update",
            bg="#2980b9",
            fg="white",
            font=("Arial", 11, "bold"),
            width=10,
            command=self.update_customer
        ).grid(row=0, column=1, padx=5)

        Button(
            btn_frame,
            text="Delete",
            bg="#c0392b",
            fg="white",
            font=("Arial", 11, "bold"),
            width=10,
            command=self.delete_customer
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

        right.place(
            x=440,
            y=60,
            width=900,
            height=620
        )

        Label(
            right,
            text="Customer List",
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
        ).grid(row=0,column=0,padx=5)

        cmb_search = ttk.Combobox(
            search_frame,
            textvariable=self.search_by,
            values=("Mobile","Name","City"),
            state="readonly",
            width=15
        )

        cmb_search.grid(
            row=0,
            column=1,
            padx=5
        )

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
            command=self.search_customer 
        ).grid(row=0,column=3,padx=5)

        Button(
            search_frame,
            text="Show All",
            bg="#27ae60",
            fg="white",
            font=("Arial",10,"bold"),
            width=10, 
            command=self.fetch_data
        ).grid(row=0,column=4,padx=5)

        # ================= Table Frame =================

        table_frame = Frame(right, bd=3, relief=RIDGE)
        table_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.customer_table = ttk.Treeview(
            table_frame,
            columns=(
                "id",
                "name",
                "mobile",
                "email",
                "address",
                "city",
                "state",
                "pincode"
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.customer_table.xview)
        scroll_y.config(command=self.customer_table.yview)

        self.customer_table.heading("id", text="ID")
        self.customer_table.heading("name", text="Customer Name")
        self.customer_table.heading("mobile", text="Mobile")
        self.customer_table.heading("email", text="Email")
        self.customer_table.heading("address", text="Address")
        self.customer_table.heading("city", text="City")
        self.customer_table.heading("state", text="State")
        self.customer_table.heading("pincode", text="Pincode")

        self.customer_table.column("id", width=50)
        self.customer_table.column("name", width=150)
        self.customer_table.column("mobile", width=120)
        self.customer_table.column("email", width=180)
        self.customer_table.column("address", width=200)
        self.customer_table.column("city", width=100)
        self.customer_table.column("state", width=100)
        self.customer_table.column("pincode", width=100)

        self.customer_table["show"] = "headings"

        self.customer_table.pack(fill=BOTH, expand=True)

        self.customer_table.bind("<ButtonRelease-1>", self.get_data)

        self.fetch_data() 

    def save_customer(self):
        if self.name.get() == "" or self.mobile.get() == "":
            messagebox.showerror(
                "Error",
                "Customer Name and Mobile are required."
            )
            return 
        con = connect_db()

        if con is None:
            return

        cur = con.cursor()
        sql = """
        INSERT INTO customers
        (
            customer_name,
            mobile,
            email,
            address,
            city,
            state,
            pincode
       )
       VALUES
       (%s,%s,%s,%s,%s,%s,%s)
       """

        address = self.txt_address.get("1.0", END).strip()

        values = (
            self.name.get(),
            self.mobile.get(),
            self.email.get(),
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
                "Customer Saved Successfully."
            )
            self.fetch_data() 

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
            cur.execute("SELECT * FROM customers")

            rows = cur.fetchall()

            if len(rows) != 0:
                self.customer_table.delete(*self.customer_table.get_children())

                for row in rows:
                    self.customer_table.insert(
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
        selected = self.customer_table.focus()

        content = self.customer_table.item(selected)

        row = content["values"]

        if row:
            self.customer_id = row[0]
            self.name.set(row[1])
            self.mobile.set(row[2])
            self.email.set(row[3])

            self.txt_address.delete("1.0", END)
            self.txt_address.insert(END, row[4])

            self.city.set(row[5])
            self.state.set(row[6])
            self.pincode.set(row[7])

    def update_customer(self):

        if self.customer_id == "":

            messagebox.showerror(
                "Error",
                "Please select a customer first."
            )
            return

        con = connect_db()

        if con is None:
            return

        cur = con.cursor()

        try:

            sql = """
            UPDATE customers
            SET
                customer_name=%s,
                mobile=%s,
                email=%s,
                address=%s,
                city=%s,
                state=%s,
                pincode=%s
            WHERE id=%s
            """

            address = self.txt_address.get("1.0", END).strip()

            values = (

                self.name.get(),
                self.mobile.get(),
                self.email.get(),
                address,
                self.city.get(),
                self.state.get(),
                self.pincode.get(),
                self.customer_id

            )

            cur.execute(sql, values)

            con.commit()

            messagebox.showinfo(
                "Success",
                "Customer Updated Successfully."
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

    def delete_customer(self):
        if self.customer_id == "":
            messagebox.showerror(
                "Error",
                "Please select a customer first."
            )
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Do you really want to delete this customer?"
        )

        if not confirm:
            return

        con = connect_db()

        if con is None:
            return

        cur = con.cursor()

        try:
            cur.execute(
                "DELETE FROM customers WHERE id=%s",
                (self.customer_id,)
            )

            con.commit()

            messagebox.showinfo(
                "Success",
                "Customer Deleted Successfully."
            )

            self.fetch_data()
            self.clear() 
            
            try:
                self.clear()
            except Exception:
                pass

        except Exception as e:
            messagebox.showerror(
                "Database Error",
                str(e)
            )

        finally:
            con.close()

    def clear(self):
        self.customer_id = ""
        self.name.set("")
        self.mobile.set("")
        self.email.set("")
        self.city.set("")
        self.state.set("")
        self.pincode.set("")
        self.txt_address.delete("1.0", END)
        self.customer_table.selection_remove(
            self.customer_table.selection()
        )
        self.search_txt.set("")

    def search_customer(self): 
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
            column = {
                "Mobile": "mobile",
                "Name": "customer_name",
                "City": "city"
            }[self.search_by.get()]

            sql = f"SELECT * FROM customers WHERE {column} LIKE %s"

            cur.execute(
                sql,
                ('%' + self.search_txt.get() + '%',)
            )

            rows = cur.fetchall()

            self.customer_table.delete(
                *self.customer_table.get_children()
            )

            for row in rows:
                self.customer_table.insert(
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


if __name__ == "__main__":

    root = Tk()
    obj = Customer(root)
    root.mainloop()

        