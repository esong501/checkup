# checkup
Tool for evaluating student performance on Tophat

## Dependencies
- openpyxl
  - Installing openpyxl is as simple as running `pip install openpyxl`
  - Alternatively, you can follow the tutorial [here](https://openpyxl.readthedocs.io/en/stable/tutorial.html).

## How do we read TopHat's result files?
In our "Questions Answers" sheet, columns A-E hold student info
A - Tophat Username
B - Student ID
C - Email they registered for Tophat with
D - First Name
E - Last Name

Within the questions tab is where many of the quantifiable metrics exist.
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