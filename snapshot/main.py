import csv
import json
import os
from functools import reduce

from snapshot.application.service.balance_service import BalanceService


def main():
    main_func()
    # test_func()


def main_func():
    balance_service = BalanceService()
    folder_path = os.path.join(os.getcwd(), "files")

    for filename in os.listdir(folder_path):
        with open(os.path.join(folder_path, filename), 'r') as f:
            if filename.endswith(".csv"):
                reader = list(map(dict, csv.DictReader(f)))

            elif filename.endswith(".json"):
                reader = json.load(f)
            else:
                continue
        balance_service.save_to_db(reader, filename)


def test_func():
    with open('old_files/cardano_lp_minswap_20240610.csv', 'r') as f:
        reader = list(map(dict, csv.DictReader(f)))

    index = 0
    for row in reader:
        print(f"{row['payment_address']}, {row['amount_agix']}, {row['stake_address']}")
        index += 1
        if index == 100:
            break

    with open('old_files/cardano_staking_20240610.json', 'r') as f:
        reader = json.load(f)

    index = 0
    for row in reader:
        print(f"{row['address']}, {row['balance']}, {row['stake_key']}")
        index += 1
        if index == 100:
            break

if __name__ == "__main__":
    main()
