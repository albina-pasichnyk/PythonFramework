from HW_21.models.order_model import Order
from HW_21.repositories.orders_repository import OrdersRepository
from HW_21.models.product_model import Product
from HW_21.repositories.products_repository import ProductsRepository

product_repo = ProductsRepository()
order_repo = OrdersRepository()

products = [
    Product(name='product_1', price=10),
    Product(name='product_2', price=9.9),
    Product(name='product_3', price=50),
    Product(name='product_4', price=15),
    Product(name='product_5', price=99.9)
]
product_repo.insert_many(products)
product_repo.get_all()

orders = [
    Order(product_id=1, quantity=3),
    Order(product_id=2, quantity=5),
    Order(product_id=3, quantity=1),
    Order(product_id=3, quantity=15),
    Order(product_id=5, quantity=2)
]
order_repo.insert_many(orders)

report = product_repo.get_products_order_report()
for row in report:
    print(row)
