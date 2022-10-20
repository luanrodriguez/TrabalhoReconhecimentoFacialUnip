A instalação dos requisitos necessários para rodar a biblioteca face_recognition no Windows pode ser um pouco trabalhosa.

A primeira etapa é fazer download do instalador do Visual Studio, através do link: https://visualstudio.microsoft.com/pt-br/downloads/.
Após baixar, execute o instalador e aperte "next" até chegar na janela de instalação de extensões. É muito importante instalar a opção "Desenvolvimento para desktop com c++". O único motivo para baixar o Visual Studio é para conseguir instalar essa extensão. Com a extensão instalada, podemos fechar o Visual Studio

A próxima etapa é instalar o CMake pelo link: https://cmake.org/download/. Com o instalador aberto, é preciso selecionar a opção de adicionar o CMake à variável de ambiente PATH e continuar a instalação.

A próxima etapa é instalar o Python, a versão recomendada LTS. Basta ir dando "next" até encontrar a checkbox "Add to PATH", selecione a checkbox e continue a instalação.

Com o Python instalado, abra o terminal cmd ou powershell do Windows, navegue até esse projeto e digite ".\venv\Scripts\activate", esse comando vai ativar o ambiente virtual, que será usado para instalar as bibliotecas do Python localmente.

Com o ambiente ativado, digite pip install -r requirements.txt e aguarde a instalação das bibliotecas Python.

Com as bibliotecas instaladas, basta digitar python run.py para executar o projeto.

