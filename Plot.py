import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Grade letter
letter = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D',
          'D-', 'F', 'FNS', 'R', 'NR']

# Color scheme for the grade letter
colors = ['limegreen'] * 3 + ['gold'] * 3 + ['darkorange'] * 3 + [
    'orangered'] * 7


def plotGrade(courses, fout):
    """
    Plot the grade distribution for a semester given its data and save it in
    a given output file.

    :param courses: dictionary {"course_id | course_name": [grade]}
    :param fout: Path to the output file
    :return: None
    """

    fig, ax = plt.subplots(len(courses), figsize=(8, 10))
    sns.set_palette(colors)
    plot_counter = 0

    # Go through all course of a semester and plot its grade distribution
    for c in courses.keys():
        grades = pd.DataFrame(
            {'Letter grade': letter, 'Nb students': courses[c]})

        # Create the plot
        sns.barplot(x='Letter grade', y='Nb students', data=grades,
                    ax=ax[plot_counter])

        # Personalize the plot
        ax[plot_counter].set_title(c)
        ax[plot_counter].set_xlabel('')

        # Increment the index for the plotting
        plot_counter += 1

    # Fix layout and save the fig to the output file
    fig.tight_layout()
    fig.savefig(fout, format='pdf')
