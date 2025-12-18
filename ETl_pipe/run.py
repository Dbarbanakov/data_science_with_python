from src.core import *
from logs.logger import log_event
from utils.utils import transform

if __name__ == "__main__":
    log_event("ETL Job Started")

    log_event("Extract phase Started")
    df = extract_all()
    log_event("Extract phase Ended")

    log_event("Transform phase Started")
    df = transform(df)
    log_event("Transform phase Ended")

    log_event("Load phase Started")
    load_to_csv(df)
    log_event("Load phase Ended")

    log_event("ETL Job Ended")
    print(df)
