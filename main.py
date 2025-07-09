
class Student:
    def __init__(self, full_name, age, birthday, gender):
        self.full_name = full_name
        self.age = age
        self.birthday = birthday
        self.gender = gender
        self.courses = []

    def __call__(self, course_obj):
        self.courses.append(course_obj)
        return f"{course_obj} added to {self.full_name}'s courses"

    def __len__(self):
        return len(self.courses)

    def __iter__(self):
        return iter(self.courses)

    def __contains__(self, course):
        return any(c == course for c in self.courses)

    def __add__(self, other):
        full_name = f"{self.full_name} + {other.full_name}"
        age = (self.age + other.age) // 2
        birthday = self.birthday
        gender = self.gender
        new_student = Student(full_name, age, birthday, gender)
        new_student.courses = self.courses + other.courses
        return new_student

    def __sub__(self, other):
        new_student = Student(self.full_name, self.age, self.birthday, self.gender)
        new_student.courses = [course for course in self.courses if course not in other.courses]
        return new_student

    def __mul__(self, other):
        return len(self.courses) * len(other.courses)

    def __truediv__(self, other):
        return len(self.courses) / len(other.courses) if len(other.courses) != 0 else 0

    def __iadd__(self, other):
        if isinstance(other, str):
            self.courses.append(other)
        elif isinstance(other, list):
            self.courses.extend(other)
        return self

    def __isub__(self, other):
        if isinstance(other, str) and other in self.courses:
            self.courses.remove(other)
        return self

    def __imul__(self, other):
        self.courses *= other
        return self

    def __itruediv__(self, other):
        if isinstance(other, int) and other > 0:
            self.courses = self.courses[:len(self.courses) // other]
        return self

    def __pow__(self, power):
        self.courses = [course * power for course in self.courses]
        return self

    def __repr__(self):
        return f"<Student: {self.full_name}, Age: {self.age}, Courses: {self.courses}>"


Student1 = Student("Ali Valiyev", 20, "2005-05-06", "male")
s2 = Student("Laylo Karimova", 22, "2003-09-15", "female")

print(Student1("Math"))
print(Student1("Physics"))
print(s2("Biology"))
print(s2("Chemistry"))

print("Courses in Student1:", Student1.courses)
print("Courses in s2:", s2.courses)

print("Math in Student1:", "Math" in Student1)
print("Chemistry in Student1:", "Chemistry" in Student1)

print("Length of Student1:", len(Student1))

print("Iterating over Student1:")
for course in Student1:
    print("-", course)

s3 = Student1 + s2
print("Student1 + s2:", s3)

s4 = s3 - s2
print("s3 - s2:", s4)

print("Student1 * s2:", Student1 * s2)
print("Student1 / s2:", Student1 / s2)

Student1 += "English"
print("Student1 after += 'English':", Student1)

Student1 -= "Physics"
print("Student1 after -= 'Physics':", Student1)

Student1 *= 2
print("Student1 after *= 2:", Student1)

Student1 /= 2
print("Student1 after /= 2:", Student1)

Student1 **= 2
print("Student1 after **= 2:", Student1)

