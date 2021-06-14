import pandas as pd
import json




def getData(hsn):
    data = pd.read_excel (r'List.xlsx') 
    json_str = data.to_json(orient='records')
    df = pd.DataFrame(data, columns= ['HSN','GST','Name of Commodity'])
    # result = df.to_json(orient="split")
    # json_str = data.to_json(orient='records')
    parsed = json.loads(json_str)
    arr = []
    for i in parsed:
        if str(i['HSN']) == hsn:
            arr.append(i)
 
    return arr

