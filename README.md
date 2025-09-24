# ALX Book Store Database

## Overview
This project contains a MySQL database schema for an **online bookstore**.  
The database is designed to manage information about **books, authors, customers, orders, and order details**.

## Database Name
`alx_book_store`

## Schema Design
The database contains the following tables:

1. **Authors**
   - `author_id` (Primary Key)
   - `author_name`

2. **Books**
   - `book_id` (Primary Key)
   - `title`
   - `author_id` (Foreign Key → Authors)
   - `price`
   - `publication_date`

3. **Customers**
   - `customer_id` (Primary Key)
   - `customer_name`
   - `email`
   - `address`

4. **Orders**
   - `order_id` (Primary Key)
   - `customer_id` (Foreign Key → Customers)
   - `order_date`

5. **Order_Details**
   - `orderdetailid` (Primary Key)
   - `order_id` (Foreign Key → Orders)
   - `book_id` (Foreign Key → Books)
   - `quantity`

## How to Run
1. Make sure you have MySQL installed.
2. Clone or download this project.
3. Run the SQL file:
   ```bash
   mysql -u your_username -p < alx_book_store.sql
