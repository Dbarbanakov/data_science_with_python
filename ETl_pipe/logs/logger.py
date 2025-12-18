from datetime import datetime


log_file = "logs/dealership_logfile.txt"


def log_event(message):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"{ts} - {message}\n")
