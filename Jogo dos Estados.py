# Crie um "jogo dos estados". Neste jogo, o jogador precisa responder
# o nome da capital de cada Estado do Brasil. O jogo deve perguntar
# ao usuário "Qual a capital do Estado X?", e checar se o usuário
# respondeu de forma correta. Após cada pergunta, o usuário pode escolher
# parar o jogo ou continuar para a próxima pergunta. Quando o usuário
# decidir parar, ou quando todas as perguntas forem respondidas,
# o código mostra o número bruto e porcentagem de acertos.

# Dicionário com os estados e suas respectivas capitais
estados_capitais = {
    'Acre': 'Rio Branco',
    'Alagoas': 'Maceió',
    'Amapá': 'Macapá',
    'Amazonas': 'Manaus',
    'Bahia': 'Salvador',
    'Ceará': 'Fortaleza',
    'Distrito Federal': 'Brasília',
    'Espírito Santo': 'Vitória',
    'Goiás': 'Goiânia',
    'Maranhão': 'São Luís',
    'Mato Grosso': 'Cuiabá',
    'Mato Grosso do Sul': 'Campo Grande',
    'Minas Gerais': 'Belo Horizonte',
    'Pará': 'Belém',
    'Paraíba': 'João Pessoa',
    'Paraná': 'Curitiba',
    'Pernambuco': 'Recife',
    'Piauí': 'Teresina',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Rio Grande do Norte': 'Natal',
    'Rio Grande do Sul': 'Porto Alegre',
    'Rondônia': 'Porto Velho',
    'Roraima': 'Boa Vista',
    'Santa Catarina': 'Florianópolis',
    'São Paulo': 'São Paulo',
    'Sergipe': 'Aracaju',
    'Tocantins': 'Palmas'
}

def jogo_dos_estados():
    acertos = 0
    total_perguntas = len(estados_capitais)

    for estado, capital in estados_capitais.items():
        resposta = input(f"Qual a capital do Estado {estado}? ").strip().capitalize()

        if resposta == capital:
            print("Resposta correta!\n")
            acertos += 1
        else:
            print(f"Resposta incorreta. A capital do Estado {estado} é {capital}.\n")

        continuar = input("Deseja continuar jogando? (Digite 's' para sim ou qualquer outra coisa para não): ")
        if continuar.lower() != 's':
            break

    porcentagem_acertos = (acertos / total_perguntas) * 100

    print(f"\nNúmero bruto de acertos: {acertos}/{total_perguntas}")
    print(f"Porcentagem de acertos: {porcentagem_acertos:.2f}%")

# Executando o jogo
print("Bem-vindo ao Jogo dos Estados! Responda qual é a capital de cada Estado do Brasil.")
jogo_dos_estados()# Dicionário com os estados e suas respectivas capitais
estados_capitais = {
    'Acre': 'Rio Branco',
    'Alagoas': 'Maceió',
    'Amapá': 'Macapá',
    'Amazonas': 'Manaus',
    'Bahia': 'Salvador',
    'Ceará': 'Fortaleza',
    'Distrito Federal': 'Brasília',
    'Espírito Santo': 'Vitória',
    'Goiás': 'Goiânia',
    'Maranhão': 'São Luís',
    'Mato Grosso': 'Cuiabá',
    'Mato Grosso do Sul': 'Campo Grande',
    'Minas Gerais': 'Belo Horizonte',
    'Pará': 'Belém',
    'Paraíba': 'João Pessoa',
    'Paraná': 'Curitiba',
    'Pernambuco': 'Recife',
    'Piauí': 'Teresina',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Rio Grande do Norte': 'Natal',
    'Rio Grande do Sul': 'Porto Alegre',
    'Rondônia': 'Porto Velho',
    'Roraima': 'Boa Vista',
    'Santa Catarina': 'Florianópolis',
    'São Paulo': 'São Paulo',
    'Sergipe': 'Aracaju',
    'Tocantins': 'Palmas'
}

def jogo_dos_estados():
    acertos = 0
    total_perguntas = len(estados_capitais)

    for estado, capital in estados_capitais.items():
        resposta = input(f"Qual a capital do Estado {estado}? ").strip().capitalize()

        if resposta == capital:
            print("Resposta correta!\n")
            acertos += 1
        else:
            print(f"Resposta incorreta. A capital do Estado {estado} é {capital}.\n")

        continuar = input("Deseja continuar jogando? (Digite 's' para sim ou qualquer outra coisa para não): ")
        if continuar.lower() != 's':
            break

    porcentagem_acertos = (acertos / total_perguntas) * 100

    print(f"\nNúmero bruto de acertos: {acertos}/{total_perguntas}")
    print(f"Porcentagem de acertos: {porcentagem_acertos:.2f}%")

# Executando o jogo
print("Bem-vindo ao Jogo dos Estados! Responda qual é a capital de cada Estado do Brasil.")
jogo_dos_estados()

