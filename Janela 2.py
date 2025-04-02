import tkinter

root       = tkinter.Tk()
root.title("Hello World gráfico")
root.geometry("900x600")
labelFrase = tkinter.Label(root, 
                           text='Olá Developer!',
                           font=("verdana",45,"bold","italic"),
                           fg="darkgrey",
                           bg="black")   
labelFrase.pack(padx=5,pady=5)

labelNome = tkinter.Label(root,
                  text= "Digite seu nome",
                  font=("verdana",16,"bold"),
                  fg="white",
                  bg="black")

                
labelNome.pack(padx=5,pady=5)

entryNome = tkinter.Entry(root,width=50,
                          font=("verdana", 15))
entryNome.pack(padx=5,pady=5)

buttonGravar =  tkinter.Button(root,
                               text="Gravar",
                               command=None)
buttonGravar.pack(padx=5,pady=5)


root.mainloop()


