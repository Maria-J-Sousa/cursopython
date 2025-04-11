#crud é um sistema simples que pode fazer cadastro, adicionar, modificar, excluir e limpar...
import  tkinter as tk #tk é o apelido para tkinter, para não escrever toda hora.
from tkinter import ttk, messagebox #from, porque está importando duas ferramentas que estão dentro do tkinter.

#Dados em memória
pets = [] #[] significa que está criando uma lista
next_pet_id = 1 #variável de código do pet, é o contador de cada cadastro. 


#Configuração da janela principal
root =tk.Tk()
root.title("Sistema de Cadastro de Pets")
root.geometry("800x500")

#Frame do formulário (Comando para montar o retêngula na tela em que vai ter o label e o entry)
frame_form = ttk.LabelFrame(root,text="Formulário de Pet")
frame_form.pack(padx=10, pady=10, fill='x')

#Nome do Tutor

ttk.Label(frame_form,text="Tutor:").grid(row=0,column=0,padx=5,pady=5,sticky='e')
entry_tutor = ttk.Entry(frame_form, width=40)
entry_tutor.grid(row=0, column=1,padx=5,pady=5)

ttk.Label(frame_form,text="Nome do Pet:").grid(row=1,column=0,padx=5,pady=5,sticky='e')
entry_nomepet = ttk.Entry(frame_form, width=40)
entry_nomepet.grid(row=1, column=1,padx=5,pady=5)

ttk.Label(frame_form,text="Espécie:").grid(row=2,column=0,padx=5,pady=5,sticky='e')
entry_especie = ttk.Entry(frame_form, width=40)
entry_especie.grid(row=2, column=1,padx=5,pady=5)

ttk.Label(frame_form,text="Raça:").grid(row=3,column=0,padx=5,pady=5,sticky='e')
entry_raca = ttk.Entry(frame_form, width=40)
entry_raca.grid(row=3, column=1,padx=5,pady=5)

ttk.Label(frame_form,text="Idade:").grid(row=4,column=0,padx=5,pady=5,sticky='e')
entry_idade = ttk.Entry(frame_form, width=40)
entry_idade.grid(row=4, column=1,padx=5,pady=5) 

#pack é gerenciador de layout e coloca um embaixo do outro. Os frames coloca pack, pois vai ficar um abaixo do outro.
# o grid cria uma grade com linha e coluna (row e column).

#Frame de Botões
frame_botoes =ttk.Frame(root)
frame_botoes.pack(pady=5)

btn_adicionar=ttk.Button(frame_botoes, text="Adicionar", command=None,)
btn_adicionar.grid(row=0,column=0,padx=5)

btn_modificar=ttk.Button(frame_botoes, text="Modificar", command=None,)
btn_modificar.grid(row=0,column=1,padx=5)

btn_excluir=ttk.Button(frame_botoes, text="Excluir", command=None,)
btn_excluir.grid(row=0,column=2,padx=5)

btn_limpar=ttk.Button(frame_botoes, text="Limpar", command=None,)
btn_limpar.grid(row=0,column=3,padx=5)

#Tabela de pets
frame_tabela = ttk.Frame(root)
frame_tabela.pack(padx=10,pady=5,fill='both', expand= True)

tree =ttk.Treeview(frame_tabela,columns=('ID', 'Tutor','Nome','Espécie','Raça','Idade'), show='headings')
tree.heading('ID',text='ID')
tree.heading('Tutor',text='Tutor')
tree.heading('Nome',text='Nome')
tree.heading('Espécie',text='Espécie')
tree.heading('Raça',text='Raça')
tree.heading('Idade',text='Idade')

root.mainloop()

