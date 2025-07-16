import random
from product_pipeline import copy_product_data

def copy_customer_data():
    customer_count = random.randint(580, 700)
    print(f"\n Customer records: {customer_count}")

    if customer_count > 500:
        print(" Copying customer data to ADLS...")
        if customer_count > 600:
            copy_product_data(customer_count)
    else:
        print(" Skipping (count < 500)")

if __name__ == "__main__":
    copy_customer_data()  