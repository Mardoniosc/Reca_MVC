# coding: utf-8
from Model.DAO.ConformidadeDAO import ConformidadeDAO
from Model.DTO.ConformidadeDTO import ConformidadeDTO

class ConformidadeCTR:
    @staticmethod
    def enviar_email(problema, usuario, matricula, chamado, unidade,
                     servidor, mensagem_de_erro):
        conformidadeDTO = ConformidadeDTO
        conformidadeDTO.Problema = problema
        conformidadeDTO.Usuario = usuario
        conformidadeDTO.Matricula = matricula
        conformidadeDTO.Chamado = chamado
        conformidadeDTO.Unidade = unidade
        conformidadeDTO.Servidor = servidor
        conformidadeDTO.Mensagemdeerro = mensagem_de_erro

        conformidadeDAO = ConformidadeDAO
        conformidadeDAO.enviar_email_conformidade(conformidadeDTO)
