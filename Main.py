import sys
import re
from pathlib import Path


def parseGrade(path):
    """
    Obtain grades from a file and parse them.

    :param path: file containing grades
    :return: Dictionnary {course_id:[grade_distribution]}
    """

    expected_grade = 16

    # Define regex for parsing
    course_id_regex = re.compile("^[A-Z]{4}\s[0-9]{3}$")
    gpa_regex = re.compile("^[0-9]{1,2}\.[0-9]{2,3}$")
    digit_regex = re.compile("^\d+$")

    try:
        semester_result = dict()
        course_id = ""
        course_name = ""
        course_grade = list()

        # Read through the file
        fin = open(path, "r")
        for line in fin:

            # Remove useless whitespace
            line = line.strip()

            # Find course id
            if course_id_regex.match(line):

                # Add a class to the semester and reset variale to default
                if course_id != "":
                    semester_result[course_id+" | "+course_name] = course_grade
                course_id = line.strip()
                course_name = ""
                course_grade = []

            # Find course name
            elif len(line) > 2 \
                    and not line == "UGRD Standard Grade" \
                    and not gpa_regex.match(line) \
                    and not course_id_regex.match(line) \
                    and not digit_regex.match(line):
                course_name = line

            # Find grade distribution
            elif digit_regex.match(line):
                course_grade.append(line)

        # Add last course of the semester
        if course_id != "":
            semester_result[course_id + " | " + course_name] = course_grade

        # Clean for course with missing info
        for k in list(semester_result):
            if len(semester_result[k]) != 16:
                print(k,": input invalid. Will not be processed")
                del semester_result[k]

        #Testing
        for key,value in semester_result.items():
            print(key,":",value)


    except IOError as e:
        print(e.args)


try:
    expected_arg = 2
    # Making sure number of arguments is respected
    if len(sys.argv) < expected_arg + 1:
        print("Missing argument")
        exit()
    if len(sys.argv) > expected_arg + 1:
        print("Unexpected argmument")
        exit()

    # Retrieving path for input / output file
    fin_path = Path(sys.argv[1])
    fout_path = Path(sys.argv[2])

    # Verify that input file exist
    if not fin_path.exists():
        raise FileNotFoundError()

    # Verify if output file exist
    if fout_path.exists():

        # Ask the user if he want to override the file
        while (True):
            print("The output file already exist do you want to override it? (yes/no) ", end="")
            answer = input().strip().lower()

            # Exit loop if the answer is valid
            if answer == "no":
                exit()
            if answer == "yes":
                break

    parseGrade(fin_path)


except FileNotFoundError:
    print(sys.argv[1], ": Input file not found")
