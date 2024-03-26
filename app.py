from flask import Flask, render_template, request, jsonify

# Utils 
from utils import get_tokens
from utils import get_price_model

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/message', methods=['POST', 'GET'])
def get_tokens_message():

    if request.method == "GET":
        return render_template('prompts.html', data={
            "error" : None,
            "count_tokens": None,
            "lista_tokens": []
        })


    message = request.form.get("message",'')
    model = request.form.get('modelOption','')
    
    tolta_tokens , lista_tokens = get_tokens.get_count_tokens(message, model)
    
    
    if message == '':
        return render_template('prompts.html', data={
            "error" : "Please enter a message",
            "count_tokens" : None,
            "lista_tokens": []
        })


    return render_template('prompts.html' , data={
            "error" : None,
            "count_tokens" : tolta_tokens,
            "lista_tokens" : lista_tokens
        })


@app.route('/pricing', methods=['POST', 'GET'])
def calculate_data():
    
    if request.method == "GET":
        return render_template('calculate.html', data={
            "error" : None,
            "pricing" : None,
            
        })
    
    
    prompt_number = int(request.form.get("prompt_number",0))
    output_token = int(request.form.get("output_token",0))
    days = int(request.form.get("days",0))
    users = int(request.form.get("users",0))
    model = request.form.get('modelOption','')
    
    if prompt_number == 0 or output_token == 0 or days == 0 or users == 0:
        return render_template('calculate.html', data={
            "error" : "no value can be equal to 0",
            "users" : 0,
            "days" : 0,
        })
    
    pricing = get_price_model.get_price_token(prompt_number, output_token, days, users, model)
    
    
    return render_template('calculate.html', data={
            "error" : None,
            "pricing" : pricing,
            "users" : users,
            "days" : days,
        })

if __name__ == '__main__':
    app.run(debug=True)