from src.core import *
from logs.logger import log_event
from utils.utils import transform

if __name__ == "__main__":
    data_dir = Path.cwd() / "data"
    target_file = data_dir / "transformed_data.csv"

    log_event("ETL Job Started")

    log_event("Extract phase Started")
    df = extract_all(data_dir)
    log_event("Extract phase Ended")

    log_event("Transform phase Started")
    df = transform(df)
    log_event("Transform phase Ended")

    log_event("Load phase Started")
    df.to_csv(target_file, index=False)
    log_event("Load phase Ended")

    log_event("ETL Job Ended")
    print(df)
