# Index Trading using a simple Algorithm

## Introduction
This project is created as part of exercise for NUS Fintech course. The idea behind the algorithm is very simple, 
when market rises a lot, trim position, and when market drops sigificantly over a certain period of time, add to position.

This Python code will only run on QuantConnect (www.quantconnect.com) as proprietary QuantConnect Classes are used.

## Results
Over a 10-year period from 1 Jan 2011 to 1 Jan 2021, the annualized return is 
Over a 6-year period from 1 Jan 2015 to 1 May 2021, the annualized return is 14.4%

## Future Improvements Ideas (if ever LOL)
1.  Should add a stop loss trigger to protect downside. Will do so if one day I want to use this for real trading.
2.  Need to check the distribution of daily returns of each index to find out how frequently will index move by certain 
quantum to then better match the trading trigger points to desired level of trade frequency. At the moment, I have only
randomly picked 5 to 8% index moves within 2 weeks to trigger a trade. Of course this is not exactly random because I
roughly know that indices generally do not move by more than 5% within 2 weeks, and thus I picked this level to trigger
trades during higher level of volatility.
