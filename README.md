# E-Commerce Product Scraper

A web-based book scraping application built using Python, Flask, BeautifulSoup, HTML, CSS, and JavaScript. It allows users to search for books and view product information through a simple and user-friendly interface.

## Project Overview

The E-Commerce Product Scraper is a web application that collects book information from [Books to Scrape](https://books.toscrape.com/) and displays the results on a website.

Users can search for books and explore product details such as book titles, prices, ratings, images, and product links.

## Purpose

The purpose of this project is to learn and implement web scraping techniques using Python and to understand how scraped data can be integrated into a web application.

This project was developed to:

- Practice web scraping using BeautifulSoup and Requests.
- Extract product information from a website.
- Build a backend using Flask.
- Connect the backend with a frontend using JavaScript.
- Display scraped data in a user-friendly interface.
- Understand how frontend and backend components work together.

## Features

- Search books by title.
- Scrape book information from a website.
- Display book titles, prices, ratings, and images.
- View book details through external links.
- Simple and user-friendly interface.
- Responsive book listing layout.

## Demo Screenshots

### 1. Home Page & Book Search

The home page provides a search bar where users can enter a book title and search for books.
<img width="1872" height="958" alt="Screenshot 2026-11-25 140731" src="https://github.com/user-attachments/assets/67201748-4060-4c88-84ce-d3fcab65c021" />

### 2. Book Search Results

The application displays book information in individual cards, including book covers, titles, prices, ratings, and a View Details button.
<img width="1882" height="915" alt="Screenshot 2026-11-25 140759" src="https://github.com/user-attachments/assets/4e42d970-625a-46bf-9afc-775f3b7e26fd" />

## Technologies Used

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask
- BeautifulSoup
- Requests
- Flask-CORS

## Project Structure

```text
E-Commerce-Product-Scraper/
│
├── backend/
│   ├── app.py
│   ├── scraper.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Awantika14-ui/E-Commerce-Product-Scraper.git
```

### 2. Navigate to the project folder

```bash
cd E-Commerce-Product-Scraper
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 6. Start the Flask backend

```bash
python app.py
```

The backend runs at:

`http://127.0.0.1:5000/`

### 7. Start the frontend

Open a second terminal and navigate to the frontend directory:

```bash
cd frontend
python -m http.server 8000
```

Open your browser and visit:

`http://127.0.0.1:8000/`

## Data Source

This project uses [Books to Scrape](https://books.toscrape.com/), a website specifically designed for practicing web scraping.

## Learning Outcomes

- Gained practical experience with Python web scraping.
- Learned how to extract website data using BeautifulSoup.
- Practiced building web applications using Flask.
- Understood frontend and backend integration.
- Worked with HTTP requests and scraped data handling.
- Improved understanding of displaying dynamic data on a webpage.

---

*Developed as a hands-on project to gain practical experience in Python web scraping, Flask, and frontend-backend integration.*
