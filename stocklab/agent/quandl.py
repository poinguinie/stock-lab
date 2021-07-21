import quandl

quandl.ApiConfig.api_key = 'fbqysXUCkz7nEszzMXsP'
data = quandl.get('BCHARTS/BITFLYERUSD',
                  start_date='2019-03-07', end_date='2019-03-07')

print(data)
