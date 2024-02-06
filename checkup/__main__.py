try:
    # making sure users have openpyxl installed
    from openpyxl import load_workbook
except:
    print("openpyxl is not installed.\nPlease make sure pip is installed and run 'pip install openpyxl'")
    exit()
import math
import checkup.ls as ls
import checkup.uinput as uin
import checkup.output as out
import excel.analyze as an

DEFAULT_THRESHOLDS = [50,50]

while True:
    filename = uin.choose_file()
    if filename == None:
        print("Exiting...")
        quit()
    wb = load_workbook(filename)
    while True:
        if DEFAULT_THRESHOLDS[0] == DEFAULT_THRESHOLDS[1]:
            input_str = "Run analysis with default thresholds ({}% for both)? 'y' or 'n': ".format(DEFAULT_THRESHOLDS[0])
        else:
            input_str = "Run analysis with default thresholds ({}% for participation, {}% for correctness)? 'y' or 'n': "\
                .format(DEFAULT_THRESHOLDS[0], DEFAULT_THRESHOLDS[1])
        default = input(input_str)
        if default not in 'yn':
            continue
        break
    try:
        if default == 'y':
            students = an.get_students(wb)
        else:
            students = an.get_students(wb, uin.set_threshold())
    except:
        print("\n**This file does not appear to be a TopHat results file.\nPlease make sure the correct file has been selected.")
        continue
    # if default == 'y':
    #     students = an.get_students(wb)
    # else:
    #     students = an.get_students(wb, uin.set_threshold())
    out.write_csv(filename, students)
