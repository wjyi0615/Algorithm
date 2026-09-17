def solution(phone_book):
    book = set(phone_book)

    for number in phone_book:
        for i in range(1, len(number)):
            if number[:i] in book:
                return False

    return True