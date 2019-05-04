# coding: utf-8
class ConformidadeDAO:
    @staticmethod
    def enviar_email_conformidade(email):
        import win32com.client
        emails = "<p781355@mail.caixa>;<p787959@mail.caixa>;<p772920@mail.caixa>;<P787457@mail.caixa>;<p783923@mail.caixa>;<p786990@mail.caixa>;<p741597@mail.caixa>;<P787959@mail.caixa>;<p760350@mail.caixa>;<p787945@mail.caixa>;<p780942@mail.caixa>"
        emails_copias = "p667646@mail.caixa;p788641@mail.caixa"

        const = win32com.client.constants
        olMailItem = 0x0
        obj = win32com.client.Dispatch("Outlook.Application")
        newMail = obj.CreateItem(olMailItem)
        newMail.Subject = " Demanda Conformidade - " + email.Problema
        # newMail.Body = "I AM\nTHE BODY MESSAGE!"
        newMail.BodyFormat = 2  # olFormatHTML https://msdn.microsoft.com/en-us/library/office/aa219371(v=office.11).aspx
        newMail.HTMLBody = "<HTML><BODY><p style='font-family:Consolas;font-size:14'>" \
                           "À" \
                           "<br>   Equipe Conformidade   " \
                           "<br>   " \
                           "<br>     1. Conforme requisição do usuário - " + email.Usuario + "" \
                           " matrícula     " + email.Matricula + "     em chamado     " + email.Chamado + "     " \
                           "o mesmo informa que apresenta erro no SIGAT, ocorre mensagem de erro conforme descrito abaixo. " \
                           "Unidade     " + email.Unidade + " " \
                           "<br> " \
                           "<br>             1.1 Servidor:     " + email.Servidor + "" \
                           "<br>" \
                           "<br>     2. Problema/Msg de erro informado:      " + email.Mensagemdeerro + "  " \
                           "<br> " \
                           "<br>     3. Favor realizar os procedimentos necessário para regularização do mesmo.  " \
                           "<br>   " \
                           "<br>   " \
                           "<br>     4. Abaixo informações repassadas ao usuário.   " \
                           "<br>                     Informado para usuário que o setor responsável irá realizar os " \
                           "procedimentos necessários para regularização da ocorrência.   " \
                           "<br>     <br>   " \
                           "<br>     <br>   " \
                           "<br><img src='C:\\PUBMOVE\\assinatura2.png'></BODY></HTML>"

        newMail.To = emails
        newMail.CC = emails_copias
        newMail.display()
