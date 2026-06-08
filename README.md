# Python Job Listings Scraper

A simple Python web scraping project that collects job listings from the Fake Python Jobs website and stores them in a CSV file.

## 📌 Project Overview

This project was built as part of the roadmap.sh **Python Job Listings Scraper** challenge. The scraper extracts job-related information from a sample job board website and saves the collected data for further analysis.

## 🚀 Features

* Scrapes job listings from the website
* Extracts:

  * Job Title
  * Company Name
  * Location
  * Job Details URL
* Stores scraped data in a CSV file
* Handles missing fields gracefully
* Clean and beginner-friendly code structure

## 🛠️ Technologies Used

* Python
* Requests
* BeautifulSoup4 (bs4)
* CSV Module

## 📂 Project Structure

```bash
Python-Job-Listings-Scraper/
│
├── scraper.py
├── jobs.csv
├── requirements.txt
└── README.md
```

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/prajjukorban/Python-Job-Listings-Scraper.git
```

2. Navigate to the project directory:

```bash
cd Python-Job-Listings-Scraper
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Usage

Run the scraper:

```bash
python scraper.py
```

After execution, a `jobs.csv` file will be generated containing all scraped job listings.

## 📊 Sample Output

| Job Title        | Company     | Location |
| ---------------- | ----------- | -------- |
| Python Developer | ABC Company | New York |
| Data Analyst     | XYZ Corp    | Remote   |

## 🎯 Learning Outcomes

Through this project, I learned:

* Web scraping fundamentals
* Working with HTML structures
* Extracting data using BeautifulSoup
* Handling HTTP requests with Requests
* Exporting data to CSV files
* Data collection and preprocessing techniques

## 🌐 Source Website

https://realpython.github.io/fake-jobs/

## 📝 Project Reference

This project is inspired by the roadmap.sh Python Job Listings Scraper project:

https://roadmap.sh/projects/job-listings-scraper

## 👨‍💻 Author

**Prajwal K**

* GitHub: https://github.com/prajjukorban

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
