import  pandas as pd
df = pd.read_csv("diamonds.csv")
print(df)

"'Encodes as True and False"
"Sk Learn require to convert to DF and then concatenate"
"""here it happens in one step"""

encoded_df = pd.get_dummies(df['cut'])
print(encoded_df)

final_df = pd.concat([df,encoded_df],axis=1)
print(final_df)

