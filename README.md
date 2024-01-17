# checkup
Tool for evaluating student performance on TopHat

## Dependencies
- openpyxl
  - Installing openpyxl is as simple as running `pip install openpyxl`
  - Alternatively, you can follow the tutorial [here](https://openpyxl.readthedocs.io/en/stable/tutorial.html).
 
## Usage
Upon cloning this repository, checkup can be run by navigating to the repo and running
    
    python -m checkup

You may find that your Python interpreter is named with a version number. In most cases you would replace `python` with
`python3` (though you may find that your interpreter is named something else).

checkup is able to run from other directories, but you must set the `PYTHONPATH` variable to this repo's directory. 
This can be done in various ways on [Windows](https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-so-it-finds-my-modules-packages) 
and in Bash can be done as such:

    PYTHONPATH=/<path to checkup repo> python -m checkup

### Functionality
checkup compiles a csv file of students who are not meeting certain thresholds of accuracy or participation on
TopHat quizzes. The user specifies a TopHat results file and percentage thresholds (if desired) and checkup will
return any students (first name, last name, email) who are not currently meeting those thresholds.

Once checkup is started, it will check in the current working directory for Excel (.xlsx) files, as exported results
from TopHat are stored in this format. If no Excel files exist, checkup will terminate. Otherwise, checkup will display
the current files in the directory and prompt the user to select which file to analyze, as well as ask the user if they
would like to analyze this file with the default thresholds or set their own. If the file selected is a TopHat
results file, checkup will go into the Summary tab of the sheets and add each student to a csv file. This csv file will be
created in the current working directory with the name `<name of Excel file>.csv`. For example, if the name of our Excel
file is `TopHat_results_week3.xlsx`, then our csv file will be named `TopHat_results_week3.xlsx.csv`.

If you would like to change the default thresholds for quicker execution, you can edit the `DEFAULT_THRESHOLDS` variable
within `checkup/__main__.py`.

### How do we read TopHat's result files?
In our sheet, columns A-E hold student info
A - Tophat Username
B - Student ID
C - Email they registered for Tophat with
D - First Name
E - Last Name

Within the "Summary" tab is where many of the quantifiable metrics exist.
- Average % is the score of all questions that hold point value.
  - At the time of development \(Fall '23\), we only take into account whether or not
    students answered these questions. As such, any answer will
    gain points.
  - Some questions do not hold point value. If students don't
    answer these questions, they do NOT deduct from this field.
    - In other words, this is Grade / Weight.
- Grade is the score this student has accumulated from each question.
- Weight is the total score a student can get from each question.
- Participation is a percentage of how many questions a student has
  answered.
  - This includes questions that hold no point values.
- Correct answers show how many questions students got right.
  - This only applies to questions that have correct answers
    associated with them. For CS 111, these are only
    prelecture questions.
- Incorrect answers is the inverse of the previous field.
- Missed items is how many questions this student did not submit an
  answer for.
