import matplotlib.pyplot as plt

# Grade letter
grades_letter = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F', 'FNS', 'R', 'NR']

# Dictionary with grade distribution of a semester
semester_grade = {'BIOL 201 -- INTRODUCTORY BIOLOGY': [6, 4, 6, 9, 6, 2, 2, 2, 3, 4, 1, 1, 2, 0, 0, 0],
                  'MAST 219 -- MULTIVARIABLE CALCULUS II': [15, 8, 4, 2, 2, 2, 3, 2, 1, 3, 3, 2, 18, 0, 0, 0]}

# Will need to check if fout is a .pdf file
fout = 'grade.pdf'

# Color scheme for the grade letter
colors = ['limegreen'] * 3 + ['gold'] * 3 + ['darkorange'] * 3 + ['orangered'] * 7

fig = plt.figure()
nb_plot = len(semester_grade)
plot_counter = 1

# Go through all course of a semester and plot its grade distribution
for k in semester_grade.keys():
    # Create the plot
    plt.subplot(nb_plot, 1, plot_counter)

    # Personalize the plot
    plt.bar(grades_letter, semester_grade[k], color=colors)
    plt.title(k)
    plt.xlabel("Letter Grade")
    plt.ylabel("Nb Students")

    # Increment the index for the plotting
    plot_counter += 1

# Fix layout and save the fig to the output file
fig.tight_layout()
fig.savefig(fout, format='pdf')
