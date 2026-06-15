class Employee:
    def __init__(self, first_name, last_name, age, experience_years, position, salary, employee_code):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"
        self.age = age
        self.experience_years = experience_years
        self.position = position
        self.salary = salary
        self.employee_code = employee_code
        self.address = ""

    def set_address(self, street, apartment):
        self.address = f"{street}, {apartment}"

    def get_info(self):
        return f"{self.full_name} is {self.age} years old"

    def get_experience_info(self):
        return f"Experience: {self.experience_years} years"

    def get_employee_card(self):
        return f'Employee: {self.full_name} | Age: {self.age} | Position: {self.position} | Salary: ${self.salary}'

    def parse_employee_code(self):
        """আপনার কোডের স্ট্রিং স্লাইসিং পার্টটি এখানে ডাইনামিক করা হয়েছে"""
        return {
            "department": self.employee_code[0:3],
            "year_code": self.employee_code[4:8],
            "initials": self.employee_code[9:11],
            "last_three": self.employee_code[-3:]
        }