from flask import Flask

from routs.auth import auth_bp
from routs.admin_ruta import admin_bp

app=Flask(__name__)
app.secret_key="Tajna sifra"

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)

if __name__=="__main__":
    app.run(debug=True)




