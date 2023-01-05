# kalshi_python

 This library is the official python SDK for algorithmic trading on [Kalshi](https://kalshi.com). 
    
This SDK is powered by [Kalshi's trading api](https://trading-api.readme.io). 

By using this SDK, you agree to Kalshi's Developer Agreement (https://kalshi.com/developer-agreement).

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage

### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install kalshi-python
```

Then import the package:
```python
import kalshi_python 
```

## Quick start

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import uuid
import kalshi_python
from kalshi_python.models import *
from pprint import pprint

config = kalshi_python.Configuration()
# Comment the line below to use production
config.host = 'https://demo-api.kalshi.co/trade-api/v2'

# Create an API configuration passing your credentials.
# Use this if you want the kalshi_python sdk to manage the authentication for you.
kalshi_api = kalshi_python.ApiInstance(
    email='YOUR_EMAIL_HERE',
    password='YOUR_PASSWORD_HERE',
    configuration=config,
)

# Alternatively you can manage the authentication yourself by doing:
# kalshi_api = kalshi_python.ApiInstance(
#     configuration=config,
# )
# loginResponse = kalshi_api.login(LoginRequest(email='YOUR_EMAIL_HERE', password='YOUR_PASSWORD_HERE'))
# token = loginResponse.token
# kalshi_api.set_api_token(loginResponse.token)
# # The token used above can eventually expire if you stop using it for more than 30 minutes.
# # In that case you should redo the process by doing a new login request and setting the api token again in the same way.

# Checks if the exchange is available.
exchangeStatus = kalshi_api.get_exchange_status()
print('Exchange status response: ')
pprint(exchangeStatus)

# Gets the data for a specific series.
seriesTicker = 'FED'
seriesResponse = kalshi_api.get_series(seriesTicker)
print('\nSeries: ' + seriesTicker)
pprint(seriesResponse)

# Gets the data for a specific event.
eventTicker = 'FED-23DEC'
eventResponse = kalshi_api.get_event(eventTicker)
print('\nEvent: ' + seriesTicker)
pprint(eventResponse)

# Replace the series ticker with the market ticker you want.
marketTicker = 'FED-23DEC-T3.00'
marketResponse = kalshi_api.get_market(marketTicker)
print('\nMarket: ' + marketTicker)
pprint(marketResponse)

# Gets the balance for your kalshi account.
balanceResponse = kalshi_api.get_balance()
print('\nUser balance: ')
pprint(balanceResponse)

if exchangeStatus.trading_active:
    # Submit an order for 10 yes contracts at 50cents on 'FED-23DEC-T3.00'.
    orderUuid = str(uuid.uuid4())
    orderResponse = kalshi_api.create_order(CreateOrderRequest(
        ticker=marketTicker,
        action='buy',
        type='limit',
        yes_price=50,
        count=10,
        client_order_id=orderUuid,
        side='yes',
    ))
    print('\nOrder submitted: ')
    pprint(orderResponse)
else:
    print('\nThe exchange is not trading active, no orders will be sent right now.')
```


## Additional resources

The documentation for the underlying web api used by the sdk [can be found here](https://trading-api.readme.io). 


## Author

support@kalshi.com
