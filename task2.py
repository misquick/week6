host_count = {}

with open("mbox.txt", "r") as file:
    for line in file:
        if line.startswith("From:"):
            parts = line.split()
            if len(parts) >= 2:
                email = parts[1]
                if "@" in email:
                    host = email.split("@")[1]
                    host_count[host] = host_count.get(host, 0) + 1

for host, count in host_count.items():
    print(f"{host}")

print(f"Total number of hosts: {len(host_count)}")
