
# Fetch-NSE-DATA

This module is used to fetch NSE DATA of Share Market.It basically fetch many informations like Most Active Equities, Index Performances, Price Band Hitters, Volume Gainers, 52 Week High / Low, Top 20 Gainer / Loosers etc.



## Installation

Install module with cmd

```bash
  pip install Fetch-NSE-DATA
```
    
## Fetch INFO

 - [Most Active Equities](https://github.com/nirupma2208/Fetch_NSE_DATA/blob/niru/README.md#most-active-equities)
 - [Index Performances](https://github.com/nirupma2208/Fetch_NSE_DATA/blob/niru/README.md#index-performances)
 - [Price Band Hitters](https://github.com/nirupma2208/Fetch_NSE_DATA/blob/niru/README.md#price-band-hitters)
 - [Volume Gainers](https://github.com/nirupma2208/Fetch_NSE_DATA/blob/niru/README.md#volume-gainers)
 - [52 Week High / Low](https://github.com/nirupma2208/Fetch_NSE_DATA/blob/niru/README.md#52-week-high--low)
 - [Top 20 Gainer / Loosers](https://github.com/nirupma2208/Fetch_NSE_DATA/blob/niru/README.md#top-20-gainer--loosers)
 - [TurnOver](https://github.com/nirupma2208/Fetch_NSE_DATA/blob/niru/README.md#turnover)
 - [Most Active Contracts](https://github.com/nirupma2208/Fetch_NSE_DATA/blob/niru/README.md#most-active-contracts)
 - [Most Active Futures](https://github.com/nirupma2208/Fetch_NSE_DATA/blob/niru/README.md#most-active-futures)
 - [Most Active Options](https://github.com/nirupma2208/Fetch_NSE_DATA/blob/niru/README.md#most-active-options)
 - [Most Active Calls](https://github.com/nirupma2208/Fetch_NSE_DATA/blob/niru/README.md#most-active-calls)
 - [Most Active Puts](https://github.com/nirupma2208/Fetch_NSE_DATA/blob/niru/README.md#most-active-puts)
 - [Most Active By OI](https://github.com/nirupma2208/Fetch_NSE_DATA/blob/niru/README.md#most-active-by-oi)
 - [Fetch Option Chain](https://github.com/nirupma2208/Fetch_NSE_DATA/blob/niru/README.md#option-chain)
 - [Fetch Option Chain By Symbol](https://github.com/nirupma2208/Fetch_NSE_DATA/blob/niru/README.md#option-chain-by-symbol)

## Import Module

```bash
  from Fetch_NSE_DATA.NSE_DATA import *
```


### Most Active Equities

```python
securities =Fetch_Nse_Data(MostActiveEquites.SECURITIES)

sme = Fetch_Nse_Data(MostActiveEquites.SME)

etf = Fetch_Nse_Data(MostActiveEquites.ETF)

```

### Index Performances
 - **All Indices**
    ```python
    allIndices = Fetch_Nse_Data(IndexPerformances.ALL_INDICES)
    ```
 - **BROAD MARKET INDICES**
    ```python
    broad_market = Fetch_Nse_Data(IndexPerformances.BROAD_MARKET)
    ```
 - **SECTORAL INDICES**
    ```python
    sectoral = Fetch_Nse_Data(IndexPerformances.SECTORAL)
    ```
 - **STRATEGY INDICES**
    ```python
    strategy = Fetch_Nse_Data(IndexPerformances.STRATEGY)
    ```
 - **THEMATIC INDICES**
    ```python
    thematic = Fetch_Nse_Data(IndexPerformances.THEMATIC)
    ```
 - **FIXED INCOME INDICES**
    ```python
    fixed_income = Fetch_Nse_Data(IndexPerformances.FIXED_INCOME)
    ```

### Price Band Hitters
 - **BAND_HITTERS**
    ```python
    band_hitters = Fetch_Nse_Data(PriceBandHitters.BAND_HITTERS)
    ```
 - **UPPER_BAND_HITTERS**
    ```python
    upper_band_hitters = Fetch_Nse_Data(PriceBandHitters.UPPER_BAND_HITTERS)
    ```
 - **LOWER_BAND_HITTERS**
    ```python
    lower_band_hitters = Fetch_Nse_Data(PriceBandHitters.LOWER_BAND_HITTERS)
    ```
 - **BOTH_BAND_HITTERS**
    ```python
    both_band_hitters = Fetch_Nse_Data(PriceBandHitters.BOTH_BAND_HITTERS)
    ```

### Volume Gainers 
```python
volume = Fetch_Nse_Data(VolumeGainers.VOLUME)
```
### 52 Week High / Low
 - **High**
    ```python
    week_high = Fetch_Nse_Data(WeekHighLow.WEEK_HIGH)
    ```
 - **Low**
    ```python
    week_low = Fetch_Nse_Data(WeekHighLow.WEEK_LOW)
    ```
### Top 20 Gainer / Loosers
 - **GAINERS**
    ```python
    gainers = Fetch_Nse_Data(Top20GainerLoosers.GAINERS)
    ```
 - **LOOSERS**
    ```python
    loosers = Fetch_Nse_Data(Top20GainerLoosers.LOOSERS)
    ```
### TurnOver 
```python
growth = Fetch_Nse_Data(TurnOver.GROWTH)
```

### Most Active Contracts
 - **EQUITY**
    ```python
    equity = Fetch_Nse_Data(MostActiveContracts.EQUITY)
    ```
 - **Currency**
    ```python
    currency = Fetch_Nse_Data(MostActiveContracts.CURRENCY)
    ```

### Most Active Futures
 - **EQUITY**
    ```python
    equity_f = Fetch_Nse_Data(MostActiveFutures.EQUITY)
    ```
 - **Currency**
    ```python
    currency_f = Fetch_Nse_Data(MostActiveFutures.CURRENCY)
    ```
### Most Active Options
 - **EQUITY**
    ```python
    equity_O = Fetch_Nse_Data(MostActiveOptions.EQUITY)
    ```
 - **Currency**
    ```python
    currency_O = Fetch_Nse_Data(MostActiveOptions.CURRENCY)
    ```
### Most Active Calls 
 - **EQUITY**
    ```python
    equity_C = Fetch_Nse_Data(MostActiveCalls.EQUITY)
    ```
 - **Currency**
    ```python
    currency_C = Fetch_Nse_Data(MostActiveCalls.CURRENCY)
    ```
### Most Active Puts
 - **EQUITY**
    ```python
    equity_P = Fetch_Nse_Data(MostActivePuts.EQUITY)
    ```
 - **Currency**
    ```python
    currency_P = Fetch_Nse_Data(MostActivePuts.CURRENCY)
    ```
### Most Active By OI
 - **EQUITY**
    ```python
    equity_OI = Fetch_Nse_Data(MostActiveOI.EQUITY)
    ```
 - **Currency**
    ```python
    currency_OI = Fetch_Nse_Data(MostActiveOI.CURRENCY)
    ```
### Option Chain
 - **Indices**
    ```python
    nifty = Fetch_Nse_Data(OptionChain.NIFTY) # NIFTY, BANKNIFTY, FINNIFTY

    ```
 - **Currency**
    ```python
    eurinr = Fetch_Nse_Data(OptionChain.EURINR) # EURINR, USDINR, GBPINR, JPYINR, EURUSD,GBPUSD,USDJPY
    ```
### Option Chain By Symbol

```python
AARTIIND = OptionChainIndices_By_Symbol('AARTIIND')
```


  

 

## License

[MIT](https://choosealicense.com/licenses/mit/)


## Feedback

If you have any feedback, please reach out to me at niru3913@gmail.com

