import random

from faker import Faker

fake = Faker()


class GenFakeData:
    @staticmethod
    def generate_employee_id():
        return str(random.randint(10000, 99999))

    @staticmethod
    def generate_first_name():
        return fake.first_name()

    @staticmethod
    def generate_middle_name():
        return fake.first_name()

    @staticmethod
    def generate_last_name():
        return fake.last_name()
