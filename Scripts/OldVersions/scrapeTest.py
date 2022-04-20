from urllib.request import urlopen

url ="https://en.wiktionary.org/w/index.php?title=also&action=edit&section=7"

page=urlopen(url)
html_bytes=page.read()
html=html_bytes.decode("utf-8")

fl_out=open("testOut.txt","w",encoding="utf-8")
fl_out.write(html)
fl_out.close()