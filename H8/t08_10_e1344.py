def insertion_sort(arr, key_func):
    for i in range(1, len(arr)):
        key_value = arr[i]
        j = i - 1
        while j >= 0 and key_func(arr[j]) > key_func(key_value):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_value
    return arr

n = int(input().strip())
students = []
for _ in range(n):
    surname = input().strip()
    name = input().strip()
    cls = input().strip()
    birthdate = input().strip()
    students.append((cls, surname, name, birthdate))
sorted_students = insertion_sort(students, key_func=lambda student: ((int(student[0][:-1]), student[0][-1]), student[1]))
for student in sorted_students:
    print(" ".join(student))