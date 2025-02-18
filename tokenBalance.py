from web3 import Web3
import csv

# --- Configuration ---

# Pulsechain RPC endpoint (replace with a valid endpoint if needed)
rpc_url = "https://rpc.pulsechain.com"
web3 = Web3(Web3.HTTPProvider(rpc_url))

if not web3.is_connected():
    raise Exception("Unable to connect to Pulsechain")

# Token contract address (replace with your Pulsechain token's contract address)
token_address = web3.to_checksum_address("0x3ca80d83277e721171284667829c686527B8b3c5")

# Minimal ERC-20 ABI with only the balanceOf function
abi = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "type": "function",
    }
]

# Create contract instance
token_contract = web3.eth.contract(address=token_address, abi=abi)

# Get token decimals
try:
    DECIMALS = token_contract.functions.decimals().call()
except Exception as e:
    DECIMALS = 18  # Default to 18 if decimals() call fails

def format_balance(balance):
    """Convert raw balance to human readable format"""
    return "{:,.4f}".format(balance / (10 ** DECIMALS))

# List of wallet addresses (update with your wallets)
wallets = [
    "0x6D5FC6Ac6e753f68d4F64cc7b605D925Cf642D5e",
    "0xcCC5EEeFbcaD36A29c52Aa73DC1c90DE2AC53bE3",
    "0x04599096e590634f2c33C42D2eDfD15Dd73e043f",
    "0x3fefd06828689252A69207718985B9a78350561F",
    "0x4695ea9D27b98256999ACba2f165bd1E9610bBa9",
    "0xaA3D951A416c807759d66a364748aa590F68B247",
    "0xeAd9AEc78f52aD06B1752f719C106Be10Ec8489B",
    "0x963588d57BfaFeA746dA0D0c71599c4Eb7DB70b2",
    "0x614f16CAf6717400597007B87A7ce1776D7984c1",
   


    # Add more wallets as needed
]

# --- Processing and CSV Export ---
results = []
total_end = 0

for wallet in wallets:
    try:
        wallet_checksum = web3.to_checksum_address(wallet)
        # Fetch current balance
        end_balance = token_contract.functions.balanceOf(wallet_checksum).call()
        
        formatted_balance = format_balance(end_balance)
        results.append((wallet, formatted_balance))
        total_end += end_balance

        print(f"Wallet {wallet}:  Balance={formatted_balance}")
    except Exception as e:
        print(f"Error processing wallet {wallet}: {e}")



# Write results to CSV
csv_filename = "wallet_balances.csv"
with open(csv_filename, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write header row
    csvwriter.writerow(["Wallet", "Token Balance"])
    # Write wallet rows
    for row in results:
        csvwriter.writerow(row)
    # Write totals row
    csvwriter.writerow(["TOTAL", format_balance(total_end)])

print(f"CSV file exported as {csv_filename}")
