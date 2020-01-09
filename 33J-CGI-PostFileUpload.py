#!C:\Users\Harshal\AppData\Local\Programs\Python\Python36\python.exe

import cgi, os
import cgitb;

cgitb.enable()

form = cgi.FieldStorage()

# Get filename here.
fileitem = form['filename']

# Test if the file was uploaded
if fileitem.filename:
    # strip leading path from file name to avoid
    # directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    print(fn)
    open('/tmp/' + fn, 'wb').write(fileitem.file.read()) #write binary

    message = 'The file "' + fn + '" was uploaded successfully'

else:
    message = 'No file was uploaded'

print
"""\
Content-Type: text/html\n
<html>
   <body>
      <p>%s</p>
   </body>
</html>
""" % (message,)