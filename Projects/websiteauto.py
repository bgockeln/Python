import sys
import webbrowser
URLS = {
    "learn": ["https://www.learnpython.org/", "https://www.w3schools.com/python/"],
    "personal": ["https://www.wp.de/lokales/hagen/", "https://www.bild.de/"]
}

def open_webpages(urls):
    for url in urls:
        print(url)
        webbrowser.open_new_tab(url)

if __name__ == "__main__":
    set_name = sys.argv[1]
    urls = URLS[set_name]
    open_webpages(urls)