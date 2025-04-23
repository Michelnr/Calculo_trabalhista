salario = 1500  # float(input('Qual seu ultimo salario?: R$'))
data_ad = str('01/01/2022')  # input('Qual a data da admição? dd/mm/aaaa '))
data_de = str('13/10/2022')  # (input('Qua a data de demissão? dd/mm/aaaa '))
ferias_vencida = str('N')  # (input('O trabalhador possui ferias vencidas? (S/N) ')).upper().strip()
aviso_previo = str('N')  # (input('Teve aviso previo? (S/N) ')).upper().strip()
dias_trab = int(data_de[0:2])
mes_trab = int(10)  # (input('Quantos meses foram trabalhados no ultimo ano? (Mês) '))

total = 0
def imposto_trabalhista(salario):
    fgts = 
    inss = 

# Salario proporcional
if dias_trab > 15:
    print(f'\nSalario proporcioal: R${salario:.2f}')
    total += salario
else:
    print(f'\nSalario proporcional: R${salario / 30 * dias_trab:.2f}')
    total += salario / 30 * dias_trab

# Salario aviso previo
if 'N' in aviso_previo:
    print(f'Aviso previo: {salario:.2f}')
    total += salario
else:
    print(f'Aviso previo: R$0.00')

# Ferias vencidas
if 'S' in ferias_vencida:
    total += salario / 3 + salario
    print(f'Ferias vencidas: {salario / 3 + salario:.2f}')

# Ferias proporcionais
if dias_trab <= 15:
    ferias_mesesAnt = salario / 12 * (mes_trab - 1) + salario / 12 / 3 * (mes_trab - 1)
    ferias_mesAtual = salario / 30  + salario / 30 / 3
    print(f'Ferias proporcional: {ferias_mesesAnt + ferias_mesAtual:.2f}')
    total += ferias_mesesAnt + ferias_mesAtual
else:
    ferias_mesesAnt = salario / 12 * mes_trab + salario / 12 / 3 * mes_trab
    print(f'Ferias proporcional: {ferias_mesesAnt:.2f}')
    total += ferias_mesesAnt

# 13° proporcional
print(f'13° Proporcional: {salario / 12 * mes_trab:.2f}')
total += salario / 12 * mes_trab

print(f'Total = {total:.2f}')
