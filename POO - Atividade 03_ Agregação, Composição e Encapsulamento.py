class ClienteEduardoAquino:
    def __init__(self, cpf, nome, email, telefone, endereco):
        self._cpf = cpf
        self._nome = nome
        self._email = email
        self._telefone = telefone
        self._endereco = endereco

    @property
    def cpf(self):
        return self._cpf

    @property
    def nome(self):
        return self._nome

    @property
    def email(self):
        return self._email

    @property
    def telefone(self):
        return self._telefone

    @property
    def endereco(self):
        return self._endereco

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @email.setter
    def email(self, email):
        self._email = email

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    def fix_cellphone_number(self):
        new_phone = []
        for a in self._telefone:
            if a != '(' and a != ')' and a != '-':
                new_phone.append(a)
        self._telefone = ''.join(new_phone)
        self._telefone = self._telefone.split()
        self._telefone = ''.join(self._telefone)
        return self._telefone

    def print_customers_in(self):
        print(f'CPF: {self._cpf}\nNome: {self._nome}\nE-mail: {self._email}\nTelefone: {self._telefone}\nEndereço: '
              f'{self._endereco}')
        print('=' * 45)


class CarroEduardoAquino:
    def __init__(self, modelo, marca, ano, preco, dono):
        self._modelo = modelo
        self._marca = marca
        self._ano = ano
        self._preco = preco
        self._titular = dono

    @property
    def modelo(self):
        return self._modelo

    @property
    def marca(self):
        return self._marca

    @property
    def ano(self):
        return self._ano

    @property
    def preco(self):
        return self._preco

    @property
    def titular(self):
        return self._titular

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @ano.setter
    def ano(self, ano):
        self._ano = ano

    @preco.setter
    def preco(self, preco):
        self._preco = preco

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    def aumentar_preco(self, valor):
        self._preco += (self._preco * valor) / 100

    def diminuir_preco(self, valor):
        self._preco -= (self._preco * valor) / 100

    def print_cars(self):
        print(f'Modelo: {self._modelo}\nMarca: {self._marca}\nAno: {self._ano}\nPreço: R$ {self._preco:.2f}\n')
        print('=' * 45)


customers, cars, stuff_to_print = [], [], []


def print_customers_out():
    counter = 1
    for a in customers:
        print(f'[ {counter} ] - {a.nome}')
        counter += 1


def fix_choice(option, valor):
    if (type(option) == int and option in range(1, valor)) or (option.isnumeric() and int(option) in range(1, valor)):
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


def listar_todos_carros_por_cliente():
    print('Foi encontrado 1 carro!' if len(cars) < 2 else f'Foram encontrados {len(cars)} carros!')
    counter = 1
    for a in customers:
        print(f'\nCliente {counter}\n{a.nome}')
        counter2 = 1
        for b in cars:
            if a == b.titular:
                print(f'\nCarro {counter2}')
                b.print_cars()
                counter2 += 1
        counter += 1
    menu()


def buscar_clientes_por_marca():
    stuff_to_print.clear()
    counter, brand = 0, input('Marca: ').strip().title()
    for a in cars:
        if a.marca == brand and a.titular not in stuff_to_print:
            stuff_to_print.append(a.titular)
            counter += 1
    if counter == 0:
        print(f'Não há clientes proprietários de carros {brand}!')
    elif counter == 1:
        print(f'Foi encontrado um proprietário de um carro {brand}')
        for b in stuff_to_print:
            print('\nCliente')
            b.print_customers_in()
    elif counter > 1:
        print(f'Foram encontrados {counter} proprietários de carros {brand}!')
        counter2 = 1
        for c in stuff_to_print:
            print(f'\nCliente {counter2}')
            c.print_customers_in()
            counter2 += 1
    menu()


def buscar_carros_por_nome():
    stuff_to_print.clear()
    counter, name = 0, input('Nome: ').strip().title()
    for a in list(filter(lambda x: x.titular.nome == name, cars)):
        stuff_to_print.append(a)
        counter += 1
    if counter == 0:
        print(f'Não há carros cadastrados no nome de {name}!')
    elif counter == 1:
        print(f'Foi encontrado um carro no nome de {name}!')
        for b in stuff_to_print:
            print('\nCarro')
            b.print_cars()
    elif counter > 1:
        print(f'Foram encontrados {counter} carros no nome de {name}!')
        counter2 = 1
        for c in stuff_to_print:
            print(f'\nCarro {counter2}')
            c.print_cars()
            counter2 += 1
    menu()


def register_customer_to_car(car):
    print('=' * 45)
    print('==============Novo Cliente==============')
    customer = ClienteEduardoAquino(int(input('CPF [Ex.: 11111111111]: ')), input('Nome: ').strip().title(), input(
        'E-mail: ').strip().lower(), input('Telefone: '), input('Endereço: '))
    if "@" not in customer.email:
        print('E-mail inválido!')
        register_customer_to_car(car)
    else:
        if not customer.telefone.isnumeric():
            customer.telefone = customer.fix_cellphone_number()
        customers.append(customer)
        car.titular = customer
        cars.append(car)
        print('Cadastro realizado com sucesso!')


def register_new_car(car):
    print('Escolha uma opção: ')
    choice = input('[ 1 ] - Deixar sem cliente\n[ 2 ] - Adicionar um cliente\nOpção: ')
    choice, choice2 = fix_choice(choice, 3), 'a'
    if not choice:
        print('Opção Inválida!')
        register_new_car(car)
    elif choice == 1:
        cars.append(car)
        print('Cadastro realizado com sucesso!')
    elif choice == 2:
        while not fix_choice(choice2, 3):
            choice2 = input('[ 1 ] - Cliente existente\n[ 2 ] - Novo cliente\nOpção: ')
            choice2 = fix_choice(choice2, 3)
            if not choice2:
                pass
            elif choice2 == 1:
                print('==============Cliente Existente==============')
                cpf = int(input('Informe o CPF [Ex.: 11111111111]: '))
                counter = 0
                for a in customers:
                    if a.cpf == cpf:
                        car.titular = a
                        cars.append(car)
                        counter += 1
                if counter == 0:
                    print('Usuário não encontrado!')
                    choice2 = 'a'
                else:
                    print('Cadastro realizado com sucesso!')
            elif choice2 == 2:
                register_customer_to_car(car)


def existing_or_new(position):
    choice2 = input('[ 1 ] - Cliente existente\n[ 2 ] - Novo cliente\nOpção: ')
    choice2 = fix_choice(choice2, 3)
    if not choice2:
        existing_or_new(position)
    elif choice2 == 1:
        cpf = int(input('Informe o CPF [Ex.: 11111111111]: '))
        counter = 0
        for a in customers:
            if a.cpf == cpf:
                cars[position - 1].titular = a
                counter += 1
        if counter == 0:
            print('Usuário não encontrado!')
            existing_or_new(position)
        else:
            print('Cadastro realizado com sucesso!')
    elif choice2 == 2:
        register_customer_to_car(cars[position - 1])


def add_customer_to_car():
    counter = 1
    print('Escolha um carro: ')
    for a in cars:
        print(f'[ {counter} ] - {a.marca} {a.modelo}, Ano {a.ano}')
        counter += 1
    choice = input('Opção: ')
    choice = fix_choice(choice, len(cars) + 1)
    if not choice:
        print('Opção inválida!')
        add_customer_to_car()
    else:
        existing_or_new(choice)


def register_car():
    print('=' * 45)
    choice = input('[ 1 ] - Adicionar um cliente a um carro já existente\n[ 2 ] - Cadastrar um novo carro\nOpção: ')
    choice = fix_choice(choice, 3)
    if choice == 1:
        add_customer_to_car()
    elif choice == 2:
        modelo, marca, ano, preco = input('Modelo: ').strip().title(), input('Marca: ').strip().title(), int(input(
            'Ano: ')), float(input('Preço [Ex.: 10000.00]: R$ '))
        car = CarroEduardoAquino(modelo, marca, ano, preco, None)
        register_new_car(car)
    else:
        print('Opção Inválida!')
        register_car()
    menu()


def register_customer():
    print('=' * 45)
    customer = ClienteEduardoAquino(int(input('CPF [Ex.: 11111111111]: ')), input('Nome: ').strip().title(), input(
        'E-mail: ').strip().lower(), (input('Telefone: ')), (input('Endereço: ')))
    if "@" not in customer.email:
        print('E-mail inválido!')
        register_customer()
    else:
        if not customer.telefone.isnumeric():
            customer.telefone = customer.fix_cellphone_number()
        customers.append(customer)
        print('Cadastro realizado com sucesso!')
        menu()


def menu():
    print('=' * 45)
    print('{:^45}'.format('Programa Atv 3 - v.1.0'))
    print('[ 1 ] - Cadastrar Cliente\n[ 2 ] - Cadastrar Carro\n[ 3 ] - Buscar carros por Nome\n[ 4 ] - Buscar clientes '
          'por Marca\n[ 5 ] - Listar todos os Carros por Cliente\n[ 6 ] - Sair')
    choice = input('Opção: ')
    choice = fix_choice(choice, 7)
    print('=' * 45)
    if choice == 1:
        register_customer()
    elif choice == 2:
        register_car()
    elif choice == 3:
        buscar_carros_por_nome()
    elif choice == 4:
        buscar_clientes_por_marca()
    elif choice == 5:
        listar_todos_carros_por_cliente()
    elif choice == 6:
        leave()
    else:
        print('Opção Inválida!')
        menu()


menu()
