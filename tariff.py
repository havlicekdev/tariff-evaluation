class Tariff:

    # init
    def __init__(self):
        self.assets = None
        self.shares = None
        self.check = None
        self.status = None

        # list of investors
        self.investors = []

    # add new investor
    def addInvestor(self, investor):
        self.investors.append(investor)

        # re/calculate share for every investor
        for investor in self.investors:
            investor.setShare((investor.getAsset() / self.getAssets()) * 100)

    # remove existing investor
    def removeInvestor(self, investor_id):

        # remove existing investor from the tariff
        for investor in self.investors:
            if investor.getId() == investor_id:
                self.investors.remove(investor)
                break

        # recalculate share of every investor in the tariff
        for investor in self.investors:
            investor.setShare((investor.getAsset() / self.getAssets()) * 100)

    # list of investors
    def getListOfInvestors(self):
        return self.investors

    # total assets
    def getAssets(self):
        self.assets = 0
        for investor in self.investors:
            self.assets += investor.getAsset()

        return self.assets

    # total shares
    def getShares(self):
        self.shares = 0
        for investor in self.investors:
            self.shares += investor.getShare()

        return round(self.shares * 100) / 100.0

    def getLength(self):
        return len(self.investors)

    def getTariffValorization(self):
        self.tariff_valorization = 0
        self.sum_of_valorizations = 0
        for investor in self.investors:
            self.sum_of_valorizations += investor.getShare()

        self.tariff_valorization = (self.sum_of_valorizations / self.getLength())
        return self.tariff_valorization


    def getStatus(self):
        self.status = ("\nTariff status"
                       "\n\nId"
                       "\tAsset"
                       "\tShare(%)"
                       "\t\tDeposit"
                       "\tValorization"
                       "\tValorization(%)"
                       "\n"
                       "")
        for investor in self.getListOfInvestors():
            self.status += (str(investor.id)
                            + "\t" + str(investor.asset)
                            + "\t" + str(investor.share)
                            + "\t" + str(investor.getDeposit())
                            + "\t" + str(investor.getValorization())
                            + "\t\t\t" + str(investor.getValorizationRate())
                            + "\n")

        self.status += "\nTotal tariff assets:\t\t" + str(self.getAssets()) + "\n"
        self.status += "Total tariff shares:\t\t" + str(self.getShares()) + "(%)\n"
        self.status += "Total tariff valorization(%):\t" + str(self.getTariffValorization()) + "(%)\n\n"

        return self.status
