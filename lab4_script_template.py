
from log_analysis import  get_log_file_path_from_cmd_line, filter_log_by_regex
import re

def main():
    # Check if the log file exists
    log_file = get_log_file_path_from_cmd_line()
    # Filter all the logs based on the regex 
    #filter_result = filter_log_by_regex(log_file, regex, ignore_case=True, print_summary=False, print_records=False) 
    # Get a tally of all the destination ports 
    port_dict = tally_port_traffic(log_file)
    # Port Reports 
    port_stats = generate_port_traffic_report(log_file, 40686)
    print(port_stats[:6])

def tally_port_traffic(log_file):
    """Process the log file and tally the number of records for each DPT"""
    # Dictionary to count the occurences
    destination_port = {}

    with open(log_file, 'r') as logs:
        # Regex pattern for DPT
        dpt_regex = r'DPT=([0-9]+)' 
        # Search through the logs for lines with DPT
        for log in logs:
            dpt_match = re.search(dpt_regex, log)
            # If there isn't a dictionary key for this port make one 
            # Otherewise add one if it already exists
            if dpt_match:
                port = dpt_match.group(0)
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

        report_info = []

        for line in all_lines:
            group_match = re.search(groups_regex, line)

            if group_match:
                report_info.append(group_match.groups())
                
    return report_info 

# TODO: Step 11
def generate_invalid_user_report(log_file):
    return

# TODO: Step 12
def generate_source_ip_log(log_file, ip_address):
    return

if __name__ == '__main__':
    main()
