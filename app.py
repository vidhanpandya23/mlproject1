from src.genericml.logger import logging
from src.genericml.exception import CustomException
from src.genericml.components.data_ingestion import DataIngestion
from src.genericml.components.data_ingestion import DataIngestionConfig
from src.genericml.components.data_transformation import DataTransformationConfig, DataTransformation
from src.genericml.components.model_trainer import ModelTrainerConfig, ModelTrainer

import sys


if __name__=="__main__":
    logging.info("The execution has started")
 
    try:
        # data_ingestion =DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        # data_transformation_config=DataIngestionConfig()
        data_transformation =DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)

        ## Model Training

        model_trainer =ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr,test_arr))

    except Exception as e:
        raise CustomException(e,sys)