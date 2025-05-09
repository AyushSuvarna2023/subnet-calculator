import ipaddress

def is_valid_ip(ip):
    """Validate if the given IP address is valid."""
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def is_valid_subnet_mask(mask):
    """Validate if the given subnet mask is valid."""
    try:
        ipaddress.ip_address(mask)
        # Check if the mask is a valid subnet mask (e.g., 255.255.255.0)
        return ipaddress.IPv4Network(f'0.0.0.0/{mask}', strict=False).prefixlen == ipaddress.IPv4Network(f'0.0.0.0/{mask}').prefixlen
    except ValueError:
        return False

def calculate_subnet_info(ip_input):
    try:
        if '/' in ip_input:
            network = ipaddress.ip_network(ip_input, strict=False)
        else:
            ip, netmask = ip_input.split()
            # Check if the IP and subnet mask are valid
            if not is_valid_ip(ip):
                print("Invalid IP address.")
                return
            if not is_valid_subnet_mask(netmask):
                print("Invalid subnet mask.")
                return
            
            # Create the network object
            network = ipaddress.IPv4Network(f"{ip}/{netmask}", strict=False)

        # Display the subnet information
        print(f"\nSubnet Information for {network}:")
        print(f"Network Address: {network.network_address}")
        print(f"Broadcast Address: {network.broadcast_address}")
        print(f"Subnet Mask: {network.netmask}")
        print(f"Prefix Length (CIDR): /{network.prefixlen}")
        print(f"Total Number of Addresses: {network.num_addresses}")
        print(f"Number of Usable Hosts: {network.num_addresses - 2}")
        print(f"First Usable Host: {list(network.hosts())[0]}")
        print(f"Last Usable Host: {list(network.hosts())[-1]}")
        print(f"Network Class: {get_network_class(network)}")
        print(f"Is Private: {network.is_private}")
    
    except ValueError:
        print("Invalid input. Please enter either:")
        print(" - CIDR format: 192.168.1.0/24")
        print(" - IP + Subnet Mask: 192.168.1.0 255.255.255.0")

def get_network_class(network):
    """Determine the network class (A, B, C, etc.)"""
    first_octet = int(str(network.network_address).split('.')[0])
    if first_octet <= 127:
        return 'Class A'
    elif first_octet <= 191:
        return 'Class B'
    elif first_octet <= 223:
        return 'Class C'
    elif first_octet <= 239:
        return 'Class D (Multicast)'
    else:
        return 'Class E (Reserved)'

def main():
    while True:
        user_input = input("Enter IP (CIDR or with subnet mask), or type 'exit' to quit: ")
        if user_input.lower() == 'exit':
            print("Exiting...")
            break
        calculate_subnet_info(user_input)

if __name__ == "__main__":
    main()
