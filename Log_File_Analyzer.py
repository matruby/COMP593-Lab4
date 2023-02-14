
from log_analysis import  get_log_file_path_from_cmd_line, filter_log_by_regex
import pandas as pd
import re

def main():
    # Check if the log file exists
    log_file = get_log_file_path_from_cmd_line()
    # Filter all the logs based on the regex 
    filter_result = filter_log_by_regex(log_file, r'^.*sshd.*$', ignore_case=True, print_summary=False, print_records=False) 
    print(filter_result)
    # Get a tally of all the destination ports 
    port_dict = tally_port_traffic(log_file)
    print(port_dict)
    # Generate Destination Port Reports
    generate_port_traffic_report(log_file, 1026)
    # Generate port reports for all of the DPT's that have more than 100
    for port, occr in port_dict.items():
        if occr >= 100:
            generate_port_traffic_report(log_file, port) 

    # Create an invalid user report
    generate_invalid_user_report(log_file) 
    # Create a file that seperates logs by specified SRC IP
    generate_source_ip_log(log_file, '220.195.35.40')
    
def tally_port_traffic(log_file):
    """Process the log file and tally the number of records for each DPT"""
    destination_port = {}
    # Open the file and read through it line by line
    with open(log_file, 'r') as logs:
        all_logs = logs.readlines()
        # Regex pattern for DPT
        dpt_regex = r'DPT=([0-9]+)' 
        # Search through the logs for lines with DPT
        for log in all_logs:
            dpt_match = re.search(dpt_regex, log)
            # If there isn't a dictionary key for this port make one 
            # Otherewise add one if it already exists
            if dpt_match:
                port = dpt_match.group(1)
                destination_port[port] = destination_port.get(port, 0) + 1

    return destination_port

def generate_port_traffic_report(log_file, port_number):
    """
    Extract the date, time, src_ip, dst_ip, src_port, 
    dst_port from the file with the specified port num
    """
    with open(log_file, 'r') as logs:
        all_lines = logs.readlines()
        
        # Regex to match all dates
        groups_regex = f'([A-Z][a-z]+)\s([0-9]+)\s([0-9]+:[0-9]+:[0-9]+).*SRC=([0-9]+[.][0-9]+[.][0-9]+[.][0-9]+).*DST=([0-9]+[.][0-9]+[.][0-9]+[.][0-9]+).*SPT=([0-9]+).*DPT=({port_number})'
        # Convert to a raw string
        raw_re = repr(groups_regex)[1:-1]  

        # Get all the proper fields from the report
        report_info = []
        for line in all_lines:
            group_match = re.search(groups_regex, line)
            if group_match:
                report_info.append(group_match.groups())

        # convert the date to the proper format
        proper_format = [] 
        for entry in report_info:
            proper_format.append([f'{entry[1]}-{entry[0]}', entry[2], entry[3], entry[4], entry[5], entry[6]])

        # Make a dataframe of the data grabbed from the log
        report_df = pd.DataFrame(proper_format, columns=['Date', 'Time', 'Source IP Address', \
                'Destination IP Address', 'Source Port', 'Destination Port'])

        # Make a csv file from the dataframe
        report_df.to_csv(f'.\destination_port_{port_number}_report.csv', index=False) 

    return None 

def generate_invalid_user_report(log_file):
    """
    Make a CSV report that contains the date,
    time, username, IP address of attempted 
    logins
    """
    # Read in the file and create get all the lines with regex
    invalid_lines = []
    with open(log_file, 'r') as logs:
        all_lines = logs.readlines()
        invalid_re = r'^.*invalid user.*$'

        # Get all the matches and add them to list
        for line in all_lines:
            entry_match = re.search(invalid_re, line, re.I)
            if entry_match:
                invalid_lines.append(entry_match.group())

    # Find needed info from lines 
    final_format = []
    for line in invalid_lines:
        group_regex = r'([A-Z][a-z]+)\s([0-9]+)\s([0-9]+:[0-9]+:[0-9]+).*user\s([A-Za-z]+)\sfrom\s([0-9]+[.][0-9]+[.][0-9]+[.][0-9]+)'
        fields_match = re.search(group_regex, line)
        if fields_match:
            # Get all the info in group format and then add it to the list in the correct format
            all_info = fields_match.groups()
            final_format.append([f'{all_info[1]}-{all_info[0]}', all_info[2], all_info[3], all_info[4]])

    # Convert to dataframe and then export to CSV
    invalid_user_df = pd.DataFrame(final_format, columns=['Date', 'Time', 'Username', 'IP Address'])
    invalid_user_df.to_csv('.\invalid_users.csv')

    return None

def generate_source_ip_log(log_file, ip_address):
    """
    Get all of the records matching a source IP address
    """
    all_records = []
    with open(log_file, 'r') as logs:
        all_lines = logs.readlines()
        # Regex for the SRC IP given
        ip_regex = f'^.*SRC=({ip_address}).*$'
        # Loop through all the lines and match the lines with SRC IP
        for line in all_lines:
            line_search = re.search(ip_regex, line)
            if line_search:
                all_records.append(line_search.group())
    # Split it up the IP address and then replace the .'s with _
    split_str = ip_address.split('.')
    proper_ip = '_'.join(split_str)
    # Write all the lines to the file
    with open(f'source_ip_{proper_ip}.log', 'w') as new_log:
        for record in all_records:
            new_log.write(record)
            new_log.write('\n')

    return None

if __name__ == '__main__':
    main()
