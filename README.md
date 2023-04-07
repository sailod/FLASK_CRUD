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
curl --location --request GET 'http://127.0.0.1:5000/order?id=1'
```