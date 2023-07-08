# Projeto Cad Uni
# python version 3.10

# importando módulos
import time
from menu import Menu
from metodos import Validacao


# rodando como script
if __name__ == "__main__":
    # instacia a classe menu
    m = Menu()
    # instacia a classe validação
    v = Validacao()

    # chama as funções do menu para escolha do usuário
    while True:
        try:
            m.menu_principal()
            opc = int(input('\033[1;34;40mDigite a opçao desejada:\033[m \n'))
            if opc == 1:
                time.sleep(0.2)
                m.menu_cadastro()
                opc = int(input('\033[1;34;40mDigite a opçao desejada:\033[m\n'))

                if opc == 1:
                    time.sleep(0.2)
                    v.cadastrar_usuario()
                    print('\033[1;34;40mDeseja continuar? [s/n]\033[m')
                    opc = input().upper()
                    if opc == 'S':
                        time.sleep(0.2)
                        continue

                    elif opc == 'N':
                        print('\033[1;34;40mVolte sempre!!\033[m')
                        break

                    else:
                        print('\033[1;34;40mOpção inválida\033[m')
                        time.sleep(0.8)

                elif opc == 2:
                    time.sleep(0.2)
                    v.cadastrar_motorista()
                    print('\033[1;34;40mDeseja continuar? [s/n]\033[m')
                    opc = input().upper()
                    if opc == 'S':
                        time.sleep(0.2)
                        continue

                    elif opc == 'N':
                        print('\033[1;34;40mVolte sempre!!\033[m')
                        break

                    else:
                        print('\033[1;34;40mOpção inválida\033[m')
                        time.sleep(0.8)

                elif opc == 3:
                    time.sleep(0.2)
                    v.cadastrar_cartao()
                    print('\033[1;34;40mDeseja continuar? [s/n]\033[m')
                    opc = input().upper()
                    if opc == 'S':
                        time.sleep(0.2)
                        continue

                    elif opc == 'N':
                        print('\033[1;34;40mVolte sempre!!\033[m')
                        break

                    else:
                        print('\033[1;34;40mOpção inválida\033[m')
                        time.sleep(0.8)

                elif opc == 4:
                    time.sleep(0.2)
                    v.cadastrar_onibus()
                    print('\033[1;34;40mDeseja continuar? [s/n]\033[m')
                    opc = input().upper()
                    if opc == 'S':
                        time.sleep(0.2)
                        continue

                    elif opc == 'N':
                        print('\033[1;34;40mVolte sempre!!\033[m')
                        break

                    else:
                        print('\033[1;34;40mOpção inválida\033[m')
                        time.sleep(0.8)

                elif opc == 5:
                    time.sleep(0.2)
                    m.menu_principal()

                else:
                    print('\033[1;34;40mDigite uma opção válida\033[m\n\n')
                    time.sleep(0.8)

            elif opc == 2:
                time.sleep(0.2)
                m.menu_visualizar()
                opc = int(input('\033[1;34;40mDigite a opção desejada:\033[m \n'))

                if opc == 1:
                    time.sleep(0.2)
                    v.visualizar_usuario()
                    print('\033[1;34;40mDeseja continuar? [s/n]\033[m')
                    opc = input().upper()
                    if opc == 'S':
                        time.sleep(0.2)
                        continue

                    elif opc == 'N':
                        print('\033[1;34;40mVolte sempre!!\033[m')
                        break

                    else:
                        print('\033[1;34;40mOpção inválida\033[m')
                        time.sleep(0.8)

                elif opc == 2:
                    time.sleep(0.2)
                    v.visualizar_motorista()
                    print('\033[1;34;40mDeseja continuar? [s/n]\033[m')
                    opc = input().upper()
                    if opc == 'S':
                        time.sleep(0.2)
                        continue

                    elif opc == 'N':
                        print('\033[1;34;40mVolte sempre!!\033[m')
                        break

                    else:
                        print('\033[1;34;40mOpção inválida\033[m')
                        time.sleep(0.8)

                elif opc == 3:
                    time.sleep(0.2)
                    v.visualizar_cartao()
                    print('\033[1;34;40mDeseja continuar? [s/n]\033[m')
                    opc = input().upper()
                    if opc == 'S':
                        continue

                    elif opc == 'N':
                        print('\033[1;34;40mVolte sempre!!\033[m')
                        break

                    else:
                        print('\033[1;34;40mOpção inválida\033[m')
                        time.sleep(0.8)

                elif opc == 4:
                    time.sleep(0.2)
                    v.visualizar_onibus()
                    print('\033[1;34;40mDeseja continuar? [s/n]\033[m')
                    opc = input().upper()
                    if opc == 'S':
                        time.sleep(0.2)
                        continue

                    elif opc == 'N':
                        print('\033[1;34;40mVolte sempre!!\033[m')
                        break

                    else:
                        print('\033[1;34;40mOpção inválida\033[m')
                        time.sleep(0.8)

                elif opc == 5:
                    time.sleep(0.2)
                    m.menu_principal()

                else:
                    print('\033[1;34;40mDigite uma opção válida:\033[m')
                    time.sleep(0.8)

            elif opc == 3:
                print('\033[1;34;40mVolte sempre!!\033[m')
                break

            else:
                print('\033[1;34;40mOpção inválida!\033[m\n\n')
                time.sleep(0.8)

        except ValueError:
            print('\033[1;34;40mOpção inválida!\033[m\n\n')
            time.sleep(0.8)
