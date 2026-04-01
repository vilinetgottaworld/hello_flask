from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    #여기에 내 데이터를 만든다!
    my_profile= {
        "name": "홍길동",
        "age": 20
    }

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)