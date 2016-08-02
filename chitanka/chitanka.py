import mechanize
from time import sleep

#Make a Browser (think of this as chrome or firefox etc)
br = mechanize.Browser()


# Open your site
br.open('http://pypi.python.org/pypi/xlwt')

filetypes=[".zip",".exe",".tar.gz"] #you will need to do some kind of pattern matching on your files
myfiles=[]
for l in br.links():
    for t in filetypes:
        if t in str(l): #check if this link has the file extension we want (you may choose to use reg expressions or something)
            myfiles.append(l)


def downloadlink(l):
    f=open("/home/slavi/Desktop/" + l.text,"w") #perhaps you should open in a better way & ensure that file doesn't already exist.
    br.click_link(l)
    f.write(br.response().read())
    print l.text," has been downloaded"
    #br.back()

for l in myfiles:
    sleep(1) #throttle so you dont hammer the site
    downloadlink(l)