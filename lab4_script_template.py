
from log_analysis import  get_log_file_path_from_cmd_line, filter_log_by_regex

def main():
    log_file = get_log_file_path_from_cmd_line()
    # Get the regex to be used
    re_filter = str(input('What regex would you like to use on this file: '))
    raw_re = repr(re_filter)[1:-1]
    default_settings = input('Would you like to use default settings for search (y/n): ')
    if default_settings == 'n':
        # Ask the user if they want it to be case sensitive
        case_sens = input('Would you like this match to be case sensitive (y/n): ')
        if case_sens == 'y':
            case_sens = True
        elif case_sens == 'n':
            case_sens = False
        # Ask the user if they want printing of records that pass through the filter
        rec = input('Would you like to print records that pass through filter (y/n): ')
        if rec == 'y':
            rec = True
        elif rec == 'n':
            rec = False
        # Ask the user if they want to print a summary sentence
        summary = input('Would you like to print a summary sentence (y/n): ')
        if summary == 'y':
            summary = True
        elif summary == 'n':
            summary = False
        
        # Search result
        result = filter_log_by_regex(log_file, raw_re, ignore_case=case_sens, print_summary=summary, print_records=rec) 
    else:
        # Search result 
        result = filter_log_by_regex(log_file, raw_re)

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
