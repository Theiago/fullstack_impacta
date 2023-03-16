from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def main():
    nota1 = request.args.get("nota1", type=float)
    nota2 = request.args.get("nota2", type=float)
    if nota1 and nota2:
        if nota1 > 10 or nota2 > 10:
            return "Insira notas válidas"
        media = str((nota1 + nota2) / 2)
        return f"<h1>A sua média é de {media}</h1>"

if __name__ == '__main__':
    app.run()