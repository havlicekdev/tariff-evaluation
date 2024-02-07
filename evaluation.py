class Evaluation:

    def __init__(self, tariff):
        self.deposit_id_share = None
        self.investor_deposit = None
        self.investor_id = None
        self.value_for_evaluation = None
        self.tariff_investors = None
        self.tariff_assets = None
        self.tariff = tariff

    def evaluate(self, value_for_evaluation):

        # New tariff value for evaluation
        self.value_for_evaluation = value_for_evaluation

        # Get tariff assets
        self.tariff_assets = self.tariff.getAssets()

        # Get tariff investors
        self.tariff_investors = self.tariff.getListOfInvestors()

        # Evaluation
        for investor in self.tariff_investors:
            investor.setAsset(round(value_for_evaluation * (investor.getShare()/100)))

    def deposit_evaluate(self, investor_id, investor_deposit, value_for_evaluation):

        # Variables
        self.investor_id = investor_id
        self.investor_deposit = investor_deposit

        # New tariff value for evaluation
        self.value_for_evaluation = value_for_evaluation

        # Get tariff assets
        self.tariff_assets = self.tariff.getAssets()

        # Get tariff investors
        self.tariff_investors = self.tariff.getListOfInvestors()

        # Evaluation
        for investor in self.tariff_investors:
            investor.setAsset(round(value_for_evaluation * (investor.getShare()/100)))

        # Deposit
        for investor in self.tariff_investors:
            if investor.getId() == self.investor_id:
                investor.setAsset(round(investor.getAsset() + investor_deposit))

        # Percentage conversion for deposit investor
        self.deposit_id_share = 0

        for investor in self.tariff_investors:
            if investor.getId() == self.investor_id:
                print(investor.getAsset())
                print(self.tariff.getAssets())
                investor.setShare((investor.getAsset() / self.tariff.getAssets())*100)
                self.deposit_id_share = investor.getShare()

        print(self.deposit_id_share)

        # Percentage conversion for another investors
        for investor in self.tariff_investors:
            if investor.getId() != self.investor_id:
                investor.setShare((investor.getAsset() / self.tariff.getAssets())*100)





    def withdrawal_evaluate(self, investor_id, investor_withdrawal, value_for_evaluation):

        # Variables
        self.investor_id = investor_id
        self.investor_withdrawal = investor_withdrawal

        # New tariff value for evaluation
        self.value_for_evaluation = value_for_evaluation

        # Get tariff assets
        self.tariff_assets = self.tariff.getAssets()

        # Get tariff investors
        self.tariff_investors = self.tariff.getListOfInvestors()

        # Evaluation
        for investor in self.tariff_investors:
            investor.setAsset(round(value_for_evaluation * (investor.getShare() / 100)))

        # Withdrawal
        for investor in self.tariff_investors:
            if investor.getId() == self.investor_id:
                investor.setAsset(round(investor.getAsset() - investor_withdrawal))

        # Percentage conversion for deposit investor
        self.deposit_id_share = 0

        for investor in self.tariff_investors:
            if investor.getId() == self.investor_id:
                print(investor.getAsset())
                print(self.tariff.getAssets())
                investor.setShare((investor.getAsset() / self.tariff.getAssets()) * 100)
                self.deposit_id_share = investor.getShare()

        print(self.deposit_id_share)

        # Percentage conversion for another investors
        for investor in self.tariff_investors:
            if investor.getId() != self.investor_id:
                investor.setShare((investor.getAsset() / self.tariff.getAssets()) * 100)
