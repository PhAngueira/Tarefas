from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)
#-------------------------------------------

#lista de tarefas (inicialmente vazia)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks = tasks)

@app.route('/adicionar_tarefa', methods=['POST'])
def adicionar_tarefa():
    nova_tarefa = request.form.get('tarefa')
    tasks.append(nova_tarefa)
    return redirect(url_for('index'))

#-------------------------------------------
#principal
if __name__ == "__main__":
    app.run(debug=True)