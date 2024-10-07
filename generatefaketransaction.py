import random
from faker import Faker
import string

def generate_transaction_id(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_fake_transactions(n=10):
    faker = Faker()
    transactions = []

    for _ in range(n):
        transaction = {
            "transaction_id": generate_transaction_id(),
            "date": faker.date(),
            "amount": round(random.uniform(100.00, 5000.00), 2)
        }
        transactions.append(transaction)

    return transactions

def main():
    transactions = generate_fake_transactions()
    for transaction in transactions:
        print(f"Transaction ID: {transaction['transaction_id']}, Date: {transaction['date']}, Amount: ${transaction['amount']}")

if __name__ == "__main__":
    main()
