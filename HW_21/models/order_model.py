from sqlalchemy.orm import relationship
from sqlalchemy import Column, INTEGER, ForeignKey

from HW_21.models.base_model import Base


class Order(Base):
    __tablename__ = 'orders'
    id = Column(INTEGER, primary_key=True)
    product_id = Column(INTEGER, ForeignKey('products.id'))
    quantity = Column(INTEGER)
    product = relationship('Product', back_populates='orders')

    def __str__(self):
        return f'id:{self.id}\tproduct_id: {self.product_id}\tquantity: {self.quantity}'
