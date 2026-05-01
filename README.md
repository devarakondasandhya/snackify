# Snackify Snacks & Sweets Corner

A console-based shop management and food ordering system built using **Python and MySQL**.  
This project simulates a real-world snacks shop with separate functionalities for **owner (admin)** and **customers**.

---

## Overview

Snackify allows shop owners to manage menu items and staff, while customers can browse items, place orders, and generate a bill.

This project demonstrates the use of:
- Database connectivity in Python
- CRUD operations using MySQL
- Menu-driven console applications

---

## Features

### Owner Module
- Add new food items to menu
- View all menu items
- Update price of items
- Add new staff members
- View staff details
- Update staff salary

### Customer Module
- View available menu
- Order items using serial number
- Add multiple items to order
- Generate final bill with total amount

---

## Tech Stack

- **Programming Language:** Python
- **Database:** MySQL
- **Connector:** mysql-connector-python

---

## Setup & Installation

### 1. Install Requirements
Make sure you have:
- Python installed
- MySQL installed and running

---

### 2. Start MySQL Server (Mac)

bash
sudo /usr/local/mysql/support-files/mysql.server start


### 3. Create Database & Tables
- Run the setup file:
  mysql -u root -p < setup.sql
- This will:
  . Create database snackify
  . Create required tables (menu, staff)

### 4. Configure Database in Code
Open main.py and update:
- passwd = 'your_mysql_password'
- database = 'snackify'

### 5. Run the Application
python main.py
