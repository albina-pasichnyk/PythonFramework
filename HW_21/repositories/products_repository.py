from sqlalchemy import select, label

from HW_21.models.order_model import Order
from HW_21.models.product_model import Product
from HW_21.session_db import session


class ProductsRepository:
    def __init__(self):
        self.__session = session

    def get_by_id(self, id_value: int):
        product = self.__session.get(Product, {'id': id_value})
        return product

    def get_all(self):
        all_products = self.__session.query(Product).all()
        for product in all_products:
            print(f'\n {product}')
        return all_products

    def insert_one(self, product: Product):
        self.__session.add(product)

    def insert_many(self, products: list):
        self.__session.add_all(products)

    def get_products_order_report(self):
        sql_query = select(Product.name, Product.price, Order.quantity,
                           label('total_price', Product.price * Order.quantity)).select_from(Product).join(Order,
                                                                                                           Product.id == Order.product_id)
        results = self.__session.execute(sql_query)
        return results
