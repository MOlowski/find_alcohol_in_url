import pandas as pd

# get alcohol reviews
df = pd.read_csv('alcohol_reviews.csv')
df = df[['brand','name']]

# get brand only once
alcohols = df.drop_duplicates(subset='brand')
alcohols = alcohols.astype(str).apply(lambda col: col.str.lower())

# alcohol categories
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
# add columns category and name
alcohols['category'] = alcohols.apply(lambda row: check_category(row['name'], categories), axis=1)
alcohols['name'] = alcohols['name'].apply(lambda row: ' '.join(row.split()[:3]) if len(row.split()) >=3 else row)

# replace stopwords, etc. 
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

# save alcohol brands
alcohols.to_csv('alcohols.csv')