from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
   <head>
      <title>Top Software Companies With Revenue Table</title>
   </head>
<body bgcolor="" align="center">
<table border="5" cellspacing="6" cellpadding="8" height="30" width="70" align="center">
<caption>Top Five Revenue Generating Software Companies</caption>
   <tr> 
        <th>Rank</th>
        <th>Company</th>
        <th>Sales</th>
        <th>Nationality</th>
   </tr> 
   <tr>
        <td>1</td>
        <td>MicroSoft</td>
        <td>57.9</td>
        <td>USA</td>

   </tr>
 <tr>
        <td>2</td>
        <td>Oracle</td>
        <td>21.0</td>
        <td>USA</td>

   </tr>
<tr>
        <td>3</td>
        <td>SAP</td>
        <td>16.1</td>
        <td>Germany</td>

   </tr>
<tr>
       <td>4</td>
       <td>Computer Associates</td>
       <td>4.2</td>
       <td>USA<td>
   </tr>
<tr>
       <td>5</td>
       <td>Adobe</td>
       <td>3.4</td>
       <td>USA<td>
   </tr>

       


</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()