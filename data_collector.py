import Glassdoor_Scraper
import pandas as pd

path = '/Users/rohit/Downloads/chromedriver'
df = Glassdoor_Scraper.get_jobs('data scientist', 1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index=False)