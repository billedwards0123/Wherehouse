import csv
import json
from pathlib import Path

CSV_FILE = Path('pam_reference_inventory.csv')
JSON_FILE = Path('inventory.json')

def main():
    items = []
    with CSV_FILE.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row.get('Item', '').strip()
            if not name:
                continue
            location = row.get('Location', '').strip() or 'N/A'
            try:
                qty = int(float(row.get('Par_Min', '0') or 0))
            except ValueError:
                qty = 0
            try:
                par = int(float(row.get('Par_Max', '0') or 0))
            except ValueError:
                par = 0
            items.append({
                'name': name,
                'location': location,
                'quantity': qty,
                'par_level': par,
            })
    with JSON_FILE.open('w', encoding='utf-8') as f:
        json.dump(items, f, indent=2)
    print(f"Wrote {len(items)} items to {JSON_FILE}")

if __name__ == '__main__':
    main()
