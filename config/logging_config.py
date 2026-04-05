import logging
import os
from datetime import datetime

LOG_FOLDER = "logs"
log_file = os.path.join(LOG_FOLDER, f"app_{datetime.now().strftime('%Y%m%d')}.log")

# configure the logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info("Logging initialized")