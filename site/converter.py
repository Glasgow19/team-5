import pandas as pd
import json
import numpy as np
import random

# READ THE EXCEL FILE
df = pd.read_excel("db.xlsx")

# COLUMNS TO REMOVE
cols=["Alternative exhibit names","Visitor experience","Visitor interaction tips",
"Good to know","On floor?","Photo location","Photo 1 filename","Photo 1 link",
"Photo 2 filename","Photo 2 link"]

# DROP THE COLUMNS
df.drop(cols, axis=1, inplace=True)

#DONT CHANGE THESE
df = df.replace(np.nan, '', regex=True)
df.insert(0, 'id', range(0, 0 + len(df)))
df["links"] = "https://www.glasgowsciencecentre.org/"
df["HOH"] = [random.choice([True, False]) for k in df.index] # HARD OF HEARING
df["HOS"] = [random.choice([True, False]) for k in df.index] # HARD OF SIGHT
df["HOM"] = [random.choice([True, False]) for k in df.index] # HARD OF MOBILITY
d = df.to_dict(orient='records')

# DUMP to FILE
with open('db.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=4)
