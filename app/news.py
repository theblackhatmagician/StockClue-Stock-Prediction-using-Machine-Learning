import requests


def getNews():

    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/v2/list"

    querystring = {"region":"in","snippetCount":"20","s":"INFY.NS"}

    payload = "Pass in the value of uuids field returned right in this endpoint to load the next page, or leave empty to load first page"
    headers = {
        'content-type': "text/plain",
        'x-rapidapi-key': "a945ad3a16mshb1cdbceb72aec55p1f0e6bjsn3f852dd42dc9",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    news = []

    data = response.json()
    if 'message' not in data.keys():
        for i in data['data']['main']['stream']:     
            d = [] 
            d.append(i['content']['title'])
            d.append(i['content']['pubDate'].split('T')[0])
            news.append(d)
    else:
        news.append(["asdf","1234"])
        print("can't fetch news")
        

    return news

