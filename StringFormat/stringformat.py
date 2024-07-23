

student_name = input('Enter Your Name:')
student_id= int(input('Enter Your id Card Number '))
print(f'Student Name :{student_name} \n Student id:{student_id}')
print(f'Student Name :{student_name.title()} \n Student id:{student_id}')
print(f'Student Name :{student_name.upper()} \n Student id:{student_id}')

#format method:

print('Student Name:{} \nStudent.id:{}'.format(student_name,student_id))
print('Student Name:{} \nStudent.id:{}'.format (student_id ,student_name))

