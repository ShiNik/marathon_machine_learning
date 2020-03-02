# User define import
from my_package import config
from my_package import data_cleanup

# python import
import pandas as pd
import os



def pre_processing(df):
    # pre-processing:
    #create a map of Id to Name
    # drop Name
    #convert sex to numeric value
    return

def main():
    data_path = os.path.join(os.getcwd(), "data\\marathon_2016.csv")
    df = pd.read_csv(data_path)
    half_marathon, full_marathon = data_cleanup.perform_cleanup(df, config.dataset_threshold)
    pre_processing(df)

main()