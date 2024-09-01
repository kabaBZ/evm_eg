import json
from eth_account import Account


def create_wallets(num_wallets):
    wallets = []
    for _ in range(num_wallets):
        account = Account.create()
        private_key = account.key.hex()
        address = account.address
        wallet = {"index": _ + 1, "private_key": private_key, "address": address}
        wallets.append(wallet)
    return wallets


num_wallets = int(input("请输入要创建的钱包数量："))
wallets = create_wallets(num_wallets)

file_name = "wallets.json"
with open(file_name, "w") as file:
    json.dump(wallets, file, indent=4)
print(f"钱包信息已保存到文件：{file_name}")
