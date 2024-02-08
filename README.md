# PPA Tariff Evaluation
Zpracovává vyhodnocení tarifů, dle historických dat

## Startovní data
Nejdříve je nutné založit tarif a vložit do něj libovolný počet investorů. Investory je možné přidávat nebo odebrat kdykoliv později.


Pojmy:
- Tariff: investiční portfolio
- Investor: individuální investor investuící deposit do aktiv tarifu
- Asset: aktiva investora nebo fondu alokována v investicích
- Share (%): procentní podíl investora na aktivech tarifu
- Deposit: finanční vklady investora vložené do tarifu
- Valorization: zhodnocení depositu investora v příslušné měně
- Valorization (%): zhodnocení depositu investora v %

- Total tariff assets: celková aktiva tarifu v příslušné měně
- Total tariff shares: součet jednotlivých procentuálních podílů investorů v tarifu
- 100% shares devided: kontrola, zda součet jednotlivých procentuálních podílů investorů v tarifu je v součtu vždy 100%

## class Tariff

Constructor:
```
__init__(self)
```

Methods:
```
addInvestor(self, investor) # Přidat nového investora do tarifu.
```
```
removeInvestor(self, investor_id) # Odebrat existujícího investora z tarifu.
```


## class Investor

Constructor:
```
__init__(self, investor_id, investor_deposit)
```

Setters & Getters:
```
setId(self, investor_id)    # set id
getId(self):                # get id

getDeposit(self)            # get investor deposit

setAsset(self, asset)       # set investor asset
getAsset(self)              # get investor asset

setShare(self, share)       # set investor share
getShare(self)              # get investor share
```
Methods:
```
incDeposit(self, deposit)   # Increase investor deposit
decDeposit(self, deposit)   # Decrease investor deposit
```
```
getValorization(self)       # Get investor valorization
getValorizationRate(self)   # Get investor valorization(%)
```

## class Evaluation