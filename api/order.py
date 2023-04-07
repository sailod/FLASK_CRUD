from flask_restful import Resource
from flask import request
from sqlalchemy.orm import Session
from db import engine, OrderModel, OrderStatus
from flask import request
from sqlalchemy import select


class Order(Resource):
    def get(self):
        with Session(engine) as session:
            existing_order = session.scalars(
                select(OrderModel).where(OrderModel.id.is_(request.args["id"]))).one()
            return existing_order.as_dict(), 200

    def post(self):
        with Session(engine) as session:

            new_order = OrderModel(
                account_id=request.get_json()["account_id"],
                price_limit=request.get_json()["price_limit"],
                amount=request.get_json()["amount"],
                status=OrderStatus.waiting
            )
            session.add(new_order)

            session.commit()

            return {"id": new_order.id}, 200
