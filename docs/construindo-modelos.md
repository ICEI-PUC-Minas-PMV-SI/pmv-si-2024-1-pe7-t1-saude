# A pergunta orientada a dados é diferente da questão de pesquisa?
Sim, a pergunta orientada a dados e a questão de pesquisa são diferentes, mesmo que tenha uma relação entre elas. Por um lado uma questão de pesquisa tem o intuito de introduzir os tópicos que serão abordados no estudo de pesquisa que estará sendo conduzido, colocando-a em um contexto específico que vai orientar a análise dos dados em um determinado campo e pode ser dividida em questões menores, incluindo perguntas orientadas a dados. Por outro lado, a pergunta orientada a dados é uma pergunta mais detalhada que se utiliza dos dados que já foram coletados pela pesquisa ou que se encontram disponíveis para coleta. Ela muitas vezes se baseia na questão de pesquisa e ajuda a orientar a pesquisa em andamento.

Dessa forma, conclui-se que a questão de pesquisa tem o intuito de fornecer uma visão geral do tema a ser estudado, introduzindo seus tópicos, enquanto as perguntas orientadas a dados têm a função de construir perguntas mais específicas para responder às questões de pesquisa.

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


# Prof. Hugo citou alguma medida de estatística descritiva que não foi abordada na Etapa 02?
Não, essas foram as estatísticas descritivas usada no dataset:

Tipo de dado: Categórico ou numérico.

Número de valores únicos: Para variáveis categóricas.

Média, mediana, moda, mínimo e máximo: Para variáveis numéricas.

Distribuição de frequência: Para variáveis categóricas e numéricas.

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



# Preparação dos dados

1.Tratamento de Valores Ausentes (Missing Values):

Para o atributo bmi: considerando que o índice de massa corporal (IMC) é uma medida importante para a saúde e que existem 201 valores ausentes, podemos preencher esses valores utilizando a média do IMC presente nos dados. Isso pode ser uma abordagem razoável, mas pode distorcer um pouco a distribuição dos dados. Uma alternativa seria imputar os valores ausentes usando métodos mais avançados, como regressão linear ou K-Nearest Neighbors (KNN), com base em outros atributos relevantes.

Remoção de Outliers para o atributo age: dado que a idade é um fator significativo na incidência de AVC e que existem outliers podem ser observados a partir da análise do dataset, uma abordagem pode ser a remoção de outliers baseada em alguma medida estatística, como o método IQR (Interquartile Range).

Correlações e Influências nos Atributos:
 - Para os atributos categóricos como smoking_status, work_type, Residence_type e ever_married:
 •	Não há valores ausentes nestes atributos. A correlação entre eles e a incidência de AVC pode ser explorada mais a fundo para determinar se eles devem ser mantidos no modelo ou se alguns deles podem ser descartados.
 - Para os atributos hypertension, heart_disease, stroke:
 •	São atributos binários e não possuem valores ausentes. Eles podem ser diretamente utilizados no modelo sem necessidade de tratamento adicional.

Resumindo:
 • Podemos preencher os valores ausentes do atributo bmi com a média dos valores existentes ou usando métodos mais avançados de imputação;
 • Remover outliers no atributo age;
 •	Explorar a correlação e influência dos atributos categóricos na incidência de AVC.
 •	Utilizar diretamente os atributos binários sem tratamento adicional.
 •	Manter o atributo avg_glucose_level para avaliação em modelos.


2.Transformação de Dados:

IMC (Índice de Massa Corporal): normalizar os valores de IMC para uma escala específica, como a faixa de 0 a 1, para torná-los comparáveis entre si. Isso pode ser feito usando técnicas de normalização, como a fórmula Min-Max.
Nível Médio de Glicose: da mesma forma que o IMC, normalizar os valores do nível médio de glicose para uma escala específica, como a faixa de 0 a 1, para torná-los comparáveis entre si.
- Codificação de Variáveis Categóricas:
Tabagismo: converter as categorias de histórico de tabagismo em variáveis numéricas usando a técnica de one-hot encoding. Cada categoria (nunca fumou, fumou anteriormente, fuma, desconhecida) se tornará uma nova coluna binária.
Vínculo Empregatício: da mesma forma, converter as categorias de vínculo empregatício em variáveis numéricas usando one-hot encoding. Cada categoria (filho, trabalho público, nunca trabalhou, empresa privada, autônomo) se tornará uma nova coluna binária.
Estado Civil: converter as categorias de estado civil em variáveis numéricas usando one-hot encoding. Neste caso, temos apenas duas categorias (casado, não casado), então apenas uma nova coluna binária será criada.
Gênero:
Converter as categorias de sexo em variáveis numéricas usando one-hot encoding. Neste caso, temos três categorias (feminino, masculino, outros), então duas novas colunas binárias serão criadas.

Resumindo:
Normalizar os valores de IMC e nível médio de glicose para uma escala específica para torná-los comparáveis.
Codificar variáveis categóricas (tabagismo, vínculo empregatício, estado civil e sexo) usando one-hot encoding para que elas possam ser utilizadas em modelos de machine learning.


3.Feature Engineering: 

A idade é um atributo significativamente associado ao risco de AVC. Podemos criar faixas etárias (por exemplo, 0-18 anos, 18-35 anos, 35-55 anos, 55+ anos) como novos atributos para capturar diferentes grupos etários e seu impacto no risco de AVC. Uma possível engenharia de características seria calcular a duração do tabagismo para os ex-fumantes ou a quantidade média de cigarros fumados por dia para os fumantes, como medidas mais detalhadas do histórico de tabagismo.
Seleção de características relevantes: os atributos relacionados à saúde da pessoa, como nível médio de glicose, hipertensão e histórico de doenças cardíacas, mostraram uma correlação mais forte com o risco de AVC. Portanto, podemos priorizar esses atributos durante a modelagem.
Também podemos considerar a idade como uma característica principal devido à sua forte correlação com o AVC, conforme indicado pela análise.
Descarte de características menos importantes:nem todas as características podem ser igualmente relevantes para prever o AVC. Por exemplo, o atributo "tipo de residência" não parece ter correlação com o risco de AVC com base no mapa de calor. Portanto, pode-se optar por descartá-lo durante a modelagem para simplificar o modelo e reduzir o ruído.
Tratamento de valores ausentes: para lidar com os valores nulos no atributo IMC, poderíamos preenchê-los com a média ou mediana do IMC da amostra, garantindo que não introduzimos viés significativo nos dados.
Transformação de dados: poderíamos transformar variáveis categóricas, como histórico de tabagismo e estado civil, em variáveis binárias (por exemplo, nunca fumou = 0, fuma = 1) para facilitar a modelagem.


4.Tratamento de dados desbalanceados:

Para lidar com dados desbalanceados, como no caso do atributo binário "stroke", onde a maioria dos pacientes não teve AVC (95,1%), enquanto apenas uma minoria teve (4,9%), algumas técnicas podem ser consideradas:

Oversampling: Consiste em aumentar a representação da classe minoritária, neste caso, os casos de AVC, gerando novas amostras sintéticas a partir dos dados existentes. Isso pode ser feito utilizando técnicas como SMOTE (Synthetic Minority Over-sampling Technique) para gerar exemplos sintéticos da classe minoritária.
Undersampling: Consiste em reduzir a representação da classe majoritária, neste caso, os casos sem AVC, selecionando aleatoriamente uma quantidade igual de amostras da classe majoritária para equilibrar as classes.
Algoritmos que lidam naturalmente com desbalanceamento: Alguns algoritmos de aprendizado de máquina são menos sensíveis a desbalanceamentos de classe, como árvores de decisão, Random Forests, gradient boosting, SVM com pesos nas classes, entre outros. Esses algoritmos podem ser uma opção quando o desbalanceamento não é muito extremo.


5.Divisão dos dados: 

Após realizar a análise exploratória dos dados e identificar os atributos relevantes para prever o risco de AVC, o próximo passo seria dividir o conjunto de dados em dois subconjuntos: um conjunto de treinamento e um conjunto de teste.
Conjunto de treinamento: este conjunto será usado para treinar o modelo de aprendizado de máquina. Ele consistirá em uma parte significativa dos dados, por exemplo, 70-80% do conjunto de dados total.
Conjunto de teste: este conjunto será usado para avaliar o desempenho do modelo treinado. Ele consistirá em uma porção menor dos dados, geralmente 20-30% do conjunto de dados total.
Importância da separação: Ao dividir os dados em conjuntos de treinamento e teste, garantimos que o modelo seja avaliado em dados que não foram vistos durante o treinamento. Isso ajuda a estimar o desempenho do modelo em dados não vistos e a identificar se o modelo está superestimando ou subestimando o desempenho.
Avaliação do modelo: Após treinar o modelo usando o conjunto de treinamento, ele será avaliado usando o conjunto de teste. Métricas de avaliação, como precisão, recall, F1-score e curva ROC, podem ser calculadas para entender o desempenho do modelo na previsão do risco de AVC com base nos atributos fornecidos.





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
