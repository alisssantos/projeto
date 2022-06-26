from cgitb import text
from tkinter import*
from tkinter import ttk
from turtle import clear

tela_entrar = Tk()
tela_entrar.geometry('800x450+300+100')
tela_entrar.resizable(width=0, height=0)
tela_entrar.title('BARBERSHOP')

note = ttk.Notebook(tela_entrar)
note.place(x=5, y=0, width=790, height=440)

#janela de envio de dados
tela1 = Frame(tela_entrar,bg='#D8E1FF', borderwidth= 2, relief='sunken')
note.add(tela1, text='tela de envio')

tela2 = Frame(tela_entrar,bg='#D8E1FF', borderwidth= 2, relief='sunken')
note.add(tela2, text='tela de cadastro')

#dados  armazenar e limpar da tela 1
def armazenar(): 
    #função que ira coletar os dados gerais colocados no sistema e ira atribuir a outras variaveis que serão exibidas por meio de print 
       
    nome_coleta = caixa_nome.get()
    barbeiro_coleta = caixa_nome_barbeiro.get()
    servico_coleta = cb_servicos.get()
    valor_coleta = caixa_valor.get()
    pag_coleta = cb_pagamento.get()
    with open('salvando_dados.txt', 'a') as arquivo:
        arquivo.write(' CLIENTE: {} \n BARBEIRO: {}\n SERVIÇO: {}\n VALOR: {} \n FORMA DE PAGAMENTO: {}\n'.format(nome_coleta, barbeiro_coleta, servico_coleta, valor_coleta, pag_coleta ))
        arquivo.close()
        print('DADOS SALVOS')
        
def limpar(): #função que limpar as determinadas variáveis
    caixa_nome.delete(0,END)
    caixa_nome_barbeiro.delete(0,END)
    caixa_valor.delete(0,END)

#dados de armazenar e limpar da tela 2

lista_servicos =['BARBA', 'CORTE NA TESOURA', 'CORTE TESOURA E MÁQUINA']    #lista de serviços da barbearia
lista_pagamento = ['AVISTA','CARTÃO', 'PIX']    #lista das possiveis formas de pagamento


#texto nome
nome = Label(tela1, text='NOME COMPLETO DO CLIENTE',bg='#D8E1FF')
nome.place(x=150, y=50)

#caixa de entrada do nome
caixa_nome = Entry(tela1, border=2)
caixa_nome.place(x=400 , y=50, width = 250 )

#Texto nome barbeiro
nome_barbeiro = Label(tela1, text = 'NOME DO BARBEIRO',bg='#D8E1FF')
nome_barbeiro.place(x = 150, y = 100)

#caixa de entrada do nome barbeiro
caixa_nome_barbeiro= Entry(tela1, border=2)
caixa_nome_barbeiro.place(x=400 , y=100, width = 250 )

#texto serviços
lb_servicos = Label(tela1, text='SERVIÇO REALIZADO',bg='#D8E1FF')
lb_servicos.place(x=150, y=150)

#combo box de serviços
cb_servicos = ttk.Combobox(tela1, values=lista_servicos, state='readionly')
cb_servicos.set('SELECIONE')
cb_servicos.place(x=400, y=150)

#texto valor
valor = Label(tela1, text='VALOR DO SERVIÇO',bg='#D8E1FF')
valor.place(x=150, y=200)

#caixa valor
caixa_valor =Entry(tela1, border=2)
caixa_valor.place(x=400, y=200)

#texto onde pede para ser selecionado a forma de pagamento
pagamento = Label(tela1, text='FORMA DE PAGAMENTO',bg='#D8E1FF', font='calibri, 10')
pagamento.place(x=150, y=250)

cb_pagamento = ttk.Combobox(tela1, values = lista_pagamento, state = 'readionly')
cb_pagamento.set('SELECIONE')
cb_pagamento.place(x=400, y=250)


b1=Button(tela1, text='ARMAZENAR', command=armazenar)
b2=Button(tela1, text='LIMPAR', command = limpar)

b1.place(x=150, y=320, width = 130)
b2.place(x=480, y=320, width = 100)

#dados da tela2

def armazenar2():
    coleta_cod = caixa_cod_cad.get()
    coleta_nome_cad = caixa_nome_cad.get()
    coleta_fone = caixa_fone_cad.get()
    coleta_sexo = cb_sexo.get()
    coleta_end = caixa_end_cad.get()
    coleta_n = caixa_n.get()
    coleta_comp = caixa_comp_end.get()
    coleta_cep = caixa_cep.get()
    coleta_estado = lista_estado.get()
    coleta_email = caixa_email_cad.get()
    coleta_cargo = cb_cargo.get()
    with open('DADOS DE CADASTRO.txt', 'a') as cadastro:
        cadastro.write('\n CÓDIGO: {} \n NOME: {}\n TELEFONE: {}\n SEXO: {} \n ENDEREÇO: {}\n N° CASA: {} \n COMPLEMENTO: {} \n CEP: {} \n ESTADO: {}\n E-MAIL: {} \n CARGO: {} \n '.format(coleta_cod, coleta_nome_cad, coleta_fone, coleta_sexo, coleta_end, coleta_n, coleta_comp, coleta_cep, coleta_estado, coleta_email, coleta_cargo))
        cadastro.close()
        print('DADOS SALVOS')

#cod do usuário
cod_cad = Label(tela2, text='CÓDIGO', bg='#D8E1FF')
cod_cad.place(x=1, y=1)
caixa_cod_cad = Entry(tela2, border=2)
caixa_cod_cad.place(x=60, y=1, width = 50)

#campo de nome do cadastro
nome_cad = Label(tela2, text='NOME', bg='#D8E1FF')
nome_cad.place(x=150, y=1)
caixa_nome_cad = Entry(tela2, border=2)
caixa_nome_cad.place(x=200, y=1, width = 250)

#campo de telefone
fone_cad = Label(tela2, text='TELEFONE',  bg='#D8E1FF')
fone_cad.place(x=470, y=1)
caixa_fone_cad = Entry(tela2, border=2)
caixa_fone_cad.place(x=550, y=1, width = 150)

#campo de endereço
end_cad = Label(tela2, text='ENDEREÇO', bg='#D8E1FF')
end_cad.place(x=1, y=50)
caixa_end_cad = Entry(tela2, border=2)
caixa_end_cad.place(x=80, y=50, width = 250)

#campo sobre sexo do usuário 
lista_sexo =['MASCULINO', 'FEMININO', 'OUTROS']
lb_sexo = Label(tela2, text='SEXO',bg='#D8E1FF')
lb_sexo.place(x=480, y=100)
cb_sexo = ttk.Combobox(tela2, values=lista_sexo, state='readionly')
cb_sexo.set('SELECIONE')
cb_sexo.place(x=530, y=100)

#campo de numero da casa
n = Label(tela2, text='N°', bg='#D8E1FF')
n.place(x=350, y=50)
caixa_n = Entry(tela2, border=2)
caixa_n.place(x=380, y=50, width=40)

#campo de complemento
comp_end = Label(tela2, text='Complemento', bg='#D8E1FF')
comp_end.place(x=440, y=50)
caixa_comp_end = Entry(tela2, border=2)
caixa_comp_end.place(x=540, y=50,  width = 190)

#cep
cep = Label (tela2, text='CEP', bg='#D8E1FF')
cep.place(x=1, y=100)
caixa_cep = Entry (tela2, border=2)
caixa_cep.place(x=50, y=100, width=100)

#lista de estados
lista_de_estados = ["Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará",
                    "Espirito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul",
                    "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro",
                    "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina",
                    "São Paulo", "Sergipe", "Tocantins"]

estado = Label(tela2, text='ESTADO', bg='#D8E1FF')
estado.place(x=210, y=100)
lista_estado = ttk.Combobox(tela2, text='ESTADO', values=lista_de_estados, state = 'readionly')
lista_estado.place(x=170, y=100,)
lista_estado.set('SELECIONE')
lista_estado.place(x=280, y=100)

#campo de Email
email_cad = Label(tela2, text='E-MAIL', bg='#D8E1FF')
email_cad.place(x=1, y=140 )
caixa_email_cad = Entry(tela2, border=2)
caixa_email_cad.place(x=60, y=140, width = 350)

#cargo
lista_cargo = ['PROPRIETÁRIO', 'BARBEIRO', 'ATENDERNTE']
cargo = Label(tela2, text='CARGO', bg='#D8E1FF')
cargo.place(x=430, y= 140)
cb_cargo = ttk.Combobox(tela2, text='CARGO', values=lista_cargo, state = 'readionly')
cb_cargo.set('SELECIONE')
cb_cargo.place(x=500, y=140)



bt_arm = Button(tela2, text='ARMAZENAR', bg='#D8E1FF', command=armazenar2)
bt_arm.place(x=140, y=290)
tela_entrar.mainloop()