import webbrowser
import time

count = 0
while count< 3:
    time.sleep(3)
    webbrowser.open("https://www.google.com")
    count += 1

