# my_sites.py
import webbrowser

# 1. Dictionary mapping numbers to (site name, URL)
sites = {
    1: ("Google",    "https://www.google.com"),
    2: ("YouTube",   "https://www.youtube.com"),
    3: ("Wikipedia", "https://www.wikipedia.org"),
    4: ("Reddit",    "https://www.reddit.com"),
    5: ("GitHub",    "https://www.github.com"),
    # Add more as you like!
}

# 2. Function to open a website given the URL
def open_site(url):
    webbrowser.open(url)
