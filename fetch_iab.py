import pandas as pd

data = {
    'arts & entertainment': 'IAB1',
    'automotive': 'IAB2',
    'business': 'IAB3',
    'careers': 'IAB4',
    'education': 'IAB5',
    'family & parenting': 'IAB6',
    'health & fitness': 'IAB7',
    'food & drink': 'IAB8',
    'hobbies & interests': 'IAB9',
    'home & garden': 'IAB10',
    'law, gov\'t & politics': 'IAB11',
    'news': 'IAB12',
    'personal finance': 'IAB13',
    'society': 'IAB14',
    'science': 'IAB15',
    'pets': 'IAB16',
    'sports': 'IAB17',
    'style & fashion': 'IAB18',
    'technology & computing': 'IAB19',
    'travel': 'IAB20',
    'real estate': 'IAB21',
    'shopping': 'IAB22',
    'religion & spirituality': 'IAB23',
    'uncategorized': 'IAB24',
    'non-standard content': 'IAB25',
    'illegal content': 'IAB26'
}
def fetch_iab_taxonomy_code(input_str):
    result = []
    input_list = input_str.split(',')
    
    for item in input_list:
        item = item.strip()
        matched_keys = [key for key in data.keys() if item in key]
        
        if matched_keys:
            result.extend(data[key] for key in matched_keys)
    
    return result
# Example data_dict
data_dict = {'arts and entertainment': 'value1', 'sports': 'value2', 'technology': 'value3'}
input_string = 'entertainment,technology'

cat_list = ['entertainment,technology','news,xxx','travel']
pixalate_df = pd.DataFrame(cat_list,columns =['appStoreCategories_new'])
pixalate_df['IAB_Code'] = pixalate_df.apply(lambda x:fetch_iab_taxonomy_code(x['appStoreCategories_new'].lower()),axis=1)
print(pixalate_df)


