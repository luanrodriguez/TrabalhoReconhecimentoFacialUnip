# Importação das bibliotecas
import os
import json
from time import sleep
import face_recognition as fr

# Inicialização de variaveis globais
name = ''
access_level = 0
allow_access = False
running_script = True
registered_people = dict()
access_level_content = {
    1: '\nBem vindo a pagina de exibicao de dados ambientais',
    2: '\nBem vindo a pagina de cadastro de dados ambientais',
    3: '\nBem vindo a pagina de atualizacao/exclusao de dados ambientais',
    4: '\nBem vindo a pagina de administrador',
}

try:
    # Leitura do arquivo JSON contendo os usuários cadastrados no sistema
    with open('registered_people.json', encoding='utf-8') as json_database:
        registered_people = json.load(json_database)
        json_database.close()

    # Requisição via console da imagem a ser analisada
    print('\nBem vindo a base de dados ambientais\nPor favor, autentique-se.')
    image_to_compare_path = input("\nDigite o caminho da imagem:\n")
    print('\nAnalisando...')

    # Carregamento e análise das características faciais da imagem requisitada
    image_to_compare = fr.load_image_file(image_to_compare_path)
    image_to_compare_face_encoding = fr.face_encodings(image_to_compare)[0]

    # Laço entre as pessoas cadastradas no sistema
    for registered_people_key in registered_people.keys():
        registered_person = registered_people[registered_people_key]

        # Carregamento e análise das características faciais da pessoa cadastrada
        registered_image = fr.load_image_file(registered_person['image_path'])
        registered_face_encoding = fr.face_encodings(registered_image)[0]

        # Comparação das características faciais da pessoa requisitada e da pessoa cadastrada
        results = fr.compare_faces([registered_face_encoding], image_to_compare_face_encoding)
        
        # Caso o resultado seja verdadeiro, permite o acesso ao sistema, reconhecendo o nome e o nível de acesso
        if results[0]:
            allow_access = True
            access_level = registered_person['access_level']
            name = registered_person['name']
            break
    
    os.system('cls')
    # Exibe sucesso em tela
    if allow_access:
        print(f'\nBem vindo, {name}!')
        print(f'Você possui nivel {access_level} de acesso')

        while(running_script):
            print('\nQual pagina deseja acessar?')
            print('\n1 - Exibicao de dados ambientais (Nível 1)')
            print('\n2 - Cadastro de dados ambientais (Nível 2)')
            print('\n3 - Atualizacao/Exclusao de dados ambientais (Nível 3)')
            print('\n4 - Administrador (Nível 4)')
            
            try:
                chosen_number = int(input('\nDigite o numero correspondente:\n'))
            except:
                print('\nDigite um numero entre 1 e 4')

            # Restringe acesso as páginas através dos níveis
            os.system('cls')
            if(chosen_number > 0 and chosen_number < 5):

                if(chosen_number <= access_level):
                    print(access_level_content[chosen_number])
                    running_script = False
                else:
                    print('\nVoce nao tem permissao para acessar essa pagina')
            else:
                print('\nDigite um numero entre 1 e 4')

    # Exibe falha em tela
    else:
        print('\nAcesso negado!')

except Exception as error:
    sleep(1)
    
    # Caso a exceção seja do tipo "index", o rosto não foi identificado
    if(type(error) == IndexError):
        print('\nNao foi possivel reconhecer um rosto na imagem')
    
    # Caso um erro desconhecido aconteça, imprime em tela
    else:
        print(f'\nHouve um erro durante a analise:')
        print(f'{error}\n')