import os

from dotenv import load_dotenv
from web3 import Web3

load_dotenv()

provider_url = os.getenv("RPC_URL")

w3 = Web3(Web3.HTTPProvider(provider_url))

# 测试网络联通状态
w3.is_connected()

# 获取最新区块高度
latest_block = w3.eth.get_block("latest")
print(latest_block.number)

# 账户地址和私钥（仅示例，不要在实际场景中使用）
from_address = os.getenv("from_address")
to_address = os.getenv("to_address")
private_key = os.getenv("private_key")

# 判断地址是否合法
is_addr = w3.is_address(from_address)
print(is_addr)

# 获取地址余额wei
wallet = w3.to_checksum_address(from_address)
balance = w3.eth.get_balance(wallet)
print(balance)

# 获取地址余额
wei = w3.from_wei(balance, "ether")
print(wei)

# 获取私钥账户
from_addr = w3.to_checksum_address(from_address)
# 转账
to_addr = w3.to_checksum_address(to_address)
# 设置转账金额
value = w3.to_wei(0.1, "ether")
# 获取最新的 nonce 值
nonce = w3.eth.get_transaction_count(from_addr)

# 设置交易参数
transaction = {
    "nonce": nonce,
    "to": to_addr,
    "value": value,
    "gas": 21000,
    "gasPrice": w3.eth.gas_price,
    "chainId": 1513,  # 1 代表以太坊主网 1513 story测试网
}

# 使用私钥签名交易
signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
# 发送交易
txn_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)

# 打印交易哈希
print(f"Transaction sent with hash: {txn_hash.hex()}")
