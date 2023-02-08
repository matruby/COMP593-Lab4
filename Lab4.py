
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
    
