from flask import Flask,render_template
from flask_socketio import SocketIO,send,emit

app=Flask(__name__)
app.config['SECRET_KEY']='secretkey'
app.config['DEBUG']=True
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message from user')
def receive_message_from_user(message):
    print('USER NAME: {}'.format(message))
    emit('from flask',message)

'''
@socketio.on('message')
def receive_message(message):
    print('##:{}'.format(message))
    send('This is a messge from flask')

@socketio.on('custom event')
def receive_custom_event(message):
    print('The custom event is: {}'.format(message['name']))
    emit('from flask',{'extension':'Flask-SocketIO'},json=True)
'''

if __name__ == '__main__':
    socketio.run(app)