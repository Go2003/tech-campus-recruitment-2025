## Solutions Considered

1. #### Loading Entire File into Memory

    Approach: Read the entire log file into memory and filter lines matching the given date.
    Problem: This approach is impractical for large files (~1TB) as it consumes too much RAM.

2. #### Using Line-by-Line Processing (Streaming) ✅ (Final Choice)

    Approach: Read the file line by line, check if it starts with the target date, and write matching logs to an output file.
    Why Chosen?
        Memory Efficient: Only one line is kept in memory at a time.
        Fast & Scalable: Works well for large files.
        Handles Compressed Files (.gz): Reads .gz files directly without decompression.

## Final Solution Summary

The script opens the log file and reads it line by line.
If a log starts with the given date, it is written to the output file.
This method is optimized for large files, avoiding excessive memory usage.
It also supports compressed logs (.gz), making it versatile.

## Steps to Run

1. ###### Prerequisites

    Install Python (if not already installed).
    Ensure your log file (somet.log or somet.log.gz) is in the working directory.

2.  ###### Run the Script

    For a Normal Log File (.log)

    ```bash
    python extract_logs.py 2024-12-01
    ```

3. ###### Output

    Extracted logs will be saved in:

    ```plaintext
    output/output_2024-12-01.txt
    ```

    Example extracted logs:

    ```plaintext
    2024-12-01 14:23:45 INFO User logged in
    2024-12-01 14:24:10 ERROR Failed to connect to thedatabase
    ```
