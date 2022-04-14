class AgendaEduardoAquino:
    def __init__(self, nome, email, telefone, idade, endereco):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.idade = idade
        self.endereco = endereco

    def capitalizar_nome(self):
        self.nome = self.nome.title()
        return self.nome

    def pegar_numero(self):
        return self.endereco.split()[-1]

    def imprimir(self):
        print(f'Nome: {self.capitalizar_nome()}\nE-mail: {self.email}\nTelefone: {self.telefone}\nIdade: {self.idade}\n'
              f'Endereço: {self.endereco.title()}')
        print('================================')

    def fix_cellphone_number(self):
        new_phone = []
        for f in self.telefone:
            if f != '(' and f != ')' and f != '-':
                new_phone.append(f)
        self.telefone = ''.join(new_phone)
        self.telefone = self.telefone.split()
        self.telefone = ''.join(self.telefone)
        return self.telefone

    def get_email(self):
        return self.email

    def get_age(self):
        return self.idade


agendas = []
impressos = []


def sair():
    resp = input('Tem certeza que deseja sair (SIM/NÃO)? ').strip().upper()[0]
    if resp == 'S':
        print('Agenda finalizada!')
        exit()
    else:
        menu()


def listar_maiores_idade():
    impressos.clear()
    counter_9 = 0
    if not agendas:
        print('Não há agendas cadastradas.')
    else:
        for n in agendas:
            if n.idade >= 18:
                impressos.append(n)
                counter_9 += 1
        if counter_9 == 0:
            print('Não foram encontradas agendas de pessoas maiores de idade.')
        elif counter_9 == 1:
            print('Foi encontrada 1 agenda de pessoas maiores de idade.\n')
            for o in impressos:
                print('Agenda 1')
                o.imprimir()
        elif counter_9 > 1:
            print(f'Foram encontradas {counter_9} agendas de pessoas maiores de idade.\n')
            counter_10 = 1
            for p in impressos:
                print(f'Agenda {counter_10}')
                p.imprimir()
                counter_10 += 1
    menu()


def listar_por_email():
    if not agendas:
        print('Não há agendas cadastradas.')
    else:
        impressos = sorted(agendas, key=AgendaEduardoAquino.get_email)
        print(f'Total de agendas: {len(impressos)}')
        counter_8 = 1
        for m in impressos:
            print(f'Agenda {counter_8}')
            m.imprimir()
            counter_8 += 1
    menu()


def listar_por_nome():
    if not agendas:
        print('Não há agendas cadastradas.')
    else:
        impressos = sorted(agendas, key=AgendaEduardoAquino.capitalizar_nome)
        print(f'Total de agendas: {len(impressos)}')
        counter_7 = 1
        for l in impressos:
            print(f'Agenda {counter_7}')
            l.imprimir()
            counter_7 += 1
    menu()


def buscar_por_telefone():
    impressos.clear()
    counter_5 = 0
    new_phone_searched = []
    phone = input('Informe o telefone a ser buscado [Ex.: (DDD) 9****-****]: ').strip()
    for h in phone:
        if h != '(' and h != ')' and h != '-':
            new_phone_searched.append(h)
    phone = ''.join(new_phone_searched)
    phone = phone.split()
    phone = ''.join(phone)
    for i in agendas:
        if i.fix_cellphone_number() == phone:
            impressos.append(i)
            counter_5 += 1
    if counter_5 == 0:
        print('Não há agendas cadastradas com esse telefone.')
    elif counter_5 == 1:
        print('Foi encontrada 1 agenda com esse telefone.\n')
        for j in impressos:
            print('Agenda 1')
            j.imprimir()
    elif counter_5 > 1:
        print(f'Foram encontradas {counter_5} agendas com esse telefone.\n')
        counter_6 = 1
        for k in impressos:
            print(f'Agenda {counter_6}')
            k.imprimir()
            counter_6 += 1
    menu()


def buscar_por_email():
    impressos.clear()
    counter_3 = 0
    email = input('Informe o e-mail a ser buscado: ').strip().lower()
    if '@' not in email:
        print('E-mail inválido!')
        buscar_por_email()
    for e in agendas:
        if e.email == email:
            impressos.append(e)
            counter_3 += 1
    if counter_3 == 0:
        print('Não há agendas cadastradas com esse e-mail.')
    elif counter_3 == 1:
        print('Foi encontrada 1 agenda com esse e-mail.\n')
        for f in impressos:
            print('Agenda 1')
            f.imprimir()
    elif counter_3 > 1:
        print(f'Foram encontradas {counter_3} agendas com esse e-mail.\n')
        counter_4 = 1
        for g in impressos:
            print(f'Agenda {counter_4}')
            g.imprimir()
            counter_4 += 1
    menu()


def buscar_por_nome():
    impressos.clear()
    counter_1 = 0
    name = input('Informe o nome a ser buscado: ').strip().title()
    for b in agendas:
        if b.capitalizar_nome() == name:
            impressos.append(b)
            counter_1 += 1
    if counter_1 == 0:
        print('Não há agendas cadastradas com esse nome.')
    elif counter_1 == 1:
        print('Foi encontrada 1 agenda com esse nome.\n')
        for c in impressos:
            print('Agenda 1')
            c.imprimir()
    elif counter_1 > 1:
        print(f'Foram encontradas {counter_1} agendas com esse nome.\n')
        counter_2 = 1
        for d in impressos:
            print(f'Agenda {counter_2}')
            d.imprimir()
            counter_2 += 1
    menu()


def cadastrar():
    print('===============================')
    agenda = AgendaEduardoAquino(input('Nome: ').strip(), input('E-mail: ').strip().lower(),
                                 input('Telefone [Ex.: (DDD) 9****-****]: ').strip(), int(input('Idade: ')),
                                 input('Endereço [Ex.: Rua ***..., Número]: ').strip().title())
    if "@" not in agenda.email:
        print('E-mail inválido!')
        cadastrar()
    else:
        agendas.append(agenda)
        print('Cadastro realizado com sucesso!')
        menu()


def menu():
    print('===============================')
    print('{:^32}'.format('Programa Agenda - v.1.0'))
    print('1 - Cadastrar\n2 - Buscar por Nome\n3 - Buscar por E-mail\n4 - Buscar por telefone\n5 - Listar em ordem por '
          'Nome\n6 - Listar em ordem por E-mail\n7 - Listar Maiores de Idade (>18)\n8 - Sair')
    option = int(input('Opção: '))
    print('===============================')
    if option == 1:
        cadastrar()
    elif option == 2:
        buscar_por_nome()
    elif option == 3:
        buscar_por_email()
    elif option == 4:
        buscar_por_telefone()
    elif option == 5:
        listar_por_nome()
    elif option == 6:
        listar_por_email()
    elif option == 7:
        listar_maiores_idade()
    elif option == 8:
        sair()
    else:
        print('Opção Inválida!')
        menu()


menu()

'''
def buscar():
    nome_procurado = input('Nome: ')
    for c in filter(lambda x:x.nome == nome_procurado, contatos):
        c.imprimir()
'''
