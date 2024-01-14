company = {}

while True:
    name = input()

    if name == "End":
        break

    company_name, employee_id = name.split(" -> ")

    if company_name not in company:
        company[company_name] = []
    if employee_id not in company[company_name]:
        company[company_name].append(employee_id)

for companies, empolyee in company.items():
    print(companies)
    for employees in empolyee:
        print(f"-- {employees}")
