
import os 
import re 
import sys

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
     
def filter_log_by_regex(log_file, regex, ignore_case=True, print_summary=False, print_records=False): 
    """Gets a list of records in a log file that match a specified regex."""  
    matched_lines = [] 
    # Convert the regex to a raw string
    raw_re = repr(regex)[1:-1] 

    with open(log_file, 'r') as read_file:
        logs = read_file.readlines()
        
        # Look through all the logs line by line
        for log in logs:
            if ignore_case:
                search_match = re.search(raw_re, log, re.I)
            else:
                search_match = re.search(raw_re, log)
            
            # Check that there is a match and if there is capture groups or not
            if search_match and search_match.lastindex:
                matched_lines.append(search_match.groups())
            elif search_match and not search_match.lastindex:
                matched_lines.append(search_match.group())
    
    # See if the user wants all the matches printed
    if print_records == True:
        [print(f"{line_num} - {line}") for line_num, line in enumerate(matched_lines)]
    # See if th user wants a summary of all the matches printed
    if print_summary == True:
        print(f"There is a total of {len(matched_lines)} matches for this log file.")
        print(f"The regex matching was case{'in' if ignore_case else ''}-sensitive.")
    
    return matched_lines

