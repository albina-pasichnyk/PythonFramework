from HW_22.base_mongo_class import BaseMongo


class ProductsCollection(BaseMongo):
    def __init__(self):
        super().__init__('test', 'products')

    def find_by_name(self, name: str):
        return self.find_one({'name': name})

    def filter_by_price(self, price: int):
        return self.find({'price': {'$gt': price}})

    def insert_one_product(self, name: str, price: int):
        self.insert_one({'name': name, 'price': price})

    def insert_many_products(self, products_list: list):
        self.insert_many(products_list)

    def update_price_for_product(self, name: str, new_price: int):
        self.update_one({'name': name}, {'$set': {'price': new_price}})

    def delete_by_name(self, name: str):
        self.delete_one({'name': name})
