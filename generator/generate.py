import csv
import random
import os
import sys

NUM_ROWS = 50


COLUMNS = ["flight", "destination", "airline", "price"]

def generate_row():

    return {
        "flight": random.randint(100, 150),
        "destination": random.choice(["Dubai", "Istanbul", "Doha", "Male", "Antalya", "Abu Dhabi", "Bodrum", "Izmir"]),
        "airline": random.choice(["Aeroflot", "Emirates", "Turkish Airlines", "Ural Airlines", "S7", "Air Arabia"]),
        "price": random.randint(7000, 30000),
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)