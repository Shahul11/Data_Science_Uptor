import  pandas as pd
from sklearn.preprocessing import  OneHotEncoder


df = pd.read_csv("diamonds.csv")
print(df)

# one_hot_encoder =  OneHotEncoder(sparse_output=False)
# encoder_data =  one_hot_encoder.fit_transform(df[['cut']])
# print(encoder_data)
# print(df)
#
#
# """Newly generated dataframe with new columns and their appropraite names"""
# encoded_df = pd.DataFrame(encoder_data, columns=one_hot_encoder.get_feature_names_out())
# print(encoded_df)


# """One Hot Encoding for multiple categorical columns"""
# one_hot_encoder = OneHotEncoder(sparse_output=False)
# encoder_data = one_hot_encoder.fit_transform(df[['cut','color']])
# print(encoder_data)
#
#
#
# """Newly Generated dataframe with new columns and their appropriate names"""
# encoded_df = pd.DataFrame(encoder_data,columns=one_hot_encoder.get_feature_names_out())
# print(encoded_df)
#
# """Joining (Concatenationg) the DF to the encoded DF, that we get to view them all together
# This display the cut column also"""
#
# final_df = pd.concat([df, encoded_df], axis=1)
# print(final_df)


one_hot_encoder =  OneHotEncoder(sparse_output=False)
encoder_data =  one_hot_encoder.fit_transform(df[['cut','color']])
encoded_df = pd.DataFrame(encoder_data,columns=one_hot_encoder.get_feature_names_out())
print(encoder_data)
print(encoded_df)
print(df['color'].nunique())
print(df['cut'].nunique())
print("====================")
print(df['color'].unique())
print(df['cut'].unique())