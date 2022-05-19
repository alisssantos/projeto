from tkinter import*
from tkinter import ttk
from turtle import clear


tela_entrar = Tk()
tela_entrar.geometry('833x400')

note = ttk.Notebook(tela_entrar)
note.place(x=5, y=0, width=833, height=400)

#janela de envio de dados
tela1 = Frame(tela_entrar,bg='#00BFFF', borderwidth= 2 )
note.add(tela1, text='tela de envio')

tela2 = Frame(tela_entrar,bg='#00BFFF', borderwidth= 2 )
note.add(tela2, text='tela de relatório')

#criação de arquivo txt que ira coletar os dados enviados do sistema e armazenar em um arquivo txt.
def envio(): #parametro (a) irá enviar os dados do sistema para um arquivo txt e (arquivo) é a variável.
    with open('salvando_dados.txt', 'a') as arquivo: #parametro (a) irá enviar os dados do sistema para um arquivo txt
        arquivo.write(' Nome: {}\n barbeiro: {}\n Serviço: {}\n Valor Pago: {}\n Forma de Pagamento: {}\n'.format(nome_coleta,barbeiro_coleta,servico_coleta,valor_coleta,pag_coleta))
        print('dados armazenados com sucesso.')

def imprimir(): 
    #função que ira coletar os dados gerais colocados no sistema e ira atribuir a outras variaveis que serão exibidas por meio de print 
    
    global nome_coleta,barbeiro_coleta,servico_coleta,valor_coleta,pag_coleta #global deixa a variável alocada em todo o cód
    
    nome_coleta = caixa_nome.get()
    barbeiro_coleta = caixa_nome_barbeiro.get()
    servico_coleta = cb_servicos.get()
    valor_coleta = float(caixa_valor.get())
    pag_coleta = cb_pagamento.get()
    print(' CLIENTE: {} \n BARBEIRO: {}\n SERVIÇO: {}\n VALOR: {} \n FORMA DE PAGAMENTO: {}\n'.format(nome_coleta, barbeiro_coleta, servico_coleta, valor_coleta, pag_coleta ))
    
def limpar(): #função que limpar as determinadas variáveis
    caixa_nome.delete(0,END)
    caixa_nome_barbeiro.delete(0,END)
    caixa_valor.delete(0,END)
    
lista_servicos =['BARBA', 'CORTE NA TESOURA', 'CORTE TESOURA E MÁQUINA']    #lista de serviços da barbearia
lista_pagamento = ['AVISTA','CARTÃO', 'PIX']    #lista das possiveis formas de pagamento


#texto nome
nome = Label(tela1, text='NOME COMPLETO DO CLIENTE')
nome.place(x=500, y=50)

#caixa de entrada do nome
caixa_nome = Entry(tela1, border=2)
caixa_nome.place(x=700 , y=50, width = 250, )

#Texto nome barbeiro
nome_barbeiro = Label(tela1, text = 'NOME DO BARBEIRO')
nome_barbeiro.place(x = 500, y = 100)

#caixa de entrada do nome barbeiro
caixa_nome_barbeiro= Entry(tela1)
caixa_nome_barbeiro.place(x=700 , y=100, width = 150)

#texto serviços
lb_servicos = Label(tela1, text='SELECIONE O SERVIÇO REALIZADO')
lb_servicos.place(x=500, y=150)

#combo box de serviços
cb_servicos = ttk.Combobox(tela1, values=lista_servicos, state='readionly')
cb_servicos.set('SELECIONE')
cb_servicos.place(x=700, y=150)

#texto valor
valor = Label(tela1, text='Selecione o Valor do Serviço')
valor.place(x=500, y=200)

#caixa valor
caixa_valor =Entry(tela1)
caixa_valor.place(x=700, y=200)

#texto onde pede para ser selecionado a forma de pagamento
pagamento = Label(tela1, text='Marque a Forma de Pagamento')
pagamento.place(x=500, y=250)

cb_pagamento = ttk.Combobox(tela1, values = lista_pagamento, state = 'readionly')
cb_pagamento.set('SELECIONE')
cb_pagamento.place(x=700, y=250)

b1=Button(tela1, text='confirmar', command = imprimir)
b2=Button(tela1, text='ARMAZENAR',command = envio)
b3=Button(tela1, text='LIMPAR', command = limpar)
b4=Button(tela1, text='DADOS DO DIA')
b1.place(x=600, y=300)
b2.place(x=600, y=400)
b3.place(x=750, y=300)
b4.place(x=750, y=400)








tela_entrar.mainloop()