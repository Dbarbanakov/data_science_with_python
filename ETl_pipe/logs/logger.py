from datetime import datetime


log_file = "logs/dealership_logfile.txt"


def log_event(message, file=log_file):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file, "a") as f:
        f.write(f"{ts} - {message}\n")
