class Investor:

    def __init__(self, investor_id, investor_deposit, investor_share):
        self.deposit = investor_deposit
        self.id = investor_id
        self.asset = investor_deposit
        self.share = investor_share

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def incDeposit(self, deposit):
        self.deposit += deposit

    def decDeposit(self, deposit):
        self.deposit -= deposit

    def getDeposit(self):
        return self.deposit

    def setAsset(self, asset):
        self.asset = asset

    def getAsset(self):
        return self.asset

    def setShare(self, share):
        self.share = share

    def getShare(self):
        return self.share

    def getValorization(self):
        return self.getAsset() - self.getDeposit()

    def getValorizationRate(self):
        if self.getDeposit() <= 0:
            return 0
        else:
            return round((self.getAsset() - self.getDeposit()) / self.getDeposit() * 100 * 100)/100.0




