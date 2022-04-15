import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s:')

file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)





class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info("created employee: {} - {}".format(self.fullname, self.email))

    @property
    def email(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
emp1 = Employee('John', 'Smith')
emp2 = Employee('Corey', 'Schafer')
emp3 = Employee('Corey', 'Schafer')

