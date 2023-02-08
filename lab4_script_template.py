
import sys
import os

def main():
    log_file = get_log_file_path_from_cmd_line()
    print(log_file)

# TODO: Step 3
def get_log_file_path_from_cmd_line():
    """Gets command line argument and checks if it is valid""" 
    # Possible path to log file
    log_path = sys.argv
    # Check if there is only 1 argument given, if the path given is a file and is a log file
    if len(log_path) == 2 and os.path.isfile(log_path[1]) and log_path[1][-4:] == '.log':
        return log_path[1]
    elif len(log_path) > 2:
        print('Too many arguments given!!\nEXITING')
        sys.exit()
    elif len(log_path) < 1:
        print('Add a log file path as argument, then retry')
        sys.exit()
    else:
        print("File doesn't exist, try with an existing file\nOr file isn't a log file")
        sys.exit()


# TODO: Steps 4-7
def filter_log_by_regex(log_file, regex, ignore_case=True, print_summary=False, print_records=False):
    """Gets a list of records in a log file that match a specified regex.

    Args:
        log_file (str): Path of the log file
        regex (str): Regex filter
        ignore_case (bool, optional): Enable case insensitive regex matching. Defaults to True.
        print_summary (bool, optional): Enable printing summary of results. Defaults to False.
        print_records (bool, optional): Enable printing all records that match the regex. Defaults to False.

    Returns:
        (list, list): List of records that match regex, List of tuples of captured data
    """
    return

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
