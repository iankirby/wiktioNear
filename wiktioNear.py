from urllib.request import urlopen

url="https://en.wiktionary.org/wiki/also#English"

page=urlopen(url)
html_bytes=page.read()
html=html_bytes.decode("utf-8")

fl_out=open("./FilesOut/test.txt","w",encoding="utf-8")
fl_out.write(html)
fl_out.close()