import csv


def load(receipts):
    print('Start csv')
    file = open('receipts.csv', 'w')

    with file:
        fnames = receipts[0].keys()
        writer = csv.DictWriter(file, fieldnames=fnames)

        writer.writeheader()
        for receipt in receipts:
            writer.writerow(receipt)

    print('CSV finished')
