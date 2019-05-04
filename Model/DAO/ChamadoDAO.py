import mysql.connector


class ChamadoDAO:
    global dados_de_conexao
    global con

    dados_de_conexao = mysql.connector.connect(db="sd_chamados", user="sd", passwd="sd", host="DF7562NT713")
    con = dados_de_conexao

    @staticmethod
    def cadastrar_chamado(chamado):
        cur = con.cursor()
        try:
            sql = "insert into registros  (id,data_registro,atendente,chamado,problema,estatus,nome_logico,vip,critico,hora_registro)" \
                  "VALUES (null,%d,'%s','%s','%s','%s','%s',%d,%d,'%s')" % (
                      chamado.Data_registro, chamado.Atendente, chamado.Registro, chamado.Problema, chamado.Status,
                      chamado.Nome_logico, chamado.Vip, chamado.Critico, chamado.Hora_registro)

            cur.execute(sql)
            con.commit()
            con.close()
            return "Cadastrado"
        except mysql.connector.IntegrityError:
            con.close()
            return "Repetido"

        except TypeError:
            con.close()
            return "Erro_preenchimento"

    @staticmethod
    def atualizar_chamado(chamado):
        cur = con.cursor()
        try:
            sql = (
                    "UPDATE `registros` SET `data_registro` = %d, `atendente` = '%s', `chamado` = '%s', `problema` = '%s', "
                    "`estatus` = '%s', `nome_logico` = '%s', `vip` = %d, `critico` = %d, "
                    "`hora_registro` = '%s' WHERE `registros`.`id` = %d;" % (
                    chamado.Data_registro, chamado.Atendente, chamado.Registro, chamado.Problema, chamado.Status,
                    chamado.Nome_logico, chamado.Vip, chamado.Critico, chamado.Hora_registro, chamado.Id))
            cur.execute(sql)
            con.commit()
            return "Atualizado"
        except mysql.connector.IntegrityError:
            return "Repetido"
        except TypeError:
            return "Erro_preenchimento"

    @staticmethod
    def excluir_chamado(registro):
        cur = con.cursor()
        cur.execute("DELETE FROM `registros` WHERE `registros`.`chamado` = '%s';" % registro)
        con.commit()

    @staticmethod
    def consultar_todos_chamados(usuario_):
        cur = con.cursor()
        sql = "select * from registros WHERE atendente='%s'" % usuario_
        cur.execute(sql)

        # recuperando o resultado da pesquisa
        recset = cur.fetchall()
        return recset

    @staticmethod
    def consulta_todos_registros_usuario(usuario_):

        cur = con.cursor()
        sql = "select data_registro,problema,chamado,estatus from registros WHERE atendente='%s' ORDER BY id DESC LIMIT 100" % usuario_
        cur.execute(sql)
        # recuperando o resultado da pesquisa
        recset = cur.fetchall()

        return recset

    @staticmethod
    def consulta_wo(registro):
        cur = con.cursor()
        sql = "select * from registros WHERE chamado = '%s';" % registro
        cur.execute(sql)
        recset = cur.fetchall()
        return recset
