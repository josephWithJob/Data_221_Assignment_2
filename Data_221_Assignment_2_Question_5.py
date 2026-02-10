# Assignment 2 Question 5
# Joseph Krosel

# Imports library
import pandas as pd

# Reads the file and saves it
student_information = pd.read_csv('student.csv')

# Creates lists to store information
grade_band = []
average_absences_per_grade_band = [0, 0, 0]
number_of_students_per_grade_band = [0, 0, 0]
number_of_students_with_internet_per_grade_band = [0, 0, 0]

# Sorts through the list to check for conditions and manipulates list
for index in range(0, len(student_information)):
    if student_information.iloc[index, 0] <= 9:
        grade_band.append("Low")
        number_of_students_per_grade_band[0] += 1
        average_absences_per_grade_band[0] += student_information.iloc[index, 1]
        number_of_students_with_internet_per_grade_band[0] += student_information.iloc[index, 3]
    elif student_information.iloc[index, 0] <= 14:
        grade_band.append("Medium")
        number_of_students_per_grade_band[1] += 1
        average_absences_per_grade_band[1] += student_information.iloc[index, 1]
        number_of_students_with_internet_per_grade_band[1] += student_information.iloc[index, 3]
    else:
        grade_band.append("High")
        number_of_students_per_grade_band[2] += 1
        average_absences_per_grade_band[2] += student_information.iloc[index, 1]
        number_of_students_with_internet_per_grade_band[2] += student_information.iloc[index, 3]

student_information['grade_band'] = grade_band
student_information.to_csv('student.csv', index=False)

average_absences_per_grade_band = [average_absences_per_grade_band[0] / number_of_students_per_grade_band[0],
                             average_absences_per_grade_band[1] / number_of_students_per_grade_band[1],
                             average_absences_per_grade_band[2] / number_of_students_per_grade_band[2]]
# Formates the data for the csv
new_data_for_new_file = {'grade_band': ['Low', 'Medium', 'High'],
        'Number of Students': number_of_students_per_grade_band,
        'Average Absences': [average_absences_per_grade_band[0] / number_of_students_per_grade_band[0],
                             average_absences_per_grade_band[1] / number_of_students_per_grade_band[1],
                             average_absences_per_grade_band[2] / number_of_students_per_grade_band[2]],
        'Percentage With Internet': [number_of_students_with_internet_per_grade_band[0] / number_of_students_per_grade_band[0],
                                     number_of_students_with_internet_per_grade_band[1] / number_of_students_per_grade_band[0],
                                     number_of_students_with_internet_per_grade_band[2] / number_of_students_per_grade_band[0]]}

data_frame_for_new_csv = pd.DataFrame(new_data_for_new_file)

# Export the DataFrame to a CSV file
data_frame_for_new_csv.to_csv('student_bands.csv', index=False)