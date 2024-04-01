from text_summarizer.config.configuration import ConfigurationManager
from text_summarizer.components.model_evaluation import ModelEvaluation
from text_summarizer.logging import logger
import zipfile

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self, load_pre_trained: bool = False):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        if not load_pre_trained:
            model_trainer = ModelEvaluation(config=model_trainer_config)
            model_trainer.evaluate()

