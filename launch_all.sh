#!/bin/bash

echo "Starting btc price api on port 5000..."
nohup python exchange.py > btc_price_api.log &
echo "Started"

echo "Starting trading platform api on port 5001..."
nohup python api/trading_platform.py > trading_platform_api.log &
echo "Started"

echo "Starting orders handler daemon..."
nohup python process_orders.py > order_processor.log &
echo "Started"
