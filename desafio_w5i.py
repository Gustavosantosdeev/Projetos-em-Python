import datetime

registros = {}

# marcando a entrada 
def entrada():
    cpf = input("Digite o CPF para entrada: ")
    hora_entrada = datetime.datetime.now()
    # verificação de existência de refgistro
    if len(cpf) == 11:
        if cpf in registros and registros[cpf]["entrada"] and not registros[cpf]["saida"]:
                print("Erro: Entrada já registrada para este CPF.")
        else:
            registros[cpf] = {"entrada": hora_entrada, "saida": None}
            print("Entrada registrada com sucesso.")
    else:
        print("CPF INVÁLIDO")
        
# marcando a saída
def saida():
    cpf = input("Digite o CPF para saída: ")
    hora_saida = datetime.datetime.now()
    # verificação para validar a saída
    if len(cpf) == 11:
        if cpf in registros and registros[cpf]["entrada"] and not registros[cpf]["saida"]:
            registros[cpf]["saida"] = hora_saida
            print("Saída registrada com sucesso.")
        elif cpf not in registros:
            print("Erro: CPF não tem entrada registrada. Primeiro o registre.")
    else:
        print("CPF INVÁLIDO")

# exibindo os resultados
def exibir():
    for cpf, dados in registros.items():
        entrada = dados["entrada"]
        saida = dados["saida"]
        # validação de exitencia de ambos ou de um ou outro
        if entrada and saida:
            duracao = saida - entrada
            print(f"CPF:{cpf}  Entrada:{entrada}  Saída:{saida}  Duração:{duracao}")
        elif entrada and saida == None:
            print("Falta registrar a saída.")
        elif entrada == None and saida:
            print("Falta registrar a entrada.")
        else:
            print("Erro: Informações incompletas para exibição.")

# loopzinho maroto
while True:
    print("\n1. Realizar entrada")
    print("2. Realizar saída")
    print("3. Ver registros")
    print("4. Sair")
    op = input("Escolha uma opção: ")

    if op == "1":
        entrada()
    elif op == "2":
        saida()
    elif op == "3":
        exibir()
    elif op == "4":
        break
    else:
        print("Por favor, selecione uma opção disponível.")