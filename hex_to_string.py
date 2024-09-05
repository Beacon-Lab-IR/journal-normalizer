#!/bin/

import re
import sys

def hex_to_string(hex_string):
    """Convert hexadecimal string to ASCII string."""
    try:
        bytes_object = bytes.fromhex(hex_string)
        return bytes_object.decode('utf-8', errors='ignore')
    except ValueError as e:
        return hex_string


def process_log_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Find all hexadecimal sequences
            hex_match = re.search(r'.*audit: (PROCTITLE|EXECVE).*=([0-9A-Fa-f\s]{20,})', line)
            if hex_match:
                hex_string = hex_match.group(2).replace(" ", "")  # Remove spaces for conversion
                readable_text = hex_to_string(hex_string)
                # Replace the HEX content with the readable text
                line = line.replace(hex_match.group(2), readable_text)
            # Write the processed line to the output file
            outfile.write(line)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python hex_to_string.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Process the log file
    process_log_file(input_file, output_file)