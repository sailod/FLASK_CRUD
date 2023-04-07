from flask_restful import Resource
from flask import request
from sqlalchemy.orm import Session
from db import engine, AccountModel
from flask import request
from sqlalchemy import select


class Account(Resource):
    def get(self):
        with Session(engine) as session:
            existing_account = session.scalars(select(AccountModel).where(
                AccountModel.id == request.args["id"])).one()
            return existing_account.as_dict(), 200

    def post(self):
        with Session(engine) as session:
            new_account = AccountModel(
                name = request.get_json()["name"],
                usd_balance = request.get_json()["usd_balance"],
                btc_balance = 0
            )

            session.add(new_account)

            session.commit()

            return {"id": new_account.id}, 200
