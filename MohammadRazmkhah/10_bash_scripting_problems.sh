#!/bin/bash

# 1. Count the number of lines in a file that contain a specefic keyword.

	grep -w $keyword $file | wc -l

# 2. Find the top 5 most frequent words in a text file.

	tr -cs '[:alnum:]' '[\n*]' < $file | sort | uniq -ic | sort -nr | head -5

# 3. Extract all email addresses from a log file

	grep -o -E '[[:alnum:]_.+-]+@[[:alnum:]_-]+\.[[:alnum:]{2,}' $logfile | uniq

# 4. Sort a list of numbers in descending order.

	sort -nr $file

# 5. Filter out lines from a log file that containes errors.

	grep -e 'error' -e 'failed' -e 'exception' -e 'traceback' -e 'unable' -e 'denied' -e 'fault' -e 'kernel panic' $logfile

# 6. Calculate the total size of all files in a directory.

	du -sh $path

# 7. Convert a CSV file to JSON format.

	csvjson input.csv -o output.json

# 8. Find and display all running processes that are consuming the most CPU.

	ps -eo pid,cmd,%cpu --sort=-%cpu | head

# 9. Combine two text files into a single file, with each line from the first file followed by the corresponding line from second file.

	paste $file1 $file2 > combined.txt

#10. Extract all unique IP addresses from a log file.

	grep -E -o "([0-9]{1,3}\.){3}[0-9]{1,3}" $logfile | sort -u
