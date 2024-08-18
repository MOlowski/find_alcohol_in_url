import pandas as pd

df = pd.read_csv('alcohol_reviews.csv')
df = df[['brand','name']]

alcohols = df.drop_duplicates(subset='brand')
alcohols = alcohols.astype(str).apply(lambda col: col.str.lower())

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

def check_category(text, cats):
    for cat in cats:
        if cat in text:
            return cat
    return 'other'

alcohols['category'] = alcohols.apply(lambda row: check_category(row['name'], categories), axis=1)
alcohols['name'] = alcohols['name'].apply(lambda row: ' '.join(row.split()[:3]) if len(row.split()) >=3 else row)

to_replace = {
    '.': '',
    '"': '',
    '&': '',
    ',': '',
    ' ': '-',
    '174':''
}

for old, new in to_replace.items():
    alcohols['brand'] = alcohols['brand'].str.replace(old, new, regex=False)
    alcohols['name'] = alcohols['name'].str.replace(old, new, regex=False)

alcohols.to_csv('alcohols.csv')