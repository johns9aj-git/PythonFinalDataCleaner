import argparse, csv, re, os, sys

def validate_file(path):
    if not os.path.isfile(path):
        print(f"Error: File '{path}' does not exist.")
        sys.exit(1)

parser = argparse.ArgumentParser(description="Clean up a CSV file by stripping whitespace, removing duplicates, and filtering with regex.")
parser.add_argument("-i", "--input", required=True, help="Path to input CSV file")
parser.add_argument("-o", "--output", required=True, help="Path to save the cleaned CSV file")
parser.add_argument("--dedup", action="store_true", help="Remove duplicate rows")
parser.add_argument("--strip", action="store_true", help="Strip whitespace from all fields")
parser.add_argument("--filter", help="Regex pattern to filter rows")
parser.add_argument("--column", type=int, help="Index (0-based) of column to apply regex filter to")

args = parser.parse_args()

# Validate input file exists
validate_file(args.input)

# Validate regex arguments
if args.filter and args.column is None:
    print("Error: --filter requires --column to be specified.")
    sys.exit(1)

try:
    pattern = re.compile(args.filter) if args.filter else None
except re.error as e:
    print(f"Invalid regex pattern: {e}")
    sys.exit(1)

seen = set()
with open(args.input, newline='') as infile, open(args.output, "w", newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    for row_number, row in enumerate(reader, 1):
        if args.strip:
            row = [cell.strip() for cell in row]
        
        # Apply regex filter
        if pattern:
            if args.column >= len(row):
                print(f"Warning: Row {row_number} does not have column {args.column}, skipping.")
                continue
            if not pattern.search(row[args.column]):
                continue  # Skip rows that don't match
        
        # Deduplication
        if args.dedup:
            row_tuple = tuple(row)
            if row_tuple in seen:
                continue
            seen.add(row_tuple)

        writer.writerow(row)

print(f" Cleaning complete. Output saved to '{args.output}'.")
