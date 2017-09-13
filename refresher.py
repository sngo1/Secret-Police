# Samantha Ngo
# Softdev - pd7
# HW#2
# 2017-09-12

import random;

CLASSES = {

        7: [ 'Helen', 'Shakil', 'Eric', 'Jennifer Y', 'Jennifer Z', 'Arif', 'Queenie', 'Jawadul', 'Shaina', 'Vivien', 'Brian', 'Naotaka', 'Bayan', 'Adam', 'Caleb', 'Terry', 'Jason', 'Alessandro', 'Samantha', 'Carol', 'Joyce', 'Shannon', 'Charles', 'Taylor', 'Kelly', 'Leo', 'Khyber', 'Ibnul', 'Eugene', 'Yuyang', 'Karina', 'Tiffany', 'Holden', 'Michael'],

        8: ['Masha', 'Adrian', 'David', 'Eric', 'Josh', 'Jerome', 'Henry', 'Jackie', 'Giorgio', 'Karen', 'Sonal', 'Xavier', 'Bermet', 'Alex', 'Iris', 'Manahal', 'Donia', 'Md', 'Connie', 'Lisa', 'Xing', 'Angelica', 'Angel', 'Augie', 'Dimitriy', 'Yiduo', 'Gordon', 'Tiffany', 'Clive', 'Jonathan', 'Sasha', 'Daniel'],

        9: [ 'Yu Qi', 'Michela', 'Kristin', 'Fabiha', 'Maxim', 'Marcus', 'Ish', 'James', 'Ryan', 'Edward', 'Adeeb', 'Jake', 'Cynthia', 'Kevin', 'Levi', 'Edmond', 'Kyle', 'Andrew', 'Max', 'Jenny', 'Philip', 'Shan', 'Mansour', 'Ray', 'Jake', 'Ida', 'Kerry', 'Stanley', 'Jackie', 'William', 'Tina', 'Michael']

}

num_students_pd7 = len(CLASSES[7]);
num_students_pd8 = len(CLASSES[8]);
num_students_pd9 = len(CLASSES[9]);

""" Triple quotes denote a block comment. """

# WITHOUT having to provide the dictionary:
def get_rand_student(period):
    """
	if period == 7:
		student_number = random.randint(0,num_students_pd7 - 1);
	elif period == 8:
	    student_number = random.randint(0,num_students_pd8 - 1);
	elif period == 9:
		student_number = random.randint(0,num_students_pd9 - 1);
	else:
		return "Period does not exist.";
	return CLASSES[period][student_number];
        """
    try:
        return CLASSES[period][random.randint(0, len(CLASSES[period]) - 1)]
    except:
        return "Period does not exist."
    

# Test Code
print(get_rand_student(7));
print(get_rand_student(7));
print(get_rand_student(8));
print(get_rand_student(8));
print(get_rand_student(9));
print(get_rand_student(9));
print(get_rand_student(10));
