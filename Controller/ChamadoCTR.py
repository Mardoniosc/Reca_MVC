# coding: utf-8
from Model.DAO.ChamadoDAO import ChamadoDAO
from Model.DTO.ChamadoDTO import ChamadoDTO

class ChamadoCTR:

    @staticmethod
    def cadatrar_chamado(data_registro, atendente, chamado, problema,
                         status, nome_logico, vip, critico, hora_registro):
        chamadoDTO = ChamadoDTO
        chamadoDTO.Data_registro = data_registro
        chamadoDTO.Atendente = atendente
        ChamadoDTO.Chamado = chamado
        chamadoDTO.Problema = problema
        chamadoDTO.Status = status
        chamadoDTO.Nome_logico = nome_logico
        chamadoDTO.Vip = vip
        chamadoDTO.Critico = critico
        chamadoDTO.Hora_registro = hora_registro

        chamadoDAO = ChamadoDAO
        chamadoDAO.cadastrar_chamado(chamadoDTO)

    @staticmethod
    def atualizar_chamado(id, data_registro, atendente, chamado, problema, status, nome_logico, vip, critico, hora_registro):
        chamadoDTO = ChamadoDTO
        chamadoDTO.Id = id
        chamadoDTO.Data_registro = data_registro
        chamadoDTO.Atendente = atendente
        ChamadoDTO.Chamado = chamado
        chamadoDTO.Problema = problema
        chamadoDTO.Status = status
        chamadoDTO.Nome_logico = nome_logico
        chamadoDTO.Vip = vip
        chamadoDTO.Critico = critico
        chamadoDTO.Hora_registro = hora_registro

        chamadoDAO = ChamadoDAO
        chamadoDAO.atualizar_chamado(chamadoDTO)

    @staticmethod
    def consultar_todos_chamados(usuario):
        chamadoDAO = ChamadoDAO
        query = chamadoDAO.consultar_todos_chamados(usuario)
        return query

    @staticmethod
    def consulta_todos_registros_usuario(usuario):
        chamadoDAO = ChamadoDAO
        query = chamadoDAO.consulta_todos_registros_usuario(usuario)
        return query

    @staticmethod
    def consulta_wo(registro):
        chamadoDAO = ChamadoDAO
        query = chamadoDAO.consulta_wo(registro)
        return query

