class Tariff:

    def __init__(self):
        self.status = str
        self.check = None
        self.shares = None
        self.assets = None
        self.investors = []

    def addInvestor(self, investor):
        self.investors.append(investor)

    def getListOfInvestors(self):
        return self.investors

    def getAssets(self):
        self.assets = 0
        for investor in self.investors:
            self.assets += investor.getAsset()

        return self.assets

    def getShares(self):
        self.shares = 0
        for investor in self.investors:
            self.shares += investor.getShare()

        return self.shares

    def checkBeforeStart(self):
        # check
        self.check = self.getShares()

        if self.check == 100.0:
            return True
        else:
            return False

    def getLength(self):
        return len(self.investors)

    def getStatus(self):
        self.status = "\n\nTariff status\n\nId\tAsset\tShare(%)\n"
        for investor in self.getListOfInvestors():
            self.status += str(investor.id) + "\t" + str(investor.asset) + "\t" + str(investor.share) + "\n"

        self.status += "\nTotal tariff assets:\t" + str(self.getAssets()) + "\n"
        self.status += "Total tariff shares:\t" + str(self.getShares()) + "(%)\n"
        self.status += "100% shares devided:\t" + str(self.checkBeforeStart()) + "\n\n"

        return self.status
