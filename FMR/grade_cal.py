def grade_calculator(score):
    if score >= 90:
        return 'O Grade'
    elif score >= 80:
        return 'A Grade'
    elif score >= 70:
        return 'B Grade'
    elif score >= 60:
        return 'C Grade'
    else:
        return 'Fail'


name = input("Enter student's name: ")
maths_score = float(input("Enter Physics score: "))
physics_score = float(input("Enter Maths score: "))
chemistry_score = float(input("Enter Chemistry score: "))
English_score=float(input("Enter English score"))
Tamil_score=float(input("Enter Tamil Score"))
average_mark = (maths_score + physics_score + chemistry_score +English_score +Tamil_score) / 5
grade = grade_calculator(average_mark)

student_details = {
    'Name': name,
    'Maths Score': maths_score,
    'Physics Score': physics_score,
    'Chemistry Score': chemistry_score,
    'English Score':English_score,
    'Tamil_Score':Tamil_score,
    'Average Score': average_mark,
    'Grade': grade
}


print("\nStudent Grade Report:")
for key, value in student_details.items():
    print(f"{key}: {value}")

if __name__ =="__calculate_grade__":
 grade_calculator()