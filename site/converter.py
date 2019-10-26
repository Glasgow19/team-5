import pandas as pd
import json

# READ THE EXCEL FILE
df = pd.read_excel("db.xlsx")
# COLUMNS TO REMOVE
cols=["Alternative exhibit names","Visitor experience","Visitor interaction tips",
"Good to know","On floor?","Photo location","Photo 1 filename","Photo 1 link",
"Photo 2 filename","Photo 2 link"]
# DROP THE COLUMNS
df.drop(cols, axis=1, inplace=True)

d = df.to_dict(orient='records')
# DUMP TO FILE
with open('db.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=4)
