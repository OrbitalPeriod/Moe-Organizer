import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs
from database import getImageID, getFile, topTags
import base64

class MyHanlder(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        self.send_header("Content-type", "text/html")
        self.end_headers()


        
        query_components = parse_qs(urlparse(self.path).query)
        tag = ""
        html = ""

        if 'input_tag' in query_components:
            tag = query_components["input_tag"][0]
            html = htmlcreater.searched_tag(tag)
        elif 'request_toptags' in query_components:
            html = htmlcreater.toptags()
        elif 'back' in query_components:
            html = htmlcreater.initialSearchHTML()
        else:
            html = htmlcreater.initialSearchHTML()

        '''
        if self.path == "/":
            self.path = "search.html"
        
        html = f"<html><head></head><body><h1>requested {tag}!</h1></body></html>"
        '''
        self.wfile.write(bytes(html, "utf8"))
        
        return

def run_server():
    print("starting server")
    handler_object = MyHanlder

    my_server = socketserver.TCPServer(("", 8000), handler_object)
    my_server.serve_forever()

class htmlcreater():
    def initialSearchHTML():
        return open("html_templates//search.html", "r").read()
        pass
    def searched_tag(tag):
        images = getImageID(tag)

        body = ""

        for imageID in images:
            filepath = getFile(imageID)
            data_uri = base64.b64encode(open(filepath, 'rb').read()).decode('utf-8')
            img_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)

            body = body + f"<div class='row'>{img_tag}</div>"

        html = "<!DOCTYPE html><html><head><title>Moe-organizer</title></head><body><form action=''>Take me back to the home page! <br> <input type='submit' id='back' name='back' value='back'></br></form>" + body + "</body></html>"
        return html
        pass
    def toptags():
        toptaglist = topTags()

        body = ""
        for tag in toptaglist:
            body = body + "<div class='row>{0}: {1}</div>".format(tag[0], tag[1])
        
        html = "<!DOCTYPE html><html><head><title>Moe-organizer</title></head><body><form action=''>Take me back to the home page! <br> <input type='submit' id='back' name='back' value='back'></br></form>" + body + "</body></html>"
        return html



    