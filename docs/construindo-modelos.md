# Pergunta orientada a dados (???)

Justificar a definição / diferença da questão de pesquisa


# Vale a pena combinar outras bases de dados:
Sim. É importante combinar outras bases de dados que tenham outras informações para resolver o problema identificado isso pode ser uma estratégia valiosa para aprimorar os modelos de IA em prevenção de AVC,

Porquê?

Para organizaçoes de outras categorias pode ser usados dados desta empresa para agregar valor a pesquisa. Por exemplo: a empresa SEST SENAT atende a um publico de trabalhadores do transporte. Esta empresa presta serviços odontológicos, nutricional, psicológico e fisioterapia. Esta empresa é nacional possui um enorme publico e um banco de dados específico de um público que trabalha no transporte. Se a empresa pretender aumentar seu atendimento na fisioterapia e nutricão, ela poderá usar os dados para que atraves do resultado faça um trabalho voltado para a prevençao do AVC, oferecendo seus serviços para aqueles que tem porcentagem alta de chances de um AVC futuro, aumentar a qualidade de vida de seus funcionários e cuidar para estes sejam alertados e cobrados por um cuidado, assim dimunuirá as doenças bem como o afastamento por AVC. 

Vantagens:
Ampliação da Variedade de Dados: 
Melhor Compreensão dos Padrões: 
Maior Precisão do Modelo: 
Personalização das Intervenções
Adaptação ao Contexto do SEST SENAT:

Pode-se remover ou nao alguns atributos com dados faltantes, pode ser uma solução mesmo que nao seja desejável. Podemos inferir dados apartir de dados conhecidos. Ex: O dataset escolhido tem o IMC , mas não tem o peso de cada individuo. Tratar os valores como especial substituindo o valor omisso em caso de nao respondidos por outros ou -1. Isso poderá trazer novas regras de aprendizagem de máquina.


Diante do exposto combinar diferentes bases de dados pode ser vantajoso para a pesquisa em prevenção de AVC, especialmente ao implementar em diferentes tipos de empresas. Isso amplia a variedade de dados, melhora a compreensão de padrões, aumenta a precisão do modelo, permite personalização das intervenções e adaptação ao contexto do SEST SENAT. No entanto, é crucial garantir a privacidade e segurança dos dados, além de seguir as melhores práticas éticas e regulatórias.


# Tipos de dados do _dataset_

Qual o tipo de cada um dos atributos?

id: Identificador único - Quantitativo discreto não normalizado;

gender: "Masculino", "Feminino" ou "Outro" - Qualitativo polinominal não ordinal;

age: Idade do paciente - Quantitativo discreto não normalizado;

hypertension: 0 se o paciente não tiver hipertensão, 1 se tiver - Qualitativo binominal assimétrico / Quantitativo binário;

heart_disease: 0 se o paciente não tiver doença cardíaca, 1 se tiver - Qualitativo binominal assimétrico / Quantitativo binário;

ever_married: "Sim" ou "Não" - Qualitativo binominal simétrico ;

work_type: "Criança", "Esfera pública", "Nunca trabalhou", "Esfera privada" or "Conta própria" - Qualitativo polinominal não ordinal;

Residence_type: "Rural" ou "Urbano" - Qualitativo binominal simétrico / Quantitativo binário;

avg_glucose_level: Nível médio de glicose no sangue - Quantitativo contínuo não normalizado;

bmi: Indice de massa corporal - Quantitativo contínuo não normalizado;

smoking_status: "fumou previamente", "nunca fumou", "fuma" ou "desconhecido" - Qualitativo binominal simétrico / Quantitativo binário;

stroke: 0 se o paciente não tiver tido um derrame, 1 se tiver - Qualitativo binominal assimétrico / Quantitativo binário;




## <b>Estatísticas descritivas no dataset:</b>

Tipo de dado: Categórico ou numérico.

Número de valores únicos: Para variáveis categóricas.

Média, mediana, moda, mínimo e máximo: Para variáveis numéricas.

Distribuição de frequência: Para variáveis categóricas e numéricas.


# Preparação dos dados

Nesta etapa, deverão ser descritas todas as técnicas utilizadas para pré-processamento/tratamento dos dados.

Algumas das etapas podem estar relacionadas à:

* Limpeza de Dados: trate valores ausentes: decida como lidar com dados faltantes, seja removendo linhas, preenchendo com médias, medianas ou usando métodos mais avançados; remova _outliers_: identifique e trate valores que se desviam significativamente da maioria dos dados.

* Transformação de Dados: normalize/padronize: torne os dados comparáveis, normalizando ou padronizando os valores para uma escala específica; codifique variáveis categóricas: converta variáveis categóricas em uma forma numérica, usando técnicas como _one-hot encoding_.

* _Feature Engineering_: crie novos atributos que possam ser mais informativos para o modelo; selecione características relevantes e descarte as menos importantes.

* Tratamento de dados desbalanceados: se as classes de interesse forem desbalanceadas, considere técnicas como _oversampling_, _undersampling_ ou o uso de algoritmos que lidam naturalmente com desbalanceamento.

* Separação de dados: divida os dados em conjuntos de treinamento, validação e teste para avaliar o desempenho do modelo de maneira adequada.
  
* Manuseio de Dados Temporais: se lidar com dados temporais, considere a ordenação adequada e técnicas específicas para esse tipo de dado.
  
* Redução de Dimensionalidade: aplique técnicas como PCA (Análise de Componentes Principais) se a dimensionalidade dos dados for muito alta.

* Validação Cruzada: utilize validação cruzada para avaliar o desempenho do modelo de forma mais robusta.

* Monitoramento Contínuo: atualize e adapte o pré-processamento conforme necessário ao longo do tempo, especialmente se os dados ou as condições do problema mudarem.

* Entre outras....

Avalie quais etapas são importantes para o contexto dos dados que você está trabalhando, pois a qualidade dos dados e a eficácia do pré-processamento desempenham um papel fundamental no sucesso de modelo(s) de aprendizado de máquina. É importante entender o contexto do problema e ajustar as etapas de preparação de dados de acordo com as necessidades específicas de cada projeto.

# Descrição dos modelos

Nesta seção, conhecendo os dados e de posse dos dados preparados, é hora de descrever os algoritmos de aprendizado de máquina selecionados para a construção dos modelos propostos. Inclua informações abrangentes sobre cada algoritmo implementado, aborde conceitos fundamentais, princípios de funcionamento, vantagens/limitações e justifique a escolha de cada um dos algoritmos. 

Explore aspectos específicos, como o ajuste dos parâmetros livres de cada algoritmo. Lembre-se de experimentar parâmetros diferentes e principalmente, de justificar as escolhas realizadas.

Como parte da comprovação de construção dos modelos, um vídeo de demonstração com todas as etapas de pré-processamento e de execução dos modelos deverá ser entregue. Este vídeo poderá ser do tipo _screencast_ e é imprescindível a narração contemplando a demonstração de todas as etapas realizadas.

# Avaliação dos modelos criados

## Métricas utilizadas

Nesta seção, as métricas utilizadas para avaliar os modelos desenvolvidos deverão ser apresentadas (p. ex.: acurácia, precisão, recall, F1-Score, MSE etc.). A escolha de cada métrica deverá ser justificada, pois esta escolha é essencial para avaliar de forma mais assertiva a qualidade do modelo construído. 

## Discussão dos resultados obtidos

Nesta seção, discuta os resultados obtidos pelos modelos construídos, no contexto prático em que os dados se inserem, promovendo uma compreensão abrangente e aprofundada da qualidade de cada um deles. Lembre-se de relacionar os resultados obtidos ao problema identificado, a questão de pesquisa levantada e estabelecendo relação com os objetivos previamente propostos. 

# Pipeline de pesquisa e análise de dados

Em pesquisa e experimentação em sistemas de informação, um pipeline de pesquisa e análise de dados refere-se a um conjunto organizado de processos e etapas que um profissional segue para realizar a coleta, preparação, análise e interpretação de dados durante a fase de pesquisa e desenvolvimento de modelos. Esse pipeline é essencial para extrair _insights_ significativos, entender a natureza dos dados e, construir modelos de aprendizado de máquina eficazes. 
