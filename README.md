---

# 🛍️ Etsy Product Scraper (Stealth Mode)

This project is a **Python-based Etsy web scraper** built using `undetected-chromedriver` and `Selenium`.
It allows you to **scrape product listings from Etsy** without being blocked, capturing product details like **title, price, shop name, rating, and review count**.

---

## 🚀 Features

* Stealth scraping using `undetected-chromedriver` (avoids bot detection).
* Extracts:

  * Product name
  * Price (USD)
  * Shop name
  * Rating
  * Review count (auto-converted from shorthand like `2.8k` → `2800`)
  * Category (search term)
  * Scraped date
* Handles **multiple pages of results**.
* Saves data to a clean **CSV file** for further analysis.

---

## 🛠️ Requirements

Make sure you have Python 3.8+ installed.
Install dependencies using:

```bash
pip install undetected-chromedriver selenium pandas
```

---

## 📂 Usage

1. Clone this repository:

```bash
git clone https://github.com/yourusername/etsy-product-scraper.git
cd etsy-product-scraper
```

2. Run the script with your desired search term:

```bash
python etsy_scraper.py
```

3. Example run:

```python
scrape_etsy_stealth("everyday items", num_pages=5)
```

This will scrape **5 pages of Etsy search results** for "everyday items".

---

## 📊 Output

The scraped data is saved in:

```
etsy_products_stealth_v2.csv
```

With columns:

| Product Name | Price (USD) | Shop Name | Rating | Review Count | Category | Scraped Date |
| ------------ | ----------- | --------- | ------ | ------------ | -------- | ------------ |

---

## ⚠️ Notes

* Etsy’s website structure may change; if selectors break, update the CSS selectors in the script.
* Respect Etsy’s [robots.txt](https://www.etsy.com/robots.txt) and use responsibly (educational/research purposes only).
* For large-scale scraping, add delays or proxies to avoid rate limiting.

---

## 📌 Example

Running with `search_term="jewelry"` and `num_pages=2` will produce something like:

```csv
Product Name,Price (USD),Shop Name,Rating,Review Count,Category,Scraped Date
"Silver Necklace","35.00","ShinyJewels","4.9","1200","jewelry","2025-08-31"
"Handmade Bracelet","18.50","CraftyHands","4.8","560","jewelry","2025-08-31"
...
```

---

## 📜 License

This project is licensed under the MIT License – free to use and modify.

---

👉 Do you want me to also make a **sample `etsy_scraper.py` file with argparse** (so you can run it from the command line with `--search "jewelry" --pages 3`)? That would make it even more user-friendly for GitHub.
