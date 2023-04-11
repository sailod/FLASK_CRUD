This is a simple web trading platform written with Flask  
The goal was to create simple RESTful API using Flask and SQLAlchemy for managing BTC trading requests.  
The API manage requests for just buying assets (eg. BTC) and has the following operations:  
createAccount(name, usd_balance): Creates an account on the application with 0 BTC.  
fetchAccountDetails(account_id): Fetches account details.  
createLimitOrder(account_id, price_limit, amount): Creates a limit order, waiting to be executed when the price limit is reached.  
fetchOrderDetails(order_id): Fetches order details and status.  
The limit orders created execute (be marked as processed) as soon as the market  
price (given by exchange.py) is lower than the price limit set in the order and the account  
details reflect the new USD balance and BTC balance.


### Install

```
pip install -r requirements.txt
```

### Run
This will run the api for btc price, the api for users/orders and a background job that processes and fills orders

```
python launch_all.sh

```

### Test

add account:
```
curl --location --request POST 'http://127.0.0.1:5001/account' \
--header 'Content-Type: application/json' \
--data-raw '{
            "name": "Barak Kochana",
            "usd_balance": 15000
        }'
```
get account:
```
curl --location --request GET 'http://127.0.0.1:5001/account?id=1'
```
add order:
```
curl --location --request POST 'http://127.0.0.1:5001/order' \
--header 'Content-Type: application/json' \
--data-raw '{
            "account_id": 1,
            "price_limit": 15000,
            "amount": 10
        }'

```
get order:
```
curl --location --request GET 'http://127.0.0.1:5001/order?id=1'
```
