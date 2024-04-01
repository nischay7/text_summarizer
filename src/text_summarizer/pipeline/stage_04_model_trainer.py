from text_summarizer.config.configuration import ConfigurationManager
from text_summarizer.components.model_trainer import ModelTrainer
from text_summarizer.logging import logger
import zipfile

class ModeltrainerTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self, load_pre_trained: bool = False):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        if not load_pre_trained:
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train()

