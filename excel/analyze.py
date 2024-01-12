import excel.indices as idx

# Some interesting things to note about openpyxl
# docs found here: https://openpyxl.readthedocs.io/en/stable/index.html

# Any cell with no value inside will have a value of None

# ws = wb['Questions Answers']
# print(wb['Questions Answers']['F14'].value)
# # for col in ws.iter_cols():
# #     for cell in col:
# #         if cell in ws[1] and 'Pre-Lecture' in cell.value:
# #             pass
# row_count = ws.max_row
# column_count = ws.max_column
# print(row_count, column_count)

# Summary tab:
# Column F is average, column L is participation
# student records start at row 3

def get_students(wb, thresholds=[50,50]):
    """ takes a openpyxl workbook handle and a set of thresholds (int list. Index 0 is 
        participation, index 1 is correctness). Default thresholds are 50% for both
        participation and correctness. If any students do not meet these thresholds,
        they will be added to a list of students to contact
    """
    # load worksheet
    ws = wb['Summary']
    # instantiate list of students. List will consist of:
    # [[<first name>, <last name>, <email>, <'p' and/or 'c'>]]
    info_ls = []
    for i in range(3,ws.max_row):
        if idx.get_int(ws['F'][i]) < thresholds[1] and idx.get_int(ws['L'][i]) < thresholds[0]:
            info_ls += [[ws['D'][i].value, ws['E'][i].value, ws['C'][i].value, 'pc']]
        elif idx.get_int(ws['F'][i]) < thresholds[1]:
            info_ls += [[ws['D'][i].value, ws['E'][i].value, ws['C'][i].value, 'c']]
        elif idx.get_int(ws['L'][i]) < thresholds[0]:
            info_ls += [[ws['D'][i].value, ws['E'][i].value, ws['C'][i].value, 'p']]
    return info_ls
