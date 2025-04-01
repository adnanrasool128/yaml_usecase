# YAML-Based Student Data Management in Python

## 📌 Overview
This project demonstrates how to work with YAML files in Python. The application reads student information from a YAML file and allows users to view all students and filter them by GPA.

## 🔧 Features
✅ Load student data from a YAML file
✅ Display all student records
✅ Filter students based on a minimum GPA
✅ Interactive command-line interface

## ⚙️ Prerequisites
Before running the project, ensure you have the following installed:
- **Python 3.7+** [Download here](https://www.python.org/downloads/)
- **PyYAML library** (install using `pip install pyyaml`)

## 📂 Project Structure
```
📁 project-directory/
 ├── 📄 students.yaml    # YAML file containing student data
 ├── 📄 app.py           # Python script to read and process data
 ├── 📄 README.md        # Project documentation
```

## 🛠 Installation & Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```
2. **Create a Virtual Environment (Optional)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate  # Windows
   ```
3. **Install Dependencies**
   ```bash
   pip install pyyaml
   ```
![img](https://github.com/AnugyaAg/yaml_usecase/blob/f2ad796d42e51f3700be3b9a2c834075c77762d9/images/IMG1.png)
## 📄 YAML File (students.yaml)
Create a `students.yaml` file with the following structure:
```yaml
students:
  - name: Alice
    age: 21
    major: Computer Science
    gpa: 3.8
  - name: Bob
    age: 22
    major: Mathematics
    gpa: 3.5
  - name: Charlie
    age: 20
    major: Physics
    gpa: 3.9
```

## 🚀 Running the Application
Execute the script using the following command:
```bash
python app.py
```

## 📝 Usage
1. The program will first display all students.
2. It will then prompt you to enter a minimum GPA to filter students.
3. Filtered results will be displayed accordingly.

## 📌 Example Output
```
All Students:
Name: Alice, Age: 21, Major: Computer Science, GPA: 3.8
Name: Bob, Age: 22, Major: Mathematics, GPA: 3.5
Name: Charlie, Age: 20, Major: Physics, GPA: 3.9

Enter minimum GPA to filter students: 3.6

Students with GPA >= 3.6:
Name: Alice, Age: 21, Major: Computer Science, GPA: 3.8
Name: Charlie, Age: 20, Major: Physics, GPA: 3.9
```
![img](https://github.com/AnugyaAg/yaml_usecase/blob/f2ad796d42e51f3700be3b9a2c834075c77762d9/images/IMG2.png)
