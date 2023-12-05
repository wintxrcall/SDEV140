# Renee Guldi
# SDEV140 - MJovanovich
# December 4, 2023

from datetime import datetime

def read_file_into_lists(file_name):
    # initialize an empty list - we will return this from the function call
    parsed_vals = []
    # 
    with open(file_name, 'r') as input_file:
        rows = input_file.readlines()

        for row in rows:
            items = row.split(',')

            for i in range(0, len(items), 1):
                items[i] = items[i].strip()

            parsed_vals.append(items)

    return parsed_vals

##
def check_header_row(header_row, expected_fields):
    if len(header_row) != len(expected_fields):
        return False
        
    for i in range(0, len(expected_fields), 1):
        if header_row[i] != expected_fields[i]:
            return False
    return True

##
def clean_validate_data_rows(data_rows, first_data_line_number):
    cleaned_data = []

    line_number = first_data_line_number

    for data_row in data_rows:
        student_id = ''
        student_FN = ''
        student_LN = ''
        DOB = ''
        grade = ''

        ## student ID 
        student_id = data_row[0]
        if len(student_id) != 6:
            raise ValueError(f"Error: ID must be a c followed by FIVE(5) numerical characters.")
        ## name
        name_parts = data_row[1].split(' ')
        if len(name_parts) != 2:
            raise ValueError(f"Error on line {line_number}: First and Last name not provided")
        
        student_FN = name_parts[0]
        student_LN = name_parts[1]

        ## DOB
        DOB = data_row[2]
        if DOB != '':
            try:
                date = datetime.strptime(DOB, '%Y-%m-%d')
            except ValueError as e:
                raise(f"Error on line {line_number}: Invalid date. Expecting: YYYY-MM-DD.")
        ## GRADE
        valid_grades = ['A', 'B', 'C', 'D', 'F']
        grade = data_row[3]
        if grade.upper() not in valid_grades:
            raise ValueError(
                    f"Error on line {line_number}: Grade not valid.")

        cleaned_data.append([student_id, student_LN, student_FN, DOB, grade])
        line_number += 1
    return cleaned_data

def display_output(output_rows):
    # for output_row in output_rows:
    #     print(output_row)
    print('Student ID, Last Name, First Name, Date of Birth, Grade')
    print('-------------------------------------------------------')

    for output_row in output_rows:
        print("{:<20}{:<20}{:<20}{:<20}{:<20}".format(
            output_row[0],
            output_row[1],
            output_row[2],
            output_row[3],
            output_row[4],
        ))

def remove_duplicate_records(records):
    deduped_list = []
    added_items = []

    for record in records:
        if record[0] not in added_items:
            added_items.append(record[0])
            deduped_list.append(record)

    return deduped_list

if __name__ == "__main__":
    
    STUDENTS_FILE_PATH = 'students.csv'
    HEADER_FIELDS = ["id", "name", "dob", "grade"]
    
    try:
         parsed_data = read_file_into_lists(STUDENTS_FILE_PATH)
    
    except FileNotFoundError as e:
         print(f"File not found: "+ str(e))
         exit()

    if len(parsed_data) == 0:
        print("Empty file.")
        exit()    

    header_row = parsed_data[0]

    if check_header_row(header_row, HEADER_FIELDS):
        print('Header row not in expected format. Expected: ' + str(HEADER_FIELDS))
        exit()

    data_rows = parsed_data[1:]

    cleaned_data = []
    try: 
        cleaned_data = clean_validate_data_rows(data_rows, 2)
    except ValueError as e:
        print(e)
        exit()

    cleaned_data = remove_duplicate_records(cleaned_data)

    display_output(cleaned_data)