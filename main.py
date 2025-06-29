from models import (
    create_agencia, get_agencia, get_all_agencias, update_agencia, delete_agencia,
    create_cliente, get_cliente, get_all_clientes, update_cliente, delete_cliente,
    create_cartao, get_cartao, get_all_cartoes, update_cartao, delete_cartao,
    create_transferencia, get_transferencia, get_all_transferencias, update_transferencia, delete_transferencia
)
from utils import validate_input, validate_int_input, validate_float_input, validate_date_input, validate_datetime_input
import sys

def display_menu(title, options):
    print(f"\n--- {title} ---")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    print("0. Voltar")
    choice = validate_int_input("Selecione uma opção: ", min_val=0, max_val=len(options))
    return choice

def handle_agencia_menu():
    while True:
        choice = display_menu("Gerenciamento de Agências", [
            "Criar Agência", "Visualizar Agência", "Listar Todas as Agências",
            "Atualizar Agência", "Deletar Agência"
        ])

        if choice == 1:
            agencia_id = validate_int_input("ID da Agência: ")
            nome = validate_input("Nome da Agência: ")
            cidade = validate_input("Cidade da Agência: ")
            create_agencia(agencia_id, nome, cidade)
        elif choice == 2:
            agencia_id = validate_int_input("ID da Agência a visualizar: ")
            agencia = get_agencia(agencia_id)
            if agencia:
                print(f"\nID: {agencia['id_agencia']}, Nome: {agencia['nome']}, Cidade: {agencia['cidade']}")
            else:
                print("Agência não encontrada.")
        elif choice == 3:
            agencias = get_all_agencias()
            if agencias:
                print("\n--- Todas as Agências ---")
                for agencia in agencias:
                    print(f"ID: {agencia['id_agencia']}, Nome: {agencia['nome']}, Cidade: {agencia['cidade']}")
            else:
                print("Nenhuma agência cadastrada.")
        elif choice == 4:
            agencia_id = validate_int_input("ID da Agência a atualizar: ")
            agencia = get_agencia(agencia_id)
            if agencia:
                new_nome = validate_input(f"Novo nome da Agência (atual: {agencia['nome']}): ")
                new_cidade = validate_input(f"Nova cidade da Agência (atual: {agencia['cidade']}): ")
                update_agencia(agencia_id, new_nome, new_cidade)
            else:
                print("Agência não encontrada.")
        elif choice == 5:
            agencia_id = validate_int_input("ID da Agência a deletar: ")
            delete_agencia(agencia_id)
        elif choice == 0:
            break

def handle_cliente_menu():
    while True:
        choice = display_menu("Gerenciamento de Clientes", [
            "Criar Cliente", "Visualizar Cliente", "Listar Todos os Clientes",
            "Atualizar Cliente", "Deletar Cliente"
        ])

        if choice == 1:
            cliente_id = validate_int_input("ID do Cliente: ")
            nome = validate_input("Nome do Cliente: ")
            cpf = validate_input("CPF do Cliente (11 dígitos): ", r"^\d{11}$", "CPF inválido. Deve conter 11 dígitos numéricos.")
            id_agencia = validate_int_input("ID da Agência vinculada: ")
            create_cliente(cliente_id, nome, cpf, id_agencia)
        elif choice == 2:
            cliente_id = validate_int_input("ID do Cliente a visualizar: ")
            cliente = get_cliente(cliente_id)
            if cliente:
                print(f"\nID: {cliente['id_cliente']}, Nome: {cliente['nome']}, CPF: {cliente['cpf']}, ID Agência: {cliente['id_agencia']}")
            else:
                print("Cliente não encontrado.")
        elif choice == 3:
            clientes = get_all_clientes()
            if clientes:
                print("\n--- Todos os Clientes ---")
                for cliente in clientes:
                    print(f"ID: {cliente['id_cliente']}, Nome: {cliente['nome']}, CPF: {cliente['cpf']}, ID Agência: {cliente['id_agencia']}")
            else:
                print("Nenhum cliente cadastrado.")
        elif choice == 4:
            cliente_id = validate_int_input("ID do Cliente a atualizar: ")
            cliente = get_cliente(cliente_id)
            if cliente:
                new_nome = validate_input(f"Novo nome do Cliente (atual: {cliente['nome']}): ")
                new_cpf = validate_input(f"Novo CPF do Cliente (atual: {cliente['cpf']}): ", r"^\d{11}$", "CPF inválido. Deve conter 11 dígitos numéricos.")
                new_id_agencia = validate_int_input(f"Novo ID da Agência vinculada (atual: {cliente['id_agencia']}): ")
                update_cliente(cliente_id, new_nome, new_cpf, new_id_agencia)
            else:
                print("Cliente não encontrado.")
        elif choice == 5:
            cliente_id = validate_int_input("ID do Cliente a deletar: ")
            delete_cliente(cliente_id)
        elif choice == 0:
            break

def handle_cartao_menu():
    while True:
        choice = display_menu("Gerenciamento de Cartões", [
            "Criar Cartão", "Visualizar Cartão", "Listar Todos os Cartões",
            "Atualizar Cartão", "Deletar Cartão"
        ])

        if choice == 1:
            cartao_id = validate_int_input("ID do Cartão: ")
            numero = validate_input("Número do Cartão (16 dígitos): ", r"^\d{16}$", "Número do cartão inválido. Deve conter 16 dígitos numéricos.")
            tipo = validate_input("Tipo do Cartão ('débito' ou 'crédito'): ", r"^(débito|crédito)$", "Tipo de cartão inválido. Use 'débito' ou 'crédito'.")
            validade = validate_date_input("Data de Validade (YYYY-MM-DD): ")
            id_cliente = validate_int_input("ID do Cliente proprietário: ")
            create_cartao(cartao_id, numero, tipo, validade, id_cliente)
        elif choice == 2:
            cartao_id = validate_int_input("ID do Cartão a visualizar: ")
            cartao = get_cartao(cartao_id)
            if cartao:
                print(f"\nID: {cartao['id_cartao']}, Número: {cartao['numero']}, Tipo: {cartao['tipo']}, Validade: {cartao['validade']}, ID Cliente: {cartao['id_cliente']}")
            else:
                print("Cartão não encontrado.")
        elif choice == 3:
            cartoes = get_all_cartoes()
            if cartoes:
                print("\n--- Todos os Cartões ---")
                for cartao in cartoes:
                    print(f"ID: {cartao['id_cartao']}, Número: {cartao['numero']}, Tipo: {cartao['tipo']}, Validade: {cartao['validade']}, ID Cliente: {cartao['id_cliente']}")
            else:
                print("Nenhum cartão cadastrado.")
        elif choice == 4:
            cartao_id = validate_int_input("ID do Cartão a atualizar: ")
            cartao = get_cartao(cartao_id)
            if cartao:
                new_numero = validate_input(f"Novo número do Cartão (atual: {cartao['numero']}): ", r"^\d{16}$", "Número do cartão inválido. Deve conter 16 dígitos numéricos.")
                new_tipo = validate_input(f"Novo tipo do Cartão (atual: {cartao['tipo']}) ('débito' ou 'crédito'): ", r"^(débito|crédito)$", "Tipo de cartão inválido. Use 'débito' ou 'crédito'.")
                new_validade = validate_date_input(f"Nova data de Validade (atual: {cartao['validade']}) (YYYY-MM-DD): ")
                new_id_cliente = validate_int_input(f"Novo ID do Cliente proprietário (atual: {cartao['id_cliente']}): ")
                update_cartao(cartao_id, new_numero, new_tipo, new_validade, new_id_cliente)
            else:
                print("Cartão não encontrado.")
        elif choice == 5:
            cartao_id = validate_int_input("ID do Cartão a deletar: ")
            delete_cartao(cartao_id)
        elif choice == 0:
            break

def handle_transferencia_menu():
    while True:
        choice = display_menu("Gerenciamento de Transferências", [
            "Criar Transferência", "Visualizar Transferência", "Listar Todas as Transferências",
            "Atualizar Transferência", "Deletar Transferência"
        ])

        if choice == 1:
            transferencia_id = validate_int_input("ID da Transferência: ")
            valor = validate_float_input("Valor da Transferência: ", min_val=0.01)
            data = validate_datetime_input("Data e Hora da Transferência (YYYY-MM-DD HH:MM:SS): ")
            id_cliente_origem = validate_int_input("ID do Cliente de Origem: ")
            id_cliente_destino = validate_int_input("ID do Cliente de Destino: ")
            create_transferencia(transferencia_id, valor, data, id_cliente_origem, id_cliente_destino)
        elif choice == 2:
            transferencia_id = validate_int_input("ID da Transferência a visualizar: ")
            transferencia = get_transferencia(transferencia_id)
            if transferencia:
                print(f"\nID: {transferencia['id_transferencia']}, Valor: {transferencia['valor']}, Data: {transferencia['data']}, Origem: {transferencia['id_cliente_origem']}, Destino: {transferencia['id_cliente_destino']}")
            else:
                print("Transferência não encontrada.")
        elif choice == 3:
            transferencias = get_all_transferencias()
            if transferencias:
                print("\n--- Todas as Transferências ---")
                for transferencia in transferencias:
                    print(f"ID: {transferencia['id_transferencia']}, Valor: {transferencia['valor']}, Data: {transferencia['data']}, Origem: {transferencia['id_cliente_origem']}, Destino: {transferencia['id_cliente_destino']}")
            else:
                print("Nenhuma transferência cadastrada.")
        elif choice == 4:
            transferencia_id = validate_int_input("ID da Transferência a atualizar: ")
            transferencia = get_transferencia(transferencia_id)
            if transferencia:
                new_valor = validate_float_input(f"Novo valor da Transferência (atual: {transferencia['valor']}): ", min_val=0.01)
                new_data = validate_datetime_input(f"Nova data e hora da Transferência (atual: {transferencia['data']}) (YYYY-MM-DD HH:MM:SS): ")
                new_id_cliente_origem = validate_int_input(f"Novo ID do Cliente de Origem (atual: {transferencia['id_cliente_origem']}): ")
                new_id_cliente_destino = validate_int_input(f"Novo ID do Cliente de Destino (atual: {transferencia['id_cliente_destino']}): ")
                update_transferencia(transferencia_id, new_valor, new_data, new_id_cliente_origem, new_id_cliente_destino)
            else:
                print("Transferência não encontrada.")
        elif choice == 5:
            transferencia_id = validate_int_input("ID da Transferência a deletar: ")
            delete_transferencia(transferencia_id)
        elif choice == 0:
            break

def main_menu():
    while True:
        choice = display_menu("Sistema de Banco de Dados", [
            "Gerenciar Agências", "Gerenciar Clientes",
            "Gerenciar Cartões", "Gerenciar Transferências"
        ])

        if choice == 1:
            handle_agencia_menu()
        elif choice == 2:
            handle_cliente_menu()
        elif choice == 3:
            handle_cartao_menu()
        elif choice == 4:
            handle_transferencia_menu()
        elif choice == 0:
            print("Saindo do sistema. Até mais!")
            sys.exit() # Exit the program

if __name__ == "__main__":
    main_menu()