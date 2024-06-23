# Implantação da solução
## Front-end
Link para acesso ao projeto: https://stroke-pmv-si-2024-1-pe7-t1-saude.onrender.com/
## Visão Geral
O frontend é uma interface web onde os usuários podem inserir suas informações pessoais para prever o risco de AVC. Os resultados dessas previsões e as avaliações dos modelos são mostrados na mesma página.

## Tecnologias Utilizadas
- Linguagens: HTML, CSS, JavaScript
- Frameworks/Bibliotecas: N/A (Vanilla JavaScript)

## Requisitos de Implantação
- Navegador web moderno (Google Chrome, Mozilla Firefox, Safari, etc.)
- Conexão com a internet para acessar a página web

## Como Utilizar
1. Preencher o Formulário:
   Insira as informações solicitadas no formulário, como gênero, idade, histórico de hipertensão, histórico de doença cardíaca, estado civil, tipo de trabalho, tipo de residência, nível médio de glicose, IMC e status de fumante.

2. Enviar o Formulário:
   Clique no botão "Enviar" para submeter as informações preenchidas.

3. Visualizar Resultados:
   Os resultados das previsões e avaliações dos modelos serão exibidos na página após o envio do formulário.

## Back-end

## Visão Geral
O backend é responsável por receber as solicitações de previsão, processar essas solicitações usando modelos de aprendizado de máquina treinados e retornar os resultados.

## Tecnologias Utilizadas
- Linguagem de Programação: Python 3
- Framework Web: Flask
- Bibliotecas Python: pandas, scikit-learn, imbalanced-learn, datetime, flask-cors

# Render

## 1. Visão Geral
O Render é uma plataforma que simplifica a implantação e hospedagem de aplicativos na nuvem. Ele permite que você implante e gerencie aplicativos da web, incluindo tanto o frontend quanto o backend, de maneira simples e eficiente.

O Render desempenha um papel crucial ao hospedar tanto o frontend quanto o backend do aplicativo.

## 2. Front-end - stroke-prediction-front-end
O frontend, que consiste em HTML, CSS e JavaScript, é hospedado como um aplicativo web estático no Render. Quando os usuários acessam o URL fornecido pelo Render, eles recebem diretamente os arquivos estáticos do frontend. Os dados inseridos pelos usuários no formulário de previsão de AVC são enviados para o backend por meio de chamadas de API.

## 3. Back-end - stroke-prediction-backend
O backend, escrito em Python usando o framework Flask, é hospedado como um aplicativo web no Render. Quando o frontend envia dados do formulário para o backend, ele faz uma chamada para a API fornecida pelo backend, que é hospedada no Render. O backend processa os dados recebidos, realiza a previsão do AVC com base nos modelos de aprendizado de máquina treinados e retorna os resultados para o frontend.

## 4. Comunicação entre Front-end e Back-end
A comunicação entre o frontend e o backend é realizada por meio de solicitações HTTP. Quando um usuário preenche o formulário no frontend e o envia, o frontend faz uma solicitação POST para a URL da API do backend, passando os dados do formulário como carga útil. O backend recebe essa solicitação, processa os dados e retorna os resultados para o frontend em formato JSON.

## 5. Resumo
O Render atua como o ambiente de hospedagem para o frontend e o backend do seu aplicativo, garantindo que ambos os componentes estejam disponíveis e acessíveis para os usuários finais. Ele facilita a implantação e o gerenciamento do seu aplicativo na nuvem.

# Limitações do Render

## 1. Limitações de Escalabilidade e Performance
- **Limitações de Recursos**: Pode haver restrições na quantidade de CPU, memória e armazenamento, impactando a capacidade de lidar com grandes volumes de tráfego.
- **Escalabilidade Automática**: A escalabilidade automática do Render pode não ser tão avançada ou personalizável quanto em AWS, Google Cloud ou Azure.
- **Latência**: A latência pode aumentar dependendo da localização geográfica dos servidores do Render e dos usuários, afetando a experiência do usuário.

## 2. Limitações de Configuração 
- **Opções de Configuração**: A interface simplificada do Render pode limitar opções de configuração avançada para servidores, redes ou segurança.

## 3. Limitações de Integração
- **Integração com Outros Serviços**: Pode haver desafios na integração com serviços ou APIs não nativamente suportados pelo Render.
- **Serviços Complementares**: Render pode não oferecer a mesma gama de serviços complementares que outras plataformas de nuvem, exigindo o uso de serviços externos.

## 4. Segurança e Compliance
- **Controles de Segurança**: Oferece medidas de segurança básicas, mas pode não ter os níveis avançados de controles de segurança e compliance (PCI-DSS, HIPAA) que outras plataformas oferecem.
- **Gerenciamento de Chaves e Certificados**: A gestão de certificados SSL/TLS e chaves de API pode ser mais limitada.

## 5. Suporte e Manutenção
- **Suporte Técnico**: A qualidade e disponibilidade do suporte técnico podem variar conforme o plano de assinatura. A falta de suporte imediato pode ser um problema crítico.
- **Atualizações e Manutenção**: A frequência e qualidade das atualizações podem ser desafiadoras para manter o ambiente de hospedagem atualizado com correções de segurança e melhorias de performance.

## 6. Desenvolvimento e Teste
- **Ambientes de Desenvolvimento e Teste**: Pode não oferecer a mesma flexibilidade ou número de ambientes de desenvolvimento e teste que outras plataformas, limitando a capacidade de testar mudanças extensivamente.
- **Debugging e Monitoramento**: Ferramentas de debugging e monitoramento podem ser menos avançadas, dificultando a identificação e resolução de problemas rapidamente.

## 7. Limitações de Monitoramento
- No Render, o acesso às métricas detalhadas de recursos do aplicativo, como memória e uso de CPU, está disponível apenas para instâncias pagas. Usuários no plano gratuito não têm acesso a essas métricas. Para desbloquear o monitoramento completo de desempenho e obter insights sobre o uso de recursos do aplicativo, é necessário atualizar para um plano premium. Esta atualização permite exibir métricas detalhadas diretamente na página de monitoramento do Render.


#  Monitoramento da implantação

## Plano de Monitoramento e Teste de Carga do Sistema

### Primeiros Testes Manuais

Os primeiros testes foram conduzidos manualmente em computadores e dispositivos móveis, sem ferramentas de automação, observando os seguintes pontos: 

1. Tempo de Resposta: A primeira requisição apresentou um tempo médio de resposta de 2 minutos e 49 segundos, medido em dois testes realizados ao longo de 6 horas. Em contraste, a segunda requisição, e as subsequentes, apresentaram tempos médios de 0,6 segundos. Para requisições simultâneas, o tempo médio de resposta foi de 0,7 segundos. 

2. Utilização de Recursos: Após a primeira requisição, o tempo médio de utilização de recursos foi de 0,6 segundos. 

3. Simulação de Requisições: Foram simuladas de 4 a 5 requisições simultâneas, com retorno de resultados ao mesmo tempo. Em um teste de 8 minutos, foram realizadas em média 15 requisições com intervalos de 30 segundos entre cada uma. O tempo médio de resposta após a segunda requisição foi consistentemente de 0,6 segundos. 

4. Simulação de Requisições: Foram simuladas de 4 a 5 requisições simultâneas, com retorno de resultados ao mesmo tempo. Em um teste de 8 minutos, foram realizadas em média 15 requisições com intervalos de 30 segundos entre cada uma. O tempo médio de resposta após a segunda requisição foi consistentemente de 0,6 segundos. 

5. Ambientes de Teste: Os testes foram realizados em um computador com Windows 11 (64 bits) e processador Intel Core i5-1235U (12ª geração) a 1.30 GHz, além de dispositivos Android e iPhone. 

6. Requisitos de Sistema: O sistema requer um mínimo de 512 MB de memória para operar eficazmente. 

### Testes com Apache JMeter:

- Primeira Simulação:
Configuração: 1 usuário, 1 contador de interação. 
Resultados: 
Tempo de Amostra: 1312 ms. 
Latência: 371 ms. 
Tempo de Conexão: 86 ms. 
Hora de Início: 12:04. 

- Segunda Simulação: 
Configuração: 1 usuário, 2 contadores de interação simultâneas. 
Resultados: 
Tempo de Amostra: Primeira interação: 1138 ms e segunda interação: 416 ms. 
Latência: Primeira interação: 385 ms e segunda interação: 386 ms. 
Tempo de Conexão: Primeira interação: 68 ms e segunda interação: 0 ms. 
Hora de Início: 12:12. 

- Terceira Simulação:
Configuração: 10 usuários, 1 contador de interação. 
Resultados: 
Tempo de Amostra: Primeira interação: 1027 ms e última interação: 386 ms. 
Latência: Variou de 427 ms a 255 ms. 
Tempo de Conexão: Primeira interação: 186 ms, a segunda interação: 88 ms, as interações subsequentes: variando de 22 ms a 17 ms. 
Hora de Início: entre 12:10 e 12:21. 

- Quarta Simulação: 
Configuração: 10 usuários, 2 contadores de interação (totalizando 20 requisições). 
Resultados: 
Tempo de Amostra: Variou de 1158 ms a 259 ms. 
Latência: Variou de 242 ms a 453 ms. 
Tempo de Conexão: Variou de 0 ms a 199 ms, com a 10ª amostra tendo a maior taxa (199 ms). 
Hora de Início: 12:36. 

Parâmetros dos Testes de Carga 
Requisições por Segundo: Dependendo do número de usuários e contadores de interação, variou de 1 a 20 requisições por segundo. 
Threads em Paralelo: Testes variaram de 1 a 10 threads. 
Tempo de Execução: Variou entre 8 a 15 minutos por bateria de testes. 
Baterias de Teste: Cada simulação foi executada em diferentes cenários, ajustando usuários e contadores de interação para observar o comportamento do sistema sob carga variável. 


# Apresentação da solução

Nesta seção, um vídeo de, no máximo, 5 minutos onde deverá ser descrito o escopo todo do projeto, um resumo do trabalho desenvolvido, incluindo a comprovação de que a implantação foi realizada e, as conclusões alcançadas.
[Eixo 7 - Apresentação.pdf](https://github.com/user-attachments/files/15944631/Eixo.7.-.Apresentacao.pdf)

