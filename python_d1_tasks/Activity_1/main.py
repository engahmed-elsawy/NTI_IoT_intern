# main.py
from my_sites import sites, open_site

print("\nYour favorite websites:")
for num, (name, url) in sites.items():
    print(f"{num}. {name}")

try:
    choice = int(input("\nEnter the number of the site to open: "))
    if choice in sites:
        site_name, url = sites[choice]
        print(f"Opening {site_name}...")
        open_site(url)
    else:
        print("Invalid choice. Please run the program again and choose a valid number.")
except ValueError:
    print("Invalid input. Please enter a number.")
