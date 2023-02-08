
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

    # The final list will contain the proper format (src:port)
    final_lst = [] 
    for count in range(len(src)):
        # Get just the source and the port
        proper_src = re.search(r'[0-9]+[.][0-9]+[.][0-9]+[.][0-9]+', src[count])
        proper_port = re.search(r'[0-9]+', port[count])
        # String with proper formatting
        proper_str = f'{proper_src.group()}:{proper_port.group()}'
        final_lst.append(proper_str)

    # Sort the list in final_lst
    final_lst.sort()
    # Count the number of occurences of a single IP address
    occr = {} 
    for src_port in final_lst:
        occr[src_port] = occr.get(src_port, 0) + 1
    
    # Make a list to be added to a file with format of Occurence - src:port
    [final_format.append(f'{v} - {k}') for k, v in occr.items()]   

with open(r'C:\Users\rubes\COMP593-Lab4\report.txt', 'w') as txt_file:
    for line in final_format:
        txt_file.write(f'{line}\n')

