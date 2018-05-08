import re

def parseGrade(path):
    """
    Obtain grades from a file and parse them.

    :param path: file containing grades
    :return: Dictionary {"course_id | course_name": [grade]}
    """

    # Expected number of letter grade
    nb_letter = 16

    # Define regex for parsing
    course_id_regex = re.compile("^[A-Z]{4}\s[0-9]{3}$")
    gpa_regex = re.compile("^[0-9]{1,2}\.[0-9]{2,3}$")
    digit_regex = re.compile("^\d+$")

    try:
        semester = dict()
        course_id = ""
        course_name = ""
        nb_student_for_grade = list()

        # Read through the file
        fin = open(path, "r")
        for line in fin:

            # Remove useless whitespace
            line = line.strip()

            # Find course id
            if course_id_regex.match(line):

                # Add a class to the semester and reset variable to default
                if course_id != "":
                    semester[course_id+" | "+course_name] = nb_student_for_grade
                course_name = ""
                nb_student_for_grade = []
                course_id = line.strip() # Set course_id for for next grade dist. value

            # Find course name
            elif len(line) > 2 \
                    and not line == "UGRD Standard Grade" \
                    and not gpa_regex.match(line) \
                    and not course_id_regex.match(line) \
                    and not digit_regex.match(line):
                course_name = line # Set course name for next grade dist. value

            # Find grade distribution and add it to the class
            elif digit_regex.match(line):
                nb_student_for_grade.append(int(line))

        # Add last course of the semester
        if course_id != "":
            semester[course_id + " | " + course_name] = nb_student_for_grade

        # Clean for course with missing info
        for k in list(semester):
            if len(semester[k]) != nb_letter:
                print(k,": Invalid input, this course will not be processed.")
                del semester[k]

        return semester

    except IOError as e:
        print(e)