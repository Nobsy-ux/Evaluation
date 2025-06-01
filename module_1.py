def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

def main():
    students = [
        {"name": "Alice", "grades": [88, 92, 79]},
        {"name": "Bob", "grades": [75, 70, 68]},
        {"name": "Charlie", "grades": [95, 100, 98]},
        {"name": "Daisy", "grades": [58, 62, 55]},
    ]
    process_all_students(students)

