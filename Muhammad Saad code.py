from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd
import requests
import seaborn as sns

# Ask the user for input using the standard input() function
target_url = input('Enter the website URL you want to scrape: ')

# Fetch and parse the webpage with BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(target_url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

# Extract paragraph text lengths as an example dataset
paragraphs = [p.get_text() for p in soup.find_all('p')]
data = {
    'Paragraph_Index': range(len(paragraphs)),
    'Character_Count': [len(p) for p in paragraphs],
}

# Process the data using pandas
df = pd.DataFrame(data)
print('Successfully scraped and parsed the data into a DataFrame.')
print(df.head())

# Create a visualization using seaborn and matplotlib
sns.set_theme(style='darkgrid')
plt.figure(figsize=(9, 5))
sns.lineplot(data=df, x='Paragraph_Index', y='Character_Count', marker='o')
plt.title('Character Count per Paragraph from Scraped Website')
plt.xlabel('Paragraph Index')
plt.ylabel('Character Count')
plt.show()