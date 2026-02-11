# Styling
from rich.progress import Progress
from rich.console import Console

# Worker
import nmap

# Internal
from helper import is_valid_ip, is_txt_file
from log_manager import Logger

console = Console()
log = Logger()


def host_discovery(ip_or_file: str, timing: str = "-T4") -> dict:
    """
    Performs the host discovery scan using nmap .

    :param ip_or_file: Target IP or subnet to scan (e.g., '192.168.0.1/24') OR a .txt file with a list of IP addresses.
    :param timing: Timing option for scan speed (default: '-T4')
    :return: Dictionary of hosts scanned with their status.
    """

    nm = nmap.PortScanner()

    try:

        final_output = []

        if is_valid_ip(ip_or_file):

            ip = ip_or_file

            log.info(f"Found 1 IP address: {ip}")

            nm.scan(ip, arguments=f"-sn {timing}")

            host_state_dict = {host: nm[host].state() for host in nm.all_hosts()}

            final_output.append(host_state_dict)

        elif is_txt_file(ip_or_file):

            list_of_ips = ""

            file = ip_or_file

            with open(file, "r") as f:
                list_of_ips = f.readlines()

            log.info(f"Found {len(list_of_ips)} host(s)")

            for ip_address in list_of_ips:

                log.info(f"Scanning {ip_address}")

                nm.scan(ip_address, arguments=f"-sn {timing}")

                host_state_dict = {host: nm[host].state() for host in nm.all_hosts()}

                final_output.append(host_state_dict)

        else:
            print("Invalid Input")
            return {}

    except Exception as e:
        print("Error during scan: ", e)
        return {}

    log.success("Successfully performed the scan.")
    return final_output
