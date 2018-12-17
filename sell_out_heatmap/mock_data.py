import pandas as pd
import numpy as np
import json
import codecs

# python -c 'from data_clean_util import *; get_dataframes_re()'
# python -c 'import numpy as np; l = np.array([131, 3226, 62, 186]); print(l/l.sum()*100); print(l/l.sum()*100-100);'
# REFERENCES: https://github.com/keras-team/keras/issues/741
def get_companies_data():
    df = pd.read_csv('data.csv')
    NUM_POINTS = df.shape[0]
    AVERAGE_SALE_PRICE = 350000
    SD_SALE_PRICE = 100000
    sales_opportunities = np.random.normal(AVERAGE_SALE_PRICE, SD_SALE_PRICE, NUM_POINTS)
    df['value'] = pd.Series(sales_opportunities)
    df.to_csv('processed/data.csv')
    sales_to_geojson(df)

def sales_to_geojson(df):
    dic = {
        "type": "FeatureCollection",
        "features": None
    }

    features = []
    for index, row in df.iterrows():
        feature = {
            "type": "Feature",
            "geometry": { "type": "Point", "coordinates": [row.long, row.lat] },
            "properties": { "company": row.company, "value": row.value}
        }
        features.append(feature)

    dic['features'] = features
    json_str = json.dumps(dic)
    with codecs.open(filename='processed/data.geojson',mode='w',encoding='utf8') as f:
        f.write(json_str)
    

get_companies_data()
#renderer.field = "num_units";

#// ['#f0f9e8','#bae4bc','#7bccc4','#43a2ca','#0868ac']
#// ['#f0f9e8','#bae4bc','#7bccc4','#43a2ca','#0868ac']
#https://s3.us-east-2.amazonaws.com/bizubox-playground/data.csv
