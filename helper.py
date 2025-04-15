from faker import Faker

faker = Faker('ru_RU')

def generate_reg_data():
    name = faker.first_name()
    last_name = faker.last_name()
    city = faker.city()
    number = faker.random_number(digits=12)
    return name, last_name, city, number