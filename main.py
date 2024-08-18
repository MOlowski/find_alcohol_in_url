import json
import pandas as pd

from functions import find_urls

categories = [
    "beer", 
    "wine", 
    "cider", 
    "mead", 
    "sake", 
    "gin", 
    "brandy", 
    "whiskey", 
    "rum", 
    "tequila", 
    "vodka", 
    "absinthe"
    ]

url = "https://urlkeywords.cloudtechnologies.dev/keywordURLs"

headers = {"Content-Type": "application/json"}

# load alcohol brands df
df = pd.read_csv('alcohols.csv')

# find urls
results, found_brand_with_urls_num = find_urls(df, categories, url, headers)

print(f'found {len(results['results'])} results')

# save results
with open('molowski.json', 'w') as file:
    json.dump(results, file)

# save brand with urls number only
with open('brand_result.json', 'w') as file:
    json.dump(found_brand_with_urls_num, file)