import requests

def fetchindicators():
    '''#simple moving average (SMA)
    url = 'https://www.alphavantage.co/query?function=SMA&symbol=INFY.BO&interval=daily&time_period=10&series_type=open&apikey=TA38JZVNEUGSWUAK'
    r = requests.get(url)
    data = r.json()
    sma = data['Technical Analysis: SMA']['2021-07-09']['SMA']

    #exponential moving average (EMA)
    url = 'https://www.alphavantage.co/query?function=EMA&symbol=INFY.BO&interval=daily&time_period=10&series_type=open&apikey=TA38JZVNEUGSWUAK'
    r = requests.get(url)
    data = r.json()
    ema = data['Technical Analysis: EMA']['2021-07-09']['EMA']

    #moving average convergence / divergence (MACD)
    url = 'https://www.alphavantage.co/query?function=MACD&symbol=INFY.BO&interval=daily&series_type=open&apikey=TA38JZVNEUGSWUAK'
    r = requests.get(url)
    data = r.json()
    macd = data['Technical Analysis: MACD']['2021-07-09']['MACD']

    # relative strength index (RSI)
    url = 'https://www.alphavantage.co/query?function=RSI&symbol=INFY.BO&interval=daily&time_period=10&series_type=open&apikey=TA38JZVNEUGSWUAK'
    r = requests.get(url)
    data = r.json()
    rsi = data['Technical Analysis: RSI']['2021-07-09']['RSI']

    #commodity channel index (CCI)
    url = 'https://www.alphavantage.co/query?function=CCI&symbol=INFY.BO&interval=daily&time_period=10&apikey=TA38JZVNEUGSWUAK'
    r = requests.get(url)
    data = r.json()
    cci = data['Technical Analysis: CCI']['2021-07-09']['CCI']'''

    #return [sma,ema,macd,rsi,cci]
    return ['1568.5600','1558.2659','41.7640','61.8636','-74.5271']