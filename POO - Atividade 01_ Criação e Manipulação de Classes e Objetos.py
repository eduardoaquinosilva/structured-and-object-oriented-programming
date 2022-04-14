class CarroEduardoAquino:
    def __init__(self, modelo, marca, ano, preco):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.preco = preco

    def pega_preco(self):
        return self.preco

    def aumentar_preco(self, valor):
        self.preco += (self.preco * valor) / 100

    def aumentar_preco_10(self):
        self.preco = self.preco * 1.1

    def diminuir_preco(self, valor):
        self.preco -= (self.preco * valor) / 100

    def diminuir_preco_5(self):
        self.preco = self.preco * 0.95


carro_eduardo_aquino_1 = CarroEduardoAquino(input('Modelo do carro 1: '), input('Marca do carro 1: '),
                                            int(input('Ano do carro 1: ')), float(input('Preco do carro 1: R$ ')))
carro_eduardo_aquino_2 = CarroEduardoAquino(input('Modelo do carro 2: '), input('Marca do carro 2: '),
                                            int(input('Ano do carro 2: ')), float(input('Preco do carro 2: R$ ')))
carro_eduardo_aquino_3 = CarroEduardoAquino(input('Modelo do carro 3: '), input('Marca do carro 3: '),
                                            int(input('Ano do carro 3: ')), float(input('Preco do carro 3: R$ ')))
carro_eduardo_aquino_4 = CarroEduardoAquino(input('Modelo do carro 4: '), input('Marca do carro 4: '),
                                            int(input('Ano do carro 4: ')), float(input('Preco do carro 4: R$ ')))
carro_eduardo_aquino_5 = CarroEduardoAquino(input('Modelo do carro 5: '), input('Marca do carro 5: '),
                                            int(input('Ano do carro 5: ')), float(input('Preco do carro 5: R$ ')))
carros_eduardo_aquino = [carro_eduardo_aquino_1, carro_eduardo_aquino_2, carro_eduardo_aquino_3, carro_eduardo_aquino_4,
                         carro_eduardo_aquino_5]
carros = sorted(carros_eduardo_aquino, key=CarroEduardoAquino.pega_preco)
for a in carros:
    print(f'Modelo: {a.modelo}')
    print(f'Marca: {a.marca}')
    print(f'Ano: {a.ano}')
    print(f'Preço: R$ {a.preco:.2f}')
