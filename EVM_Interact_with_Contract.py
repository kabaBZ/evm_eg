import os

from dotenv import load_dotenv
from web3 import Web3

load_dotenv()

# story测试网rpc
provider_url = os.getenv("RPC_URL")

# 账户地址和私钥（仅示例，不要在实际场景中使用）
from_address = os.getenv("from_address")
private_key = os.getenv("private_key")

web3 = Web3(Web3.HTTPProvider(provider_url))

# 合约地址
contract_address = "0xFaa402A8bc7C88D252cd4Bc64C154fcB8031d015"  # Story NFT 合约地址

# 合约 ABI（这是一个示例 ABI，实际使用时需要用你的合约的 ABI）
contract_abi = [
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "storyProtocolGateway",
                "type": "address",
            },
            {"internalType": "address", "name": "licenseRegistry", "type": "address"},
            {"internalType": "address", "name": "pilTemplate", "type": "address"},
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {"inputs": [], "name": "ECDSAInvalidSignaTrue", "type": "error"},
    {
        "inputs": [{"internalType": "uint256", "name": "length", "type": "uint256"}],
        "name": "ECDSAInvalidSignaTrueLength",
        "type": "error",
    },
    {
        "inputs": [{"internalType": "bytes32", "name": "s", "type": "bytes32"}],
        "name": "ECDSAInvalidSignaTrueS",
        "type": "error",
    },
    {"inputs": [], "name": "EnforcedPause", "type": "error"},
    {"inputs": [], "name": "ExpectedPause", "type": "error"},
    {
        "inputs": [{"internalType": "address", "name": "owner", "type": "address"}],
        "name": "OwnableInvalidOwner",
        "type": "error",
    },
    {
        "inputs": [{"internalType": "address", "name": "account", "type": "address"}],
        "name": "OwnableUnauthorizedAccount",
        "type": "error",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "ip",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256",
            },
        ],
        "name": "Minted",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newOwner",
                "type": "address",
            },
        ],
        "name": "OwnershipTransferred",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "account",
                "type": "address",
            }
        ],
        "name": "Paused",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": False, "internalType": "bool", "name": "flag", "type": "bool"}
        ],
        "name": "SignaTrueCheckFlipped",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "account",
                "type": "address",
            }
        ],
        "name": "Unpaused",
        "type": "event",
    },
    {
        "inputs": [],
        "name": "LICENSE_REGISTRY",
        "outputs": [
            {"internalType": "contract ILicenseRegistry", "name": "", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "PIL_TEMPLATE",
        "outputs": [
            {
                "internalType": "contract IPILicenseTemplate",
                "name": "",
                "type": "address",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "SPG",
        "outputs": [
            {
                "internalType": "contract IStoryProtocolGateway",
                "name": "",
                "type": "address",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "deriativeIPMetadataHash",
        "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "derivativeIPMetadataURI",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "bool", "name": "flag", "type": "bool"}],
        "name": "flipSkipSignaTrueCheck",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "addressToCheck", "type": "address"}
        ],
        "name": "getHasMinted",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "string", "name": "twHash", "type": "string"}],
        "name": "getIsTwitterHashUsed",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "addressToCheck", "type": "address"}
        ],
        "name": "getMintedTokenId",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getNFTContract",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getParentIpId",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getParentLicenseTermsId",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getParentTokenId",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getSkipSignaTrueCheck",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "hasMinted",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "bytes", "name": "signaTrue", "type": "bytes"},
            {"internalType": "string", "name": "twHash", "type": "string"},
        ],
        "name": "mintNFTGated",
        "outputs": [
            {"internalType": "address", "name": "ipId", "type": "address"},
            {"internalType": "uint256", "name": "tokenId", "type": "uint256"},
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "mintedUserToTokenId",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "nftContract",
        "outputs": [
            {"internalType": "contract ISPGNFT", "name": "", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "pause",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "paused",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "string", "name": "metadataURI", "type": "string"},
            {"internalType": "bytes32", "name": "metadataHash", "type": "bytes32"},
        ],
        "name": "setDerivativeIPMetadata",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "_signer", "type": "address"}],
        "name": "setSignerAddress",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "signer",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "newOwner", "type": "address"}],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "unpause",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "string", "name": "", "type": "string"}],
        "name": "usedTwHashes",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
]

# 创建合约实例
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# # 调用合约中的函数读取状态变量
# variable_value = contract.functions.mintNFTGated().call()

# print(f"The value of myVariable is: {variable_value}")


# 构建交易
## 构建合约交互参数
twHash = "0x0000000000000000000000000000000000000000000000000000000000000000"
bytes = b""
print(f"gas:{web3.eth.gas_price}")
## 交易计数flag
nonce = web3.eth.get_transaction_count(web3.to_checksum_address(from_address))
print(f"nonce:{nonce}")

# # type0 交易参数
# transaction = {
#     "chainId": 1513,  # 1 为以太坊主网
#     "gas": 1361328,
#     "gasPrice": web3.eth.gas_price,  # web3.to_wei("734", "gwei"),
#     "nonce": nonce,
# }

# type2 交易参数（EIP-1559）
transaction = {
    "chainId": 1513,  # 1 为以太坊主网
    "type": "0x02",
    "from": web3.to_checksum_address(from_address),
    # "to": web3.to_checksum_address(contract_address),
    "value": web3.to_wei(0, "ether"),
    "gas": 1361328,
    "maxFeePerGas": web3.to_wei(
        "734", "gwei"
    ),  # 愿意为交易支付的每单位 gas 的最高费用。它包含了 Base Fee 和 Priority Fee（小费）之和。
    "maxPriorityFeePerGas": web3.to_wei(
        "734", "gwei"
    ),  #  这是给矿工的小费，用于激励矿工优先处理你的交易。通常在网络拥堵时，可以提高这个值以更快地处理交易
    "nonce": nonce,
}
transaction = contract.functions.mintNFTGated(bytes, twHash).build_transaction(
    transaction
)

# 签名交易
signed_txn = web3.eth.account.sign_transaction(transaction, private_key)

# 发送交易
txn_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)

# 打印交易哈希
print(f"Transaction sent with hash: {txn_hash.hex()}")

# 等待交易确认
txn_receipt = web3.eth.wait_for_transaction_receipt(txn_hash)
print(f"Transaction receipt: {txn_receipt}")
