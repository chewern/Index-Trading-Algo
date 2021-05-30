import numpy as np
import pandas as pd

class Weird(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2015, 1, 1)  
        self.SetEndDate(2021, 5, 1) 
        self.SetCash(1000000)  
        self.SetBrokerageModel(BrokerageName.InteractiveBrokersBrokerage)
        
        self.spy = self.AddEquity("SPY",Resolution.Daily)
        self.eem = self.AddEquity("EEM", Resolution.Daily)
        self.qqq = self.AddEquity("QQQ", Resolution.Daily)
        
        self.spy.SetDataNormalizationMode(DataNormalizationMode.Raw)
        self.eem.SetDataNormalizationMode(DataNormalizationMode.Raw)
        self.qqq.SetDataNormalizationMode(DataNormalizationMode.Raw)
        
        self.SetWarmup(100);

    def OnData(self, data):
        if self.IsWarmingUp: return
    
        if not self.Portfolio.Invested:
            self.SetHoldings("SPY", 0.5)
            self.SetHoldings("QQQ", 0.5)
            self.SetHoldings("EEM", -0.2)
            self.Debug("entered initial positions")

        spy = self.History(["SPY"], 14)
        spy_data = spy['close'].tolist()
        if spy_data[-1] > 1.06*spy_data[0]:
            self.SetHoldings("SPY", 0.4)
        
        if spy_data[0] > 1.06*spy_data[-1]:
            self.SetHoldings("SPY", 0.6)
            

        qqq = self.History(["QQQ"], 14)
        qqq_data = qqq['close'].tolist()
        if qqq_data[-1] > 1.08*qqq_data[0]:
            self.SetHoldings("QQQ", 0.4)
        
        if qqq_data[0] > 1.08*qqq_data[-1]:
            self.SetHoldings("QQQ", 0.6)

        eem = self.History(["EEM"], 14)
        eem_data = eem['close'].tolist()
        if eem_data[-1] > 1.1*eem_data[0]:
            self.SetHoldings("EEM", -0.3)
        
        if eem_data[0] > 1.1*eem_data[-1]:
            self.SetHoldings("EEM", 0)