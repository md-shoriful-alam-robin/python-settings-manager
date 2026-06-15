from employee import Employee

def main():
    # একজন নতুন এমপ্লয়ির অবজেক্ট তৈরি করা
    emp = Employee(
        first_name='John',
        last_name='Doe',
        age=28,
        experience_years=5,
        position='Data Analyst',
        salary=75000,
        employee_code='DEV-2026-JD-001'
    )
    
    # অ্যাড্রেস সেট করা
    emp.set_address('123 Main Street', 'Apartment 4B')

    # আউটপুট প্রিন্ট করা
    print("--- Employee Basic Info ---")
    print(emp.get_info())
    print(emp.get_experience_info())
    
    print("\n--- Employee Card ---")
    print(emp.get_employee_card())
    
    print("\n--- Employee Code Details ---")
    code_details = emp.parse_employee_code()
    print(f"Department: {code_details['department']}")
    print(f"Year Code: {code_details['year_code']}")
    print(f"Initials: {code_details['initials']}")
    print(f"Last Three: {code_details['last_three']}")

if __name__ == "__main__":
    main()