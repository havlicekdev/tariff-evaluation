class Investor:

    def __init__(self, id, asset, share):
        self.id = id
        self.asset = asset
        self.share = share

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setAsset(self, asset):
        self.asset = asset

    def getAsset(self):
        return self.asset

    def setShare(self, share):
        self.share = share

    def getShare(self):
        return self.share
