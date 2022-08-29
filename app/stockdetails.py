from nsetools import Nse

def stockDetails():
    try:
        nse = Nse()
        details = nse.get_quote('infy')
        data = [details['open'],details['closePrice'],details['lastPrice'], details['dayHigh'],details['dayLow'],details['quantityTraded'],details['previousClose'],details['averagePrice'],details['cm_adj_low_dt']]
        return data
    except:
        return [1556.00,1560.75,1560.75,1569.90,1551.00,3436594,0,0]
