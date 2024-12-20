import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
print(f"Log file name: {LOG_FILE}")  

logs_path = os.path.join(os.getcwd(), "logs")
print(f"Logs path: {logs_path}")  
os.makedirs(logs_path, exist_ok=True)  
print("Logs directory created or already exists.")  
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
print(f"Log file full path: {LOG_FILE_PATH}")  

logging.basicConfig(
    filename=LOG_FILE_PATH,  
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,  
)


