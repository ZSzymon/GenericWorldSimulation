import os

from userConfig import Config

PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
CONFIG_DIR = os.path.join(PROJECT_DIR, "config")

config = Config.configFromFile()