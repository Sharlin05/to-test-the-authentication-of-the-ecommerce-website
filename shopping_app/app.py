from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "dev-secret-key"  # change in production

# Hardcoded user for demo/testing
VALID_USERNAME = "testuser"
VALID_PASSWORD = "testpass"

@app.route('/')
def home():
    if session.get('logged_in'):
        return render_template('index.html', username=session.get('username'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            session['logged_in'] = True
            session['username'] = username
            flash('You are now logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    # Run on all interfaces for container/remote friendliness; default port 5000
    # Turn debug off when running under the test runner to avoid the reloader
    app.run(host='0.0.0.0', port=5000, debug=False)
