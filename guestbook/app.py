import os, socket, json
from flask import Flask, request, redirect, render_template, jsonify
import redis
app = Flask(__name__)
memory = []
db = redis.Redis(host=os.environ['REDIS_HOST'], port=6379, password=os.getenv('REDIS_PASSWORD'), decode_responses=True) if os.getenv('REDIS_HOST') else None
@app.get('/health')
def health():
    try:
        if db: db.ping()
        return jsonify(status='ok', host=socket.gethostname())
    except redis.RedisError:
        return jsonify(status='unavailable'), 503
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        entry={'name':request.form.get('name','익명')[:50], 'message':request.form.get('message','')[:500]}
        if entry['message']:
            if db: db.lpush('entries',json.dumps(entry,ensure_ascii=False))
            else: memory.insert(0,entry)
        return redirect('/')
    entries=[json.loads(x) for x in db.lrange('entries',0,99)] if db else memory
    return render_template('index.html', entries=entries, host=socket.gethostname(), storage='Redis' if db else 'Memory', title=os.getenv('APP_TITLE','조서빈의 방명록'), color=os.getenv('THEME_COLOR','#2563eb'))
if __name__ == '__main__': app.run(host='0.0.0.0',port=5000)
