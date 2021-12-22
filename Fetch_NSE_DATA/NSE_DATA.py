import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    }

BASE = 'https://www.nseindia.com/api/'
Indices = 'option-chain-indices?symbol='
currency = 'option-chain-currency?symbol='


class MostActiveEquites:
    SECURITIES = BASE + 'live-analysis-most-active-securities?index=volume'
    SME = BASE + 'live-analysis-most-active-sme?index=volume'
    ETF = BASE + 'live-analysis-most-active-etf?index=volume'


class IndexPerformances:
    ALL_INDICES = BASE + 'allIndices'
    BROAD_MARKET = 'BROAD MARKET INDICES'
    SECTORAL = 'SECTORAL INDICES'
    STRATEGY = 'STRATEGY INDICES'
    THEMATIC = 'THEMATIC INDICES'
    FIXED_INCOME = 'FIXED INCOME INDICES'


class PriceBandHitters:
    BAND_HITTERS = BASE + 'live-analysis-price-band-hitter'
    UPPER_BAND_HITTERS = 'upper'
    LOWER_BAND_HITTERS = 'lower'
    BOTH_BAND_HITTERS = 'both'


class VolumeGainers:
    VOLUME = BASE + 'live-analysis-volume-gainers'


class WeekHighLow:
    WEEK_HIGH = BASE + 'live-analysis-52Week?index=high'
    WEEK_LOW = BASE + 'live-analysis-52Week?index=low'


class Top20GainerLoosers:
    GAINERS = BASE + 'live-analysis-variations?index=gainers'
    LOOSERS = BASE + 'live-analysis-variations?index=loosers'


class TurnOver:
    GROWTH = BASE + 'snapshot-capital-market-tbg-eod-statistics'


class MostActiveContracts:
    EQUITY = BASE + 'snapshot-derivatives-equity?index=contracts&limit=20'
    CURRENCY = BASE + 'currency-derivatives?index=most_act_cont'


class MostActiveFutures:
    EQUITY = BASE + 'snapshot-derivatives-equity?index=futures'
    CURRENCY = BASE + 'currency-derivatives?index=most_act_futs'


class MostActiveOptions:
    EQUITY = BASE + 'snapshot-derivatives-equity?index=options&limit=20'
    CURRENCY = BASE + 'currency-derivatives?index=most_act_opt'


class MostActiveCalls:
    EQUITY = BASE + 'snapshot-derivatives-equity?index=calls'
    CURRENCY = BASE + 'currency-derivatives?index=most_act_call'


class MostActivePuts:
    EQUITY = BASE + 'snapshot-derivatives-equity?index=puts'
    CURRENCY = BASE + 'currency-derivatives?index=most_act_puts'


class MostActiveOI:
    EQUITY = BASE + 'snapshot-derivatives-equity?index=oi'
    CURRENCY = BASE + 'currency-derivatives?index=most_act_oi&limit=10'


class OptionChain:
    NIFTY = '{0}{1}NIFTY'.format(BASE, Indices)
    BANKNIFTY = '{0}{1}BANKNIFTY'.format(BASE, Indices)
    FINNIFTY = '{0}{1}FINNIFTY'.format(BASE, Indices)
    EURINR = '{0}{1}EURINR'.format(BASE, currency)
    USDINR = '{0}{1}USDINR'.format(BASE, currency)
    GBPINR = '{0}{1}GBPINR'.format(BASE, currency)
    JPYINR = '{0}{1}JPYINR'.format(BASE, currency)
    EURUSD = '{0}{1}EURUSD'.format(BASE, currency)
    GBPUSD = '{0}{1}GBPUSD'.format(BASE, currency)
    USDJPY = '{0}{1}USDJPY'.format(BASE, currency)


def DATA(url):
    try:
        session = requests.Session()
        session.get('https://www.nseindia.com', headers=headers)
        response = session.get(url, headers=headers)
        return response.json()
    except Exception as error:
        print(error)
        return {}


def OptionChainIndices_By_Symbol(Symbol):
    Indices = BASE + 'option-chain-indices?symbol=' + Symbol
    return DATA(Indices)


def Fetch_Nse_Data(constant):
    if constant == IndexPerformances.BROAD_MARKET or constant == IndexPerformances.SECTORAL or constant == IndexPerformances.STRATEGY or constant == IndexPerformances.THEMATIC or constant == IndexPerformances.FIXED_INCOME:
        result = []
        for i in DATA(IndexPerformances.ALL_INDICES)['data']:
            if i['key'] == IndexPerformances.BROAD_MARKET and constant == IndexPerformances.BROAD_MARKET:
                result.append(i)
            elif i['key'] == IndexPerformances.SECTORAL and constant == IndexPerformances.SECTORAL:
                result.append(i)
            elif i['key'] == IndexPerformances.STRATEGY and constant == IndexPerformances.STRATEGY:
                result.append(i)
            elif i['key'] == IndexPerformances.THEMATIC and constant == IndexPerformances.THEMATIC:
                result.append(i)
            elif i['key'] == IndexPerformances.FIXED_INCOME and constant == IndexPerformances.FIXED_INCOME:
                result.append(i)
        else:
            return result
    elif constant == IndexPerformances.ALL_INDICES:
        return DATA(constant)
    elif constant == PriceBandHitters.UPPER_BAND_HITTERS:
        return DATA(PriceBandHitters.BAND_HITTERS)['upper']
    elif constant == PriceBandHitters.LOWER_BAND_HITTERS:
        return DATA(PriceBandHitters.BAND_HITTERS)['lower']
    elif constant == PriceBandHitters.BOTH_BAND_HITTERS:
        return DATA(PriceBandHitters.BAND_HITTERS)['both']
    else:
        return DATA(constant)

