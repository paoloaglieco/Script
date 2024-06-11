#Directory enumeration

import requests
import threading
import sys

sub_list = open("wordlist.txt").read()
directories = sub_list.splitlines()

def dir_enum_thread(dir_enum):
    try:
        r = requests.get(dir_enum)
        if r.status_code == 404:
            pass
        else:
            print(f"Valid Directory: {dir_enum}")
    except Exception as e:
        print(f"Error checking directory: {dir_enum} - {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python dir_enum_threaded.py <target_url>")
        sys.exit(1)

    target_url = sys.argv[1]

    threads = []
    for dir in directories:
        dir_enum = f"http://{target_url}/{dir}.html"
        thread = threading.Thread(target=dir_enum_thread, args=(dir_enum,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()

