from http.server import HTTPServer, BaseHTTPRequestHandler
content='''<html>
<h1>Configuration Deatails of laptop</h1>
<h2>Device Specifications</h2>
<pre>Device name	gokul
Processor	Intel(R) Core(TM) Ultra 5 125H (1.20 GHz)
Installed RAM	16.0 GB (15.5 GB usable)
Device ID	44952AEB-9FBF-4B81-8CD0-0F0DD542EE4F
Product ID	00342-42784-48227-AAOEM
System type	64-bit operating system, x64-based processor
Pen and touch	No pen or touch input is available for this display

</pre>
<h2>Support</h2>
<p>Manufacturer Acer
<pre>
</html>'''
class Myserver(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()
        self.wfile.write(content.encode())
print("This is my webserver")
server_address=('',8000)
http=HTTPServer(server_address,Myserver)
http.serve_forever()