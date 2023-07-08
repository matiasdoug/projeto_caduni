# Esta classe contem o menu pricipal, menu de cadastro e menu de visualizar
class Menu:

    def menu_principal(self):
        print('\033[1;34;40m*==================================================================*\033[m')
        print('\033[1;34;40m*====================== BEM VINDO AO CAD UNI ======================*\033[m\n')
        print(f'\033[1;34;40mDigite a opção desejada:\033[m \n'
                '\033[1;34;40m[ 1 ] Cadastrar\033[m\n'
                '\033[1;34;40m[ 2 ] Visualizar um cadastro\033[m\n'
                '\033[1;34;40m[ 3 ] Sair\033[m\n')

    def menu_cadastro(self):

        print(f'\033[1;34;40mO que deseja cadastrar?\033[m \n'
              '\033[1;34;40m[ 1 ] Usuário\033[m\n'
              '\033[1;34;40m[ 2 ] Motorista\033[m\n'
              '\033[1;34;40m[ 3 ] Cartão\033[m\n'
              '\033[1;34;40m[ 4 ] Ônibus\033[m\n'
              '\033[1;34;40m[ 5 ] Menu principal\033[m\n')

    def menu_visualizar(self):

        print(f'\033[1;34;40mO que deseja visualizar?\033[m \n'
              '\033[1;34;40m[ 1 ] Usuário\033[m\n'
              '\033[1;34;40m[ 2 ] Motorista\033[m\n'
              '\033[1;34;40m[ 3 ] Cartão\033[m\n'
              '\033[1;34;40m[ 4 ] Ônibus\033[m\n'
              '\033[1;34;40m[ 5 ] Voltar ao menu\033[m\n')



