
endpoints = ["/login", "/produtos", "/pedidos"]

status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]

#função que verifica se um codigo http é sucesso ou não
#200 --> True
#401 --> false

def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299

#função que verifica se tem dois erros seguidos
# na lista de requisiçoes (codigo http) de um endpoint.
#[200, 200, 401, 200, 500] --> False --> requisicoes
#[201, 500, 502, 201, 500] ---> pedidos

def erros_seguidos(requisiçoes):
    for i in range (len(requisiçoes) - 1):
        codigo_atual = requisiçoes [i]
        prox_codigo = requisiçoes [i + 1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True
    return False
#[200, 200, 401, 200, 500]
#[201, 500, 502, 201, 500]

def analisar_endpoint (requisiçoes):
    qtd_sucessos = 0
    for codigo in requisiçoes:
        if eh_sucesso(codigo):
            qtd_sucessos += 1

    qtd_total_req = len(requisiçoes)
    qtd_erros = qtd_total_req = qtd_sucessos
    percentual_sucesso = (qtd_sucessos / qtd_total_req) * 100

    tem_erros_seguidoss = erros_seguidos(requisiçoes)

    if tem_erros_seguidoss:
        classificacao = 'critico'

    elif percentual_sucesso > 80:
        classificacao = 'estavel'

    else:
        classificacao = 'instavel'

    return (qtd_sucessos, qtd_erros, percentual_sucesso, classificacao)

#percorrendo toda a matriz
qtd_maior_erro = -1
endpoint_maior_erro = ""

for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    requisicoes_endpoint = status[i]

    sucesso, erros, percentual, classsificaçao = analisar_endpoint(requisicoes_endpoint)


    print(f"Endpoint: {nome_endpoint}")
    print(f"Requisicoes: {requisicoes_endpoint}")
    print(f"Sucessos: {sucesso}")
    print(f"Erros: {erros}")
    print(f"% de sucesso: {percentual}")
    print(f"classificacao: {classsificaçao}")
    print("-" * 38)
    print()
    if erros > qtd_maior_erro:
        qtd_maior_erro = erros
        endpoint_maior_erro = nome_endpoint

    print(f"Endpoint + erros: {endpoint_maior_erro} ({qtd_maior_erro}) ")

