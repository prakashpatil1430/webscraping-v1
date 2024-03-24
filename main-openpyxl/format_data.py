from openpyxl import Workbook

workbook = Workbook()
balance_sheet = workbook.create_sheet("employee", 0)
balance_sheet.append(["EmpName", "Salary", 'Date', 'Multiplier', 'SkillLevel'])  # Header row

# Save the workbook to a file
workbook.save(filename='new_test.xlsx')

# Close the workbook when done
workbook.close()
