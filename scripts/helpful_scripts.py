from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000
# one of the possibilities to represent the price in MockV3Aggregator.deploy
# Web3.toWei(STARTING_PRICE, "ether")

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]


def get_account():
    # get which one network is running
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        print("network is development")
        return accounts[0]

    else:
        print("network is testnet")
        # return accounts.add(os.getenv("PRIVATE_KEY"))
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print("Mocks Deployed!")
