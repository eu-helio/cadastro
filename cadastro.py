from PyQt5 import uic, QtWidgets


def funcao_principal():
    # Nome
    linha1 = formulario.lineEdit.text()
    # CPF
    linha2 = formulario.lineEdit_2.text()
    # RG
    linha3 = formulario.lineEdit_3.text()
    # Nascimento
    linha4 = formulario.lineEdit_4.text()
    # whatsapp
    linha5 = formulario.lineEdit_5.text()
    # telefone
    linha6 = formulario.lineEdit_6.text()
    # Rua
    linha7 = formulario.lineEdit_7.text()
    # numero
    linha8 = formulario.lineEdit_8.text()
    # referencia
    linha9 = formulario.lineEdit_9.text()
    # Plano
    linha10 = formulario.lineEdit_10.text()
    # Datainst
    linha11 = formulario.lineEdit_11.text()

#Botoes

if formulario.radioButton.isChecked() :
      print("Plano de TV Incluído")
elif formulario.radioButton_2.isChecked() :
       print("Telefone Fixo Incluido")
elif  formulario.radioButton_5.isChecked() :
      print("Vencimento todo dia 01")
elif  formulario.radioButton_5.isChecked() :
      print("Vencimento todo dia 05")
elif  formulario.radioButton_5.isChecked() :
       print("Vencimento todo dia 10")
elif  formulario.radioButton_5.isChecked() :
       print("Vencimento todo dia 15")
elif  formulario.radioButton_5.isChecked() :
       print("Vencimento todo dia 20")
elif formulario.radioButton_5.isChecked() :
       print("Vencimento todo dia 25")
elif formulario.radioButton_5.isChecked() :
       print("Vencimento todo dia 30")
     
   
   
   
   
#Saidas

    print("Nome:",linha1)
    print("CPF:",linha2)
    print("RG",linha3)
    print("Data de nascimento:",linha4)
    print("Whatsapp:",linha5)
    print("Telefone",linha6)
    print("Rua:",linha7)
    print("Numero:",linha8)
    print("Refêrencia",linha9)
    print("Plano:",linha10)
    print("Data da instalação:",linha11)
    

    

app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()
