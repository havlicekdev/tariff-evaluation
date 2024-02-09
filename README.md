# Tariff Evaluation

This tool allows you to:
- Create a new tariff with the possibility of an unlimited number of investors.
- Add or remove individual investors at any time.
- Evaluate the asset value of the tariff on any date.
- Evaluate the value of the tariff assets at any date and allow any investor to make a new deposit.
- Evaluate the value of the tariff assets at any date and allow any investor to withdraw the deposit.

This tool provides the following information:
- The value of the tariff assets at any time
- Valorization of tariff assets at any moment
- The value of an individual investor's assets at any given time
- Valorization of the individual investor's assets at every moment
- Ability to track each investment of each individual investor separately.

## How it works
First, you need to create a new tariff, then the tariff must be filled by at least one investor.
Investors can be added or removed at any time later.

On day D, the current value of the tariff assets is added using the method:
```
evaluate(self, value_for_evaluation)    # Evaluate the tariff
```
This recalculates the values of individual investors' assets, their asset valorization, or their share in the tariff.


Method:
```
deposit_evaluate(self, investor_id, investor_deposit, value_for_evaluation) # Evaluate the tariff and new deposit
```
allows an individual investor to make a new deposit at any time.


Method:
```
withdrawal_evaluate(self, investor_id, investor_withdrawal, value_for_evaluation)   # Evaluate the tarif and new withdrawal
```
allows to withdraw the deposit of an individual investor at any time.


Every deposit or withdrawal has an impact on asset appreciation.
To avoid this fact, a new deposit or withdrawal should be given as a new investment.

By recording individual iterations, we get the evolution of investments over time.


### Used terms:
- Tariff: investment portfolio
- Investor: an individual investor investing a deposit in tariff assets
- Asset: the investor's or fund's assets allocated in investments
- Share (%): the investor's percentage of the tariff's assets
- Deposit: financial deposits of the investor placed in the tariff
- Valorization: valuation of the investor's deposit in the relevant currency
- Valorization (%): valuation of the investor's deposit in percent

- Total tariff assets: the total assets of the tariff in the relevant currency
- Total tariff shares: the sum of individual percentage shares of investors in the tariff
- Total tariff valorization (%): valuation of the tariff´s deposits in percent

## class Tariff

Constructor:
```
__init__(self)
```

Methods:
```
addInvestor(self, investor)         # Add a new investor into the tariff.
```
```
removeInvestor(self, investor_id)   # Remove the existing investor from the tariff.
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

Constructor
```
__init__(self, tariff)
```

Methods:
```
evaluate(self, value_for_evaluation)                                                # Evaluate the tariff
```
```
deposit_evaluate(self, investor_id, investor_deposit, value_for_evaluation)         # Evaluate the tariff and new deposit
```
```
withdrawal_evaluate(self, investor_id, investor_withdrawal, value_for_evaluation)   # Evaluate the tarif and new withdrawal
```


## Sample file
The sample.py file shows examples how to use the methods.
