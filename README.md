# PythonFinalDataCleaner
This is a simple Datacleaner tool that allows for whitespace cleanup and deletes duplicates. 

# Usage: 
-i or --input:Required argument for the path to the input CSV file. 
-o or --output: Required for where to write the cleaned CSV. 
--dedup: Oprional flag. If included, the script will remove depulicate rows. 
--strip: Optional. If included, the script will trim whitespace (ex. " Hello " to "Hello")
-- filter: Allows for regex patterns to filter rows
-- column: Allows for indexing (0-based) of column to apply regex filter to. 

Examples: 

# Basic Cleaning

python dataCleaner.py -i messy.csv -o clean.csv --strip --dedup 

# Filtering rows where column 2( index 1) matches a pattern
python dataCleaner.py -i data.csv -o filtered.csv --filter "^Admin.*" --column 1

# Combining all options
python dataCleaner.py -i messy.csv -o final.csv --strip --dedup --filter "@example\.com$" --column 2

