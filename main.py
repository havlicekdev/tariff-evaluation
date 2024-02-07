from evaluation import Evaluation
from investor import Investor
from tariff import Tariff

if __name__ == '__main__':
    # New tariff
    tariff = Tariff()

    # Add investor into tariff
    tariff.addInvestor(Investor(1, 1000000, 10.0))
    tariff.addInvestor(Investor(2, 1000000, 10.0))
    tariff.addInvestor(Investor(3, 1000000, 10.0))
    tariff.addInvestor(Investor(4, 1000000, 10.0))
    tariff.addInvestor(Investor(5, 1000000, 10.0))
    tariff.addInvestor(Investor(6, 1000000, 10.0))
    tariff.addInvestor(Investor(7, 1000000, 10.0))
    tariff.addInvestor(Investor(8, 1000000, 10.0))
    tariff.addInvestor(Investor(9, 1000000, 10.0))
    tariff.addInvestor(Investor(10, 1000000, 10.0))

    # Tariff check before evaluation
    print(tariff.checkBeforeStart())

    # Get tariff assets
    print(tariff.getAssets())

    # Get tariff shares
    print(tariff.getShares())

    # Print tariff status
    print(tariff.getStatus())

    # Tariff evaluation
    evaluation = Evaluation(tariff)
    evaluation.evaluate(12000000)

    # Print after evaluation
    print(tariff.getStatus())

    # Deposit evaluation
    evaluation.deposit_evaluate(2, 1000000, 13000000)

    # Print after evaluation
    print(tariff.getStatus())

    # Tariff evaluation
    evaluation = Evaluation(tariff)
    evaluation.evaluate(15000000)

    # Print after evaluation
    print(tariff.getStatus())

    # Deposit evaluation
    evaluation.deposit_evaluate(5, 1000000, 16000000)

    # Print after evaluation
    print(tariff.getStatus())

    # Tariff evaluation
    evaluation = Evaluation(tariff)
    evaluation.evaluate(15000000)

    # Print after evaluation
    print(tariff.getStatus())

    # Withdrawal evaluation
    evaluation.withdrawal_evaluate(2, 1000000, 15000000)

    # Print after evaluation
    print(tariff.getStatus())

    # Withdrawal evaluation
    evaluation.withdrawal_evaluate(9, 1000000, 15000000)

    # Print after evaluation
    print(tariff.getStatus())

    evaluation.withdrawal_evaluate(9, 404562, 14000000)

    # Print after evaluation
    print(tariff.getStatus())