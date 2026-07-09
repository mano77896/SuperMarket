from tkinter import *
from tkinter import messagebox
from db import connect_db

class Login:

    def __init__(self, root):

        self.root = root
        self.root.title("Super Market Billing System")
        self.root.geometry("900x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#ECF0F1")

        title = Label(
            self.root,
            text="SUPER MARKET BILLING SYSTEM",
            bg="#2C3E50",
            fg="white",
            font=("Arial", 22, "bold"),
            pady=15
        )
        title.pack(fill=X)

        login_frame = Frame(
            self.root,
            bg="white",
            bd=3,
            relief=RIDGE
        )
        login_frame.place(x=250, y=90, width=400, height=330)

        Label(
            login_frame,
            text="ADMIN LOGIN",
            bg="white",
            fg="#2C3E50",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

        Label(
            login_frame,
            text="Username",
            bg="white",
            font=("Arial", 12)
        ).pack(anchor="w", padx=30)

        self.username = Entry(
            login_frame,
            font=("Arial", 12)
        )
        self.username.pack(fill=X, padx=30, pady=5)

        Label(
            login_frame,
            text="Password",
            bg="white",
            font=("Arial", 12)
        ).pack(anchor="w", padx=30)

        self.password = Entry(
            login_frame,
            show="*",
            font=("Arial", 12)
        )
        self.password.pack(fill=X, padx=30, pady=5)

        self.show = False

        self.btn_show = Button(
            login_frame,
            text="Show Password",
            command=self.toggle_password,
            bg="#3498DB",
            fg="white"
        )
        self.btn_show.pack(pady=10)

        Button(
            login_frame,
            text="LOGIN",
            command=self.login,
            bg="#27AE60",
            fg="white",
            font=("Arial", 12, "bold"),
            width=20
        ).pack(pady=15)

    def toggle_password(self):

        if self.show:
            self.password.config(show="*")
            self.btn_show.config(text="Show Password")
            self.show = False
        else:
            self.password.config(show="")
            self.btn_show.config(text="Hide Password")
            self.show = True

    def login(self):

        user = self.username.get()
        pwd = self.password.get()

        if user == "" or pwd == "":
            messagebox.showerror(
                "Error",
                "All fields are required."
            )
            return

        con = connect_db()

        if con is None:
            messagebox.showerror(
                "Database",
                "Connection Failed."
            )
            return

        cur = con.cursor()

        cur.execute(
            "SELECT * FROM users WHERE username=%s AND password=%s",
            (user, pwd)
        )

        row = cur.fetchone()

        if row is None:
            messagebox.showerror(
                "Login Failed",
                "Invalid Username or Password"
            )
        else:
            messagebox.showinfo(
                "Success",
                "Login Successful"
            )

            self.root.destroy()

            import dashboard

        con.close()


root = Tk()
obj = Login(root)
root.mainloop()