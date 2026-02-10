# Assignment 2 Question 4
# Joseph Krosel

# Imports library
import pandas as pd
import numpy

# Reads the file and saves it
student_information = pd.read_csv('student.csv')

student_grade, student_absences, student_studytime, student_internet, student_activities = [], [], [] ,[] ,[]

# Sorts through the list to check for conditions and manipulates list
for index in range(0, len(student_information)):
    if (student_information.iloc[index, 2] >= 3 and
            student_information.iloc[index, 3] == 1 and
            student_information.iloc[index, 1] <= 5):
        student_grade.append(student_information.iloc[index, 0])
        student_absences.append(student_information.iloc[index, 1])
        student_studytime.append(student_information.iloc[index, 2])
        student_internet.append(student_information.iloc[index, 3])
        student_activities.append(student_information.iloc[index, 4])


# Formates the data for the csv
new_data_for_new_file = {'grade': student_grade,
        'absences': student_absences,
        'studytime': student_studytime,
        'internet': student_internet,
        'activities': student_activities}
data_frame_for_new_csv = pd.DataFrame(new_data_for_new_file)

# Export the DataFrame to a CSV file
data_frame_for_new_csv.to_csv('high_engagement.csv', index=False)

# Uses numpy to get the mean
average_student_grade_for_high_engagement = numpy.mean(student_grade)

# Prints data
print(f"Number of high engagement students: {len(student_grade)}. Average grade: {average_student_grade_for_high_engagement}")
