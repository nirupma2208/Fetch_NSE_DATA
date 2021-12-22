from Fetch_NSE_DATA.NSE_DATA import *

""" To Fetch Most Active Equities """

securities =Fetch_Nse_Data(MostActiveEquites.SECURITIES)
sme = Fetch_Nse_Data(MostActiveEquites.SME)
etf = Fetch_Nse_Data(MostActiveEquites.ETF)

""" To Fetch Index Performances """

# allIndices
allIndices = Fetch_Nse_Data(IndexPerformances.ALL_INDICES)

# BROAD MARKET INDICES
broad_market = Fetch_Nse_Data(IndexPerformances.BROAD_MARKET)

# SECTORAL INDICES
sectoral = Fetch_Nse_Data(IndexPerformances.SECTORAL)

# STRATEGY INDICES
strategy = Fetch_Nse_Data(IndexPerformances.STRATEGY)

# THEMATIC INDICES
thematic = Fetch_Nse_Data(IndexPerformances.THEMATIC)

# FIXED INCOME INDICES
fixed_income = Fetch_Nse_Data(IndexPerformances.FIXED_INCOME)

"""  To Fetch Price Band Hitters"""

# BAND_HITTERS
band_hitters = Fetch_Nse_Data(PriceBandHitters.BAND_HITTERS)

# UPPER_BAND_HITTERS
upper_band_hitters = Fetch_Nse_Data(PriceBandHitters.UPPER_BAND_HITTERS)

# LOWER_BAND_HITTERS
lower_band_hitters = Fetch_Nse_Data(PriceBandHitters.LOWER_BAND_HITTERS)

# BOTH_BAND_HITTERS
both_band_hitters = Fetch_Nse_Data(PriceBandHitters.BOTH_BAND_HITTERS)

"""  To Fetch Volume Gainers """
volume = Fetch_Nse_Data(VolumeGainers.VOLUME)

""" To Fetch 52 Week High / Low"""

# High
week_high = Fetch_Nse_Data(WeekHighLow.WEEK_HIGH)

# Low
week_low = Fetch_Nse_Data(WeekHighLow.WEEK_LOW)

""" To Fetch Top 20 Gainer / Loosers """
# GAINERS
gainers = Fetch_Nse_Data(Top20GainerLoosers.GAINERS)

# LOOSERS
loosers = Fetch_Nse_Data(Top20GainerLoosers.LOOSERS)

""" To Fetch TurnOver """
growth = Fetch_Nse_Data(TurnOver.GROWTH)

""" To Fetch Most Active Contracts """
# EQUITY
equity = Fetch_Nse_Data(MostActiveContracts.EQUITY)

# Currency
currency = Fetch_Nse_Data(MostActiveContracts.CURRENCY)

""" To Fetch Most Active Futures"""
# EQUITY
equity_f = Fetch_Nse_Data(MostActiveFutures.EQUITY)

# Currency
currency_f = Fetch_Nse_Data(MostActiveFutures.CURRENCY)

""" To Fetch Most Active Options"""
# EQUITY
equity_O = Fetch_Nse_Data(MostActiveOptions.EQUITY)

# Currency
currency_O = Fetch_Nse_Data(MostActiveOptions.CURRENCY)

""" To Fetch Most Active Calls"""
# EQUITY
equity_C = Fetch_Nse_Data(MostActiveCalls.EQUITY)

# Currency
currency_C = Fetch_Nse_Data(MostActiveCalls.CURRENCY)

""" To Fetch Most Active Puts"""
# EQUITY
equity_P = Fetch_Nse_Data(MostActivePuts.EQUITY)

# Currency
currency_P = Fetch_Nse_Data(MostActivePuts.CURRENCY)

""" To Fetch Most Active By OI"""
# EQUITY
equity_OI = Fetch_Nse_Data(MostActiveOI.EQUITY)

# Currency
currency_OI = Fetch_Nse_Data(MostActiveOI.CURRENCY)

""" To Fetch Option Chain"""

# for Indices
nifty = Fetch_Nse_Data(OptionChain.NIFTY) # NIFTY, BANKNIFTY, FINNIFTY

# For Currency
eurinr = Fetch_Nse_Data(OptionChain.EURINR) # EURINR, USDINR, GBPINR, JPYINR, EURUSD,GBPUSD,USDJPY

""" To Fetch Option Chain By Symbol """
AARTIIND = OptionChainIndices_By_Symbol('AARTIIND')




