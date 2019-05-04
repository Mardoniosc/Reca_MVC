#pyinstaller --onefile --windowed --icon=PadraoCaixa_icone.ico Interface_grafica.py

#pyuic5 -x tela_principal.ui -o tela_principal.py

@echo oFF
Mode 78,23
color 1f
echo.
cd %CD%
net session >nul 2>&1

:TOPO
@TITLE Transforma Arquivos .Py em .exe

cls
 echo.
 echo      ฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐ
 echo      ฐฐ                                                               ฐฐ
 echo      ฐฐ ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป ฐฐ
 echo      ฐฐ บ        SCRIPT TRANSFORMAR AQUIVOS PY EM EXE               บ ฐฐ
 echo      ฐฐ ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ ฐฐ
 echo      ฐฐ                                                               ฐฐ
 echo      ฐฐ                                                               ฐฐ
 echo      ฐฐ                                              BY: MARDONIO     ฐฐ
 echo      ฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐ
 echo.



set arquivopy=
set /p arquivopy=COLOQUE O NOME DO ARQUIVO main.py: 
set icone=
set /p icone=DIGITE O NOME DO ICONE.ICO COM EXTENSAO: 

pyinstaller -w --icon=%arquivoui% %arquivopy%
echo.
echo.
echo.
echo.
echo.
echo.Arquivo em lote executado com sucesso!

@PAUSE