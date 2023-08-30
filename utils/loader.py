import logging

from environs import Env
import os
import inspect


def load_base_configs() -> tuple[Env, logging.Logger]:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    env = Env()
    # Get the directory of the script that called this function
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    caller_file = os.path.dirname(os.path.abspath(module.__file__))

    env_file_path = os.path.join(caller_file, 'parameters.env')

    if os.path.exists(env_file_path):
        env.read_env(env_file_path)

    return env, logger
