import logging
import shutil
from pathlib import Path


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


build_dirs = ["./dist", "./build", "*.egg-info", "./*.pyd"]

for folder in build_dirs:
    rm_files = Path().glob(folder)
    for f in rm_files:
        logger.info(f"removing {f}")
        if f.exists() and f.is_file():
            f.unlink()
        if f.exists() and f.is_dir():
            shutil.rmtree(f)

