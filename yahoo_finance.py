import requests
import json
import sys

host_url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/"
end_point_historic = "stock/v2/get-historical-data?"
common_parameter = "period1=1546448400&period2=1562086800"
stock = "AMRN"

api_key = sys.argv[1]

headers={
      "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
      "X-RapidAPI-Key": api_key,
      "Content-Type": "application/json"
    }

output = requests.get(host_url + end_point_historic + common_parameter +
 "&symbol=" + stock, headers=headers)

# print(output.text)
filename = stock + ".json"

with open(filename, 'w') as fp:
    json.dump(output.json(), fp)

#stock_symbols = ["BOFA", "MSFT", "FB", "ALPHA", "AMZN", ""]

# for stocks in stock_symbols:
#     url = host_url + end_point_historic + common_parameter + "&symbol=" + stocks
#
#     filename = stocks + ".json"
#     print(url)
#     print(filename)
    # with open(filename, 'w') as fp:
    #    json.dump(output.json(), fp)
