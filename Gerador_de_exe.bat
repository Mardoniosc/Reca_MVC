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
 echo      같같같같같같같같같같같같같같같같같같같같같같같같같같같같같같같같같�
 echo      같                                                               같
 echo      같 �袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴敲 같
 echo      같 �        SCRIPT TRANSFORMAR AQUIVOS PY EM EXE               � 같
 echo      같 훤袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴� 같
 echo      같                                                               같
 echo      같                                                               같
 echo      같                                              BY: MARDONIO     같
 echo      같같같같같같같같같같같같같같같같같같같같같같같같같같같같같같같같같�
 echo.



set arquivopy=
set /p arquivopy=COLOQUE O NOME DO ARQUIVO main.py: 
set icone=
set /p icone=DIGITE O NOME DO ICONE.ICO COM EXTENSA랳: 

pyinstaller -w --icon=%arquivoui% %arquivopy%
echo.
echo.
echo.
echo.
echo.
echo.Arquivo em lote executado com sucesso!

@PAUSE