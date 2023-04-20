from ape import accounts, convert, project


def main():
    user = accounts.load("workshop")
    faucet = project.Faucet.at("0xD8c338f520C2e9289cC645b58B7471988143aA59")

    usdc = project.Token.at("0x468226e47738C470E07AAEAdbF44cEE3A869812F")

    usdc.approve(faucet.address, convert("1000 ETH", int), sender=user)
    faucet.deposit(convert("10 ETH", int), sender=user)