from lib.interface import*
cabeçalho("login do sistema")
#joao, 93407073003, 123, 1
listadeclientes=[]
l1=["ADMIN","RECEP","MEC"]
l2=[123456,123,456]
login=""
senha=""
r=""

while True:
  login=str(input("\033[1;92mDIGITE SEU USENAME:\033[m").strip().upper())
  senha=leiaInt("\033[1;92mDIGITE SUA SENHA:\033[m")
  if login==l1[0] and senha==l2[0] or login==l1[1] and senha==l2[1] or login==l1[2] and senha==l2[2]:
    while True:
#---------------------menu do admin---------------------------#    
      if login==l1[0] and senha==l2[0]:
        cabeçalho(f"SEJA BEM VINDO {l1[0]}")
        r=menu(["Gerenciar funcionários","Ver ordens de serviço","visualiza clientes","voltar para tela incial"])
        if r==4:
          cabeçalho("Login Do Sistema")
          break
        while True:
          if r == 1:
            cabeçalho("Gestao dos funcionarios:")
            r=menu(["cadastrar funcionário","deletar funcionário","Voltar"])
            if r==1:
              while True:
                r=1
                l1.append(str(input('digite o nome:')))
                cpf=int(input('digite o cpf do funcionario:'))
                l2.append(int(input('digite a senha:')))
                cargo=str(input('digite o cargo:'))
                print("\033[1;92mUsuario cadastrado com sucesso\033[m")
                if r==1:
                  break 
            if r == 2: 
                cabeçalho("Deletar funcionarios")
                for c,f in enumerate(l1):
                  print(f"{c + 1}\t -\t{f}\t")
                r=menu(["Digite qual funcionario deseja deletar","voltar"])
                if r==2:
                    break
            if r==3:
                  break
              
          if r==2:
            cabeçalho(" Ordens de serviços")
            r=menu(["visualizar","marca como concluida","Deletar","voltar"])
            if r==1:
              pass
            if r==2:
              pass
            
            if r==3:
              pass
            
            if r==4:
                break
          if r==3:
            cabeçalho("Lista de clientes")
            print(f"{listadeclientes}")
            r=menu(["voltar"])
            if r==1:
                break
#---------------------menu do admin---------------------------#                 
      elif login==l1[1] and senha==l2[1]:
        print(f"seja bem vinda {l1[1]} seu cargo recepcionista ")
        r=menu(["Cadastrar clientes (cadastrar)","Ver orçamentos (Transformar em ordem de serviço e deletar", "voltar para tela inicial"])
        if r==3:
          cabeçalho("Login Do Sistema")
          break
        while True:
          if r==1:
            while True:
              nome=str(input("nome do cliente"))
              cpf=int(input("cpf do cliente"))
              email=str(input("email do cliente"))
              telefone=int(input("telefone do cliente"))
              endereço=str(input("Endereço DO CLEINTE"))
              placadocarro=int(input("digite a placa do carro"))
              if r==1:
                break
          if r==2:
            pass

      elif login==l1[2] and senha==l2[2]:
        print(f"seja bem vindo {l1[2]} seu cargo mecanico ")
        r=menu(["Cadastrar orçamento (cadastrar)","Ver ordens de serviço (apenas as que possuem o cpf dele)", "voltar para tela inicial"])
        if r==3:
          break
                
          
            
             
              
            
            

            
              
























        
               
        
  else:
    print("\033[1;31mLogin ou Senha incorretos! Tente novamente.\033[m")

    
              









  