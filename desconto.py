nomeloja='Tairine'#variável do tipo string que contém o nome do supermercado
print('Bem Vindo a Loja da {}'.format(nomeloja))
valor=float(input('Digite o valor do produto R$:')) #variável do tipo númerico com casas decimais(float) que será preenchida com o valor determinado usuário
qtd=float(input('Digite a quantidade que deseja do produto:  ')) #variável será preenchida com o valor determinado pelo usuário
n_off= valor*qtd # esta é a variável que calcula o valor sem o desconto
print('Valor total do produto sem desconto: R$ {:.2f}'.format(n_off))
if (qtd >= 10) and (qtd <=99): # determinando condição do intervalo da quantidade que é entre 10 e 99.
  off= n_off- (n_off * 0.05) #variável abriga o cálculo do valor com desconto de 5%
  print('Valor total do produto com desconto: R$ {:.2f}  (desconto de 5%)'.format(off)) 
else: 
  if (qtd >= 100) and (qtd <= 999):  # determinando condição do intervalo da quantidade que é entre 100 e 999.
    off= n_off- (n_off * 0.10) #variável abriga o cálculo do valor com desconto de 10%
    print('Valor total do produto com desconto: R$ {:.2f}  (desconto de 10%)'.format(off))
  elif (qtd >= 1000) : # determinando condição do intervalo da quantidade que é entre 1000 para mais.
    off= n_off- (n_off * 0.15) #variável abriga o cálculo do valor com desconto de 15%
    print('Valor total do produto com desconto: R$ {:.2f}  (desconto de 15%)'.format(off)) #uso de {} para substituir variáveis, que serão inseridas pelo comando .format
print('Fim da Execução. Aguardamos seu retorno!') #mensagem de finalização do programa    