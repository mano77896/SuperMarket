# Super Market Billing System

A desktop-based Super Market Billing System developed using **Python**, **Tkinter**, and **MySQL**. This project helps manage products, customers, suppliers, billing, and inventory through an easy-to-use graphical interface.

---

## Features

- 🔐 Login System
- 📊 Dashboard
- 📦 Product Management
  - Add Product
  - Update Product
  - Delete Product
  - Search Product
  - Product Image Upload
- 👥 Customer Management
  - Add Customer
  - Update Customer
  - Delete Customer
  - Search Customer
- 🚚 Supplier Management *(Under Development)*
- 🧾 Billing Module *(Coming Soon)*
- 📈 Sales Report *(Coming Soon)*

---

## Technologies Used

- Python 3
- Tkinter
- MySQL
- Pillow (Image Processing)
- tkcalendar
- Git & GitHub

---

## 📂 Project Structure

```
SuperMarket/
│
├── backup/
├── database/
├── images/
├── modules/
│   ├── product.py
│   ├── customer.py
│   ├── supplier.py
├── reports/
├── dashboard.py
├── login.py
├── .gitignore
└── README.md
```

---

##  Installation

1. Clone the repository

```bash
git clone https://github.com/mano77896/SuperMarket.git
```

2. Install required packages

```bash
pip install pillow
pip install tkcalendar
pip install mysql-connector-python
```

3. Create the MySQL database.

4. Update the database credentials in `database/db.py`.

5. Run the application

```bash
python login.py
```

---

##  Project Status

✅ Login Module Completed

✅ Dashboard Completed

✅ Product Module Completed

✅ Customer Module Completed

🟡 Supplier Module In Progress

🔜 Billing Module

🔜 Sales Report

---

##  Developer

MANO S,
Junior Python & Web Developer

---

##  Future Improvements

- Barcode Scanner Support
- PDF Bill Generation
- Sales Analytics Dashboard
- User Roles (Admin/Cashier)
- Stock Alerts
