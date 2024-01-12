# Створити структуру даних для студентів з імен та прізвищ, можна випадкових. Придумати структуру даних, щоб вказувати, у якій групі навчається студент (Групи Python, FrontEnd, FullStack, Java). Студент може навчатися у кількох групах. Потім вивести:
# студентів, які навчаються у двох та більше групах
# студентів, які не навчаються на фронтенді
# студентів, які вивчають Python або Java


students = {'Ivanov': ['Python', 'FrontEnd'],
            'Moxov': ['FullStack', 'FrontEnd'],
            'Goroxov': ['Python', 'Java', 'FullStack'],
            'Sidorov': ['FullStack', 'Java'],
            'Morozov': ['FrontEnd', 'Java'],
            'Petrov': ['Python']}

more_than_one = [student for student, groups in students.items() if len(groups) >= 2]
print("Студенти, які навчаються у двох та більше групах:", more_than_one)

not_frotend = [student for student, groups in students.items() if 'FrontEnd' not in groups]
print("Студенти, які не навчаються на FrontEnd:", not_frotend)

python_java = [student for student, groups in students.items() if 'Python' in groups or 'Java' in groups]
print("Студенти, які навчаються на Python або Java:", python_java)