from flask import Flask
from flask.templating import render_template
from routing import routing
from upload import upload
# from _ssl import Session
# from OpenSSL import SSL

# context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
# context.use_privatekey_file('server.key')
# context.use_certificate_file('server.crt')

app = Flask(__name__)
# sess = Session()
app.secret_key = 'HRZ@2020'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 300

# sess.init_app(app)
app.register_blueprint(routing)
app.register_blueprint(upload)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
    app.debug = True
    app.run()