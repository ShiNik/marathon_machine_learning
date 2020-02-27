import data
import pandas as pd
import sklearn
import os


def data_clean_up(df):
    # drop columns: Time, Pace
    # drop row if empty cell :.isnull() , Id, Age, Rank,Year
    # Sex or Name isnull(), try to fill it otherwise drop the row
    # If one Id links to 2 names, drop one if one group smaller than another, otherwise drop both
    # If one Name links to 2 Ids, drop one  if one group smaller than another, otherwise drop both
    # group by Id, group by year, if a group has count more than one, drop both row
    # group by Id then group by Sex, if more than one group, modify the sex type of small group to the biggest type
    # group by Id, sort by year, sort by age, compare the to list fix the year is less than 505 are not matched

    return

def pre_processing(df):
    # pre-processing:
    #create a map of Id to Name
    # drop Name
    #convert sex to numeric value
    return

def main():
    data_path = os.path.join(os.getcwd(), "data\\marathon_2016.csv")
    df = pd.read_csv(data_path)
    data_clean_up(df)
    pre_processing(df)

main()