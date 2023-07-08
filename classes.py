# Classe Usário com seus atributos privados
class Usuario:

    def __init__(self, nome=None, sobrenome=None, email=None, bairro=None, dt_nascimento=None):
        self._nome = nome
        self._sobrenome = sobrenome
        self._email = email
        self._bairro = bairro
        self._dt_nascimento = dt_nascimento

    #getters e setters
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value
    @property
    def sobrenome(self):
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, value):
        self._sobrenome = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def bairro(self):
        return self._bairro

    @bairro.setter
    def bairro(self, value):
        self._bairro = value

    @property
    def dt_nascimento(self):
        return self._dt_nascimento

    @dt_nascimento.setter
    def dt_nascimento(self, value):
        self._dt_nascimento = value


# Classe Motorista com seus atributos privados
class Motorista:

    def __init__(self, nome, sobrenome, num_cnh, dt_nascimento):
        self._nome = nome
        self._sobrenome = sobrenome
        self._num_cnh = num_cnh
        self._dt_nascimento = dt_nascimento

    # getters e setters
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def sobrenome(self):
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, value):
        self._sobrenome = value

    @property
    def num_cnh(self):
        return self._num_cnh

    @num_cnh.setter
    def num_cnh(self, value):
        self._num_cnh = value

    @property
    def dt_nascimento(self):
        return self._dt_nascimento

    @dt_nascimento.setter
    def dt_nascimento(self, value):
        self._dt_nascimento = value


# Classe Cartão com seus atributos privados
class Cartao:

    def __init__(self, id_proprietario, qtd_creditos, tipo_cartao, dt_emissao):
        self._id_proprietario = id_proprietario
        self._qtd_creditos = qtd_creditos
        self._tipo_cartao = tipo_cartao
        self._dt_emissao = dt_emissao

    # getters e setters
    @property
    def id_proprietario(self):
        return self._id_proprietario

    @id_proprietario.setter
    def id_proprietario(self, value):
        self._id_proprietario = value

    @property
    def qtd_creditos(self):
        return self._qtd_creditos

    @qtd_creditos.setter
    def qtd_creditos(self, value):
        self._qtd_creditos = value

    @property
    def tipo_cartao(self):
        return self._tipo_cartao

    @tipo_cartao.setter
    def tipo_cartao(self, value):
        self._tipo_cartao = value

    @property
    def dt_emissao(self):
        return self._dt_emissao

    @dt_emissao.setter
    def dt_emissao(self, value):
        self._dt_emissao = value


# Classe Ônibus com seus atributos privados
class Onibus:

    def __init__(self, id_motorista, num_placa, num_linha, modelo, ano):
        self._id_motorista = id_motorista
        self._num_placa = num_placa
        self._num_linha = num_linha
        self._modelo = modelo
        self._ano = ano

    #getters e setters
    @property
    def id_motorista(self):
        return self._id_motorista

    @id_motorista.setter
    def id_motorista(self, value):
        self._id_motorista = value

    @property
    def num_placa(self):
        return self._num_placa

    @num_placa.setter
    def num_placa(self, value):
        self._num_placa = value

    @property
    def num_linha(self):
        return self._num_linha

    @num_linha.setter
    def num_linha(self, value):
        self._num_linha = value

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        self._modelo = value

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, value):
        self._ano = value
