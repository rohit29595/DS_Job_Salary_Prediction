import Glassdoor_Scraper
import pandas as pd

path = '/Users/rohit/Downloads/chromedriver'
df = Glassdoor_Scraper.get_jobs('data scientist', 15, False, path, 15)
print(df.head())