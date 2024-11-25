import subprocess
import sys
#run the Nmap scan
def run_nmap(target_ip):
    print(f"Scanning {target_ip} for open ports.")
    command = f"nmap -sV -O {target_ip} -oX scan_result.xml"
    subprocess.run(command, shell=True, check=True)
    print("Nmap scan is complete.")
#run actual scan
def run_scan(target_ip):
    print(f"Running vulnerability scan on {target_ip}.")
    vuln_command = f"nmap --script=vuln {target_ip} -oN vuln_scan_result.txt"
    subprocess.run(vuln_command, shell=True, check=True)
    print("Vulnerability scan is complete.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python vuln_scan.py <target_ip>")
        sys.exit(1)
    
    target_ip = sys.argv[1]
    
    run_nmap(target_ip)
    run_scan(target_ip)
    print("Vulnerability scan results saved in 'vuln_scan_result.txt'")

if _name_ == "_main_":
    main()