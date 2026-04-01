from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    my_profile= {
        "name": "나윤준",
        "age": 19,
        "school": "종로산업정보학교",
        "hobby": "직곡",
        "email": "nayoonjun09@gmail.com",
        "phone": "010-7608-2737",
        "dream": "개발자"
    }

    return render_template('index.html', data=my_profile)

if __name__ == '__main__':
    app.run(debug=True)