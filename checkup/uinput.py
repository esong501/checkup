import checkup.ls as ls

def choose_file():
    """ determine which Excel file will be analyzed. User can also input different response
        to quit
    """
    files = ls.get_excel_files()
    print("Excel (.xlsx) files in current directory:")
    for i in range(len(files)):
        print("[{}]: {}".format(i, files[i]))
    print()
    while True:
        file_choice = input("File to analyze (number next to filename) or 'q' to exit: ")
        try:
            n = int(file_choice)
            if n >= len(files) or n < 0:
                print("Index out of range")
                continue
            return files[n]
        except:
            if file_choice != 'q':
                print("Invalid option")
                continue
            return None

def set_threshold():
    """ determines the minimum thresholds for students (participation and correctness). If a 
        student fails to meet either of these thresholds, they will be marked as a student to
        reach out to. These thresholds are returned as a list:

        [<participation threshold>, <correctness threshold>]

    """
    while True:
        part = input("Specify minimum participation percentage (without %): ")
        try:
            intpart = int(part)
            if intpart > 100 or intpart < 0:
                print("Not a percentage (0-100)")
                continue
        except:
            print("Not a percentage")
            continue
        break
    while True:
        acc = input("Specify minimum correctness percentage (without %): ")
        try:
            intacc = int(acc)
            if intacc > 100 or intacc < 0:
                print("Not a percentage (0-100)")
                continue
        except:
            print("Not a percentage")
            continue
        break
    return [intpart, intacc]

# print(choose_file())
# print(set_threshold())
