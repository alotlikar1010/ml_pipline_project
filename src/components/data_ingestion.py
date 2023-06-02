import os, sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join("artifacts","train.csv")
    test_data_path = os.path.join("artifacts","test.csv")
    raw_data_path = os.path.join("artifacts","raw.csv")


class DataIngestion:
    #create constructor
    def __init__(self):
    # calling Dataingestionconfig to create file
        self.ingestion_config = DataIngestionConfig()
    
    # create function
    def initiate_data_ingestion(self):
        try:
            logging.info("Data Ingestion started")
            logging.info("Data Reading Using Pandas library from local server")
            data = pd.read_csv(os.path.join("notebook/data" ,"income_cleandata.csv"))
        # create directory 
                    #for raw data
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("Data Splited into train test split")
              #for train , test data
            train_set ,test_set = train_test_split(data , test_size= .30 , random_state= 42)

            train_set.to_csv(self.ingestion_config.train_data_path , index= False,header = True)
            test_set.to_csv(self.ingestion_config.test_data_path , index= False,header = True)

            logging.info("Data Ingestion Completed")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info("Error Occur in Data ingestion stage")
            raise CustomException(e,sys)


if __name__ =="__main__":
    obj = DataIngestion()
    treain_data_path , test_data_path = obj.initiate_data_ingestion()