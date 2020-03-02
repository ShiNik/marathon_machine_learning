import pandas as pd
import numpy as np

def distance_calculation (df):
    df['Time'] = pd.to_datetime(df['Time'])
    df['Pace'] = pd.to_datetime(df['Pace'])
    time = pd.to_timedelta(df['Time'].dt.strftime("%H:%M:%S")).dt.total_seconds().astype(int).to_numpy()
    # convert %H:%M to %M:%S by dividing by 60
    pace = pd.to_timedelta(df['Pace'].dt.strftime("%H:%M:%S")).dt.total_seconds().astype(int).to_numpy()/60
    # In marathon distance compute by miles per minuets therefore we need to
    # convert time and pace from second to minutes
    df['distance'] = time/60 *pace/60

def perform_cleanup(df, threshold):
    # drop columns: Time, Pace
    # drop row if empty cell :.isnull() , Id, Age, Rank,Year
    # Sex or Name isnull(), try to fill it otherwise drop the row
    # If one Id links to 2 names, drop one if one group smaller than another, otherwise drop both
    # If one Name links to 2 Ids, drop one  if one group smaller than another, otherwise drop both
    # group by Id, group by year, if a group has count more than one, drop both row
    # group by Id then group by Sex, if more than one group, modify the sex type of small group to the biggest type
    # group by Id, sort by year, sort by age, compare the to list fix the year is less than 505 are not matched
    distance_calculation(df)
    half_marathon = dict()
    full_marathon = dict()
    df_cleaned = df.drop(columns=['Name', 'Time', 'Pace'])
    df_cleaned.loc[df_cleaned['Sex'] == 'F', 'Sex'] = 0
    df_cleaned.loc[df_cleaned['Sex'] == 'M', 'Sex'] = 1
    df_cleaned.loc[df_cleaned['Sex'] == 'U', 'Sex'] = 2
    full_marathon = df_cleaned[df_cleaned['distance'] >= threshold].reset_index(drop=True)
    half_marathon = df_cleaned[df_cleaned['distance'] < threshold].reset_index(drop=True)
    return half_marathon, full_marathon


