from evaluation import Evaluation
from investor import Investor
from tariff import Tariff

if __name__ == '__main__':
    print("------------------------------------------------")
    print("STEP1: Initial tariff setup. Investors included. Total tariff´s assets value: 10 000 000.")

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

    # Print after initial setup
    print(tariff.getStatus())

    print("------------------------------------------------")
    print("STEP2: Tariff evaluation on D-day. New total tariff´s assets value: 12 000 000.")

    # Tariff evaluation
    evaluation = Evaluation(tariff)
    evaluation.evaluate(12000000)

    # Print after evaluation
    print(tariff.getStatus())

    print("------------------------------------------------")
    print("STEP3: Tariff evaluation on D-day and investor´s new deposit.")
    print("New total tariff´s assets value: 12 000 000.")
    print("Investor ID: 2. Investor´s new deposit: 1 000 000.")

    # Deposit evaluation
    evaluation.deposit_evaluate(2, 1000000, 12000000)

    # Print after evaluation
    print(tariff.getStatus())

    print("------------------------------------------------")
    print("STEP4: Tariff valuation on D-day and investor´s new withdrawal.")
    print("New total tariffs assets value: 13 000 000.")
    print("Investor ID: 2. Investor´s new withdrawal: 200 000.")

    # Deposit evaluation
    evaluation.withdrawal_evaluate(5, 200000, 13000000)

    # Print after evaluation
    print(tariff.getStatus())

    print("------------------------------------------------")
    print("STEP5: Tariff evaluation on D-day. Decrease in tariff´s assets value: 11 000 000.")

    # Tariff evaluation
    evaluation = Evaluation(tariff)
    evaluation.evaluate(11000000)

    # Print after evaluation
    print(tariff.getStatus())

    print("------------------------------------------------")
    print("STEP6: Tariff evaluation on D-day. Decrease in tariff´s assets value: 11 000 000.")
    print("Investor ID: 10. Investor´s new deposit: 1 000 000.")

    # Deposit evaluation
    evaluation.deposit_evaluate(10, 1000000, 11000000)

    # Print after evaluation
    print(tariff.getStatus())

    print("------------------------------------------------")
    print("STEP7: Tariff evaluation on D-day. Increase in tariff´s assets value: 11 000 000.")
    print("Investor ID: 10. Investor´s new withdrawal: 1 000 000.")

    # Withdrawal evaluation
    evaluation.withdrawal_evaluate(10, 1000000, 11000000)

    # Print after evaluation
    print(tariff.getStatus())

    print("------------------------------------------------")
    print("STEP8: Tariff evaluation on D-day. Increase in tariff´s assets value: 18 000 000.")
    print("Investor ID: 10. Investor´s new withdrawal: whole deposit.")

    # Withdrawal evaluation
    evaluation.withdrawal_evaluate(10, 1000000, 18000000)

    # Print after evaluation
    print(tariff.getStatus())


    print("------------------------------------------------")
    print("STEP9: Tariff evaluation on D-day. Increase in tariff´s assets value: 17 000 000.")
    print("Investor ID: 10. Investor´s new withdrawal: whole asset.")

    # Withdrawal evaluation
    evaluation.withdrawal_evaluate(10, 551563, 17000000)

    # Print after evaluation
    print(tariff.getStatus())

    print("------------------------------------------------")
    print("STEP10: Tariff evaluation on D-day. Increase in tariff´s assets value: 17 000 000.")
    print("Investor ID: 10. Investor´s new withdrawal: whole asset.")

    # Withdrawal evaluation
    evaluation.withdrawal_evaluate(10, 0, 16448436)

    # Remove investor id:10 from the tariff
    tariff.removeInvestor(10)

    # Print after evaluation
    print(tariff.getStatus())


    print("------------------------------------------------")
    print("STEP11: Remove investor from the Tariff")

    # Remove investor id:9 from the tariff
    tariff.removeInvestor(9)

    # Print after evaluation
    print(tariff.getStatus())

