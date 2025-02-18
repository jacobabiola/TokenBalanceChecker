# Token Balance Checker for PulseChain


## Token Balance Checker

A Python script that allows you to check ERC-20 token balances for multiple wallet addresses on PulseChain. It exports the results to a CSV file for easy analysis.

### Features

- Checks token balances for multiple wallet addresses
- Connects to PulseChain network
- Exports results to CSV format
- Supports any ERC-20 token on PulseChain

### Prerequisites

- Python 3.7 or higher
- `web3.py` library

### Installation

1. Install the required dependency:
```bash
pip install web3
```

### Configuration

Before running the script, you need to configure the following in `tokenBalance.py`:

1. **Token Contract Address**: Replace the token address with your desired token:
```python
token_address = "0x3ca80d83277e721171284667829c686527B8b3c5"
```

2. **Wallet Addresses**: Add the wallet addresses you want to check in the `wallets` list:
```python
wallets = [
    "0x6D5FC6Ac6e753f68d4F64cc7b605D925Cf642D5e",
    "0xcCC5EEeFbcaD36A29c52Aa73DC1c90DE2AC53bE3",
    # Add more wallets as needed
]
```

3. **Block Numbers** (optional): Modify the block range if needed:
```python
start_block = 21571557
end_block = 22653042
```

### Usage

Run the script using Python:

```bash
python3 tokenBalance.py 
```
OR
```bash
python tokenBalance.py 
```

The script will:
1. Connect to PulseChain
2. Check token balances for each wallet
3. Create a CSV file named `wallet_balances.csv` with the results

### Output

The script generates a CSV file with the following columns:
- Wallet Address
- Token Balance

A total balance is added at the bottom of the CSV file.

### Error Handling

- If a wallet address is invalid or there's an error checking its balance, the error will be printed to the console
- The script will continue processing other addresses even if one fails

### Network Configuration

The script uses PulseChain's RPC endpoint. If needed, you can modify the RPC URL:
```python
rpc_url = "https://rpc.pulsechain.com"
```


## License

This project is open source and available under the MIT License.

--- 
