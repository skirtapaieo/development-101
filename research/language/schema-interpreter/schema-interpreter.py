
import json

customer_schema = {
    'id': 'integer',
    'name': 'string',
    'email': 'string',
    'is_active': 'boolean'
}

def encode_customer(customer):
    for field, data_type in customer_schema.items():
        if type(customer[field]).__name__ != data_type:
            return "Invalid Data Type for Field: " + field
    return json.dumps(customer)

def decode_customer(customer_str):
    customer = json.loads(customer_str)
    for field, data_type in customer_schema.items():
        if type(customer[field]).__name__ != data_type:
            return "Invalid Data Type for Field: " + field
    return customer

# Create a customer
customer_1 = {
    'id': 1,
    'name': 'John Doe',
    'email': 'john.doe@example.com',
    'is_active': True
}

# Encode the customer
encoded_customer = encode_customer(customer_1)
print("Encoded:", encoded_customer)

# Decode the customer
decoded_customer = decode_customer(encoded_customer)
print("Decoded:", decoded_customer)

