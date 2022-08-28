# Cabeçalho
print("=" * 10, "{:^30}".format("SEJA BEM-VINDO(A)"), "=" * 10)
print("=" * 10, "{:^30}".format("PYTHON PARK RESORT"), "=" * 10)
print("=" * 10, "{:^30}".format("SISTEMA DE CADASTRO"), "=" * 10)

print("\n")

# Lista vazia
quarto = []

# Solicita que o usuário informe o número de hóspedes
num_hospedes = int(input("Informe o número de hóspedes: "))

print("\n")

for i in range(num_hospedes):
    print(" " * 10, "HÓSPEDE {:^}".format(i + 1), " " * 10)
    nome_hospede = input("Informe o nome hóspede: ").title()
    cpf_hospede = input("Informe o CPF do hóspede: ")
    cpf_hospede = "{}{}{}.{}{}{}.{}{}{}-{}{}".format(*cpf_hospede)
    dados_hospede = [nome_hospede, cpf_hospede]
    quarto.append(dados_hospede)
    print("\n")

print("=" * 8, "{:^30}".format("DADOS DO QUARTO"), "=" * 8)

for hospede in quarto:
    nome_hospede, cpf_hospede = hospede
    print("Nome: {:<10} CPF: {:>20}".format(nome_hospede, cpf_hospede))
