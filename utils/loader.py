import yaml
from .logger import logger, log_exception


def load_params(path):
    """
    Load parameters from the given YAML file.
    """
    try:
        with open(path, 'r') as file:
            params = yaml.safe_load(file)
        return params
    except Exception as e:
        log_exception()
        logger.warning("Unable to load params.yaml file")
        exit()