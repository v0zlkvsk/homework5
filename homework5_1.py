students_rating = {'ivanov_ivan': [10, 11, 7, 9],
                   'moxov_misha': [9, 6, 7, 8],
                   'goroxov_dima': [8, 6, 5, 6],
                   'sidorov_igor': [10, 11, 8, 12]}

def gpa(rating):
    return sum(rating) / len(rating)

best_student = None
worst_student = None
max_rating = 0
min_rating = float('inf')

for student, rating in students_rating.items():
    average = gpa(rating)
    if average > max_rating:
        max_rating = average
        best_student = student

    if average < min_rating:
        min_rating = average
        worst_student = student

print(f"best_student: {best_student}, gpa: {max_rating}")
print(f"worst_student: {worst_student}, gpa: {min_rating}")