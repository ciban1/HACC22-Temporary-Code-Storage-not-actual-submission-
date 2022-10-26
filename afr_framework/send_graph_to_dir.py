import os
import matplotlib.pyplot as plt

def graph_display_test():
    script_dir = os.path.dirname(__file__)
    results_dir = os.path.join(script_dir, 'Graphs/')
    sample_file_name = "sample"

    if not os.path.isdir(results_dir):
        os.makedirs(results_dir)

    plt.plot([1,2,3,4])
    plt.ylabel('some numbers')
    plt.savefig(results_dir + sample_file_name)