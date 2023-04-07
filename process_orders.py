from sqlalchemy.orm import Session
from db import engine, OrderModel, OrderStatus
import time
import requests
from sqlalchemy import  and_
from sqlalchemy.orm import query

import logging

logging.basicConfig(level=logging.INFO)


def btc_price():
    btc_price_api_response = requests.get('http://127.0.0.1:5000/btc-price')
    return btc_price_api_response.json()["price"]


while True:
    with Session(engine) as session:
        try:
            latest_btc_price = btc_price()
        except Exception as e:
            logging.error(f"failed to fetch btc price: {e}")
            continue
        # We querying and processing the orders one by one in order to make this script
        # scalable while maintaining data consistency with transactions (achieved by with_for_update)
        order_to_be_filled = session.query(OrderModel).filter(
            latest_btc_price < OrderModel.price_limit, OrderModel.status == OrderStatus.waiting).with_for_update().first()
        if order_to_be_filled:
            order_total_price = order_to_be_filled.amount * latest_btc_price
            if order_to_be_filled.account.usd_balance < order_total_price:
                continue
            order_to_be_filled.account.usd_balance -= order_total_price
            order_to_be_filled.account.btc_balance += order_to_be_filled.amount
            order_to_be_filled.status = OrderStatus.processed
            session.commit()
            logging.info(f"Filled order(id): {order_to_be_filled}")

    time.sleep(0.1)
