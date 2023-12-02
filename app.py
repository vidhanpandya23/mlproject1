from src.genericml.logger import logging
from src.genericml.exception import CustomException
from src.genericml.components.data_ingestion import DataIngestion
from src.genericml.components.data_ingestion import DataIngestionConfig
from src.genericml.components.data_transformation import DataTransformationConfig, DataTransformation


import sys


if __name__=="__main__":
    logging.info("The execution has started")
 
    try:
        # data_ingestion =DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        # data_transformation_config=DataIngestionConfig()
        data_transformation =DataTransformation()
        data_transformation.initiate_data_transformation(train_data_path,test_data_path)

    except Exception as e:
        raise CustomException(e,sys)