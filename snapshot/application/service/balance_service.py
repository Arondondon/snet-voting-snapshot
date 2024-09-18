from snapshot.config import FILE_FIELD_NAMES, DECIMALS
from snapshot.infrastructure.repository.balance_snapshot_repo import BalanceSnapshotRepository


class CSVSave:
    index = 0
    file_name = "../../balances.csv"

    @classmethod
    def save(cls, network, address, balance):
        with open(cls.file_name, "a") as f:
            f.write(f"{cls.index},{network},{address},{balance}\n")
        cls.index += 1


class BalanceService:
    def __init__(self):
        self.id = 0
        self.repo = BalanceSnapshotRepository()
        # print("id, network, address, stake_key, balance, stake")

    def save_to_db(self, user_balance_list, file_name):
        print(file_name)

        if file_name.startswith("cardano_balances"):
            user_balance_list = user_balance_list["data"]["items"]

        file_name_parts = file_name.split("_")
        field_names = FILE_FIELD_NAMES["_".join(file_name_parts[:2])]


        index = 0
        for user_balance in user_balance_list:
            # if index == 10:
            #     break

            address = user_balance[field_names["address"]].strip()
            if file_name_parts[1] == "staking":
                stake = str(user_balance[field_names["balance"]])
                balance = str(0)
            else:
                balance = str(user_balance[field_names["balance"]])
                stake = str(0)
            stake_key = user_balance[field_names["stake_key"]] if "stake_key" in field_names else None
            if file_name_parts[0] == "ethereum":
                network = "Ethereum"
            elif file_name_parts[0] == "cardano":
                network = "Cardano"
            elif file_name_parts[0] == "binance":
                network = "Binance"
            else:
                network = "UNKNOWN"

            balance = self.convert_balance(balance, network)
            stake = self.convert_balance(stake, network)
            # print(f"{self.id}, {network}, {address}, {stake_key}, {balance}, {stake}")
            self.repo.add_user_balance(network, address, balance, stake, stake_key)

            # index += 1
            self.id += 1

        # print()

    def convert_balance(self, balance_str: str, network: str) -> int:
        if balance_str.find(",") != -1:
            return self.convert_ethereum_balance(balance_str, network)

        if balance_str.find(".") != -1:
            return int(float(balance_str))

        return int(balance_str)

    def convert_ethereum_balance(self, balance, network: str) -> int:
        decimals = DECIMALS["FET"][network]
        integer, _, decimal = balance.partition(".")
        return int(integer.replace(",", "")) * 10 ** decimals + int(decimal + ("0" * (decimals - len(decimal))))

