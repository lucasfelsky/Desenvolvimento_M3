from db_connection import create_db_connection, close_db_connection

# --- Agencia CRUD Operations ---

def create_agencia(agencia_id, nome, cidade):
    connection = create_db_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO agencia (id_agencia, nome, cidade) VALUES (%s, %s, %s)",
                           (agencia_id, nome, cidade))
            connection.commit()
            print("Agência criada com sucesso.")
        except Exception as e:
            print(f"Erro ao criar a agência: {e}")
            connection.rollback()
        finally:
            cursor.close()
            close_db_connection(connection)

def get_agencia(agencia_id):
    connection = create_db_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM agencia WHERE id_agencia = %s", (agencia_id,))
            agencia = cursor.fetchone()
            return agencia
        except Exception as e:
            print(f"Erro ao procurar a agência: {e}")
            return None
        finally:
            cursor.close()
            close_db_connection(connection)

def get_all_agencias():
    connection = create_db_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM agencia")
            agencias = cursor.fetchall()
            return agencias
        except Exception as e:
            print(f"Erro ao verificar as agências: {e}")
            return []
        finally:
            cursor.close()
            close_db_connection(connection)

def update_agencia(agencia_id, new_nome, new_cidade):
    connection = create_db_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE agencia SET nome = %s, cidade = %s WHERE id_agencia = %s",
                           (new_nome, new_cidade, agencia_id))
            connection.commit()
            if cursor.rowcount > 0:
                print("Agência atualizada com sucesso.")
            else:
                print("Agência não encontrada e nenhuma alteração feita.")
        except Exception as e:
            print(f"Erro ao atualizar agência: {e}")
            connection.rollback()
        finally:
            cursor.close()
            close_db_connection(connection)

def delete_agencia(agencia_id):
    connection = create_db_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM agencia WHERE id_agencia = %s", (agencia_id,))
            connection.commit()
            if cursor.rowcount > 0:
                print("Agência apagada com sucesso.")
            else:
                print("Agência não encontrada.")
        except Exception as e:
            print(f"Erro ao deletar a agência: {e}")
            connection.rollback()
        finally:
            cursor.close()
            close_db_connection(connection)

# --- Cliente CRUD Operations ---

def create_cliente(cliente_id, nome, cpf, id_agencia):
    connection = create_db_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT id_agencia FROM agencia WHERE id_agencia = %s", (id_agencia,))
            if not cursor.fetchone():
                print(f"Error: Agência com o ID {id_agencia} não existe.")
                return False

            cursor.execute("INSERT INTO cliente (id_cliente, nome, cpf, id_agencia) VALUES (%s, %s, %s, %s)",
                           (cliente_id, nome, cpf, id_agencia))
            connection.commit()
            print("Cliente criado com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao criar o cliente: {e}")
            connection.rollback()
            return False
        finally:
            cursor.close()
            close_db_connection(connection)

def get_cliente(cliente_id):
    connection = create_db_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM cliente WHERE id_cliente = %s", (cliente_id,))
            cliente = cursor.fetchone()
            return cliente
        except Exception as e:
            print(f"Erro ao procurar o cliente: {e}")
            return None
        finally:
            cursor.close()
            close_db_connection(connection)

def get_all_clientes():
    connection = create_db_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM cliente")
            clientes = cursor.fetchall()
            return clientes
        except Exception as e:
            print(f"Erro ao verificar clientes {e}")
            return []
        finally:
            cursor.close()
            close_db_connection(connection)

def update_cliente(cliente_id, new_nome, new_cpf, new_id_agencia):
    connection = create_db_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT id_agencia FROM agencia WHERE id_agencia = %s", (new_id_agencia,))
            if not cursor.fetchone():
                print(f"Error: Agência com ID {new_id_agencia} não existe.")
                return False

            cursor.execute("UPDATE cliente SET nome = %s, cpf = %s, id_agencia = %s WHERE id_cliente = %s",
                           (new_nome, new_cpf, new_id_agencia, cliente_id))
            connection.commit()
            if cursor.rowcount > 0:
                print("Cliente atualizado com sucesso.")
                return True
            else:
                print("Cliente não encontrado ou nenhuma alteração feita.")
                return False
        except Exception as e:
            print(f"Erro ao atualizar o cliente: {e}")
            connection.rollback()
            return False
        finally:
            cursor.close()
            close_db_connection(connection)

def delete_cliente(cliente_id):
    connection = create_db_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM cliente WHERE id_cliente = %s", (cliente_id,))
            connection.commit()
            if cursor.rowcount > 0:
                print("Cliente deletado com sucesso.")
            else:
                print("Cliente não encontrado.")
        except Exception as e:
            print(f"Erro ao deletar o cliente: {e}")
            connection.rollback()
        finally:
            cursor.close()
            close_db_connection(connection)

# --- Cartao CRUD Operations ---

def create_cartao(cartao_id, numero, tipo, validade, id_cliente):
    connection = create_db_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT id_cliente FROM cliente WHERE id_cliente = %s", (id_cliente,))
            if not cursor.fetchone():
                print(f"Error: Cliente com ID {id_cliente} não existe.")
                return False

            cursor.execute("INSERT INTO cartao (id_cartao, numero, tipo, validade, id_cliente) VALUES (%s, %s, %s, %s, %s)",
                           (cartao_id, numero, tipo, validade, id_cliente))
            connection.commit()
            print("Cartão criado com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao criar o cartão: {e}")
            connection.rollback()
            return False
        finally:
            cursor.close()
            close_db_connection(connection)

def get_cartao(cartao_id):
    connection = create_db_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM cartao WHERE id_cartao = %s", (cartao_id,))
            cartao = cursor.fetchone()
            return cartao
        except Exception as e:
            print(f"Erro ao procurar o cartão: {e}")
            return None
        finally:
            cursor.close()
            close_db_connection(connection)

def get_all_cartoes():
    connection = create_db_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM cartao")
            cartoes = cursor.fetchall()
            return cartoes
        except Exception as e:
            print(f"Erro ao verificar cartões: {e}")
            return []
        finally:
            cursor.close()
            close_db_connection(connection)

def update_cartao(cartao_id, new_numero, new_tipo, new_validade, new_id_cliente):
    connection = create_db_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT id_cliente FROM cliente WHERE id_cliente = %s", (new_id_cliente,))
            if not cursor.fetchone():
                print(f"Error: Cliente com ID {new_id_cliente} não existe.")
                return False

            cursor.execute("UPDATE cartao SET numero = %s, tipo = %s, validade = %s, id_cliente = %s WHERE id_cartao = %s",
                           (new_numero, new_tipo, new_validade, new_id_cliente, cartao_id))
            connection.commit()
            if cursor.rowcount > 0:
                print("Cartão atualizado com sucesso.")
                return True
            else:
                print("Cartão não encontrado ou nenhuma alteração feita.")
                return False
        except Exception as e:
            print(f"Erro ao atualizar o cartão: {e}")
            connection.rollback()
            return False
        finally:
            cursor.close()
            close_db_connection(connection)

def delete_cartao(cartao_id):
    connection = create_db_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM cartao WHERE id_cartao = %s", (cartao_id,))
            connection.commit()
            if cursor.rowcount > 0:
                print("Cartão deletado com sucesso.")
            else:
                print("Cartão não encontrado.")
        except Exception as e:
            print(f"Erro ao deletar o cartão: {e}")
            connection.rollback()
        finally:
            cursor.close()
            close_db_connection(connection)

# --- Transferencia CRUD Operations ---

def create_transferencia(transferencia_id, valor, data, id_cliente_origem, id_cliente_destino):
    connection = create_db_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT id_cliente FROM cliente WHERE id_cliente = %s", (id_cliente_origem,))
            if not cursor.fetchone():
                print(f"Error: Remetente com o ID {id_cliente_origem} não existe.")
                return False

            cursor.execute("SELECT id_cliente FROM cliente WHERE id_cliente = %s", (id_cliente_destino,))
            if not cursor.fetchone():
                print(f"Error: Destinatário com o ID {id_cliente_destino} não existe.")
                return False

            cursor.execute("INSERT INTO transferencia (id_transferencia, valor, data, id_cliente_origem, id_cliente_destino) VALUES (%s, %s, %s, %s, %s)",
                           (transferencia_id, valor, data, id_cliente_origem, id_cliente_destino))
            connection.commit()
            print("Transferência feita com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao fazer a transferência: {e}")
            connection.rollback()
            return False
        finally:
            cursor.close()
            close_db_connection(connection)

def get_transferencia(transferencia_id):
    connection = create_db_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM transferencia WHERE id_transferencia = %s", (transferencia_id,))
            transferencia = cursor.fetchone()
            return transferencia
        except Exception as e:
            print(f"Erro ao procurar transferência: {e}")
            return None
        finally:
            cursor.close()
            close_db_connection(connection)

def get_all_transferencias():
    connection = create_db_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM transferencia")
            transferencias = cursor.fetchall()
            return transferencias
        except Exception as e:
            print(f"Erro verificando transferências: {e}")
            return []
        finally:
            cursor.close()
            close_db_connection(connection)

def update_transferencia(transferencia_id, new_valor, new_data, new_id_cliente_origem, new_id_cliente_destino):
    connection = create_db_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT id_cliente FROM cliente WHERE id_cliente = %s", (new_id_cliente_origem,))
            if not cursor.fetchone():
                print(f"Error: Novo remetente com o ID {new_id_cliente_origem} não existe.")
                return False

            cursor.execute("SELECT id_cliente FROM cliente WHERE id_cliente = %s", (new_id_cliente_destino,))
            if not cursor.fetchone():
                print(f"Error: Novo destinatário com o ID {new_id_cliente_destino} não existe.")
                return False

            cursor.execute("UPDATE transferencia SET valor = %s, data = %s, id_cliente_origem = %s, id_cliente_destino = %s WHERE id_transferencia = %s",
                           (new_valor, new_data, new_id_cliente_origem, new_id_cliente_destino, transferencia_id))
            connection.commit()
            if cursor.rowcount > 0:
                print("Transferência atualizada com sucesso.")
                return True
            else:
                print("Transferência não encontrada ou nenhuma alteração feita.")
                return False
        except Exception as e:
            print(f"Erro ao atualizar a Transferência: {e}")
            connection.rollback()
            return False
        finally:
            cursor.close()
            close_db_connection(connection)

def delete_transferencia(transferencia_id):
    connection = create_db_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM transferencia WHERE id_transferencia = %s", (transferencia_id,))
            connection.commit()
            if cursor.rowcount > 0:
                print("Transferência deletada com sucesso.")
            else:
                print("Transferência não encontrada.")
        except Exception as e:
            print(f"Erro ao deletar transferência: {e}")
            connection.rollback()
        finally:
            cursor.close()
            close_db_connection(connection)