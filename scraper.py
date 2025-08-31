import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import pandas as pd
import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_etsy_stealth(search_term, num_pages=1):
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = uc.Chrome(options=options, version_main=138)

    base_url = "https://www.etsy.com/search?q=" + search_term.replace(" ", "+")
    all_data = []

    for page in range(1, num_pages + 1):
        url = f"{base_url}&ref=pagination&page={page}"
        print(f"🔍 Scraping: {url}")

        driver.get(url)

        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "li.wt-list-unstyled div[data-listing-id]"))
            )
        except:
            print("⚠️ Product listings didn't load in time.")

        listings = driver.find_elements(By.CSS_SELECTOR, "li.wt-list-unstyled div[data-listing-id]")
        print(f"🛍️ Found {len(listings)} listings on page {page}")
        if not listings:
            print("⚠️ No listings found on this page.")
            continue

        for listing in listings:
            try:
                title = listing.find_element(By.CSS_SELECTOR, "h3").text.strip()
                print("🧾", title)
            except:
                title = None

            try:
                price_el = listing.find_elements(By.CSS_SELECTOR, "span.currency-value")
                price = price_el[0].text.strip() if price_el else None
            except:
                price = None

            try:
                shop_el = listing.find_elements(By.CSS_SELECTOR, "p")
                shop = shop_el[-1].text.strip() if shop_el else None
            except:
                shop = None

            # ✅ Extract rating and review count from updated structure
            try:
                rating = listing.find_element(By.CSS_SELECTOR, "span.wt-text-title-small").text.strip()
            except:
                rating = None

            try:
                review_count = listing.find_element(By.CSS_SELECTOR, "p.wt-text-body-smaller.wt-text-black").text.strip()
                if review_count.startswith("(") and review_count.endswith(")"):
                    review_count = review_count[1:-1]

                # Convert shorthand review counts (e.g. "2.8k") to full number
                if 'k' in review_count.lower():
                    review_count = review_count.lower().replace('k', '')
                    review_count = int(float(review_count) * 1000)
                else:
                    review_count = int(review_count.replace(",", ""))
            except:
                review_count = None

            if title and price:
                all_data.append({
                    "Product Name": title,
                    "Price (USD)": price,
                    "Shop Name": shop,
                    "Rating": rating,
                    "Review Count": review_count,
                    "Category": search_term,
                    "Scraped Date": datetime.today().strftime('%Y-%m-%d')
                })
                print(f"✅ Added: {title} - {price} - {shop}")

        time.sleep(3)

    driver.quit()
    df = pd.DataFrame(all_data)
    df.to_csv("etsy_products_stealth_v2.csv", index=False)
    print(f"✅ Scraped {len(df)} products to etsy_products_stealth_v2.csv")
    return df

# Run the scraper
scrape_etsy_stealth("everyday items", num_pages=5)
