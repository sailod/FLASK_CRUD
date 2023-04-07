from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from typing import List
import enum

from sqlalchemy import create_engine
engine = create_engine("sqlite:///trading_platform.db")


class OrderStatus(enum.Enum):
    waiting = "waiting"
    processed = "processed"

# Iam including here models for simplicity should be seperated to its own file/directory


class Base(DeclarativeBase):
    pass

    def as_dict(self):
        return {c.name: getattr(self, c.name) if type(getattr(self, c.name)) != OrderStatus else getattr(self, c.name).value for c in self.__table__.columns}


class AccountModel(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    usd_balance: Mapped[int] = mapped_column(Integer)
    btc_balance: Mapped[int] = mapped_column(Integer)

    orders: Mapped[List["OrderModel"]] = relationship(
        back_populates="account", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"Account(id={self.id!r}, name={self.name!r}"


class OrderModel(Base):
    __tablename__ = "user_order"

    id: Mapped[int] = mapped_column(primary_key=True)
    price_limit: Mapped[int] = mapped_column(Integer)
    amount: Mapped[int] = mapped_column(Integer)
    status: Mapped["OrderStatus"] = mapped_column(Enum(OrderStatus))
    account_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    account: Mapped["AccountModel"] = relationship(back_populates="orders")

    def __repr__(self) -> str:
        return f"Order(id={self.id!r}, account_id={self.account_id!r})"


Base.metadata.create_all(engine)
