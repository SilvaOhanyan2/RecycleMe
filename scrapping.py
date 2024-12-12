import pandas as pd
from bs4 import BeautifulSoup
import requests

product_list = []

# Define the URL of the page to scrape
url = "https://www.sas.am/catalog/sakhar_zamenitel_sakhara/"
response = requests.get(url)

if response.status_code == 200:  # Check if request was successful
    soup = BeautifulSoup(response.content, "html.parser")
    print("Page content fetched successfully.")

    # Locate the product grid
    product_grid = soup.find("div", class_="catalog__grid grid")
    if product_grid:
        print("Catalog grid found.")

        # Locate each product within the grid
        each_product = product_grid.find_all("div", class_="catalog__col col-xl-3 col-lg-3 col-md-4 col-sm-6 col-xs-12")
        print(f"Found {len(each_product)} products.")

        for item in each_product:
            # Extract product details
            product_name = item.find("div", class_="product__name hidden visible-sm")  # Updated class for name
            product_price = item.find("div", class_="product__price-wrap flc")  # Updated class for price
            product_code = item.find("input", {"name": "id"})  # Hidden input field for product code
            product_availability = item.find("div", class_="product__availability")  # Adjust based on actual class

            # Clean and process the price
            price = product_price.text.strip() if product_price else 'N/A'
            price = price.replace(" դր", "").replace(",", "").strip()  # Remove currency and clean format
            price = int(price) if price.isdigit() else price  # Convert to integer if it's numeric

            # Store the data
            product_data = {
                'Ապրանքի անվանում': product_name.text.strip() if product_name else 'N/A',
                'Գին': price,
                'Ապրանքի կոդ': product_code["value"] if product_code else 'N/A',
                'Հասանելիություն': 'Available' if product_price else 'Unavailable',  # Example for availability
            }
            product_list.append(product_data)
    else:
        print("Product grid not found.")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")

# Create a DataFrame from the scraped data
df = pd.DataFrame(product_list)

# Display the DataFrame
print("\nScraped Products:")
print(df)

# Optionally, save to a CSV file
df.to_csv("scraped_products.csv", index=False, encoding='utf-8')

import pandas as pd
from bs4 import BeautifulSoup
import requests

product_list = []

# Define the URL of the page to scrape
url = "https://www.sas.am/catalog/sakhar_zamenitel_sakhara/"
response = requests.get(url)

if response.status_code == 200:  # Check if request was successful
    soup = BeautifulSoup(response.content, "html.parser")
    print("Page content fetched successfully.")

    # Locate the product grid
    product_grid = soup.find("div", class_="catalog__grid grid")
    if product_grid:
        print("Catalog grid found.")

        # Locate each product within the grid
        each_product = product_grid.find_all("div", class_="catalog__col col-xl-3 col-lg-3 col-md-4 col-sm-6 col-xs-12")
        print(f"Found {len(each_product)} products.")

        for item in each_product:
            # Extract product details
            product_name = item.find("div", class_="product__name hidden visible-sm")  # Updated class for name
            product_price = item.find("div", class_="product__price-wrap flc")  # Updated class for price
            product_code = item.find("input", {"name": "id"})  # Hidden input field for product code
            product_availability = item.find("div", class_="product__availability")  # Adjust based on actual class

            # Clean and process the price
            price = product_price.text.strip() if product_price else 'N/A'
            price = price.replace(" դր", "").replace(",", "").strip()  # Remove currency and clean format
            price = int(price) if price.isdigit() else price  # Convert to integer if it's numeric

            # Store the data
            product_data = {
                'Ապրանքի անվանում': product_name.text.strip() if product_name else 'N/A',
                'Գին': price,
                'Ապրանքի կոդ': product_code["value"] if product_code else 'N/A',
                'Հասանելիություն': 'Available' if product_price else 'Unavailable',  # Example for availability
            }
            product_list.append(product_data)
    else:
        print("Product grid not found.")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")

# Create a DataFrame from the scraped data
df = pd.DataFrame(product_list)

# Display the DataFrame
print("\nScraped Products:")
print(df)

# Optionally, save to a CSV file
df.to_csv("scraped_products.csv", index=False, encoding='utf-8')

import pandas as pd
from bs4 import BeautifulSoup
import requests

product_list = []

# Define the URL of the page to scrape
url = "https://www.sas.am/catalog/bakaleya_diabet/"
response = requests.get(url)

if response.status_code == 200:  # Check if request was successful
    soup = BeautifulSoup(response.content, "html.parser")
    print("Page content fetched successfully.")

    # Locate the product grid
    product_grid = soup.find("div", class_="catalog__grid grid")
    if product_grid:
        print("Catalog grid found.")

        # Locate each product within the grid
        each_product = product_grid.find_all("div", class_="catalog__col col-xl-3 col-lg-3 col-md-4 col-sm-6 col-xs-12")
        print(f"Found {len(each_product)} products.")

        for item in each_product:
            # Extract product details
            product_name = item.find("div", class_="product__name hidden visible-sm")  # Updated class for name
            product_price = item.find("div", class_="product__price-wrap flc")  # Updated class for price
            product_code = item.find("input", {"name": "id"})  # Hidden input field for product code
            product_availability = item.find("div", class_="product__availability")  # Adjust based on actual class

            # Clean and process the price
            price = product_price.text.strip() if product_price else 'N/A'
            price = price.replace(" դր", "").replace(",", "").strip()  # Remove currency and clean format
            price = int(price) if price.isdigit() else price  # Convert to integer if it's numeric

            # Store the data
            product_data = {
                'Ապրանքի անվանում': product_name.text.strip() if product_name else 'N/A',
                'Գին': price,
                'Ապրանքի կոդ': product_code["value"] if product_code else 'N/A',
                'Հասանելիություն': 'Available' if product_price else 'Unavailable',  # Example for availability
            }
            product_list.append(product_data)
    else:
        print("Product grid not found.")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")

# Create a DataFrame from the scraped data
df = pd.DataFrame(product_list)

# Display the DataFrame
print("\nScraped Products:")
print(df)

# Optionally, save to a CSV file
df.to_csv("scraped_products.csv", index=False, encoding='utf-8')


import pandas as pd
from bs4 import BeautifulSoup
import requests

product_list = []

# Define the URL of the page to scrape
url = "https://www.sas.am/catalog/napitki/"
response = requests.get(url)

if response.status_code == 200:  # Check if request was successful
    soup = BeautifulSoup(response.content, "html.parser")
    print("Page content fetched successfully.")

    # Locate the product grid
    product_grid = soup.find("div", class_="catalog__grid grid")
    if product_grid:
        print("Catalog grid found.")

        # Locate each product within the grid
        each_product = product_grid.find_all("div", class_="catalog__col col-xl-3 col-lg-3 col-md-4 col-sm-6 col-xs-12")
        print(f"Found {len(each_product)} products.")

        for item in each_product:
            # Extract product details
            product_name = item.find("div", class_="product__name hidden visible-sm")  # Updated class for name
            product_price = item.find("div", class_="product__price-wrap flc")  # Updated class for price
            product_code = item.find("input", {"name": "id"})  # Hidden input field for product code
            product_availability = item.find("div", class_="product__availability")  # Adjust based on actual class

            # Clean and process the price
            price = product_price.text.strip() if product_price else 'N/A'
            price = price.replace(" դր", "").replace(",", "").strip()  # Remove currency and clean format
            price = int(price) if price.isdigit() else price  # Convert to integer if it's numeric

            # Store the data
            product_data = {
                'Ապրանքի անվանում': product_name.text.strip() if product_name else 'N/A',
                'Գին': price,
                'Ապրանքի կոդ': product_code["value"] if product_code else 'N/A',
                'Հասանելիություն': 'Available' if product_price else 'Unavailable',  # Example for availability
            }
            product_list.append(product_data)
    else:
        print("Product grid not found.")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")

# Create a DataFrame from the scraped data
df = pd.DataFrame(product_list)

# Display the DataFrame
print("\nScraped Products:")
print(df)

# Optionally, save to a CSV file
df.to_csv("scraped_products.csv", index=False, encoding='utf-8')

import pandas as pd
from bs4 import BeautifulSoup
import requests

product_list = []

# Define the URL of the page to scrape
url = "https://www.sas.am/catalog/sladosti_i_deserty/"
response = requests.get(url)

if response.status_code == 200:  # Check if request was successful
    soup = BeautifulSoup(response.content, "html.parser")
    print("Page content fetched successfully.")

    # Locate the product grid
    product_grid = soup.find("div", class_="catalog__grid grid")
    if product_grid:
        print("Catalog grid found.")

        # Locate each product within the grid
        each_product = product_grid.find_all("div", class_="catalog__col col-xl-3 col-lg-3 col-md-4 col-sm-6 col-xs-12")
        print(f"Found {len(each_product)} products.")

        for item in each_product:
            # Extract product details
            product_name = item.find("div", class_="product__name hidden visible-sm")  # Updated class for name
            product_price = item.find("div", class_="product__price-wrap flc")  # Updated class for price
            product_code = item.find("input", {"name": "id"})  # Hidden input field for product code
            product_availability = item.find("div", class_="product__availability")  # Adjust based on actual class

            # Clean and process the price
            price = product_price.text.strip() if product_price else 'N/A'
            price = price.replace(" դր", "").replace(",", "").strip()  # Remove currency and clean format
            price = int(price) if price.isdigit() else price  # Convert to integer if it's numeric

            # Store the data
            product_data = {
                'Ապրանքի անվանում': product_name.text.strip() if product_name else 'N/A',
                'Գին': price,
                'Ապրանքի կոդ': product_code["value"] if product_code else 'N/A',
                'Հասանելիություն': 'Available' if product_price else 'Unavailable',  # Example for availability
            }
            product_list.append(product_data)
    else:
        print("Product grid not found.")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")

# Create a DataFrame from the scraped data
df = pd.DataFrame(product_list)

# Display the DataFrame
print("\nScraped Products:")
print(df)

# Optionally, save to a CSV file
df.to_csv("scraped_products.csv", index=False, encoding='utf-8')

import pandas as pd
from bs4 import BeautifulSoup
import requests

product_list = []
# Առանց Խոլեստերին ապրանքներ
# Define the URL of the page to scrape
url = "https://www.sas.am/catalog/produkty_bez_soderzhaniya_kholesterina/"
response = requests.get(url)

if response.status_code == 200:  # Check if request was successful
    soup = BeautifulSoup(response.content, "html.parser")
    print("Page content fetched successfully.")

    # Locate the product grid
    product_grid = soup.find("div", class_="catalog__grid grid")
    if product_grid:
        print("Catalog grid found.")

        # Locate each product within the grid
        each_product = product_grid.find_all("div", class_="catalog__col col-xl-3 col-lg-3 col-md-4 col-sm-6 col-xs-12")
        print(f"Found {len(each_product)} products.")

        for item in each_product:
            # Extract product details
            product_name = item.find("div", class_="product__name hidden visible-sm")  # Updated class for name
            product_price = item.find("div", class_="product__price-wrap flc")  # Updated class for price
            product_code = item.find("input", {"name": "id"})  # Hidden input field for product code
            product_availability = item.find("div", class_="product__availability")  # Adjust based on actual class

            # Clean and process the price
            price = product_price.text.strip() if product_price else 'N/A'
            price = price.replace(" դր", "").replace(",", "").strip()  # Remove currency and clean format
            price = int(price) if price.isdigit() else price  # Convert to integer if it's numeric

            # Store the data
            product_data = {
                'Ապրանքի անվանում': product_name.text.strip() if product_name else 'N/A',
                'Գին': price,
                'Ապրանքի կոդ': product_code["value"] if product_code else 'N/A',
                'Հասանելիություն': 'Available' if product_price else 'Unavailable',  # Example for availability
            }
            product_list.append(product_data)
    else:
        print("Product grid not found.")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")

# Create a DataFrame from the scraped data
df = pd.DataFrame(product_list)

# Display the DataFrame
print("\nScraped Products:")
print(df)

# Optionally, save to a CSV file
df.to_csv("scraped_products.csv", index=False, encoding='utf-8')

import pandas as pd
from bs4 import BeautifulSoup
import requests

product_list = []
#խոլեստերին նվազեցնող ապրանքներ
# Define the URL of the page to scrape
url = "https://www.sas.am/catalog/produkty_ponizhayushchie_kholesterin1/"
response = requests.get(url)

if response.status_code == 200:  # Check if request was successful
    soup = BeautifulSoup(response.content, "html.parser")
    print("Page content fetched successfully.")

    # Locate the product grid
    product_grid = soup.find("div", class_="catalog__grid grid")
    if product_grid:
        print("Catalog grid found.")

        # Locate each product within the grid
        each_product = product_grid.find_all("div", class_="catalog__col col-xl-3 col-lg-3 col-md-4 col-sm-6 col-xs-12")
        print(f"Found {len(each_product)} products.")

        for item in each_product:
            # Extract product details
            product_name = item.find("div", class_="product__name hidden visible-sm")  # Updated class for name
            product_price = item.find("div", class_="product__price-wrap flc")  # Updated class for price
            product_code = item.find("input", {"name": "id"})  # Hidden input field for product code
            product_availability = item.find("div", class_="product__availability")  # Adjust based on actual class

            # Clean and process the price
            price = product_price.text.strip() if product_price else 'N/A'
            price = price.replace(" դր", "").replace(",", "").strip()  # Remove currency and clean format
            price = int(price) if price.isdigit() else price  # Convert to integer if it's numeric

            # Store the data
            product_data = {
                'Ապրանքի անվանում': product_name.text.strip() if product_name else 'N/A',
                'Գին': price,
                'Ապրանքի կոդ': product_code["value"] if product_code else 'N/A',
                'Հասանելիություն': 'Available' if product_price else 'Unavailable',  # Example for availability
            }
            product_list.append(product_data)
    else:
        print("Product grid not found.")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")

# Create a DataFrame from the scraped data
df = pd.DataFrame(product_list)

# Display the DataFrame
print("\nScraped Products:")
print(df)

# Optionally, save to a CSV file
df.to_csv("scraped_products.csv", index=False, encoding='utf-8')

import pandas as pd
from bs4 import BeautifulSoup
import requests

product_list = []
#օրգանիկ քաղցրավենիք
# Define the URL of the page to scrape
url = "https://www.sas.am/catalog/sladostiorganic/"
response = requests.get(url)

if response.status_code == 200:  # Check if request was successful
    soup = BeautifulSoup(response.content, "html.parser")
    print("Page content fetched successfully.")

    # Locate the product grid
    product_grid = soup.find("div", class_="catalog__grid grid")
    if product_grid:
        print("Catalog grid found.")

        # Locate each product within the grid
        each_product = product_grid.find_all("div", class_="catalog__col col-xl-3 col-lg-3 col-md-4 col-sm-6 col-xs-12")
        print(f"Found {len(each_product)} products.")

        for item in each_product:
            # Extract product details
            product_name = item.find("div", class_="product__name hidden visible-sm")  # Updated class for name
            product_price = item.find("div", class_="product__price-wrap flc")  # Updated class for price
            product_code = item.find("input", {"name": "id"})  # Hidden input field for product code
            product_availability = item.find("div", class_="product__availability")  # Adjust based on actual class

            # Clean and process the price
            price = product_price.text.strip() if product_price else 'N/A'
            price = price.replace(" դր", "").replace(",", "").strip()  # Remove currency and clean format
            price = int(price) if price.isdigit() else price  # Convert to integer if it's numeric

            # Store the data
            product_data = {
                'Ապրանքի անվանում': product_name.text.strip() if product_name else 'N/A',
                'Գին': price,
                'Ապրանքի կոդ': product_code["value"] if product_code else 'N/A',
                'Հասանելիություն': 'Available' if product_price else 'Unavailable',  # Example for availability
            }
            product_list.append(product_data)
    else:
        print("Product grid not found.")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")

# Create a DataFrame from the scraped data
df = pd.DataFrame(product_list)

# Display the DataFrame
print("\nScraped Products:")
print(df)

# Optionally, save to a CSV file
df.to_csv("scraped_products.csv", index=False, encoding='utf-8')

import pandas as pd
from bs4 import BeautifulSoup
import requests

product_list = []
#օրգանիկ ըմպելիք
# Define the URL of the page to scrape
url = "https://www.sas.am/catalog/sokinapitki/"
response = requests.get(url)

if response.status_code == 200:  # Check if request was successful
    soup = BeautifulSoup(response.content, "html.parser")
    print("Page content fetched successfully.")

    # Locate the product grid
    product_grid = soup.find("div", class_="catalog__grid grid")
    if product_grid:
        print("Catalog grid found.")

        # Locate each product within the grid
        each_product = product_grid.find_all("div", class_="catalog__col col-xl-3 col-lg-3 col-md-4 col-sm-6 col-xs-12")
        print(f"Found {len(each_product)} products.")

        for item in each_product:
            # Extract product details
            product_name = item.find("div", class_="product__name hidden visible-sm")  # Updated class for name
            product_price = item.find("div", class_="product__price-wrap flc")  # Updated class for price
            product_code = item.find("input", {"name": "id"})  # Hidden input field for product code
            product_availability = item.find("div", class_="product__availability")  # Adjust based on actual class

            # Clean and process the price
            price = product_price.text.strip() if product_price else 'N/A'
            price = price.replace(" դր", "").replace(",", "").strip()  # Remove currency and clean format
            price = int(price) if price.isdigit() else price  # Convert to integer if it's numeric

            # Store the data
            product_data = {
                'Ապրանքի անվանում': product_name.text.strip() if product_name else 'N/A',
                'Գին': price,
                'Ապրանքի կոդ': product_code["value"] if product_code else 'N/A',
                'Հասանելիություն': 'Available' if product_price else 'Unavailable',  # Example for availability
            }
            product_list.append(product_data)
    else:
        print("Product grid not found.")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")

# Create a DataFrame from the scraped data
df = pd.DataFrame(product_list)

# Display the DataFrame
print("\nScraped Products:")
print(df)

# Optionally, save to a CSV file
df.to_csv("scraped_products.csv", index=False, encoding='utf-8')

import pandas as pd
from bs4 import BeautifulSoup
import requests

product_list = []
#օրգանիկ նպարեղեն
# Define the URL of the page to scrape
url = "https://www.sas.am/catalog/bakaleyaorganic/"
response = requests.get(url)

if response.status_code == 200:  # Check if request was successful
    soup = BeautifulSoup(response.content, "html.parser")
    print("Page content fetched successfully.")

    # Locate the product grid
    product_grid = soup.find("div", class_="catalog__grid grid")
    if product_grid:
        print("Catalog grid found.")

        # Locate each product within the grid
        each_product = product_grid.find_all("div", class_="catalog__col col-xl-3 col-lg-3 col-md-4 col-sm-6 col-xs-12")
        print(f"Found {len(each_product)} products.")

        for item in each_product:
            # Extract product details
            product_name = item.find("div", class_="product__name hidden visible-sm")  # Updated class for name
            product_price = item.find("div", class_="product__price-wrap flc")  # Updated class for price
            product_code = item.find("input", {"name": "id"})  # Hidden input field for product code
            product_availability = item.find("div", class_="product__availability")  # Adjust based on actual class

            # Clean and process the price
            price = product_price.text.strip() if product_price else 'N/A'
            price = price.replace(" դր", "").replace(",", "").strip()  # Remove currency and clean format
            price = int(price) if price.isdigit() else price  # Convert to integer if it's numeric

            # Store the data
            product_data = {
                'Ապրանքի անվանում': product_name.text.strip() if product_name else 'N/A',
                'Գին': price,
                'Ապրանքի կոդ': product_code["value"] if product_code else 'N/A',
                'Հասանելիություն': 'Available' if product_price else 'Unavailable',  # Example for availability
            }
            product_list.append(product_data)
    else:
        print("Product grid not found.")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")

# Create a DataFrame from the scraped data
df = pd.DataFrame(product_list)

# Display the DataFrame
print("\nScraped Products:")
print(df)

# Optionally, save to a CSV file
df.to_csv("scraped_products.csv", index=False, encoding='utf-8')

import pandas as pd
from bs4 import BeautifulSoup
import requests

product_list = []
#առանց գլյուտեն
# Define the URL of the page to scrape
url = "https://www.sas.am/catalog/bez_glyutena/?LIMIT=60"
response = requests.get(url)

if response.status_code == 200:  # Check if request was successful
    soup = BeautifulSoup(response.content, "html.parser")
    print("Page content fetched successfully.")

    # Locate the product grid
    product_grid = soup.find("div", class_="catalog__grid grid")
    if product_grid:
        print("Catalog grid found.")

        # Locate each product within the grid
        each_product = product_grid.find_all("div", class_="catalog__col col-xl-3 col-lg-3 col-md-4 col-sm-6 col-xs-12")
        print(f"Found {len(each_product)} products.")

        for item in each_product:
            # Extract product details
            product_name = item.find("div", class_="product__name hidden visible-sm")  # Updated class for name
            product_price = item.find("div", class_="product__price-wrap flc")  # Updated class for price
            product_code = item.find("input", {"name": "id"})  # Hidden input field for product code
            product_availability = item.find("div", class_="product__availability")  # Adjust based on actual class

            # Clean and process the price
            price = product_price.text.strip() if product_price else 'N/A'
            price = price.replace(" դր", "").replace(",", "").strip()  # Remove currency and clean format
            price = int(price) if price.isdigit() else price  # Convert to integer if it's numeric

            # Store the data
            product_data = {
                'Ապրանքի անվանում': product_name.text.strip() if product_name else 'N/A',
                'Գին': price,
                'Ապրանքի կոդ': product_code["value"] if product_code else 'N/A',
                'Հասանելիություն': 'Available' if product_price else 'Unavailable',  # Example for availability
            }
            product_list.append(product_data)
    else:
        print("Product grid not found.")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")

# Create a DataFrame from the scraped data
df = pd.DataFrame(product_list)

# Display the DataFrame
print("\nScraped Products:")
print(df)

# Optionally, save to a CSV file
df.to_csv("scraped_products.csv", index=False, encoding='utf-8')




