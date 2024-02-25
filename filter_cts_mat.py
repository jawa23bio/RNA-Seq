#!/usr/bin/env python

import argparse
import pandas as pd

def filter_counts_matrix(input_file, output_file):
    # Read the unfiltered counts matrix
    counts_matrix = pd.read_csv(input_file, index_col=0, delimiter = ',')

    # Apply the filter: retain only genes (rows) where every sample has a non-zero count
    filtered_counts_matrix = counts_matrix[(counts_matrix > 0).all(axis=1)]

    # Write the filtered counts matrix to a new file
    filtered_counts_matrix.to_csv(output_file)

if __name__ == "__main__":
    # Initialize the argparse object
    parser = argparse.ArgumentParser()

    # Specify the command-line arguments
    parser.add_argument("-i", "--input", help="Input unfiltered counts matrix", dest="input", required=True)
    parser.add_argument("-o", "--output", help="Output filtered counts matrix", dest="output", required=True)

    # Parse the command-line arguments
    args = parser.parse_args()

    # Run the filter_counts_matrix function with the provided arguments
    filter_counts_matrix(args.input, args.output)

