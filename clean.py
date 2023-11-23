import logging
import shutil
from pathlib import Path


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


build_dirs = ["dist", "build", "*.egg-info"]

for folder in build_dirs:
    if Path(folder).exists() and Path(folder).is_dir():
        shutil.rmtree(folder)

