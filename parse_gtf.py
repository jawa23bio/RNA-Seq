#!/usr/bin/env python

# You can refer to the help manual by `python parse_gtf.py -h`

# argparse is a library that allows you to make user-friendly command line interfaces
import argparse
import csv

def parse_gtf(input_file, output_file):
    # Open the input GTF file for reading
    with open(input_file, 'r') as gtf_file:
        # Open the output file for writing
        with open(output_file, 'w', newline='') as output:
            # Create a CSV writer
            writer = csv.writer(output, delimiter=',')
            
            # Write header to the output file
            writer.writerow(['gene_id', 'gene_name'])
            
            # Iterate through each line in the GTF file
            for line in gtf_file:
                # Skip comment lines
                if line.startswith('##'):
                    continue
                # Split the line into columns
                columns = line.strip().split('\t')
                
                # Check if the feature type is "gene"
                if columns[2] == 'gene':
                    # Extract the key-value pairs from column 9
                    attributes = columns[8].split(';')
                    
                    # Initialize variables to store gene_id and gene_name
                    gene_id = None
                    gene_name = None
                    
                    # Iterate through the key-value pairs
                    for attr in attributes:
                        # Split the key and value (if available)
                        parts = attr.strip().split(' ', 1)
                        
                        # Check if there is a value
                        if len(parts) == 2:
                            key, value = parts
                            
                            # Remove quotes from the value
                            value = value.strip('"')
                            
                            # Check for gene_id and gene_name
                            if key == 'gene_id':
                                gene_id = value
                            elif key == 'gene_name':
                                gene_name = value
                    
                    # Write the gene_id and gene_name to the output file
                    if gene_id and gene_name:
                        writer.writerow([gene_id, gene_name])

# here we are initializing the argparse object that we will modify
parser = argparse.ArgumentParser()

# we are asking argparse to require a -i or --input flag on the command line when this
# script is invoked. It will store it in the "filenames" attribute of the object. Here
# we are only asking to provide this script one file: the GTF file we are parsing
# We also ask it to require a value for the -o or --output flag, which will specify
# the name of the file we produce

parser.add_argument("-i", "--input", help='The input file specified will be the GTF file provided by snakemake', dest="input", required=True)
parser.add_argument("-o", "--output", help='The output file name and path provided by snakemake', dest="output", required=True)

# this method will run the parser and input the data into the namespace object
args = parser.parse_args()

# Replace the code that comes after this with the code necessary to parse the GTF
parse_gtf(args.input, args.output)
