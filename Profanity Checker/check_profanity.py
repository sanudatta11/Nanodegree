import urllib
def read_files():
    quotes = open("movie_quotes.txt")
    contents = quotes.read()
    quotes.close()
    check_profanity(contents)

def check_profanity(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    result = connection.read()
    connection.close()
    if "true" in result:
        print("Profanity Found!")
    elif "false" in result:
        print("This document is safe to be sent")
    else:
        print("Couldn't read the document properly")
    
read_files()
