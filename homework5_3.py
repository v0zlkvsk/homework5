# Написати функцію переведення розмірів жіночої білизни з міжнародної у решту. Всередині функції потрібно просто звертатися до правильно складеного словника.


def size_conversion(inter_size):
    size_lst = {
        'XXS': {'DE': 36, 'US': 8, 'FR': 38, 'UK': 24},
        'XS': {'DE': 38, 'US': 10, 'FR': 40, 'UK': 26},
        'S': {'DE': 40, 'US': 12, 'FR': 42, 'UK': 28},
        'M': {'DE': 42, 'US': 14, 'FR': 44, 'UK': 30},
        'L': {'DE': 44, 'US': 16, 'FR': 46, 'UK': 32},
        'XL': {'DE': 46, 'US': 18, 'FR': 48, 'UK': 34},
        'XXL': {'DE': 48, 'US': 20, 'FR': 50, 'UK': 36},
        'XXXL': {'DE': 50, 'US': 22, 'FR': 52, 'UK': 38},
    }

    if inter_size in size_lst:
        sizes = size_lst[inter_size]
        other_sizes = {
            'DE': sizes['DE'],
            'US': sizes['US'],
            'FR': sizes['FR'],
            'UK': sizes['UK'],
        }
        return other_sizes
    else:
        return "Розміру не існує"


inter_size = input("Міжнародний розмір (наприклад XS): ")

other_sizes = size_conversion(inter_size)

if other_sizes != "Розмір не знайдено":
    print(f"Німеччина (DE): {other_sizes['DE']}")
    print(f"США (US): {other_sizes['US']}")
    print(f"Франція (FR): {other_sizes['FR']}")
    print(f"Великобританія (UK): {other_sizes['UK']}")
