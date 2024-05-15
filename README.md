# Food Ordering System using Django in Python

This project is a web-based Food Ordering System developed using Python and the Django Framework. It provides an online platform for customers to easily order their desired foods from a food shop or store. The system includes user-friendly features and functionalities and has a pleasant, light user interface with the help of the Bootstrap Framework, enhancing the user experience.

## About the Food Ordering System

### Technologies and Libraries Used:
- **Python**
- **Django**
- **SQLite3**
- **HTML**
- **CSS**
- **JavaScript**
- **jQuery**
- **Ajax**
- **Pillow Library**
- **Fontawesome**
- **Bootstrap**
- **django-tinymce4-lite**
- **jsmin**
- **sqlparse**
- **pytz**

### System Features

This Food Ordering System has two different user interfaces: one for the Admin or the Shop's Management and another for the Customers. 

- **Admin Interface:** Admins can manage their product list using Django's built-in Admin panel, which requires superuser access.
- **Customer Interface:** Customers can register, log in, browse food categories, order food, and manage their cart.

#### Customer Functionalities:
- Login and Registration
- Home
- Category List
- Order Food or Dishes
- Add Food or Dishes to Cart
- List Cart Items
- Remove Item/Items from Cart
- Place Order
- Mark Order as Delivered
- Logout

#### Admin Functionalities:
- Access the Admin Panel (Django's built-in Admin Site)
- Manage product list

### How to Run the Project

#### Requirements:
- Python (version 3.9.1 used for this project)
- PIP (Python package installer)

#### Setup/Installation:
1. **Download and Extract Source Code:** Download and extract the provided source code zip file.
2. **Open Terminal/Command Prompt:** Ensure that "python" and "pip" are added to your environment variables.
3. **Navigate to Project Directory:** Change the working directory to the extracted source code folder. For example:
   ```sh
   cd C:\Users\Personal-23\Desktop\django_fos
   ```
4. **Install Dependencies:** Run the following command to install the required Python modules:
   ```sh
   pip install -r requirements.txt
   ```
5. **Apply Migrations:** Run the migration commands:
   ```sh
   python manage.py migrate
   ```
6. **Start the Server:** Run the following command to start the Django development server:
   ```sh
   python manage.py runserver
   ```
7. **Access the Application:** Open a web browser and browse to [http://localhost:8000/](http://localhost:8000/) or [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

#### Access Information for Admin Site:
- **SuperUser/Admin:**
  - Username: `admin`
  - Password: `admin123`
- **Sample Customer:**
  - Username: `mcooper`
  - Password: `test#123`

To access the Django Admin Site, visit [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

### Notes
- Make sure to keep the terminals open and running while using the application.
- Customize and extend the functionalities as per your requirements.
