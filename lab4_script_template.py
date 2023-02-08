
import os
import re
import sys


def main():
    log_file = get_log_file_path_from_cmd_line()
    # Get the regex to be used
    re_filter = input('What regex would you like to use on this file: ')
    default_settings = input('Would you like to use default settings for search (y/n): ')
    if default_settings == 'n':
        # Ask the user if they want it to be case sensitive
        ignore_case = input('Would you like this match to be case sensitive (y/n): ')
        True if ignore_case == 'y' else False
        # Ask the user if they want printing of records that pass through the filter
        records = input('Would you like to print records that pass through filter (y/n): ')
        True if records == 'y' else False
        # Ask the user if they want to print a summary sentence
        summary = input('Wouldyou like to print a summary sentence (y/n): ')
        True if summary == 'y' else False
        
        # Search result
        result = filter_log_by_regex(log_file, re_filter, ignore_case, summary, records) 
    else:
        # Search result 
        result = filter_log_by_regex(log_file, re_filter)

# TODO: Step 3
def get_log_file_path_from_cmd_line():
    """Gets command line argument and checks if it is valid""" 
    # Possible path to log file
    log_path = sys.argv
    # Check if there is only 1 argument given, if the path given is a file and is a log file
    if len(log_path) == 2 and os.path.isfile(log_path[1]) and log_path[1][-4:] == '.log':
        return log_path[1]
    else:
        print("File doesn't exist\nOr file isn't a log file")
        sys.exit()


# TODO: Steps 4-7
def filter_log_by_regex(log_file, regex, ignore_case=True, print_summary=False, print_records=False):
    """Gets a list of records in a log file that match a specified regex."""
    # Check if it is just the default settings
    matched_lines = None
     
    # Open the log file in read mode 
    with open(log_file, 'r') as read_file:
        # Read all of the lines into a list called logs
        logs = read_file.readlines()
        # Check if ignore_case was used
        if ignore_case == False:
            matched_lines = [re.search(regex, log, re.I).group() for log in logs if re.search(regex, log, re.I) != None]
        else:
            matched_lines = [re.search(regex, log).group() for log in logs if re.search(regex, log) != None]
        # Print records if argument was used
        if print_records:
            [print(entry) for entry in matched_lines]
        # Print summary if argument was used
        if print_summary: 
            print(f'\nThere was {len(matched_lines)} lines that matched the regex!')
            if ignore_case == False:
                print('This search was case-insensitive')
            else:
                print('This search was case-sensitive')

    return matched_lines

# TODO: Step 8
def tally_port_traffic(log_file):
    return

# TODO: Step 9
def generate_port_traffic_report(log_file, port_number):
    return

# TODO: Step 11
def generate_invalid_user_report(log_file):
    return

# TODO: Step 12
def generate_source_ip_log(log_file, ip_address):
    return

if __name__ == '__main__':
    main()
