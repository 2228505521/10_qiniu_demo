from flask import Flask, jsonify, render_template
import qiniu


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/uptoken/')
def uptoken():
    AK = 'a3KafHAOJy_WPOuoV8dqTT4VvMWuhq9QNAFzD7tx'
    SK = 'W8lA713_lha9rt9mX4its0WWAPTWJWC4LiDcY8Yg'
    q = qiniu.Auth(AK, SK)

    bucket = 'jackie-cheng'
    token = q.upload_token(bucket)
    return jsonify({'uptoken': token})


if __name__ == '__main__':
    app.run(debug=True)
