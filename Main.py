import sys
from pathlib import Path
from ParseGrade import parseGrade
from Plot import plotGrade

try:
    expected_arg = 2
    # Making sure number of arguments is respected
    if len(sys.argv) < expected_arg + 1:
        print("Missing argument.")
        exit()
    if len(sys.argv) > expected_arg + 1:
        print("Unexpected argument.")
        exit()

    # Retrieving path for input / output file
    fin_path = Path(sys.argv[1])
    fout_path = Path(sys.argv[2])

    # Verify that input file exist
    if not fin_path.exists():
        raise FileNotFoundError()

    # Verify if output file exist
    if fout_path.exists():

        # Verify if file as pdf extension
        if not str(fout_path).lower().endswith('.pdf'):
            print("The output file needs to have be a .pdf.")
            exit()

        # Ask the user if he want to override the file
        while (True):
            print("The output file already exist do you want to override it? (yes/no) ", end="")
            answer = input().strip().lower()

            # Exit loop if the answer is valid
            if answer == "no":
                exit()
            if answer == "yes":
                break

    # Parse the grades
    parsed_grades = parseGrade(fin_path)

    # Plot the grades
    plotGrade(parsed_grades, fout_path)

    print("File created")


except FileNotFoundError:
    print(sys.argv[1], ": Input file not found.")
