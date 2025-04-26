import os

def descriptografa_vigenere(texto, chave):
    resultado = ""
    chave_repetida = ""
    
    c = 0
    
    for i in range(len(texto)):
        if texto[i].isalpha():
            chave_repetida += chave[c % len(chave)].lower()  
            c += 1
        else:
            chave_repetida += texto[i]

    
    for i in range(len(texto)):
        char = texto[i]
        if char.isupper():
            deslocamento = ord(chave_repetida[i]) - ord('a')  
            resultado += chr((ord(char) - ord('A') - deslocamento) % 26 + ord('A'))
        elif char.islower():
            deslocamento = ord(chave_repetida[i]) - ord('a')  
            resultado += chr((ord(char) - ord('a') - deslocamento) % 26 + ord('a'))
        else:
            resultado += char  

    return resultado

def ler_arquivo(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        print(f"Erro: Arquivo {nome_arquivo} não encontrado.")
        return None

    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        print(f"Conteúdo do arquivo {nome_arquivo}:") 
        print(conteudo)  
        return conteudo

def escrever_arquivo(nome_arquivo, conteudo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo)

nome_arquivo = 'input.txt'
mensagem_criptografada = ler_arquivo(nome_arquivo)
if mensagem_criptografada:
    chave = "criptografia"  

    texto_descriptografado = descriptografa_vigenere(mensagem_criptografada, chave)
    escrever_arquivo('mensagem_descriptografada.txt', texto_descriptografado)

    print("Texto descriptografado:") 
    print(texto_descriptografado) 





