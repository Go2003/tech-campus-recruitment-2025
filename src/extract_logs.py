import sys
import os
import gzip

def extract_logs(log_file, target_date, output_dir="../output"):
    """
    Extracts logs from a given log file for a specific date and saves them in a separate output file.

    Parameters:
    log_file (str): The path to the log file.
    target_date (str): The date for which logs need to be extracted in the format 'YYYY-MM-DD'.
    output_dir (str, optional): The directory where the output file will be saved. Defaults to 'output'.

    Returns:
    None. Prints a success message indicating the location of the saved output file.
    """
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"output_{target_date}.txt")

    # Detect if file is compressed (.gz) and open accordingly
    open_func = gzip.open if log_file.endswith(".gz") else open

    with open_func(log_file, "rt", encoding="utf-8", errors="ignore") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        for line in infile:
            if line.startswith(target_date):  # Match logs only for the given date
                outfile.write(line.strip() + "\n")  # Remove extra spaces, ensure new line

    print(f"✅ Logs for {target_date} saved in {output_file}")

if __name__ == "__main__":

    log_file = "../logs_2024.log"  #  Location of Log file
    target_date = sys.argv[1]  # First argument: Date in YYYY-MM-DD format

    if not os.path.exists(log_file):
        print(f"❌ Error: Log file '{log_file}' not found.")
        sys.exit(1)

    extract_logs(log_file, target_date)
