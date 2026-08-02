import csv
from datetime import datetime, timezone
from pathlib import Path

LOG_PATH = Path(__file__).resolve().parent / "logs" / "test_log.csv"
FIELDS = ["timestamp", "input_name", "platform", "variant",
          "url", "http_status", "state", "found"]


def save_results(input_name: str, results: list) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    first_time = not LOG_PATH.exists()

    with open(LOG_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if first_time:
            writer.writeheader()

        timestamp = datetime.now(timezone.utc).isoformat()
        for r in results:
            writer.writerow({
                "timestamp": timestamp,
                "input_name": input_name,
                "platform": r["platform"],
                "variant": r["variant"],
                "url": r["url"],
                "http_status": r["http_status"],
                "state": r["state"],
                "found": r["found"],
            })