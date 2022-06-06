from tkinter import*
from tkinter import ttk
from turtle import clear

tela_entrar = Tk()
tela_entrar.geometry('800x450+300+100')
tela_entrar.resizable(width=0, height=0)
tela_entrar.title('BARBERSHOP')
tela_entrar.iconbitmap('corte-de-barba.ico')

note = ttk.Notebook(tela_entrar)
note.place(x=5, y=0, width=790, height=440)


#janela de envio de dados do dia
tela1 = Frame(tela_entrar,bg='#D8E1FF', borderwidth= 2, relief='sunken')
note.add(tela1, text='CONTROLE DIÁRIO')

#janela de cadastro de colaborador
tela2 = Frame(tela_entrar,bg='#D8E1FF', borderwidth= 2, relief='sunken')
note.add(tela2, text='TELA DE CADASTRO')

#tela de cadastro clin]ente
tela3 = Frame(tela_entrar, bg='#D8E1FF', borderwidth=2, relief='sunken')
note.add(tela3, text='CADASTRO CLIENTE')

#dados  armazenar e limpar da tela1
def armazenar(): 
    #função que ira coletar os dados gerais colocados no sistema e ira atribuir a outras variaveis que serão exibidas por meio de print 
    cpf_coleta = caixa_cpf.get() 
    nome_coleta = caixa_nome.get()
    barbeiro_coleta = caixa_nome_barbeiro.get()
    servico_coleta = cb_servicos.get()
    valor_coleta = caixa_valor.get()
    pag_coleta = cb_pagamento.get()
    with open('salvando_dados.txt', 'a') as arquivo:
        arquivo.write('\n CPF: {} \n CLIENTE: {} \n BARBEIRO: {}\n SERVIÇO: {}\n VALOR: {} \n FORMA DE PAGAMENTO: {}\n'.format(cpf_coleta,nome_coleta, barbeiro_coleta, servico_coleta, valor_coleta, pag_coleta ))
        arquivo.close()
        print('DADOS SALVOS')
        
def limpar(): #função que limpar as determinadas variáveis
    caixa_nome.delete(0,END)
    caixa_nome_barbeiro.delete(0,END)
    caixa_valor.delete(0,END)

#dados de armazenar e limpar da tela 2

lista_servicos =['BARBA', 'CORTE NA TESOURA', 'CORTE TESOURA E MÁQUINA']    #lista de serviços da barbearia
lista_pagamento = ['A VISTA','CARTÃO', 'PIX']    #lista das possiveis formas de pagamento

#campo de CPF
cpf = Label(tela1, text='CPF', bg='#D8E1FF')
cpf.place(x=200, y=10)
caixa_cpf = Entry(tela1, border=2)
caixa_cpf.place(x=400, y=10, width=250)

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

#dados e defs da tela2
def armazenar2():
    coleta_cod = caixa_cod_cpf.get()
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

def limpar2(): #função que limpar as determinadas variáveis tela2
    caixa_cod_cpf.delete(0,END)
    caixa_nome_cad.delete(0,END)
    caixa_fone_cad.delete(0,END)
    cb_sexo.delete(0,END)
    caixa_end_cad.delete(0,END)
    caixa_n.delete(0,END)
    caixa_comp_end.delete(0,END)
    caixa_cep.delete(0,END)
    lista_estado.delete(0,END)
    caixa_email_cad.delete(0,END)
    cb_cargo.delete(0,END)

#cod do usuário
cod_cpf = Label(tela2, text='CPF', bg='#D8E1FF')
cod_cpf.place(x=30, y=20) 
caixa_cod_cpf = Entry(tela2, border=2)
caixa_cod_cpf.place(x=70, y=20, width = 130)

#campo de nome do cadastro
nome_cad = Label(tela2, text='NOME', bg='#D8E1FF')
nome_cad.place(x=220, y=20)
caixa_nome_cad = Entry(tela2, border=2)
caixa_nome_cad.place(x=270, y=20, width = 240)

#campo de telefone
fone_cad = Label(tela2, text='TELEFONE',  bg='#D8E1FF')
fone_cad.place(x=530, y=20)
caixa_fone_cad = Entry(tela2, border=2)
caixa_fone_cad.place(x=600, y=20, width = 150)

#campo de endereço
end_cad = Label(tela2, text='ENDEREÇO', bg='#D8E1FF')
end_cad.place(x=1, y=80)
caixa_end_cad = Entry(tela2, border=2)
caixa_end_cad.place(x=80, y=80, width = 250)

#campo de numero da casa
n = Label(tela2, text='N°', bg='#D8E1FF')
n.place(x=350, y=80)
caixa_n = Entry(tela2, border=2)
caixa_n.place(x=380, y=80, width=40)

#campo de complemento
comp_end = Label(tela2, text='Complemento', bg='#D8E1FF')
comp_end.place(x=440, y=80)
caixa_comp_end = Entry(tela2, border=2)
caixa_comp_end.place(x=540, y=80,  width = 190)

#cep
cep = Label (tela2, text='CEP', bg='#D8E1FF')
cep.place(x=30, y=135)
caixa_cep = Entry (tela2, border=2)
caixa_cep.place(x=80, y=135, width=100)

#lista de estados
lista_de_estados = ["Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará",
                    "Espirito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul",
                    "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro",
                    "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina",
                    "São Paulo", "Sergipe", "Tocantins"]

estado = Label(tela2, text='ESTADO', bg='#D8E1FF')
estado.place(x=220, y=135)
lista_estado = ttk.Combobox(tela2, text='ESTADO', values=lista_de_estados, state = 'readionly')
lista_estado.set('SELECIONE')
lista_estado.place(x=280, y=135)

#campo sobre sexo do usuário 
lista_sexo =['MASCULINO', 'FEMININO', 'OUTROS']
lb_sexo = Label(tela2, text='SEXO',bg='#D8E1FF')
lb_sexo.place(x=490, y=135)
cb_sexo = ttk.Combobox(tela2, values=lista_sexo, state='readionly')
cb_sexo.set('SELECIONE')
cb_sexo.place(x=530, y=135)

#campo de Email
email_cad = Label(tela2, text='E-MAIL', bg='#D8E1FF')
email_cad.place(x=30, y=200 )
caixa_email_cad = Entry(tela2, border=2)
caixa_email_cad.place(x=80, y=200, width = 350)

#cargo
lista_cargo = ['PROPRIETÁRIO', 'BARBEIRO', 'ATENDERNTE']
cargo = Label(tela2, text='CARGO', bg='#D8E1FF')
cargo.place(x=470, y= 200)
cb_cargo = ttk.Combobox(tela2, text='CARGO', values=lista_cargo, state = 'readionly')
cb_cargo.set('SELECIONE')
cb_cargo.place(x=530, y=200)

#colocação de botões para armazenar dados e de limpar dados da tela 2
bt_arm = Button(tela2, text='ARMAZENAR', bg='#D8E1FF', command=armazenar2)
bt_arm.place(x=140, y=290, width = 130)
bt_limp = Button(tela2, text='LIMPAR', bg='#D8E1FF', command=limpar2)
bt_limp.place(x=480, y=290, width=100)

#dados e defs da tela3
def armazenar3():
    coleta_cod3 = caixa_cod_cpf3.get()
    coleta_nome_cad3 = caixa_nome_cad3.get()
    coleta_fone3 = caixa_fone_cad3.get()
    coleta_sexo3 = cb_sexo3.get()
    coleta_end3 = caixa_end_cad3.get()
    coleta_n3 = caixa_n3.get()
    coleta_comp3 = caixa_comp_end3.get()
    coleta_cep3 = caixa_cep3.get()
    coleta_estado3 = lista_estado3.get()
    coleta_email3 = caixa_email_cad3.get()
    coleta_cargo3 = cb_cargo3.get()
    with open('DADOS DE CADASTRO.txt', 'a') as cadastro_cliente:
        cadastro_cliente.write('\n CÓDIGO: {} \n NOME: {}\n TELEFONE: {}\n SEXO: {} \n ENDEREÇO: {}\n N° CASA: {} \n COMPLEMENTO: {} \n CEP: {} \n ESTADO: {}\n E-MAIL: {} \n CARGO: {} \n '.format(coleta_cod3, coleta_nome_cad3, coleta_fone3, coleta_sexo3, coleta_end3, coleta_n3, coleta_comp3, coleta_cep3, coleta_estado3, coleta_email3, coleta_cargo3))
        cadastro_cliente.close()
        print('DADOS SALVOS')

def limpar3(): #função que limpar as determinadas variáveis tela2
    caixa_cod_cpf3.delete(0,END)
    caixa_nome_cad3.delete(0,END)
    caixa_fone_cad3.delete(0,END)
    cb_sexo3.delete(0,END)
    caixa_end_cad3.delete(0,END)
    caixa_n3.delete(0,END)
    caixa_comp_end3.delete(0,END)
    caixa_cep3.delete(0,END)
    lista_estado3.delete(0,END)
    caixa_email_cad3.delete(0,END)
    cb_cargo3.delete(0,END)

#cpf do usuário
cod_cpf3 = Label(tela3, text='CPF', bg='#D8E1FF')
cod_cpf3.place(x=30, y=20) 
caixa_cod_cpf3 = Entry(tela3, border=2)
caixa_cod_cpf3.place(x=70, y=20, width = 130)

#campo de nome do cadastro
nome_cad3 = Label(tela3, text='NOME', bg='#D8E1FF')
nome_cad3.place(x=220, y=20)
caixa_nome_cad3 = Entry(tela3, border=2)
caixa_nome_cad3.place(x=270, y=20, width = 240)

#campo de telefone
fone_cad3 = Label(tela3, text='TELEFONE',  bg='#D8E1FF')
fone_cad3.place(x=530, y=20)
caixa_fone_cad3 = Entry(tela3, border=2)
caixa_fone_cad3.place(x=600, y=20, width = 150)

#campo de endereço
end_cad3 = Label(tela3, text='ENDEREÇO', bg='#D8E1FF')
end_cad3.place(x=1, y=80)
caixa_end_cad3 = Entry(tela3, border=2)
caixa_end_cad3.place(x=80, y=80, width = 250)

#campo de numero da casa
n3 = Label(tela3, text='N°', bg='#D8E1FF')
n3.place(x=350, y=80)
caixa_n3 = Entry(tela3, border=2)
caixa_n3.place(x=380, y=80, width=40)

#campo de complemento
comp_end3 = Label(tela3, text='Complemento', bg='#D8E1FF')
comp_end3.place(x=440, y=80)
caixa_comp_end3 = Entry(tela3, border=2)
caixa_comp_end3.place(x=540, y=80,  width = 190)

#cep
cep3 = Label (tela3, text='CEP', bg='#D8E1FF')
cep3.place(x=30, y=135)
caixa_cep3 = Entry (tela3, border=2)
caixa_cep3.place(x=80, y=135, width=100)

#lista de estados
lista_de_estados3 = ["Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará",
                    "Espirito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul",
                    "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro",
                    "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina",
                    "São Paulo", "Sergipe", "Tocantins"]

estado3 = Label(tela3, text='ESTADO', bg='#D8E1FF')
estado3.place(x=220, y=135)
lista_estado3 = ttk.Combobox(tela3, text='ESTADO', values=lista_de_estados3, state = 'readionly')
lista_estado3.set('SELECIONE')
lista_estado3.place(x=280, y=135)

#campo sobre sexo do usuário 
lista_sexo3 =['MASCULINO', 'FEMININO', 'OUTROS']
lb_sexo3 = Label(tela3, text='SEXO',bg='#D8E1FF')
lb_sexo3.place(x=490, y=135)
cb_sexo3 = ttk.Combobox(tela3, values=lista_sexo3, state='readionly')
cb_sexo3.set('SELECIONE')
cb_sexo3.place(x=530, y=135)

#campo de Email
email_cad3 = Label(tela3, text='E-MAIL', bg='#D8E1FF')
email_cad3.place(x=30, y=200 )
caixa_email_cad3 = Entry(tela3, border=2)
caixa_email_cad3.place(x=80, y=200, width = 350)

#cargo nesse caso só serve para passar o parametro de cliente
lista_cargo3 = ['CLIENTE']
cargo3 = Label(tela3, text='CARGO', bg='#D8E1FF')
cargo3.place(x=470, y= 200)
cb_cargo3 = ttk.Combobox(tela3, text='CARGO', values=lista_cargo3, state = 'readionly')
cb_cargo3.set('SELECIONE')
cb_cargo3.place(x=530, y=200)

#colocação de botões para armazenar dados e de limpar dados da tela 2
bt3_arm = Button(tela3, text='ARMAZENAR', bg='#D8E1FF', command=armazenar3)
bt3_arm.place(x=140, y=290, width = 130)
bt3_limp = Button(tela3, text='LIMPAR', bg='#D8E1FF', command=limpar3)
bt3_limp.place(x=480, y=290, width=100)


tela_entrar.mainloop()