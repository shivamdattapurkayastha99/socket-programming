import os
ip_to_check=input("IP to check")
os.system(f"ping -n 4 {ip_to_check}")