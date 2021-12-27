import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

class SessionConfig:
    DATA_DIR = os.path.join(BASE_DIR, 'ballapp3', 'session', 'data')
    TEMPLATE_FILE = os.path.join(DATA_DIR, 'data.template')


class Config:
    pass

class JsonStorageConfig:
    GITHUB_URL = "https://github.com/jimdevops19/ballapp3"

