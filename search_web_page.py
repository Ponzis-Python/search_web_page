import urllib.request

words = ['Bluetooth', 'libstagefright', 'word2']

daLink = "file:///home/mthomas/python_progs/search_web_page/NVD_Dashboard-Mapping.html"
site = urllib.request.urlopen(daLink).read()
for word in words:
    if word.encode() in site:
       print(word)
    else:
       print(word, "not found")