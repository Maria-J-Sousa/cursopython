#crud é um sistema simples que pode fazer cadastro, adicionar, modificar, excluir e limpar...

import  tkinter as tk #tk é o apelido para tkinter, para não escrever toda hora.
from tkinter import ttk, messagebox, filedialog 
import json #from, porque está importando duas ferramentas que estão dentro do tkinter.

def carregar_de_json():
    global pets, next_pet_id
    arquivo=filedialog.askopenfilename(filetypes=["Arquivos JSON","*.json"],
    title="Selecionar arquivo JSON para carregar")

    if not arquivo: #Se o usuário cancelar
        return
    try: 
        with open(arquivo,'r', enconding='utf-8') as f: pets_carregados=json.load(f)

#Atualiza a lista de pets e o próximo ID
pets= pets_carregados
    if pets:
       next_pet_id=max(pet['id']for pet in pets)+1
    else:
        next_pet_id=1
 
    carregar_pets()

    messagebox.showinfo("Sucesso", f"Dados carregados com sucesso de:\n{arquivo}")

    except Exception as e:
    messagebox.showerror("Erro", f"Ocorreu um erro ao carregar:\n{str(e)}")



#Otree.getchildre vai fazer o loop com for somente na parte do treeview. vai apagar cada item do treeview
def carregar_pets():
    for item in tree.get_children():
        tree.delete(item)
#Esse for que é loop, vai pegar a tabela que não aparece. Ele insere na tabela o que foi feito no Treeview.        
    for pet in pets:
        tree.insert('','end', values=(pet['id'],
                                      pet['tutor'],
                                      pet['nome'],
                                      pet['especie'],
                                      pet['raca'],
                                      pet['idade']))    
#Adicionar pet é um função, não coloca aspas quando colocar no botão
def adicionar_pet():
    global next_pet_id
    tutor= entry_tutor.get()
    nome=entry_nome.get()
    especie=entry_especie.get()
    raca=entry_raca.get()
    idade=entry_idade.get()

    if not tutor or not nome:
        messagebox.showerror("Erro", "Tutor e nome do pet são obrigatórios!")
        return
    try:
        idade_int=int(idade) if idade else 0
    except ValueError:
        messagebox.showerror('Erro', "Idade deve ser um número inteiro!")
        return
    novo_pet={'id':next_pet_id,'tutor': tutor,'nome': nome,'especie':especie,'raca':raca,'idade':idade_int}

    pets.append(novo_pet)
    next_pet_id +=1

    messagebox.showinfo("Sucesso","Pet cadastrado com sucesso")
#limpar_campos()
    carregar_pets()


def selecionar_pet(event):
    selected_item = tree.selection()
    if not selected_item:
        return
    
    values = tree.item(selected_item)['values']
    limpar_campos()

#Coloca zero pq vai apagar da primeira letra até a última. Se coloasse 2, deixaria as duas primeiras
    entry_tutor.insert(0,values[1])
    entry_nome.insert(0,values[2])
    entry_especie.insert(0,values[3])
    entry_raca.insert(0,values[4])
    entry_idade.insert(0,str(values[5]))
    
def limpar_campos():
    entry_tutor.delete(0,'end')
    entry_nome.delete(0,'end')
    entry_especie.delete(0,'end')
    entry_raca.delete(0,'end')
    entry_idade.delete(0,'end')

def editar_pet():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erro","Selecione um pet para editar!")
        return
    
    pet_id  = tree.item(selected_item)['values'][0]
    tutor   = entry_tutor.get()
    nome    = entry_nome.get()
    especie = entry_especie.get()
    raca    = entry_raca.get()
    idade   = entry_idade.get()

    if not tutor or not nome:
        messagebox.showerror("Erro","Tutor e nome do pet são obrigatórios")
        return
    
    try:
        idade_int = int(idade)  if idade else 0
    except ValueError:
        messagebox.showerror("Erro", "Idade deve ser um número inteiro!")
        return
    
    for pet in pets:
        if pet['id'] == pet_id:
            pet.update({'tutor': tutor,'nome':nome,'especie':especie,'raca': raca, 'idade':idade_int})
            break

    messagebox.showinfo("Sucesso","Pet atualizado com sucesso!") 

    carregar_pets()   

def remover_pet():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erro","Selecione um pet para remover")
        return
    
    pet_id =tree.item(selected_item)['values'][0]

    if messagebox.askyesno("Confirmação","Tem certeza que deseja remover este pet?"):
        global pets
        pets = [pet for pet in pets if pet['id']!=pet_id]
        messagebox.showinfo("Sucesso","Pet removido com sucesso!")

        limpar_campos()
        carregar_pets()










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
entry_nome = ttk.Entry(frame_form, width=40)
entry_nome.grid(row=1, column=1,padx=5,pady=5)

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

btn_adicionar=ttk.Button(frame_botoes, text="Adicionar", command=adicionar_pet,)
btn_adicionar.grid(row=0,column=0,padx=5)

btn_editar=ttk.Button(frame_botoes, text="Editar", command=editar_pet,)
btn_editar.grid(row=0,column=1,padx=5)

btn_remover=ttk.Button(frame_botoes, text="Remover", command=remover_pet,)
btn_remover.grid(row=0,column=2,padx=5)

btn_limpar=ttk.Button(frame_botoes, text="Limpar", command= limpar_campos,)
btn_limpar.grid(row=0,column=3,padx=5)

#Tabela de pets 
frame_tabela = ttk.Frame(root)
frame_tabela.pack(padx=10,pady=5,fill='both', expand= True)


#Heading é o cabeçalho da planilha
tree =ttk.Treeview(frame_tabela,columns=('ID', 'Tutor','Nome','Espécie','Raça','Idade'), show='headings')
tree.heading('ID',text='ID')
tree.heading('Tutor',text='Tutor')
tree.heading('Nome',text='Nome')
tree.heading('Espécie',text='Espécie')
tree.heading('Raça',text='Raça')
tree.heading('Idade',text='Idade')

tree.column('ID',width='50')
tree.column('Tutor',width='50')
tree.column('Nome',width='50')
tree.column('Espécie',width='50')
tree.column('Raça',width='50')
tree.column('Idade',width='50')

#Scrolbar é barra de rolagem
scrollbar= ttk.Scrollbar(frame_tabela, orient='vertical',command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

tree.pack(side='left',fill='both',expand=True)
scrollbar.pack(side='right',fill='y')

#Comando bind fica monitorando o que acontece e nese comando vai selecionar o que aparecer
tree.bind('<<TreeviewSelect>>', selecionar_pet)

root.mainloop()

