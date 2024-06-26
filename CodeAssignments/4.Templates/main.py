from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello_world'))
    response.set_cookie('user_ip', user_ip)

    return response

@app.route('/hello_world')
def hello_world():
    #creamos nueva variable de la ip que detectamos en el browser
    user_ip = request.cookies.get('user_ip')

    return render_template('hello.html', user_ip= user_ip)
		# metodo es render_template con jinja2 y la variable es user_ip.
