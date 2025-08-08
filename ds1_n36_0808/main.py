import json

ARQUIVO_CADASTROS = "cadastros.json"

def exibir_menu():
    print("\n======== MENU DO SISTEMA ========\n")
    print("1 - Cadastrar pessoa")
    print("2 - Ver cadastros")
    print("3 - Sair")
    print("===================================")

def salvar_cadastros(cadastros):
    with open (ARQUIVO_CADASTROS, "w", encoding="utf-8") as arquivo:
    json.dump(cadastros, arquivo, indent=4, ensure_ascii=False)