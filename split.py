import pandas as pd
import csv
from tamil import utf8
df= pd.read_csv('/home/nagul/Documents/venmurasu-season-1/chpt5.csv')
def count_letters():
    f= open("dummy5.csv","w")
    csvwriter = csv.writer(f) 
    for index, row in df.iterrows():
        letters = utf8.get_letters(row['வார்த்தைகள்'])
        letter_count = utf8.get_letters_length( row['வார்த்தைகள்'] )
        letters.insert(0,letter_count)
        print(letters)
        csvwriter.writerow(letters)
if __name__ == "__main__":

    # most_freq()
    count_letters()