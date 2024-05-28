# Requisitor para o Auxilio desemprego:
print('\033[33m-=\033[m' * 55)
print(f'\033[31mRequisitor para o Auxilio desemprego:\n'
      f'\033[31m1\033[m - O Seguro-Desemprego pode ser solicitado mais de uma vez pelo trabalhador, \n'
      f'desde que tenha um intervalo mínimo de 16 meses entre uma solicitação e outra.\n'
      f'\033[31m2\033[m - Caso você consiga um novo trabalho após a demissão, perde automaticamente o direito ao '
      f'benefício.\n'
      f'\033[31m3\033[m - Caso tenha um CNPJ ativo durante o período de demissão, também perde o direito ao '
      f'Seguro-Desemprego,\n'
      f'já que se entende que você tem uma segunda renda para se manter.\n'
      f'\n'
      f'\033[31mRequisitos, referente ao tempo de trabalho:\n'
      f'\033[31m1ª vez:\033[m precisa de 12 meses com carteira assinada.\n'
      f'\033[31m2ª vez:\033[m precisa ter trabalhado por 9 meses nos últimos 12 meses anteriores à demissão.\n'
      f'\033[31m3ª vez:\033[m precisa ter trabalhado no mínimo 6 meses.')
print('\033[33m-=\033[m' * 55)

print('Nunca = 0\n'
      'Uma vez = 1\n'
      'Duas vez = 2\n')

# O que eu preciso - Informações fornecidas pelo usuário
qnt_solicitacao = int(input('Quantas vezes solicitou o auxilio desemprego? '))
salario1 = float(input('Qual seu ultimo salario? R$ '))
salario2 = float(input('Qual seu penultimo salario? R$ '))
salario3 = float(input('Qual seu antepenultimo salario? R$ '))
media_salario = (salario1 + salario2 + salario3) / 3
tempo_trabalho = int(input('Quantos meses Trabalhados? '))

# o que irei passar para o Usuario.
valor_parcela = 0
qnt_parcela = 0
salario_minimo = 1212

# A quantidade de parcelas varia conforme o tempo de atividade formal e a quantidade de vezes que o benefício foi
# solicitado. Veja:

# Primeira solicitação
# 12 meses de trabalho – 4 parcelas
# 24 meses de trabalho – 5 parcelas

if qnt_solicitacao == 0:
    if 12 <= tempo_trabalho < 24:
        qnt_parcela = 4
    elif tempo_trabalho >= 24:
        qnt_parcela = 5
    else:
        print(f'\033[31mNÂO\033[m tem direito ao auxilio.')
        qnt_parcela = 0
# Segunda solicitação
# 9 meses de trabalho – 3 parcelas
# 12 meses de trabalho- 4 parcelas
# 24 meses de trabalho – 5 parcelas

if qnt_solicitacao == 1:
    if 9 <= tempo_trabalho < 12:
        qnt_parcela = 3
    elif 12 <= tempo_trabalho < 24:
        qnt_parcela = 4
    elif tempo_trabalho >= 24:
        qnt_parcela = 5
    else:
        print(f'\033[31mNÂO\033[m tem direito ao auxilio.')
        qnt_parcela = 0

# Terceira solicitação
# 6 meses de trabalho – 3 parcelas
# 12 meses de trabalho – 4 parcelas
# 24 meses de trabalho – 5 parcelas

if qnt_solicitacao == 2:
    if 6 <= tempo_trabalho < 12:
        qnt_parcela = 3
    elif 12 <= tempo_trabalho < 24:
        qnt_parcela = 4
    elif tempo_trabalho >= 24:
        qnt_parcela = 5
    else:
        print(f'\033[31mNÂO\033[m tem direito ao auxilio.')
        qnt_parcela = 0

# Embora o Seguro-Desemprego considere a sua média salarial dos últimos três meses, o cálculo também envolve o
# reajuste do salário mínimo, definindo assim um percentual que não seja menor que o salário mínimo em vigor.
# Atualmente, a lei do Seguro-Desemprego determina que o valor das parcelas deve ser calculado da seguinte forma:
# Salários de até R$ 1.686,79 multiplica-se salário médio por 0,80 (80%) De R$ 1.686,80 até 2.811,60 o que exceder a
# 1.686,79 multiplica-se por 0,50(50%) e soma-se a 1.349,43 Acima de R$ 2.811,60 o valor da parcela será de 1.911,
# 84 Em 2022, o salário mínimo está fixado em R$ 1.212. Isso significa que, ao solicitar o Seguro-Desemprego,
# as parcelas não podem ser inferiores a esse valor.

if qnt_parcela != 0:
    if media_salario <= 1686.79:
        media_salario = media_salario * 0.80  # print(f'O valor da parcela será: \033[32mR${media_salario * 0.80:.2f}\033[m')
    elif 1686.80 <= media_salario <= 2811.60:
        media_salario = (media_salario - 1686.79) * 0.50 + 1349.43 # print(f'O valor da parcela será: \033[32mR${(media_salario - 1686.79) * 0.50 + 1349.43:.2f}\033[m')
    else:
        media_salario = 1911.84 # print(f'O valor da parcela será: \033[32mR$1911.84\033[m')

if qnt_parcela != 0:
    if media_salario < salario_minimo:
        print(f'Você receberá \033[32m{qnt_parcela}\033[m parcelas de \033[32mR${salario_minimo:.2f}\033[m. 1')
    else:
        print(f'Você receberá \033[32m{qnt_parcela}\033[m parcelas de \033[32mR${media_salario:.2f}\033[m. 2')

# Sendo assim, se uma pessoa recebe o salário-mínimo de R$1.212 nos três meses anteriores à demissão,
# o cálculo seria: R$1.212,00 x 80% = R$969,60. Mas, como o pagamento não pode ser inferior ao salário-mínimo,
# essa pessoa terá direito a receber parcelas de R$1.212,00 até o final do tempo previsto.
