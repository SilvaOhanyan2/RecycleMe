import sqlite3
import pandas as pd

# Example scraped data in a dictionary format
data = {
    "Ապրանքի անվանում": [
        "Շաքարի փոխարինիչ «Novasweet Стевия» 200գ", 
        "Քաղցրացուցիչ հեղուկ «Bionova Стевия Nature» 80գ",
        # Add the rest of your product names here...
    ],
    "Գին": [
        "2 990.", "1 850.",
        # Add the rest of your prices here...
    ],
    "Ապրանքի կոդ": [
        48158, 48156,
        # Add the rest of your product codes here...
    ],
    "Հասանելիություն": [
        "Available", "Available",
        # Add the rest of your availability statuses here...
    ]
}

# Convert data to a pandas DataFrame
df = pd.DataFrame(data)

# Clean the 'Գին' column by removing non-numeric characters and converting to integers
df["Գին"] = df["Գին"].str.replace(r"[^\d]", "", regex=True).astype(int)

# Connect to SQLite database (creates the database if it doesn't exist)
conn = sqlite3.connect("scraped_data.db")
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price INTEGER,
    code INTEGER,
    availability TEXT
)
''')

# Insert data into the database using pandas
df.rename(columns={
    "Ապրանքի անվանում": "name",
    "Գին": "price",
    "Ապրանքի կոդ": "code",
    "Հասանելիություն": "availability"
}, inplace=True)

df.to_sql("products", conn, if_exists="append", index=False)

# Fetch and display data to confirm it was inserted correctly
cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()

print("Database 'scraped_data.db' created and data inserted successfully!")
