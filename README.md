Jogo de Aventura
Este é um jogo simples de aventura onde o jogador deve coletar itens, como moedas, chaves, diamantes, e interagir com portais, enquanto navega por diferentes cenários. O jogo é construído usando a biblioteca Pygame e possui recursos como gráficos, sons e diferentes cenários para cada nível.

Estrutura do Projeto
A estrutura do projeto é a seguinte:

bash
game_project/
│
├── assets/
│   ├── backgrounds/   # Cenários do jogo
│   ├── images/        # Imagens de objetos como jogador, moedas, chaves, etc.
│   └── sounds/        # Sons dos itens e eventos do jogo
│
├── player.py          # Lógica do jogador (movimento, interações)
├── inventory.py       # Lógica do inventário do jogador
├── collectibles.py     # Lógica dos itens colecionáveis
├── generate_assets.py # Geração de imagens, sons e cenários
├── settings.py        # Configurações gerais do jogo
├── main.py            # Código principal do jogo (lógica e execução)
└── README.md          # Este arquivo
Descrição dos Arquivos
assets/: Contém todos os recursos visuais e sonoros utilizados no jogo.

images/: Imagens dos itens do jogo, como o jogador, moedas, chaves, etc.
sounds/: Sons para eventos como a coleta de itens e a abertura de portais.
backgrounds/: Imagens de fundo para os diferentes cenários do jogo.
player.py: Contém a lógica do jogador, incluindo movimento, interações com o ambiente e itens, e controle de estado.

inventory.py: Responsável pelo gerenciamento do inventário do jogador, onde os itens coletados são armazenados e gerenciados.

collectibles.py: Contém a lógica para os itens colecionáveis do jogo, como moedas, chaves, diamantes e portais.

generate_assets.py: Script que gera as imagens, sons e cenários utilizados no jogo. Pode ser executado para criar os recursos na pasta assets/.

settings.py: Contém configurações gerais do jogo, como o tamanho da tela e outras opções de personalização.

main.py: Código principal que controla a execução do jogo, integra a lógica do jogador, inventário, itens e cenários, e gerencia o fluxo do jogo.

Requisitos
Para rodar este jogo, você precisa ter o Python e a biblioteca Pygame instalados em seu computador.

Instale o Python (versão 3.x).

Instale o Pygame utilizando o pip:

bash

pip install pygame
Como Rodar o Jogo
Clone ou faça o download deste repositório.

Execute o código principal game.py:

bash
python game.py


Funcionalidades
Gráficos: Imagens geradas para o jogador, itens colecionáveis, e obstáculos.
Sons: Sons gerados para eventos como coleta de moedas, chaves, diamantes, e interação com portais.
Cenários: Diferentes fundos são gerados para cada nível, criando uma atmosfera única para o jogo.
Inventário: Gerencia os itens que o jogador coleta durante o jogo.
Jogador: Controla o movimento do jogador e interações com o ambiente e os itens.
Como Gerar os Assets
Os assets do jogo (imagens, sons e cenários) são gerados automaticamente com o script. Para gerar os assets, execute o seguinte comando:

bash
python generate_assets.py
Isso criará as imagens e sons necessários na pasta assets/.
