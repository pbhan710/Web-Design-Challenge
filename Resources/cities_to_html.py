# Import dependencies.
import pandas as pd

# Read 'cities.csv' and store into a Pandas DataFrame.
fp = 'cities.csv'
df = pd.read_csv(fp, index_col=False)
df['Date'] 

# Render DataFrame as an HTML table.
html = df.to_html(index=False)

with open('cities_to_html.txt', 'w') as text_file:
    text_file.write(html)