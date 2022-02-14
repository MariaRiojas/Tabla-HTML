from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {'Nombre' : 'Michael', 'Apellido' : 'Choi', 'Nombre_Completo' : 'Michael Choi'},
        {'Nombre' : 'John', 'Apellido' : 'Supsupin', 'Nombre_Completo' : 'John Supsupin'},
        {'Nombre' : 'Mark', 'Apellido' : 'Guillen', 'Nombre_Completo' : 'Mark Guillen'},
        {'Nombre' : 'KB', 'Apellido' : 'Tonel', 'Nombre_Completo' : 'KB Tonel'}
    ]
    return render_template("index.html",users=users)

if __name__=="__main__":
    app.run(debug=True)