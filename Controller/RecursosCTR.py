# coding: utf-8

import datetime, subprocess


class RecusosSistemaOperacional:
    @staticmethod
    def criar_hora_guardar():
        now = datetime.now()
        hora_agora = str(now.hour)
        minuto_agora = str(now.minute)
        segundo_agora = str(now.second)
        if len(hora_agora) == 1:
            hora_agora = "0" + hora_agora
        if len(minuto_agora) == 1:
            minuto_agora = "0" + minuto_agora
        if len(segundo_agora) == 1:
            segundo_agora = "0" + segundo_agora
        hora_atual = str(hora_agora + ":" + minuto_agora + ":" + segundo_agora)

        return hora_atual

    @staticmethod
    def criar_mostrar_data(data):
        hoje = datetime.date.today()
        dia = hoje.day
        mes = hoje.month
        ano = hoje.year
        data_mostrar = "%.2d/%.2d/%d" % (dia, mes, ano)
        data_guardar = "%d%.2d%.2d" % (ano, mes, dia)
        if data == 1:
            return data_mostrar
        else:
            return data_guardar

    @staticmethod
    def pega_nome_usuario_logado(matricula):

        comando_verifica_nome = ("net user /domain %s | FIND /I \"Nome Completo\"" % (matricula))
        try:
            nome_atendente = str(subprocess.check_output(comando_verifica_nome, shell=True))
        except:
            return False
        nome = str(nome_atendente[38:])
        nome_sobrenome = (nome.split('\\r\\n'))
        nome_sobrenome = (nome_sobrenome[0].split(' - CETEC'))
        nome_a_mostrar_guardar = (nome_sobrenome[0])
        return nome_a_mostrar_guardar