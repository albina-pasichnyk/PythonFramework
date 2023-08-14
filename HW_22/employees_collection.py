from HW_22.base_mongo_class import BaseMongo


class EmployeesCollection(BaseMongo):
    def __init__(self):
        super().__init__('test', 'employees')

    def find_by_first_name(self, first_name: str):
        return self.find_one({'first_name': first_name})

    def find_by_last_name(self, last_name: str):
        return self.find_one({'last_name': last_name})

    def find_by_position(self, position: str):
        return self.find({'position': position})

    def add_employee(self, first_name: str, last_name: str, position: str):
        self.insert_one({'first_name': first_name, 'last_name': last_name, 'position': position})

    def add_employees(self, employees_list: list):
        self.insert_many(employees_list)

    def update_position(self, new_position: str):
        self.update_many({}, {'$set': {'position': new_position}})

    def delete_by_position(self, position: str):
        self.delete_many({'position': position})
