import tkinter as tk

def adicionar_tarefa():
    nova_tarefa = entrada_tarefa.get()
    tarefas.append({"tarefa": nova_tarefa, "concluida": False})
    entrada_tarefa.delete(0, tk.END)
    listar_tarefa()

def listar_tarefa():
    lista_tarefas.delete(0, tk.END)
    for i, tarefa in enumerate(tarefas, 1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        lista_tarefas.insert(tk.END, f"{i}. {tarefa['tarefa']} - {status}")

def marcar_tarefa_como_concluida():
    numero_tarefa = lista_tarefas.curselection()
    if numero_tarefa:
        numero_tarefa = int(numero_tarefa[0])
        tarefas[numero_tarefa]["concluida"] = True
        listar_tarefa()

def excluir_tarefas_concluidas():
    global tarefas
    tarefas = [tarefa for tarefa in tarefas if not tarefa["concluida"]]
    listar_tarefa()

def sair():
    janela.destroy()

tarefas = []

janela = tk.Tk()
janela.title("Gerenciador de Tarefas")

frame = tk.Frame(janela)
frame.pack(padx=10, pady=10, side=tk.LEFT)

label_tarefa = tk.Label(frame, text="Adicionar tarefa:")
label_tarefa.grid(row=0, column=0)

entrada_tarefa = tk.Entry(frame)
entrada_tarefa.grid(row=0, column=1)

adicionar_button = tk.Button(frame, text="Adicionar tarefa", command=adicionar_tarefa, width=15)
adicionar_button.grid(row=0, column=2)

listar_button = tk.Button(frame, text="Listar tarefas", command=listar_tarefa, width=15)
listar_button.grid(row=1, column=0, columnspan=3)

marcar_button = tk.Button(frame, text="Marcar Concluída", command=marcar_tarefa_como_concluida, width=15)
marcar_button.grid(row=2, column=0, columnspan=3)

excluir_button = tk.Button(frame, text="Excluir tudo", command=excluir_tarefas_concluidas, width=15)
excluir_button.grid(row=3, column=0, columnspan=3)

sair_button = tk.Button(frame, text="Sair", command=sair, width=15)
sair_button.grid(row=4, column=0, columnspan=3)

lista_tarefas = tk.Listbox(janela)
lista_tarefas.pack(padx=10, pady=10, side=tk.RIGHT)

janela.mainloop()
