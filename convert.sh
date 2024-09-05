#!/bin/bash

# Directory containing your journal files
journal_dir="/logs"  # Change this to the directory where your journal files are located

# Loop through each .journal file in the specified directory
for journal_file in "$journal_dir"/*.journal; do
    # Extract the base name of the file (without the directory path)
    base_name=$(basename "$journal_file" .journal)

    # Define the output file name
    output_file="${journal_dir}/${base_name}.txt"

    # Convert the binary journal file to text and save it
    journalctl --file "$journal_file" > "$output_file"

    echo "Converted $journal_file to $output_file"
done
