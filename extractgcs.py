from faker import Faker
import random
from google.cloud import storage

def generate_employee_data(num_employees):
    fake = Faker()
    employees = []

    for _ in range(num_employees):
        employee = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "job_title": fake.job(),
            "address": fake.street_address(),
            "city": fake.city(),
            "state": fake.state_abbr(),
            "zip_code": fake.zipcode(),
            "phone_number": fake.phone_number(),
            "date_of_birth": fake.date_of_birth(),
            "ssn_last_four": fake.ssn()[-4:],  # Last four digits of SSN for demo purposes
            "password": fake.password(),
            "salary": random.randint(30000, 100000)
        }
        employees.append(employee)

    return employees

def write_to_gcs(bucket_name, file_name, data):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    # Convert data to a string (e.g., JSON or CSV)
    data_str = str(data)

    blob.upload_from_string(data_str)

if __name__ == "__main__":
    num_employees = 100
    employee_data = generate_employee_data(num_employees)

    # Replace 'your-bucket-name' with your actual bucket name
    bucket_name = "bucket_employeedata"
    file_name = "employee_data1.txt"

    write_to_gcs(bucket_name, file_name, employee_data)