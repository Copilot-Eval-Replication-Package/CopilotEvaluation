# GitHub Copilot AI pair programmer: Asset or Liability?
This repository contains the replication package for our Journal of Systems and Software (JSS) paper titled: __GitHub Copilot AI pair programmer: Asset or Liability?__ submitted on June 2022. This repository contains our detailed results and the python scripts which were used for generating them.

This repository is broken into two directories:
 - Copilot_on_Algorithm_Design: contains the python scripts and the results which were used to answer RQ1 of our paper: ___Can Copilot suggest correct and efficient solutions for some basic algorithmic problems?___
 - Copilot_vs_human: contains the python scripts and the results which were used to answer RQ2 of our paper: ___Are Copilot’s solutions competitive with humans’ solutions in solving programming problems?___

# Requirements
To replicate our results, you need:
 - Python 3.7
 - Access to GitHub Copilot

# Structure
  - Copilot_on_Algorithm_Design contains all the python scripts and the results for RQ1:
    - `python_comparison.py`: Provides functions for comparing the abstract syntax trees of two python programs.
    - `similarity_checker.py`: checks the python script in each sub-directory, compares the ASTs and stores the results in a csv file.
    - There are _4_ sub-directories which were named after the algorithm category which we were testing Copilot on (Binary_Trees, Elementary_Graph_Algorithms, Greedy_Algorithms, Sorting_algorithms):
        - Each sub-directory contains directories for each of the algorithms that we tested Copilot on.
            - Each algorithm directory contains _6_ `.txt` files which contain the suggestion of Copilot for each experiment.
            - The PyScript directory contains the Python scripts which were made for each of Copilot's suggestions. These scripts were used for comparing AST similarity between suggestions.
            _ The PyScript folder also contains the `comparison_results.csv`. This csv file is the output of running `similarity_checker.py` on the Python scripts.
        - Each sub-directory contains and Excel file which contains the entire results of the experiments alongside our comments.
  - Copilot_vs_Human contains all the python scripts and the results for RQ2:
  
