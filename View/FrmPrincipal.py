# coding: utf-8
import sys, os
from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox,QTableWidgetItem
from PyQt5.uic import loadUi
from Controller.ChamadoCTR import ChamadoCTR
from Controller.ConformidadeCTR import ConformidadeCTR
from Controller.RecursosCTR import RecusosSistemaOperacional

matricula = os.environ['USERNAME']
usuario_logado = RecusosSistemaOperacional.pega_nome_usuario_logado(matricula)
data_hoje = RecusosSistemaOperacional.criar_mostrar_data(1)

class FrmPrincipal(QMainWindow):
    def __init__(self):
        super(FrmPrincipal, self).__init__()
        loadUi('view/UI/Reca.ui', self)

        # Códigos de botões pagina 1

        self.input_data.setText(data_hoje)
        self.carrega_dados_gridview()
        if usuario_logado == False:
            QMessageBox.information(self, "Erro", "Não foi possivel pegar o usuário logado")
        else:
            self.input_atendente.setText(usuario_logado)
        # códigos de botões pagina 2
        self.buttonEnviarEmail.clicked.connect(self.enviar_email)


    # ---------------------------------------------- funções pagina 1 ----------------------------------------------
    def carrega_dados_gridview(self):
        todos_chamados = ChamadoCTR.consulta_todos_registros_usuario(usuario_logado)
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(todos_chamados):
            self.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                if colum_number == 0:
                    data_entry = str(data)
                    ano, mes, dia = map(int, data_entry.split('-'))
                    data = "%.2d/%.2d/%d" % (dia, mes, ano)
                    self.tableWidget.setItem(row_number, colum_number, QTableWidgetItem(str(data)))
                else:
                    self.tableWidget.setItem(row_number, colum_number, QTableWidgetItem(str(data)))

    # ---------------------------------------------- funções pagina 2 ----------------------------------------------
    def enviar_email(self):
        if self.input_problema.text() == "" or \
                self.input_Matricula.text() == "" or \
                self.input_Usuario.text() == "" or \
                self.input_Chamado.text() == "" or \
                self.input_Unidade.text() == "" or \
                self.input_Servidor.text() == "" or \
                self.input_Mensagem_de_erro.toPlainText() == "":
            QMessageBox.critical(self, "Campo em Branco", "Nenhum dos campos pode ficar em branco!")
        else:
            problema = self.input_problema.text()
            matricula = self.input_Matricula.text()
            usuario = self.input_Usuario.text()
            chamado = self.input_Chamado.text()
            unidade = self.input_Unidade.text()
            servidor = self.input_Servidor.text()
            mensagem_d_erro = self.input_Mensagem_de_erro.toPlainText()

            ConformidadeCTR.enviar_email(problema, usuario, matricula, chamado, unidade, servidor, mensagem_d_erro)

            self.input_problema.setText("")
            self.input_Matricula.setText("")
            self.input_Usuario.setText("")
            self.input_Chamado.setText("")
            self.input_Unidade.setText("")
            self.input_Servidor.setText("")
            self.input_Mensagem_de_erro.setPlainText("")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = FrmPrincipal()
    widget.show()
    sys.exit(app.exec())
