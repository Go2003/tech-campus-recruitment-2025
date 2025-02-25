import sys
import os
import gzip
import re

def extract_logs(log_file, target_date, output_dir="../output"):
    """
    Extracts logs from a given log file for a specific date and reformats them to match the expected format.
    
    Parameters:
    log_file (str): The path to the log file.
    target_date (str): The date for which logs need to be extracted (YYYY-MM-DD).
    output_dir (str, optional): The directory where the output file will be saved. Defaults to 'output'.
    
    Returns:
    None. Prints a success message indicating the location of the saved output file.
    """
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"output_{target_date}.txt")

    # Detect if file is compressed (.gz) and open accordingly
    open_func = gzip.open if log_file.endswith(".gz") else open

    # Define regex pattern to fix timestamp format (Handles 'T' separator and extra precision)
    log_pattern = re.compile(r"(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2}:\d{2})\.\d+ - (\w+) - (.+)")

    with open_func(log_file, "rt", encoding="utf-8", errors="ignore") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        for line in infile:
            if line.startswith(target_date):  
                match = log_pattern.match(line)
                if match:
                    formatted_line = f"{match.group(1)} {match.group(2)} {match.group(3)} {match.group(4)}\n"
                    outfile.write(formatted_line)
                else:
                    outfile.write(line.strip() + "\n")  # If format is already correct

    print(f"✅ Logs for {target_date} saved in {output_file}")

if __name__ == "__main__":

    log_file = "../logs_2024.log"
    target_date = sys.argv[1]

    if not os.path.exists(log_file):
        print(f"❌ Error: Log file '{log_file}' not found.")
        sys.exit(1)

    extract_logs(log_file, target_date)
