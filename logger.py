import csv
from datetime import datetime, timezone
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parent / "logs"
TEST_LOG_PATH = LOG_DIR / "test_log.csv"
FAILURES_LOG_PATH = LOG_DIR / "failures.csv"

TEST_LOG_FIELDS = ["timestamp", "input_name", "platform", "variant", "url", "http_status", "state", "found", "attempts"]
FAILURES_FIELDS = ["timestamp", "input_name", "platform", "variant", "url", "attempts", "error"]


def _write_rows(path: Path, fields: list, rows: list) -> None:
    if not rows:
        return

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    first_time = not path.exists()

    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        if first_time:
            writer.writeheader()
        for row in rows:
            writer.writerow(row)


def save_results(input_name: str, results: list) -> None:
    timestamp = datetime.now(timezone.utc).isoformat()

    success_rows = []
    failure_rows = []

    for r in results:
        if r.get("error"):
            failure_rows.append({
                "timestamp": timestamp,
                "input_name": input_name,
                "platform": r["platform"],
                "variant": r["variant"],
                "url": r["url"],
                "attempts": r["attempts"],
                "error": r["error"],
            })
        else:
            success_rows.append({
                "timestamp": timestamp,
                "input_name": input_name,
                "platform": r["platform"],
                "variant": r["variant"],
                "url": r["url"],
                "http_status": r["http_status"],
                "state": r["state"],
                "found": r["found"],
                "attempts": r["attempts"],
            })

    _write_rows(TEST_LOG_PATH, TEST_LOG_FIELDS, success_rows)
    _write_rows(FAILURES_LOG_PATH, FAILURES_FIELDS, failure_rows)