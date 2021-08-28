import pandas as pd 
from pprint import pprint

def get_data():
    
    df= pd.read_csv('mostfreq.csv')

    # df = df[30]

    # print(df)
    Row_list =[]
  
# Iterate over each row
    for rows in df.itertuples():
        # Create list for the current row
        my_list =[rows.வார்த்தைகள், rows.எண்ணிக்கை]
        
        # append the list to the final list
        Row_list.append(my_list)
    
    # Print the list
    pprint(Row_list)    


if __name__ == "__main__":
    get_data()