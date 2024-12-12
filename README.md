# RecycleMe Web Scraper and Database Integration

This project provides a Python-based tool to scrape product data from e-commerce websites, process it, and store it in a structured SQLite database. The tool is part of the RecycleMe initiative, aiming to gather and analyze data for sustainable and informed consumer decisions.

---

## Features

1. **Web Scraping**:
   - Extracts product details such as names, prices, availability, and codes.
   - Handles varying HTML structures using the `BeautifulSoup` library.
   - Automates data collection from multiple e-commerce pages.

2. **Data Cleaning**:
   - Processes and cleans price data to ensure uniformity and usability.
   - Handles missing or unavailable data gracefully.

3. **Database Integration**:
   - Stores scraped data in an SQLite database.
   - Creates tables dynamically and inserts data efficiently.
   - Provides functionality to fetch and validate stored data.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/recycleme-scraper.git
   cd recycleme-scraper
