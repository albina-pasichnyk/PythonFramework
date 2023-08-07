from sqlalchemy.orm import relationship
from sqlalchemy import Column, INTEGER, VARCHAR, DECIMAL

from HW_21.models.base_model import Base


class Product(Base):
    __tablename__ = 'products'
    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(25))
    price = Column(DECIMAL)
    orders = relationship('Order', back_populates='product')

    def __str__(self):
        return f'id:{self.id}\tname: {self.name}\tprice: {self.price}'
