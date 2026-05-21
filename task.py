from datetime import date

class Homework: 
    def __init__(self, title: str, subject: str, due: date):
        self.title = title 
        self.subject = subject
        self.due = due

    def __str__(self):
        return f'{self.title} in {self.subject} is due on {self.due}'

if __name__ == '__main__':
    print('welcome to Maleah\'s homework manager!')

    # due = date(2026, 5, 21)

    # assignment = Homework('Things Fall Apart Essay', 'English', due)

    # print(str(assignment))

    assignments = []

    choice = input('Would you like to add a new assignment? (yes/no) ')
    while choice.lower() == 'yes':
        title = input('Please enter the title of the assignment: ')
        subject = input('Please enter the subject or class the assignment is due in: ')
        due_date = input('Please enter the due date (YYYY MM DD): ')

        values = due_date.split(' ')
        due = date(int(values[0]), int(values[1]), int(values[2]))
        assignment = Homework(title, subject, due)
        assignments.append(assignment)

        choice = input('Would you like to enter another assignment? (yes/no) ')

    print('Here are your current assignments ...')
    for assignment in assignments:
        print(str(assignment))




