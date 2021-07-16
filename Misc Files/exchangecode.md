print "Content-type: text/html"
print
with open('foo.html') as f:
  print f.read()