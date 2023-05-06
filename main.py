from faker import Faker
import csv
import time
from tqdm import tqdm

def generate_fake_data(num_rows):
    fake = Faker()
    fieldnames = ['name', 'address', 'email', 'phone_number', 'job']
    with open('fake_data.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for i in tqdm(range(num_rows)):
            row = {
                'name': fake.name(),
                'address': fake.address(),
                'email': fake.email(),
                'phone_number': fake.phone_number(),
                'job': fake.job()
            }
            writer.writerow(row)
            time.sleep(0.1)

generate_fake_data(10)