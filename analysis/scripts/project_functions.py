import pandas as pd

def load_and_process(path):
    
    data_1 = ( #Read data in
        pd.read_csv(path)
    )
    
    data_1['Event_gender'].replace({"X" : "M/W"},inplace = True) #Replace 'X' values with 'M/W'

    data_2 = ( #Drop empty values, Reset index, Write processed data
        data_1
        .dropna()
        .reset_index()
        .drop('index', axis=1)
        .replace()
    )
    data_2.to_csv('../data/processed/data.csv') #Testing to see if the data is cleaned up
    return data_2

def rem_columns(df):
    df = df.copy().drop(['Discipline', 'Event', 'Athlete', 'Gender','Country_Code','Event_gender'], axis=1)
    return df

def country_medal(df):
    df = df.groupby(["Country"])["Medal"].count().reset_index(name="Count").sort_values(by='Count',ascending=False).reset_index()
    return df

def country_medal_year(df):
    df = df.groupby(["Country","Year"])["Medal"].count().reset_index(name="Count").sort_values(by='Count',ascending=False).reset_index()
    return df

def add_medalpts(df):
    df['Medal_Points'] = df['Medal'].replace({'Gold':4, 'Silver':2, 'Bronze':1})
   