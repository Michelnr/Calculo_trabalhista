def calculo_dias_trabalho(data_admissao, data_demissao):
    dias_trabalho = 0
    if data_admissao[0] > data_demissao[0]:
        dias_trabalho = (data_demissao[0] - data_admissao[0]) + 1
    return dias_trabalho
data_admissao = str(input('Data de admissão (dd/mm/aaaa): ')).split('/')
data_demissao = str(input('Data de demissão (dd/mm/aaaa): ')).split('/')

data_admissao = int(data_admissao[0])
data_demissao = int(data_demissao[0])

#if data_admissao[0] > data_demissao[0]: # Calcula quantos dias de trabalho
    
print(data_admissao)
print(data_demissao)

print(type(data_admissao))
print(type(data_demissao))