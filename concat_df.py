#!/usr/bin/env python

# You can refer to the help manual by `python concat_df.py -h`

# argparse is a library that allows you to make user-friendly command line interfaces
import argparse
import pandas as pd

def concat_counts(input_files, output_file):
    # Initialize an empty DataFrame
    concatenated_df = pd.DataFrame()

    # Loop through each input file
    for input_file in input_files:
        # Read the input file into a DataFrame
        df = pd.read_csv(input_file, delimiter = '\t')

        # Extract the gene and counts columns
        gene_column = df['gene']
        counts_column = df['count']

        # Extract the sample name without ".exon.txt"
        sample_name = input_file.split('/')[-1].split('.')[0]

        # Add counts column to the concatenated DataFrame with sample name as the column name
        concatenated_df[sample_name] = counts_column

    # Add the gene column to the concatenated DataFrame
    concatenated_df['gene'] = gene_column

    # Reorder columns to have 'gene' as the first column
    concatenated_df = concatenated_df[['gene'] + [col for col in concatenated_df.columns if col != 'gene']]

    # Save the concatenated DataFrame to a CSV file
    concatenated_df.to_csv(output_file, index=False)

# here we are initializing the argparse object that we will modify
parser = argparse.ArgumentParser()

# we are asking argparse to require a -i or --input flag on the command line when this
# script is invoked. It will store it in the "filenames" attribute of the object
# we will be passing it via snakemake, a list of all the outputs of verse so we can
# concatenate them into a single matrix using pandas 

parser.add_argument("-i", "--input", help='A list of the VERSE output filenames provided by snakemake', dest="input", required=True, nargs='+')
parser.add_argument("-o", "--output", help='The output file name and path provided by snakemake', dest="output", required=True)

# this method will run the parser and input the data into the namespace object
args = parser.parse_args()

concat_counts(args.input, args.output)

# if you try running this on the command line and supply it a value for -i or --input
# it will show up here, stored in this object

# try just running this script and supply it a random string for the -i and -o argument
# example: `python concat_df.py -i <list of files/strings> -o <list of output file>`
# try testing

print(args.input)
print(args.output)
