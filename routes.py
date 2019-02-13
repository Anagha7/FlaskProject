from app import app
from flask import render_template,flash,redirect
from app.forms import LoginForm , ChatForm
from socket import *
from threading import Thread

ip="192.168.60.201"
port=333
@app.route('/')
@app.route('/index')
def index():
    name=["Anagha","Ammu","Asha","Raghu","Dev"]
    return render_template("index.html",name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/chat')
def chat():
    form1 = ChatForm()
    th=Thread(target=server)
    th.start()

    return render_template('chats.html', title='ChatApp',sstatus=serverStatus(),form=form1)
def serverStatus():
    s=socket(AF_INET,SOCK_STREAM)

    try:
        s.connect((ip,port))
        return "Server Online"
    except:
        return "Server Offline"
    csendmsg(s)
    s.close()
def server():
    ss=socket(AF_INET,SOCK_STREAM)
    ss.bind((ip,port))
    ss.listen(3)
    while(True):
        csoc,cadd=ss.accept()
        ssendmsg(csoc,cadd)
        tr = Thread(target=crecvmsg, args=csoc)
        tr.start()
        ts = Thread(target=csendmsg)
        ts.start()

        cmsg=csoc.recv(1024).decode()
    ss.close()
def ssendmsg(so,cadd):
    so.send(("Hello" + str(cadd)).encode())
def csendmsg(so):
    form2=ChatForm()
    st=form2.msg
    so.send(st.encode())
    form2.msg=''

def crecvmsg(so):

    form3=ChatForm()
    st=form3.chatwin
    st=st+so.recv(1024)