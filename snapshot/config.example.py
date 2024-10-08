#
#
# EVENT_ID = 1000
# DATESTAMP = "20231231"
#
# DB_CONFIG = {
#     "DB_DRIVER": "mysql+pymysql",
#     "DB_HOST": "localhost",
#     "DB_USER": "unittest_root",
#     "DB_PASSWORD": "unittest_pwd",
#     "DB_NAME": "token_balances",
#     "DB_PORT": 3306
# }
#
# SNAPSHOT_TABLES = {
#     "BALANCES": f"AGIX_balance_snapshot_{DATESTAMP}",
#     "COLLECTIONS": f"wallets_collections_snapshot_{DATESTAMP}",
#     "ANSWERS": f"voting_answers_snapshot_{DATESTAMP}"
# }
#
# BALANCES_SNAPSHOT = {
#     "ETHEREUM": {
#         "BALANCES_FILE": f"files/ethereum_balances_{DATESTAMP}.csv",
#         "STAKING_FILE": f"files/ethereum_staking_{DATESTAMP}.json",
#         "INFURA": {
#             "URL": "https://mainnet.infura.io/v3/"
#         },
#         "STAKING": {
#             "SNET": {
#                 "CONTRACT": {
#                     "ADDRESS": "",
#                     "ABI": ""
#                 }
#             },
#             "SDAO": {
#                 "CONTRACT": {
#                     "ADDRESS": "",
#                     "ABI": ""
#                 }
#             }
#         }
#     },
#     "CARDANO": {
#         "BALANCES_FILE": f"files/cardano_balances_{DATESTAMP}.json",
#         "STAKING_FILE": f"files/cardano_staking_{DATESTAMP}.json",
#         "DBSYNC": {
#             "ENDPOINT": "",
#             "API_KEY": ""
#         }
#     }
# }
#
# OUT_FILES = {
#     "COLLECTIONS": f"files/collections_{DATESTAMP}.csv",
#     "COLLECTIONS_BALANCES": f"files/collections_balances_{DATESTAMP}.csv",
#     "ANSWERS": f"files/answers_{DATESTAMP}.csv"
# }




EVENT_ID = 1000
DATESTAMP = "20240919"
# TODO: fill the correct event id and datestamp

DB_CONFIG = {
    "DB_DRIVER": "mysql+pymysql",
    "DB_HOST": "localhost",
    "DB_USER": "unittest_root",
    "DB_PASSWORD": "unittest_pwd",
    "DB_NAME": "token_balances",
    "DB_PORT": 3306
}

SNAPSHOT_TABLES = {
    "BALANCES": f"FET_balance_snapshot_{DATESTAMP}",
}

original_fields_names = ["address", "balance"]
FILE_FIELD_NAMES = {
    "cardano_balances": dict(zip(original_fields_names + ["stake_key"], original_fields_names + ["stake_key"])),
    "ethereum_balances": dict(zip(original_fields_names, original_fields_names)),
    "binance_balances": dict(zip(original_fields_names, original_fields_names)),
    "ethereum_lp": dict(zip(original_fields_names, ["address", "token0"])),
    "binance_lp": dict(zip(original_fields_names, ["address", "token0"])),
    "cardano_lp": dict(zip(original_fields_names + ["stake_key"], ["BaseAddress", "Amount", "StakeAddress"])),
    # "ethereum_staking": dict(zip(original_fields_names, ["address", "balance"])),
    # "cardano_staking": dict(zip(original_fields_names + ["stake_key"], original_fields_names + ["stake_key"])),
}

DECIMALS = {
    "FET": {
        "Ethereum": 18,
        "Cardano": 8,
        "Binance": 18
    },
    "AGIX": {
        "Ethereum": 8,
        "Cardano": 8,
        "Binance": 8
    }
}

BATCH_SIZE = 5000
