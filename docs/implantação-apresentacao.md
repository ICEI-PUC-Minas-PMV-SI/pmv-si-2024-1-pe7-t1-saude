# Implantação da solução
## Front-end

### Visão Geral
O frontend é uma interface web onde os usuários podem inserir suas informações pessoais para prever o risco de AVC. Os resultados dessas previsões e as avaliações dos modelos são mostrados na mesma página.

### Tecnologias Utilizadas
- Linguagens: HTML, CSS, JavaScript
- Frameworks/Bibliotecas: N/A (Vanilla JavaScript)

### Requisitos de Implantação
- Navegador web moderno (Google Chrome, Mozilla Firefox, Safari, etc.)
- Conexão com a internet para acessar a página web

### Como Utilizar
1. Preencher o Formulário:
   Insira as informações solicitadas no formulário, como gênero, idade, histórico de hipertensão, histórico de doença cardíaca, estado civil, tipo de trabalho, tipo de residência, nível médio de glicose, IMC e status de fumante.

2. Enviar o Formulário:
   Clique no botão "Enviar" para submeter as informações preenchidas.

3. Visualizar Resultados:
   Os resultados das previsões e avaliações dos modelos serão exibidos na página após o envio do formulário.

## Back-end

### Visão Geral
O backend é responsável por receber as solicitações de previsão, processar essas solicitações usando modelos de aprendizado de máquina treinados e retornar os resultados.

### Tecnologias Utilizadas
- Linguagem de Programação: Python 3
- Framework Web: Flask
- Bibliotecas Python: pandas, scikit-learn, imbalanced-learn, datetime, flask-cors

## Render

### Visão Geral
O Render é uma plataforma que simplifica a implantação e hospedagem de aplicativos na nuvem. Ele permite que você implante e gerencie aplicativos da web, incluindo tanto o frontend quanto o backend, de maneira simples e eficiente.

O Render desempenha um papel crucial ao hospedar tanto o frontend quanto o backend do aplicativo.

### Front-end - stroke-prediction-front-end
O frontend, que consiste em HTML, CSS e JavaScript, é hospedado como um aplicativo web estático no Render. Quando os usuários acessam o URL fornecido pelo Render, eles recebem diretamente os arquivos estáticos do frontend. Os dados inseridos pelos usuários no formulário de previsão de AVC são enviados para o backend por meio de chamadas de API.

### Back-end - stroke-prediction-backend
O backend, escrito em Python usando o framework Flask, é hospedado como um aplicativo web no Render. Quando o frontend envia dados do formulário para o backend, ele faz uma chamada para a API fornecida pelo backend, que é hospedada no Render. O backend processa os dados recebidos, realiza a previsão do AVC com base nos modelos de aprendizado de máquina treinados e retorna os resultados para o frontend.

### Comunicação entre Front-end e Back-end
A comunicação entre o frontend e o backend é realizada por meio de solicitações HTTP. Quando um usuário preenche o formulário no frontend e o envia, o frontend faz uma solicitação POST para a URL da API do backend, passando os dados do formulário como carga útil. O backend recebe essa solicitação, processa os dados e retorna os resultados para o frontend em formato JSON.

### Resumo
O Render atua como o ambiente de hospedagem para o frontend e o backend do seu aplicativo, garantindo que ambos os componentes estejam disponíveis e acessíveis para os usuários finais. Ele facilita a implantação e o gerenciamento do seu aplicativo na nuvem.







Nesta seção, a implantação da solução proposta em nuvem deverá ser realizada e detalhadamente descrita. Além disso, deverá ser descrito também, o planejamento da capacidade operacional através da modelagem matemática e da simulação do sistema computacional.

Após a implantação, realize testes que mostrem o correto funcionamento da aplicação.

# Apresentação da solução

Nesta seção, um vídeo de, no máximo, 5 minutos onde deverá ser descrito o escopo todo do projeto, um resumo do trabalho desenvolvido, incluindo a comprovação de que a implantação foi realizada e, as conclusões alcançadas.

