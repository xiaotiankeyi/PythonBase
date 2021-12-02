from flask import Flask
from flask import request
from flask import render_template

# 如果想要把客户端的文件名作为服务器上的文件名
from werkzeug.utils import secure_filename

# flask实现from表单文件上传

app = Flask(__name__)


@app.route("/index/")
def index():
    return render_template("send_file.html")


@app.route("/login/", methods=['post'])
def login():
    print(request.method)
    if request.method == 'POST':
        f = request.files['file_test']
        print(f.filename)
        f.save(f"./www/uploads/{secure_filename(f.filename)}")
        return "succeed"
    else:
        return "fail"


if __name__ == "__main__":
    app.run(debug=True)
