import logging
import shutil
from pathlib import Path


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


rm_patterns = ["dist", "build", "*.egg-info", "*.pyd", "*.c"]

for pat in rm_patterns:
    rm_files = Path().rglob(pat)
    for rm_file in rm_files:
        print(f"delete {rm_file}")
        if Path.is_dir(rm_file):
            shutil.rmtree(rm_file)
        else:
            Path.unlink(rm_file)

