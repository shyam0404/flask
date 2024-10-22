from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login')
def homepage():
    return render_template('login.html')

@app.route("/welcome", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        
        username = request.form.get('username')
        password = request.form.get('password')  # Fix the typo here

        
        return render_template('welcome.html', username=username, password=password)

    
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
