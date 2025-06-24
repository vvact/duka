
# 🛒 Ecomerec – General E-Commerce Website (Kenya)

> A full-featured general e-commerce website built with Django and tailored for the Kenyan market. Ecomerec supports product browsing, cart management, order placement, and secure checkout via M-Pesa.

---

## 🌍 Overview

**Ecomerec** is an e-commerce platform developed specifically for Kenyan shoppers. It uses **Django templates** for the frontend and includes a **working M-Pesa integration** to allow seamless mobile payments directly from the site.

---

## 🚀 Key Features

- 🛍️ **Product Listings & Categories**
- 🧺 **Cart & Checkout Pages**
- 🔐 **User Registration, Login & Google Auth**
- 💰 **M-Pesa Daraja API Integration**
- 📦 **Order Placement & Confirmation**
- 🖼️ **Product Image Uploads via Firebase**
- 📱 **Responsive Design (Bootstrap)**

---

## ⚙️ Tech Stack

### 🔧 Backend
- **Python 3 & Django 5**
- **Django Templates (HTML + Bootstrap)**
- **SQLite / PostgreSQL**
- **Django Knox or SessionAuth**
- **M-Pesa Daraja API** (STK Push)

### 🖼️ Image Hosting
- **Firebase Storage** (Product and category images)

---

## 🧑‍💻 Getting Started

```bash
# Clone the repository
git clone https://github.com/vvact/ecomerec.git
cd ecomerec

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
```

---

## 💸 M-Pesa Integration

M-Pesa is integrated using the **Daraja API**:

- STK Push enabled
- Users get a prompt on their phones
- Transaction recorded and verified via M-Pesa response

> ✅ Works in sandbox or production (your choice)

---

## 📂 Folder Structure (Simplified)

```
ecomerec/
├── products/            # Product and category models
├── orders/              # Cart and order logic
├── templates/           # HTML templates (Django)
├── static/              # CSS, JS, images
├── mpesa/               # M-Pesa API logic
├── users/               # Auth system (Google login supported)
└── manage.py
```

---

## 📸 Screenshots (Add for better visibility)

- Homepage with categories
- Product listing and detail page
- Cart and checkout
- M-Pesa payment success

---

## 🌐 SEO & Metadata (example for base template)

```html
<meta name="description" content="Ecomerec is a Kenyan general e-commerce platform with M-Pesa integration. Buy electronics, fashion, groceries, and more." />
<meta name="keywords" content="kenya ecommerce, mpesa checkout, online shopping kenya, django ecommerce" />
<meta name="author" content="Victor Bunyali" />
```

---

## 🤝 Contributions

Contributions, feedback, and feature requests are welcome! Fork the repo, open an issue, or submit a pull request.

---

## 📧 Contact

**Developer**: Victor Bunyali  
**GitHub**: [https://github.com/vvact](https://github.com/vvact)  
**Email**: [your-email@example.com]

---

## 🏁 Future Features (optional)

- Vendor dashboard
- Order tracking
- Product reviews
- Mobile app version
