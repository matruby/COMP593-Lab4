
# Get all of the source IP addresses and Port numbers with 
import re 


final_format = []

# Open the log file
with open(r'C:\Users\rubes\COMP593-Lab4\gateway.log', 'r') as log_file: 
    # Read all the lines into a list
    lines = log_file.readlines()
    # Get all the lines that were port scans
    ps_srch_str = r'^.*INext-DROP-DEFLT.*$'
    ps_lines = []
    for line in lines:
        ps_match = re.search(ps_srch_str, line)
        if ps_match != None:
            ps_lines.append(ps_match.group())

    # Get matches of all the source addresses that scanned
    src_srch_str = r'SRC=[0-9]+[.][0-9]+[.][0-9]+[.][0-9]+'    
    src = [re.search(src_srch_str, line).group() for  line in ps_lines]
    # Get matches of all the ports scanned
    port = [re.search(r'DPT=[0-9]+', line).group() for line in ps_lines]
    
