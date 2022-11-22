def toMB(tamanhoEmBytes):
   tamanhoEmBytes = float(tamanhoEmBytes)
   return (float(tamanhoEmBytes/(1024*1024)))
   
def percentualPorUsuario(lista, total):
   percentual = (lista[3]/total)*100
   percentual = "{0:.2f}".format(percentual)
   lista.insert((len(cadaUsuario)), percentual)
   
def espacoMedioOcupado(lista, total):
   media = 0
   elementos = len(lista)
   media = (total)/(elementos+1)
   media = "{0:.2f}".format(media)
   return media

#MAIN
usuarios = []
posicao = 1
total = media = 0
string = ""
with open ("usuarios.txt","r") as arquivo:
   valor = 0
   for linha in arquivo:
      usuarios.append(linha.split())
      
   for cadaUsuario in usuarios:
      cadaUsuario.insert(0,posicao)
      valor = toMB(float(cadaUsuario[2]))
      total += valor
      cadaUsuario.insert((len(cadaUsuario)),valor)
      posicao+=1
      
   for cadaUsuario in usuarios:
      percentualPorUsuario(cadaUsuario, total)
      
media = espacoMedioOcupado(cadaUsuario,total)

with open ("relatorio.txt","w") as arquivo:
   arquivo.write("ACME Inc.               Uso do espaço em disco pelos usuários.\n")
   arquivo.write("--------------------------------------------------------------\n")
   arquivo.write("Nr.\tUsuário     Espaço utilizado   % do uso \n\n")
   
   for cadaUsuario in usuarios:
      percentagem=float("{0:.2f}".format(round(cadaUsuario[3],2)))
      arquivo.write(str(cadaUsuario[0])+'\t'+"{:<10}".format(cadaUsuario[1])+'\t'+"{:<10}".format(percentagem)+'MB'+'\t'+"{:<5}".format(cadaUsuario[4])+'%'+'\n')

   arquivo.write('\n\nEspaço Total Ocupado: ' + "{0:.2f}".format(total) + ' MB')
   arquivo.write('\n\nEspaço médio Ocupado: ' + "{:<1}".format(media) + ' MB')
   arquivo.close()
   
with open ("relatorio.txt","r") as arquivo:
   print(arquivo.read())
