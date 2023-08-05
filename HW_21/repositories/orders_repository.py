from HW_21.models.order_model import Order
from HW_21.session_db import session


class OrdersRepository:
    def __init__(self):
        self.__session = session

    def get_by_id(self, id_value: int):
        order = self.__session.get(Order, {'id': id_value})
        return order

    def insert_one(self, order: Order):
        self.__session.add(order)

    def insert_many(self, orders: list):
        self.__session.add_all(orders)

    def get_all(self):
        all_orders = self.__session.query(Order).all()
        for order in all_orders:
            print(f'\n {order}')
        return all_orders
