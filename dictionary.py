phone_book = {}

phone_book['J'] = "330 763 1234"
phone_book['A'] = "330 651 1251"
phone_book['B'] = "330 417 4269"
phone_book['C'] = "330 555 4613"
phone_book['D'] = "330 612 2351"

for key in phone_book.keys():
    print(key)

for key, value in phone_book.items():
    print(key, value)