from extract import get_data
from load import load


if __name__ == "__main__":
    receipts = get_data()
    load(receipts)
