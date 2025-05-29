from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, TechDays! 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# Cria uma rota para alunos
@app.route("/alunos")
def alunos():
    return "Rota para alunos"
# Cria uma rota para professores
@app.route("/aluno")
def aluno():
    return "Rota para aluno"

@app.route("/professor")
def professor():
    return "Rota para professor"
# Cria uma rota para cursos
@app.route("/cursos")
def cursos():
    return "Rota para cursos"
# Cria uma rota para disciplinas
@app.route("/disciplinas")
def disciplinas():
    return "Rota para disciplinas"
# Cria uma rota para turmas
@app.route("/turmas")
def turmas():
    return "Rota para turmas"
# Cria uma rota para matrículas
@app.route("/matriculas")
def matriculas():
    return "Rota para matrículas"
# Cria uma rota para notas
@app.route("/notas")
def notas():
    return "Rota para notas"
# Cria uma rota para frequência