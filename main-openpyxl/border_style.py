import openpyxl
from openpyxl.styles import Border, Side

# Create a new workbook
wb = openpyxl.load_workbook('example.xlsx')

balance_worksheet = wb['Balance']

# Define border styles
thin_border = Border(left=Side(style='thin'),
                     right=Side(style='thin'),
                     top=Side(style='thin'),
                     bottom=Side(style='thin'))

medium_border = Border(left=Side(style='medium'),
                       right=Side(style='medium'),
                       top=Side(style='medium'),
                       bottom=Side(style='medium'))

double_border = Border(left=Side(style='double'),
                       right=Side(style='double'),
                       top=Side(style='double'),
                       bottom=Side(style='double'))

# Apply border styles to cells
balance_worksheet['A1'].border = thin_border
balance_worksheet['B1'].border = medium_border
balance_worksheet['C1'].border = double_border

# Save the workbook
wb.save("example.xlsx")
