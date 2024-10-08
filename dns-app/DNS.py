path = "/etc/resolv.conf"
dns_file = "/opt/dns-app/dns_list.txt"

def load_dns_list():
    with open(dns_file, 'r') as file:
        dns_entries = file.read().split('---')
    dns_dict = {}
    for index, entry in enumerate(dns_entries):
        lines = entry.strip().split('\n')
        if len(lines) >= 3:
            dns_dict[str(index + 1)] = {
                'name': lines[0],
                'dns': "\n".join(lines[1:])
            }
    return dns_dict

def write_dns_to_file(dns_data):
    with open(path, 'w') as file:
        file.write(dns_data.replace("\n\n", "\n"))
        print("DNS successfully changed.")

dns_list = load_dns_list()

if dns_list:
    print("Welcome \nChoose one option from list:")
    for key, value in dns_list.items():
        print(f"{key} = {value['name']}\n{value['dns']}\n")
else:
    print("No DNS available in the list.")

print("A = add a DNS")
print("D = delete a DNS")

x = input("Option: ")

if x in dns_list:
    write_dns_to_file(dns_list[x]['dns'])
elif x == "A":
    name = input("Enter DNS name: ")
    dns1 = input("Enter first DNS (e.g., '1.1.1.1'): ")
    dns2 = input("Enter second DNS (e.g., '1.0.0.1'): ")
    new_dns = f"{name}\nnameserver {dns1}\nnameserver {dns2}"
    with open(dns_file, 'a') as file:
        file.write(f"\n---\n{new_dns}\n")
    print(f"{new_dns} has been added to the list.")
elif x == "D":
    dns_to_remove = input("Enter DNS option number to remove: ")
    if dns_to_remove in dns_list:
        del dns_list[dns_to_remove]
        with open(dns_file, 'w') as file:
            entries = "\n---\n".join(f"{value['name']}\n{value['dns']}" for value in dns_list.values() if value['dns'].strip())
            file.write(entries + "\n")
        print(f"Option {dns_to_remove} has been removed.")
    else:
        print("Invalid DNS option number.")
else:
    print("Invalid choice")
