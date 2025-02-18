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
    }
]

# Create contract instance
token_contract = web3.eth.contract(address=token_address, abi=abi)

# Define the block range (replace with your block numbers)
start_block = 21571557  # Example: starting block on Pulsechain
end_block = 22653042    # Example: ending block on Pulsechain

# List of wallet addresses (update with your wallets)
wallets = [
    "0x6D5FC6Ac6e753f68d4F64cc7b605D925Cf642D5e",
    "0xcCC5EEeFbcaD36A29c52Aa73DC1c90DE2AC53bE3",
    "0x04599096e590634f2c33C42D2eDfD15Dd73e043f",
    "0x3fefd06828689252A69207718985B9a78350561F",
    # Add more wallets as needed
]

# --- Processing and CSV Export ---
results = []
total_start = 0
total_end = 0

for wallet in wallets:
    try:
        wallet_checksum = web3.to_checksum_address(wallet)
        # Fetch balances at specified blocks using block_identifier
        start_balance = token_contract.functions.balanceOf(wallet_checksum).call(block_identifier=start_block)
        end_balance = token_contract.functions.balanceOf(wallet_checksum).call(block_identifier=end_block)
       

        results.append((wallet, end_balance ))
        total_start += start_balance
        total_end += end_balance

        print(f"Wallet {wallet}:  End={end_balance}")
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
    csvwriter.writerow(["TOTAL", total_end])

print(f"CSV file exported as {csv_filename}")
