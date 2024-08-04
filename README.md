# V01 - DJANGO SISTEMA DE CONTROLE DE ALUGUEIS

## Descrição
O **DJANGO SISTEMA DE ALUGUEL** é um sistema web desenvolvido com a última versão do Django e utiliza o banco de dados SQLite3. Este sistema é focado na experiência de pessoas que alugam seus imóveis, proporcionando uma plataforma completa para gerenciar múltiplos imóveis.

## Funcionalidades

### 1. Cadastro de Clientes
![image](https://github.com/user-attachments/assets/ff4f811f-3b0a-43bf-90f9-980beadefcf0)
- **Cadastro:** Permite o cadastro de novos clientes.
- **Edição:** Editar dados dos clientes cadastrados conforme necessário.
- **Remoção:** Remover clientes do sistema de forma fácil e segura.

### 2. Gestão de Imóveis (CRUD)
- **Cadastro:** Adicione novos imóveis com todos os detalhes necessários.
![image](https://github.com/user-attachments/assets/85ce5582-4a54-4c96-b7e1-a98f92cb7905)
- **Edição:** Atualize as informações dos imóveis existentes.
- **Remoção:** Remova imóveis do sistema de maneira simples.
- **Visualização:** Consulte detalhes completos dos imóveis cadastrados.
![image](https://github.com/user-attachments/assets/f663be8d-985c-4718-bd0a-1acd27fe8bd4)


### 3. Aluguel de Imóveis
Adicione aqui uma imagem ilustrativa da funcionalidade de aluguel.
- **Aluguel:** Permite alugar um imóvel para um cliente específico.
- **Visibilidade:** Imóveis alugados não ficam invisíveis na aba principal do site, facilitando a gestão dos imóveis que ainda precisam de um cliente.
![image](https://github.com/user-attachments/assets/eb450f86-6e89-4ded-93c7-ed84dea6b7a9)

### 4. Relatórios de Propriedades
Adicione aqui uma imagem ilustrativa dos relatórios.
- **Listagem Completa:** Listagem de todas as propriedades cadastradas no sistema.
- **Filtros Avançados:** Filtros para visualizar apenas imóveis alugados, disponíveis, ou ambos.
![image](https://github.com/user-attachments/assets/ed0bb3a2-a972-4127-902f-7b1b317c48ed)


### 5. Desvinculação de Cliente e Imóvel
- **Desvinculação:** Permite desvincular um cliente de um imóvel alugado, tornando o imóvel disponível novamente para novos aluguéis.

## Tecnologias Utilizadas
- Django (última versão)
- SQLite3

## Para utilização

1. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```
4. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```
