from flask import Flask, render_template, send_from_directory, request
from vyn.discovers import scan
app = Flask(__name__, static_folder='static', static_url_path='')
app.config.from_object("config")


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/managment/', methods=['GET', 'POST'])
def managment():
    if request.method == 'POST':
        ip = request.form.get('adresse_ip')
        iface = request.form.get('interface_reseau')
        scanner = scan(ip, iface)
        scanner.arp()      
    return render_template('managment.html')


@app.route('/admin/')
def admin():
    return render_template('admin.html')


@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == "__main__":
    app.run()
