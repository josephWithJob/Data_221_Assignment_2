# Assignment 2, Question 10
# Joseph Krosel

def find_lines_containing(filename, keyword):
    # Finds the file
    with open(filename, 'r') as file:
        file_lines = file.readlines()

    # Cycles through the file looking for the keyword
    line_count = 1
    lines_in_file_containing_keyword = []
    for line_text in file_lines:
        if keyword in line_text.split():
            # Adds the required information into a list
            lines_in_file_containing_keyword.append([line_count, line_text])
        line_count += 1

    # prints first three
    for index in range(0, 3):
        print(lines_in_file_containing_keyword[index])

    return lines_in_file_containing_keyword
