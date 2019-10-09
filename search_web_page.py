import urllib.request

words = ['Bluetooth', 'the hobbit', 'word2']

daLink = "https://foo.com"
site = urllib.request.urlopen(daLink).read()
for word in words:
    if word.encode() in site:
       print(word)
    else:
       print(word, "not found")
