import sys
from src.logging import logging
from src.exception import DLClassifierException
from src.pipeline.dataingestion_pipeline import DataIngestionTrainingPipeline
from src.pipeline.prepare_base_model import PrepareBaseModelTrainingPipeline
from src.pipeline.training_pipeline import ModelTrainingPipeline
from src.pipeline.evaluation_pipeline import EvaluationPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logging.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.error(e)
    raise DLClassifierException(e, sys)

STAGE_NAME = "Prepare Base Model"
try:
    logging.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logging.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.error(e)
    raise DLClassifierException(e, sys)

STAGE_NAME = "Training"
try:
    logging.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logging.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.error(e)
    raise DLClassifierException(e, sys)


STAGE_NAME = "Evaluation"
try:
    logging.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    model_eval = EvaluationPipeline()
    model_eval.main()
    logging.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.error(e)
    raise DLClassifierException(e, sys)