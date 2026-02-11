import ipaddress
import os

def is_valid_ip(ip: str) -> bool:
    """
    Returns whether the string provided is an IP address or not.

    :param ip: The string you want to check.

    :return: True if valid IP address, else False.
    """
    try:
        ipaddress.ip_network(ip, strict=False)
        return True
    except ValueError as e:
        return False

def is_txt_file(filepath: str) -> bool:
    """
    Returns whether the filename provided is a valid .txt file.

    :param filepath: A file path.

    :return: True is the filepath is a valid .txt file, else false.
    """
    return os.path.isfile(filepath) and filepath.endswith(".txt")



if __name__ == "__main__":
    print(is_valid_ip('192.168.153.130/24'))
    print(is_txt_file('./main.py'))