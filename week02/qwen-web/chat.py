from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.request, urllib.parse, json, html
class Handler(BaseHTTPRequestHandler):
 def do_GET(self):
  self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.end_headers()
  self.wfile.write('<meta charset="utf-8"><h1>조서빈 Qwen 실습</h1><form method="post"><input name="prompt"><button>질문</button></form>'.encode())
 def do_POST(self):
  fields=urllib.parse.parse_qs(self.rfile.read(int(self.headers['Content-Length'])).decode())
  payload=json.dumps({'model':'qwen3:0.6b','prompt':fields.get('prompt',['안녕'])[0], 'stream':False,'think':False}).encode()
  try:
   req=urllib.request.Request('http://127.0.0.1:11434/api/generate',data=payload,headers={'Content-Type':'application/json'})
   result=json.load(urllib.request.urlopen(req,timeout=180))['response']
   self.send_response(200)
  except Exception as e:
   result=str(e);self.send_response(502)
  self.send_header('Content-Type','text/html; charset=utf-8');self.end_headers();self.wfile.write(('<meta charset="utf-8"><pre>'+html.escape(result)+'</pre><a href="/">돌아가기</a>').encode())
HTTPServer(('127.0.0.1',8000),Handler).serve_forever()
