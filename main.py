from openpyxl import load_workbook
wb = load_workbook('TopHatExport-517856-AdvancedExport-20230920132707.xlsx')
print(wb['Summary']['A4'].value)