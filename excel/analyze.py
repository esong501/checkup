import excel.indices as idx
import statistics as stat

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

def get_prelecture_qs(ws):
    """ gets number of the pre-lecture questions given a worksheet
    """
    qs = 0
    for i in range(idx.col_to_index('M'), ws.max_column + 1):
        if "Pre-Lecture" not in ws[idx.index_to_col(i)][0].value:
            continue
        qs += 1
    return qs

def get_lecture_qs(ws):
    """ gets number of the pre-lecture questions given a worksheet
    """
    return idx.col_to_index(ws.max_column) - idx.col_to_index('M') - get_prelecture_qs(ws)

def sort_key(e):
    if '*' in e[0]:
        return e[4]
    return e[3]

def get_percent(ws, i, qs):
    """ given a worksheet and an index for the student, we'll calculate
        how many prelecture questions were answered correctly. This is
        done by taking the number of pre-lecture questions and using it
        as the denominator for the value in Correct
    """
    return (idx.get_int(ws['M'][i])/qs) * 100

def get_students(wb, use_thres=True, thresholds=[50,50]):
    """ takes a openpyxl workbook handle and a set of thresholds (int list. Index 0 is 
        participation, index 1 is correctness). Default thresholds are 50% for both
        participation and correctness. If any students do not meet these thresholds,
        they will be added to a list of students to contact
    """
    # load worksheet
    try:
        ws = wb['Summary']
    except:
        raise Exception()
    try:
        wsq = wb['Questions']
    except:
        raise Exception()
    # instantiate list of students. List will consist of:
    # [[<first name>, <last name>, <email>, <'p' and/or 'c'>]]

    info_ls = []
    pqs = get_prelecture_qs(wsq)
    percents = []
    for i in range(2,ws.max_row):
        percents += [get_percent(ws, i, pqs)]
    if use_thres:
        for i in range(len(percents)):
            if percents[i] < thresholds[1] and idx.get_int(ws['L'][i+2]) < thresholds[0]:
                info_ls += [[ws['D'][i+2].value, ws['E'][i+2].value, ws['C'][i+2].value, 'pc']]
            elif percents[i] < thresholds[1]:
                info_ls += [[ws['D'][i+2].value, ws['E'][i+2].value, ws['C'][i+2].value, 'c']]
            elif idx.get_int(ws['L'][i+2]) < thresholds[0]:
                info_ls += [[ws['D'][i+2].value, ws['E'][i+2].value, ws['C'][i+2].value, 'p']]
    else:
        median = stat.median(percents)
        average = stat.mean(percents)
        quarts = stat.quantiles(percents)
        info_ls += [['statistics','median',median,'average',average]]
        good = []
        med = []
        bad = []
        for i in range(len(percents)):
            if percents[i] < quarts[0]:
                bad += [['***', ws['D'][i+2].value, ws['E'][i+2].value, ws['C'][i+2].value, percents[i]]]
            elif percents[i] < quarts[1]:
                med += [['*', ws['D'][i+2].value, ws['E'][i+2].value, ws['C'][i+2].value, percents[i]]]
            else:
                good += [[ws['D'][i+2].value, ws['E'][i+2].value, ws['C'][i+2].value, percents[i]]]
        good.sort(key=sort_key)
        med.sort(key=sort_key)
        bad.sort(key=sort_key)
        info_ls += bad + med + good
    return info_ls
