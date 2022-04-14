class ClienteEduardoAquino:
    _total = 0

    def __init__(self, cpf, nome, email):
        self._cpf = cpf
        self._nome = nome
        self._email = email
        ClienteEduardoAquino._total += 1

    @property
    def cpf(self):
        return self._cpf

    @property
    def nome(self):
        return self._nome

    @property
    def email(self):
        return self._email

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @email.setter
    def email(self, email):
        self._email = email

    def imprimir(self):
        print(f'CPF: {self._cpf}\nNome: {self._nome}\nE-mail: {self._email}')

    @staticmethod
    def total_clientes():
        return f'Total de clientes: {ClienteEduardoAquino._total}'

    def fix_cpf(self):
        self._cpf = ''.join(a for a in self._cpf if a.isnumeric())
        return self._cpf


class ContaEduardoAquino:
    _total = 0

    def __init__(self, agencia, numero, saldo, titular):
        self._agencia = agencia
        self._numero = numero
        self._saldo = saldo
        self._titular = titular
        ContaEduardoAquino._total += 1

    @property
    def agencia(self):
        return self._agencia

    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return self._saldo

    @property
    def titular(self):
        return self._titular

    @agencia.setter
    def agencia(self, agencia):
        self._agencia = agencia

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    def imprimir(self):
        print(f'Agência: {self._agencia}\nNúmero: {self.visually_printable_account_number()}\nSaldo: R$ '
              f'{self._saldo:.2f}')

    @staticmethod
    def total_contas():
        return f'Total de contas: {ContaEduardoAquino._total}'

    def fix_account_number(self):
        self._numero = ''.join(a for a in self._numero if a.isnumeric())
        return self._numero

    def get_saldo(self):
        return self._saldo

    def visually_printable_account_number(self):
        self._numero = str(self._numero)
        self._numero = list(self._numero)
        while len(self._numero) < 9:
            self._numero.insert(0, '0')
        self._numero.insert(8, '-')
        self._numero = ''.join(self._numero)
        return self._numero


customers, accounts, stuff_to_print = [], [], []


def visually_printable_cpf(cpf):
    cpf = list(cpf)
    while len(cpf) < 11:
        cpf.insert(0, '0')
    for a in range(3, 12, 4):
        if a < 10:
            cpf.insert(a, '.')
        else:
            cpf.insert(a, '-')
    cpf = ''.join(cpf)
    return cpf


def fix_account_number(number):
    number = ''.join(a for a in number if a.isnumeric())
    number = int(number)
    return number


def fix_cpf(cpf):
    cpf = ''.join(a for a in cpf if a.isnumeric())
    cpf = int(cpf)
    return cpf


def fix_choice(option, value):
    if (type(option) == int and option in range(1, value)) or (option.isnumeric() and int(option) in range(1, value)):
        option = int(option)
        return option
    else:
        return False


def leave():
    answer = input('Tem certeza que deseja sair (SIM/NÃO)? ').strip().upper()[0]
    if answer == 'S':
        print('Programa Atv 3 - v.1.0 finalizado!')
        exit()
    else:
        menu()


def listar_clientes_por_ordem_saldo():
    global stuff_to_print
    stuff_to_print.clear()
    customers_in_stuff_to_print, counter = [], 1
    if not accounts:
        print('Não há contas cadastradas')
    else:
        stuff_to_print = sorted(accounts, key=ContaEduardoAquino.get_saldo)
        for a in stuff_to_print:
            if a.titular not in customers_in_stuff_to_print:
                customers_in_stuff_to_print.append(a)
        print(ContaEduardoAquino.total_contas())
        print(ClienteEduardoAquino.total_clientes())
        print('')
        for c in stuff_to_print:
            print(f'Conta {counter} - Titular: {c.titular.nome}')
            c.imprimir()
            print('=' * 45)
            counter += 1
    menu()


def search_by_name():
    stuff_to_print.clear()
    counter, name = 0, input('Nome: ').strip().title()
    for a in filter(lambda x: x.titular.nome == name, accounts):
        stuff_to_print.append(a)
        counter += 1
    if counter == 0:
        print(f'Não há contas cadastradas no nome de {name}!')
    elif counter == 1:
        print(f'Foi encontrada uma conta no nome de {name}!')
        for b in stuff_to_print:
            print('\nConta')
            b.imprimir()
    elif counter > 1:
        print(f'Foram encontradas {counter} contas no nome de {name}!')
        counter2 = 1
        for c in stuff_to_print:
            print(f'\nConta {counter2}')
            c.imprimir()
            counter2 += 1
    menu()


def search_by_cpf():
    stuff_to_print.clear()
    counter, cpf, name = 0, input('CPF [Ex.: 000.000.000-00]: ').strip().title(), None
    cpf = fix_cpf(cpf)
    for a in filter(lambda x: x.titular.cpf == cpf, accounts):
        stuff_to_print.append(a)
        name = a.titular.nome
        counter += 1
    cpf = visually_printable_cpf(str(cpf))
    if counter == 0:
        print(f'Não há contas cadastradas com o CPF {cpf}!')
    elif counter == 1:
        print(f'Foi encontrada uma conta no nome de {name}!')
        for b in stuff_to_print:
            print('\nConta')
            b.imprimir()
    elif counter > 1:
        print(f'Foram encontradas {counter} contas no nome de {name}!')
        counter2 = 1
        for c in stuff_to_print:
            print(f'\nConta {counter2}')
            c.imprimir()
            counter2 += 1
    menu()


def buscar_contas_por_cpf_ou_nome():
    print('Informe o método de busca: ')
    choice = input('[ 1 ] - CPF\n[ 2 ] - Nome\nOpção: ')
    choice = fix_choice(choice, 3)
    if not choice:
        print('Opção Inválida!')
        buscar_contas_por_cpf_ou_nome()
    elif choice == 1:
        search_by_cpf()
    elif choice == 2:
        search_by_name()


def register_customer_to_account(account):
    print('=' * 45)
    print('==============Novo Cliente==============')
    customer = ClienteEduardoAquino(input('CPF [Ex.: 000.000.000-00]: '), input('Nome: ').strip().title(), input(
        'E-mail: ').strip().lower())
    if "@" not in customer.email:
        print('E-mail inválido!')
        customer.email = input('E-mail: ').strip().lower()
    else:
        customer.cpf = customer.fix_cpf()
        customer.cpf = int(customer.cpf)
        customers.append(customer)
        account.titular = customer
        accounts.append(account)
        print('Cadastro realizado com sucesso!')


def existing_or_new(position):
    choice2 = input('[ 1 ] - Cliente existente\n[ 2 ] - Novo cliente\nOpção: ')
    choice2 = fix_choice(choice2, 3)
    if not choice2:
        print('Opção Inválida!')
        existing_or_new(position)
    elif choice2 == 1:
        cpf = input('Informe o CPF [Ex.: 000.000.000-00]: ')
        cpf = fix_cpf(cpf)
        counter = 0
        customer_has_account = False
        for a in customers:
            if a.cpf == cpf:
                for b in accounts:
                    if b.titular is not None:
                        if b.titular.cpf == a.cpf:
                            customer_has_account = True
                            break
                    else:
                        continue
                if customer_has_account:
                    print(f'{a.nome} já possui uma conta! Escolha um cliente sem conta ou cadastre um novo cliente')
                    existing_or_new(position)
                else:
                    accounts[position - 1].titular = a
                    counter += 1
        if counter == 0:
            print('Usuário não encontrado! Cadastre o cliente!')
            register_customer_to_account(accounts[position - 1])
        else:
            print('Cadastro realizado com sucesso!')
    elif choice2 == 2:
        register_customer_to_account(accounts[position - 1])


def register_new_account(account):
    print('Escolha uma opção: ')
    choice = input('[ 1 ] - Deixar sem cliente\n[ 2 ] - Adicionar um cliente\nOpção: ')
    choice, choice2 = fix_choice(choice, 3), 'a'
    if not choice:
        print('Opção Inválida!')
        register_new_account(account)
    elif choice == 1:
        accounts.append(account)
        print('Cadastro realizado com sucesso!')
    elif choice == 2:
        customer_has_account, name = None, None
        while not fix_choice(choice2, 3) or customer_has_account is None or customer_has_account is True:
            choice2 = input('[ 1 ] - Cliente existente\n[ 2 ] - Novo cliente\nOpção: ')
            choice2 = fix_choice(choice2, 3)
            if not choice2:
                print('Opção Inválida!')
            elif choice2 == 1:
                print('==============Cliente Existente==============')
                cpf = input('Informe o CPF [Ex.: 000.000.000-00]: ')
                cpf = fix_cpf(cpf)
                counter = 0
                for a in customers:
                    if a.cpf == cpf:
                        for b in accounts:
                            if b.titular.cpf == a.cpf:
                                customer_has_account = True
                                break
                        if customer_has_account:
                            print(f'{a.nome} já possui uma conta! Escolha um cliente sem conta ou cadastre um novo '
                                  f'cliente!')
                        else:
                            account.titular = a
                            name = account.titular.nome
                            counter += 1
                if customer_has_account is None and counter == 0:
                    print('Usuário não encontrado!')
                    choice2 = 'a'
                elif counter > 0:
                    accounts.append(account)
                    customer_has_account = False
                    print(f'Cadastro realizado com sucesso no nome de {name}!')
            elif choice2 == 2:
                register_customer_to_account(account)
                customer_has_account = False


def add_customer_to_account():
    counter, data_confirmed = 1, False
    while counter <= 3 and data_confirmed is False:
        agency, number = input('Informe a agência [Ex.: 1234]: '), input('Informe o número da conta [Ex.: 12345678-9]: '
                                                                         )
        while not agency.isnumeric():
            print('Agência Inválida!')
            agency = input('Informe a agência [Ex.: 1234]: ')
        else:
            agency = int(agency)
        number = fix_account_number(number)
        equal = False
        for a in accounts:
            if a.agencia == agency and a.numero == number:
                existing_or_new(accounts.index(a) + 1)
                equal, data_confirmed = True, True
                break
        if not equal:
            print('Agência ou número errado!')
            counter += 1
    else:
        if counter > 3:
            print('Muitas tentativas!')
            register_account()


def register_account():
    print('=' * 45)
    choice = input('[ 1 ] - Adicionar um cliente a uma conta já existente\n[ 2 ] - Cadastrar uma nova conta\nOpção: ')
    choice = fix_choice(choice, 3)
    if choice == 1:
        add_customer_to_account()
    elif choice == 2:
        agencia, numero, saldo = input('Agência [Ex.: 1234]: '), input('Número [Ex.: 12345678-9]: '), float(input(
            'Saldo [Ex.: R$ 100.00]: R$ '))
        while not agencia.isnumeric():
            print('Agência Inválida!')
            agencia = input('Agência [Ex.: 1234]: ')
        else:
            agencia = int(agencia)
        account = ContaEduardoAquino(agencia, numero, saldo, None)
        account.numero = int(account.fix_account_number())
        register_new_account(account)
    else:
        print('Opção Inválida!')
        register_account()
    menu()


def register_customer():
    print('=' * 45)
    customer = ClienteEduardoAquino(input('CPF [Ex.: 000.000.000-00]: '), input('Nome: ').strip().title(), input(
        'E-mail: ').strip().lower())
    while '@' not in customer.email:
        print('E-mail inválido!')
        customer.email = input('E-mail: ').strip().lower()
    else:
        customer.cpf = customer.fix_cpf()
        customer.cpf = int(customer.cpf)
        customers.append(customer)
        print('Cadastro realizado com sucesso!')
        menu()


def menu():
    print('=' * 45)
    print('{:^45}'.format('Programa Atv 4 - v.1.0'))
    print('[ 1 ] - Cadastrar Cliente\n[ 2 ] - Cadastrar Conta\n[ 3 ] - Buscar contas por CPF ou Nome\n[ 4 ] - Listar '
          'clientes por ordem de saldo\n[ 5 ] - Sair')
    choice = input('Opção: ')
    choice = fix_choice(choice, 7)
    print('=' * 45)
    if choice == 1:
        register_customer()
    elif choice == 2:
        register_account()
    elif choice == 3:
        buscar_contas_por_cpf_ou_nome()
    elif choice == 4:
        listar_clientes_por_ordem_saldo()
    elif choice == 5:
        leave()
    else:
        print('Opção Inválida!')
        menu()


menu()
