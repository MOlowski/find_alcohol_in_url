import requests
import json

# parse request if url was found 
def result_parse(result, brand, payload, matched):

    urls_num = 0
    is_url = False
    found_alc = []
    found_brand = []
    
    for source_num in range((len(result['sources']))):
        source = 'source{}'.format(source_num+1)
        if len(result['sources'][source]['urls']) > 0:
            urls_num += result['sources'][source]['quantity']
            is_url = True
    
    # if url was found save payload with brand name
    if is_url:
        alcohol = {
            "alcohol_id": payload['required'][0]['keyword'],
            "payload" : payload
        }
        matched += 1
        found_alc.append(alcohol)
        
        #save only brands and num of matched results
        brands = {
            "brand": brand,
            "urls_num": urls_num
        }
        found_brand.append(brands)

    return found_alc, found_brand, matched

# function sending request
def find_urls(df, categories, url, headers):

    # number of matched brands names
    matched_results = 0
    found = {'results':[]}
    found_brands_with_url_num = []

    for index, row in df.iterrows():
        payload = {
            'required':[],
            'optional':[],
            'optionalThreshold':0
        }

        # add brand name as required to payload 
        brand_value = row['brand'] if isinstance(row['brand'], str) else ''
        brand_splitted = brand_value.split('-')

        for brand in brand_splitted:
            if "'" in brand:
                before_quote = brand.split("'")[0]
                brand = before_quote
            if brand != 'co.' and brand != 'inc.':
                payload['required'].append({
                    'keyword': brand,
                    'mode': 'c'
                })
        
        # add name of alcohol as optional to payload
        name_splitted = row['name'].split('-')
        for name in name_splitted:
            payload['optional'].append({
                'keyword': name,
                'mode': 'c'
            })

        # add category as optional to payload
        if row['category'] != 'other':
            payload['optional'].append({
                'keyword': row['category'],
                'mode': 'c'
            })
        else:
            for category in categories:
                payload['optional'].append({
                    'keyword': category,
                    'mode': 'c'
                })
        
        if row['category'] != 'other':
            payload['optionalThreshold'] = 2
        else:
            payload['optionalThreshold'] = 1

        try:
            response = requests.post(
                url,
                data = json.dumps(payload),
                headers = headers,
            )

            found_alc, found_brand, matched_results = result_parse(response.json(), row['brand'], payload, matched_results)
            found['results'].extend(found_alc)
            found_brands_with_url_num.extend(found_brand)
            print(f'found {matched_results} index: {index} of {len(df)}')

        except:
            print('some problem')

    return found, found_brands_with_url_num