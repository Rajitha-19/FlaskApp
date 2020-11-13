from flask import Flask,request,render_template,jsonify

app=Flask(__name__)
from .data.botinfo import bot

@app.route("/")
def introduce():
  
   return render_template('index.html',data=bot,question={'key':"name",'text':"Heyy there!! I am a bot .Please Enter your name"})


@app.route("/message",methods=['POST'])
def user_message():
   if request.method=='POST':
      from .intents import handle
      return handle(request.form)
   else:
      return "INVALID"
      
if __name__=="__main__":
    app.run(threaded=True,port=5000)