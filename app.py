import yaml
def load_data(file_path):
Load data from a YAML file.
:param file_path: Path to the YAML file. :return: Data loaded from the YAML file.
188880
with open(file_path, 'r') as file:
data = yaml. safe_load(file) # Load the data as a Python dictionary
return data
def display_students(students):
BE 90 80
Display information about all students.
:param students: List of student dictionaries.
BE 90 80
print("\nAll Students:")
for student in students:
print (f"Name: {student[ 'name']}, Age: {student['age']}, Major:
{student ['major']}, GPA: {student['gpa']}")
def filter_students_by_gpa(students, min_gpa):
Filter and display students with a GPA above the specified minimum.
:param students: List of student dictionaries. :param min_gpa: Minimum GPA for filtering.
filtered_students = [s for s in students if s['gpa'] >= min_gpa]
print(f"\nStudents with GPA >= {min_gpa}:")
if filtered_students:
for student in filtered_students:
print(f"Name: {student[ 'name']}, Age: {student[ 'age']}, Major:
{student[ 'major']}, GPA: {student['gpa']}")
print ("No students found.")
def main ():
  # Load the data from the YAML file
data = load_data('students.yaml')
students = data['students']
# Display all students
display_students(students)
# Filter students by GPA
min_gpa = float(input("\nEnter minimum GPA to filter students: "))
filter_students_by_gpa(students, min_gpa)
if _name_ == "__main_":
   main()
  
