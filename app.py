from src.genericml.logger import logging
from src.genericml.exception import CustomException
from src.genericml.components.data_ingestion import DataIngestion
from src.genericml.components.data_ingestion import DataIngestionConfig
import sys


if __name__=="__main__":
    logging.info("The execution has started")

    try:
        # data_ingestion =DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        raise CustomException(e,sys)