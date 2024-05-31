# A pergunta orientada a dados é diferente da questão de pesquisa?
Sim, a pergunta orientada a dados e a questão de pesquisa são diferentes, mesmo que tenha uma relação entre elas. Por um lado uma questão de pesquisa tem o intuito de introduzir os tópicos que serão abordados no estudo de pesquisa que estará sendo conduzido, colocando-a em um contexto específico que vai orientar a análise dos dados em um determinado campo e pode ser dividida em questões menores, incluindo perguntas orientadas a dados. Por outro lado, a pergunta orientada a dados é uma pergunta mais detalhada que se utiliza dos dados que já foram coletados pela pesquisa ou que se encontram disponíveis para coleta. Ela muitas vezes se baseia na questão de pesquisa e ajuda a orientar a pesquisa em andamento.

Dessa forma, conclui-se que a questão de pesquisa tem o intuito de fornecer uma visão geral do tema a ser estudado, introduzindo seus tópicos, enquanto as perguntas orientadas a dados têm a função de construir perguntas mais específicas para responder às questões de pesquisa.

# Vale a pena combinar outras bases de dados:
Não.
"É essencial considerar a combinação de diferentes conjuntos de dados que possuam informações complementares para abordar o problema identificado. Essa estratégia pode ser valiosa para aprimorar os modelos de IA na prevenção de AVC. Contudo, para esta pesquisa específica, não encontramos um conjunto de dados que atendesse às lacunas ou agregasse valor à investigação. É importante ressaltar que a combinação de perfis de pessoas distintas não é viável; o conjunto de dados deve possuir uma lógica ou conexão direta com a pesquisa em questão.

Por que algumas pesquisas utilizam mais de um conjunto de dados?

Vantagens:

Ampliação da Variedade de Dados, Melhor Compreensão dos Padrões, Maior Precisão do Modelo, Personalização das Intervenções, Adaptabilidade

Pode-se optar por remover atributos com dados faltantes ou inferir dados a partir de informações conhecidas. Por exemplo, se o conjunto de dados selecionado incluir o IMC, mas não o peso de cada indivíduo, um novo conjunto de dados poderia tratar esses valores especiais, substituindo os valores omitidos por outros ou atribuindo um valor como -1. Isso pode resultar em novas regras de aprendizado de máquina.

A normalização de dados numéricos é outra etapa importante, visando a colocar esses dados em faixas semelhantes. Técnicas como Minmax e Z-score podem ser empregadas para esse fim.

A seleção de dados pode envolver a redução da ênfase em certos atributos e a agregação como forma de redução da dimensionalidade, combinando dois ou mais atributos em um único atributo.

Em suma, a combinação de diferentes conjuntos de dados pode ser vantajosa para algumas pesquisas, pois amplia a variedade de dados, melhora a compreensão de padrões, aumenta a precisão do modelo, permite a personalização das intervenções e a adaptação ao contexto. No entanto, é fundamental garantir a privacidade e segurança dos dados, além de seguir as melhores práticas éticas e regulatórias. Para a pesquisa em questão, não encontramos um conjunto de dados que relacione as informações de forma a agregar valor ao trabalho realizado. A menos que seja intenção da pesquisa, por exemplo, relacionar a média de pesquisas realizadas em determinadas regiões (urbanas ou rurais) com o risco de AVC, não é o objetivo do grupo ou da pesquisa referente a este trabalho."


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

hypertension: 0 se o paciente não tiver hipertensão, 1 se tiver - Quantitativo binário;

heart_disease: 0 se o paciente não tiver doença cardíaca, 1 se tiver - Quantitativo binário;

ever_married: "Sim" ou "Não" - Qualitativo binominal simétrico ;

work_type: "Criança", "Esfera pública", "Nunca trabalhou", "Esfera privada" or "Conta própria" - Qualitativo polinominal não ordinal;

Residence_type: "Rural" ou "Urbano" - Quantitativo binário;

avg_glucose_level: Nível médio de glicose no sangue - Quantitativo contínuo não normalizado;

bmi: Indice de massa corporal - Quantitativo contínuo não normalizado;

smoking_status: "fumou previamente", "nunca fumou", "fuma" ou "desconhecido" - Qualitativo polinominal simétrico 

stroke: 0 se o paciente não tiver tido um derrame, 1 se tiver - Quantitativo binário;



# Preparação dos dados

**1 - Tratamento de Valores Ausentes (Missing Values):**

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


**2 - Transformação de Dados:**

IMC (Índice de Massa Corporal): normalizar os valores de IMC para uma escala específica, como a faixa de 0 a 1, para torná-los comparáveis entre si. Isso pode ser feito usando técnicas de normalização, como a fórmula Min-Max.
Nível Médio de Glicose: da mesma forma que o IMC, normalizar os valores do nível médio de glicose para uma escala específica, como a faixa de 0 a 1, para torná-los comparáveis entre si.

Codificação de Variáveis Categóricas:
Tabagismo: converter as categorias de histórico de tabagismo em variáveis numéricas usando a técnica de one-hot encoding. Cada categoria (nunca fumou, fumou anteriormente, fuma, desconhecida) se tornará uma nova coluna binária.
Vínculo Empregatício: da mesma forma, converter as categorias de vínculo empregatício em variáveis numéricas usando one-hot encoding. Cada categoria (filho, trabalho público, nunca trabalhou, empresa privada, autônomo) se tornará uma nova coluna binária.
Estado Civil: converter as categorias de estado civil em variáveis numéricas usando one-hot encoding. Neste caso, temos apenas duas categorias (casado, não casado), então apenas uma nova coluna binária será criada.
Gênero: converter as categorias de sexo em variáveis numéricas usando one-hot encoding. Neste caso, temos três categorias (feminino, masculino, outros), então duas novas colunas binárias serão criadas.
Resumindo:
Normalizar os valores de IMC e nível médio de glicose para uma escala específica para torná-los comparáveis.
Codificar variáveis categóricas (tabagismo, vínculo empregatício, estado civil e sexo) usando one-hot encoding para que elas possam ser utilizadas em modelos de machine learning.


**3 - Feature Engineering:**

A idade é um atributo significativamente associado ao risco de AVC. Podemos criar faixas etárias (por exemplo, 0-18 anos, 18-35 anos, 35-55 anos, 55+ anos) como novos atributos para capturar diferentes grupos etários e seu impacto no risco de AVC. Uma possível engenharia de características seria calcular a duração do tabagismo para os ex-fumantes ou a quantidade média de cigarros fumados por dia para os fumantes, como medidas mais detalhadas do histórico de tabagismo.
Seleção de características relevantes: os atributos relacionados à saúde da pessoa, como nível médio de glicose, hipertensão e histórico de doenças cardíacas, mostraram uma correlação mais forte com o risco de AVC. Portanto, podemos priorizar esses atributos durante a modelagem.
Também podemos considerar a idade como uma característica principal devido à sua forte correlação com o AVC, conforme indicado pela análise.
Descarte de características menos importantes:nem todas as características podem ser igualmente relevantes para prever o AVC. Por exemplo, o atributo "tipo de residência" não parece ter correlação com o risco de AVC com base no mapa de calor. Portanto, pode-se optar por descartá-lo durante a modelagem para simplificar o modelo e reduzir o ruído.
Tratamento de valores ausentes: para lidar com os valores nulos no atributo IMC, poderíamos preenchê-los com a média ou mediana do IMC da amostra, garantindo que não introduzimos viés significativo nos dados.
Transformação de dados: poderíamos transformar variáveis categóricas, como histórico de tabagismo e estado civil, em variáveis binárias (por exemplo, nunca fumou = 0, fuma = 1) para facilitar a modelagem.


**4 - Tratamento de dados desbalanceados:**

Para lidar com dados desbalanceados, como no caso do atributo binário "stroke", onde a maioria dos pacientes não teve AVC (95,1%), enquanto apenas uma minoria teve (4,9%), algumas técnicas podem ser consideradas:

Oversampling: consiste em aumentar a representação da classe minoritária, neste caso, os casos de AVC, gerando novas amostras sintéticas a partir dos dados existentes. Isso pode ser feito utilizando técnicas como SMOTE (Synthetic Minority Over-sampling Technique) para gerar exemplos sintéticos da classe minoritária.
Undersampling: consiste em reduzir a representação da classe majoritária, neste caso, os casos sem AVC, selecionando aleatoriamente uma quantidade igual de amostras da classe majoritária para equilibrar as classes.
Algoritmos que lidam naturalmente com desbalanceamento: alguns algoritmos de aprendizado de máquina são menos sensíveis a desbalanceamentos de classe, como árvores de decisão, Random Forests, gradient boosting, SVM com pesos nas classes, entre outros. Esses algoritmos podem ser uma opção quando o desbalanceamento não é muito extremo.


**5 - Divisão dos dados:**

Após realizar a análise exploratória dos dados e identificar os atributos relevantes para prever o risco de AVC, o próximo passo será dividir o conjunto de dados em dois subconjuntos: um conjunto de treinamento e um conjunto de teste.
Conjunto de treinamento: este conjunto será usado para treinar o modelo de aprendizado de máquina. Ele consistirá em uma parte significativa dos dados, por exemplo, 70-80% do conjunto de dados total.
Conjunto de teste: este conjunto será usado para avaliar o desempenho do modelo treinado. Ele consistirá em uma porção menor dos dados, geralmente 20-30% do conjunto de dados total.
Importância da separação: Ao dividir os dados em conjuntos de treinamento e teste, garantimos que o modelo seja avaliado em dados que não foram vistos durante o treinamento. Isso ajuda a estimar o desempenho do modelo em dados não vistos e a identificar se o modelo está superestimando ou subestimando o desempenho.
Avaliação do modelo: Após treinar o modelo usando o conjunto de treinamento, ele será avaliado usando o conjunto de teste. Métricas de avaliação, como precisão, recall, F1-score e curva ROC, podem ser calculadas para entender o desempenho do modelo na previsão do risco de AVC com base nos atributos fornecidos.


**6 - Manuseio de Dados Temporais:**

Ordenação temporal: Não é mencionado no dataset explicitamente dados temporais, como datas ou timestamps. No entanto, alguns atributos, como idade, podem ser considerados temporalmente, pois representam a idade das pessoas no momento da análise. Portanto, ao analisar a correlação entre idade e risco de AVC, é importante considerar a ordem temporal dos dados e como ela pode influenciar as conclusões.
Técnicas de análise temporal: Embora não forneça dados explícitos de séries temporais, ele aborda a relação entre idade e outros fatores de risco para AVC ao longo do tempo. Por exemplo, menciona que o risco de AVC aumenta consideravelmente após os 55 anos. Ao analisar essa relação, seria útil aplicar técnicas de análise de séries temporais, como análise de tendências ao longo do tempo e modelagem de séries temporais, para entender melhor como o risco de AVC evolui com a idade.
Manipulação de dados temporais: Como não há dados de séries temporais explícitas nos dados, não há necessidade imediata de técnicas de manipulação de dados temporais, como interpolação de valores ausentes em séries temporais ou agregação de dados em intervalos de tempo específicos. No entanto, se os dados incluíssem informações temporais, seria importante garantir que fossem tratados corretamente para preservar a ordem temporal e evitar viés nos resultados da análise.
Visualização temporal: Ao explorar a relação entre idade e risco de AVC ao longo do tempo, a visualização desempenha um papel crucial. Gráficos de tendência, como gráficos de linha ou gráficos de dispersão com marcação temporal, podem ajudar a identificar padrões ou mudanças ao longo do tempo. 
Embora o dataset não forneça dados temporais explícitos, a análise de como variáveis como idade evoluem ao longo do tempo e sua relação com o risco de AVC destacam a importância de considerar a ordem temporal dos dados e aplicar técnicas específicas de análise temporal, mesmo em contextos onde os dados temporais não são diretamente fornecidos.


**7 - Redução de Dimensionalidade:**

Identificação da dimensionalidade: nos dados fornecidos são mencionados diversos atributos que podem ser usados para prever o risco de AVC, como idade, histórico de tabagismo, vínculo empregatício, estado civil, sexo, IMC, nível de glicose no sangue, entre outros. Cada atributo adiciona uma dimensão ao conjunto de dados.
Interpretação dos componentes principais: isso pode nos ajudar a identificar quais atributos são os mais importantes para prever o risco de AVC e quais podem ser descartados ou combinados para reduzir a dimensionalidade do conjunto de dados.
Visualização dos dados reduzidos: podemos visualizar os dados em um espaço de dimensão reduzida para entender melhor a estrutura dos dados e identificar padrões ou clusters que possam existir.
Ao aplicar técnicas de redução de dimensionalidade como PCA, podemos simplificar a análise de conjuntos de dados complexos relacionados ao risco de AVC, tornando mais fácil identificar padrões e relações entre os atributos e a ocorrência de AVC. Isso pode nos ajudar a desenvolver modelos mais eficazes para prever e prevenir o risco de AVC com base nos fatores de risco identificados.


**8 - Validação Cruzada:**

Preparação dos dados: Antes de aplicar a validação cruzada, é necessário preparar os dados, incluindo a seleção dos atributos relevantes, tratamento de valores nulos (como no caso do IMC) e codificação de variáveis categóricas, se necessário.
Seleção do modelo: Dado que estamos interessados em prever o risco de AVC com base nos fatores de risco identificados, podemos escolher um modelo de classificação adequado, como regressão logística, árvores de decisão, ou até mesmo modelos mais complexos como redes neurais.
Divisão dos dados: Os dados devem ser divididos em conjuntos de treinamento e teste. No entanto, em vez de usar apenas uma divisão fixa, aplicaremos a validação cruzada para dividir os dados em várias partes, treinar o modelo em cada parte e avaliar seu desempenho médio.
Validação cruzada k-fold: Neste caso, podemos usar a validação cruzada k-fold, onde os dados são divididos em k partes (ou "dobras"). O modelo é treinado k vezes, cada vez usando k-1 partes como conjunto de treinamento e a parte restante como conjunto de teste. Isso garante que cada observação seja usada tanto para treinamento quanto para teste, melhorando a robustez da avaliação do modelo.
Avaliação do desempenho: Após realizar a validação cruzada, podemos calcular métricas de desempenho, como precisão, recall, F1-score e área sob a curva ROC (AUC-ROC), para cada fold. Em seguida, podemos calcular a média e o desvio padrão dessas métricas para avaliar o desempenho geral do modelo.
Interpretação dos resultados: Com base nas métricas de desempenho obtidas durante a validação cruzada, podemos entender melhor como nosso modelo se sai na previsão do risco de AVC com base nos fatores de risco identificados. Isso nos permite fazer inferências mais confiáveis sobre a eficácia do modelo em generalizar para novos dados.



# Descrição dos modelos

## 1.1 Random Forest

Descrição: O Random Forest se destaca por sua capacidade de combinar diversas árvores de decisão em um único modelo robusto e preciso, como uma floresta de árvores trabalhando em conjunto. Essa abordagem oferece diversas vantagens, sendo elas:

Vantagens:
- Alta acurácia e robustez: O Random Forest geralmente atinge alta acurácia nas previsões, mesmo em cenários com outliers e ruídos nos dados. Isso se deve à combinação de múltiplas árvores, que minimiza o impacto de erros individuais e aumenta a confiabilidade do modelo.
- Baixo viés e menor suscetibilidade a sobreajuste: O algoritmo tende a ter um viés menor, o que significa que suas previsões são menos propensas a serem enviesadas em favor de um determinado grupo ou subconjunto de dados. Além disso, o Random Forest é menos suscetível a sobreajuste em comparação com outros modelos, como árvores de decisão individuais, pois a combinação de árvores evita que o modelo se adapte excessivamente aos dados de treinamento.
- Capacidade de lidar com dados de alta dimensionalidade: O Random Forest pode lidar com um grande número de atributos (variáveis) sem sofrer problemas de multicolinearidade, que podem afetar a precisão de outros modelos. Isso o torna adequado para datasets com diversas informações sobre os indivíduos.
- Interpretabilidade das variáveis: O Random Forest permite a interpretação das variáveis mais importantes para a predição através da importância das variáveis em cada árvore de decisão. Essa característica facilita a compreensão dos fatores que mais influenciam o resultado final e pode auxiliar em análises posteriores.

Limitações:
- Alto custo computacional: A construção do Random Forest pode ser computacionalmente custosa, especialmente para grandes conjuntos de dados. Isso ocorre devido à necessidade de treinar diversas árvores de decisão individualmente.
- Dificuldade na interpretação do modelo final: A interpretação do modelo final pode ser complexa devido à combinação de diversas árvores de decisão. Embora seja possível identificar as variáveis mais importantes, entender como as árvores interagem para gerar a predição final pode ser um desafio.


## 1.2 Decision Tree

Descrição: O Decision Tree se destaca por sua simplicidade e intuitividade, representando as decisões de forma hierárquica, similar a uma árvore. Essa característica oferece diversas vantagens, sendo elas:

Vantagens:
- Simplicidade e fácil interpretação: O Decision Tree é um dos modelos de aprendizado de máquina mais fáceis de entender e interpretar. As regras de decisão são representadas de forma clara e visual, permitindo que especialistas e leigos compreendam facilmente como o modelo chega a suas conclusões.
- Baixo custo computacional: O treinamento e a predição com Decision Trees são computacionalmente eficientes, mesmo para grandes conjuntos de dados. Isso os torna uma boa opção para análises preliminares e exploração rápida dos dados.
- Robustez a outliers: O Decision Tree é menos sensível a outliers (valores extremos) nos dados em comparação com outros modelos. Isso significa que o modelo é menos afetado por pontos de dados que se desviam significativamente do padrão gera

Limitações:
- Baixa acurácia em alguns casos: A acurácia do Decision Tree pode ser limitada em casos com dados complexos ou não lineares. Isso ocorre porque o algoritmo constrói um único hiperplano para separar as classes, o que pode não ser suficiente para capturar as nuances de dados mais complexos.
- Suscetível a sobreajuste: O Decision Tree pode sofrer sobreajuste se não for podado ou regularizado adequadamente. O sobreajuste ocorre quando o modelo se adapta excessivamente aos dados de treinamento, memorizando-os em vez de aprender as características gerais dos dados.
- Dificuldade em lidar com dados de alta dimensionalidade: O Decision Tree pode ter problemas de multicolinearidade em conjuntos de dados com um grande número de atributos. A multicolinearidade ocorre quando duas ou mais variáveis ​​apresentam alta correlação entre si, o que pode prejudicar a precisão do modelo.



## 1.3 Support Vector Machine (SVM)

Descrição: O SVM busca encontrar um hiperplano que maximiza a margem entre os pontos de dados de classes diferentes, representando a fronteira de decisão ideal. Essa abordagem oferece diversas vantagens:

Vantagens:
- Alta acurácia em problemas com dados lineares e não lineares: O SVM é conhecido por sua alta acurácia em diversos tipos de problemas de classificação, incluindo aqueles com dados lineares e não lineares. Essa flexibilidade o torna uma boa escolha para uma variedade de datasets.
- Robustez a outliers e ruídos nos dados: O SVM é relativamente robusto a outliers e ruídos nos dados. Isso ocorre porque o algoritmo foca na margem entre as classes, minimizando o impacto de pontos de dados isolados.
- Boa capacidade de generalização: O SVM tende a generalizar bem para novos dados não observados durante o treinamento. Isso se deve à sua capacidade de encontrar a fronteira de decisão ideal com base nas margens entre as classes.

Limitações:
- Alto custo computacional: O treinamento de um SVM pode ser computacionalmente custoso, principalmente para grandes conjuntos de dados. O processo de encontrar o hiperplano ideal com a margem máxima pode exigir mais recursos computacionais.
- Dificuldade na interpretação do modelo final: O modelo final do SVM pode ser difícil de interpretar, especialmente para humanos. Ao contrário de um Decision Tree, não há uma representação visual clara das regras de decisão utilizadas.
- Sensível à escolha da função de kernel: O SVM utiliza uma função de kernel para mapear os dados para um espaço de alta dimensão, onde a separação entre as classes pode ser mais fácil. A escolha da função de kernel pode afetar a precisão do modelo, exigindo algum conhecimento e experimentação para encontrar a opção mais adequada.


## 1.4 Logistic Regression
Descrição: A Regressão Logística é um algoritmo de classificação que estima a probabilidade de um evento ocorrer, modelando a relação entre uma variável dependente binária e uma ou mais variáveis independentes.

Vantagens:
- Simplicidade e fácil interpretação dos coeficientes do modelo.
- Baixo custo computacional, adequado para grandes conjuntos de dados.
- Bom desempenho em problemas lineares e com dados binários.

Limitações:
- Baixa acurácia em problemas não lineares.
- Sensível a outliers e multicolinearidade.
- Requer balanceamento das classes para melhor desempenho.

## 1.5 K-Nearest Neighbors (KNN)

Descrição: O KNN é um algoritmo baseado em instâncias que classifica os pontos de dados com base na proximidade dos vizinhos mais próximos.

Vantagens:
- Simplicidade e fácil implementação.
- Não requer um modelo paramétrico, adequado para dados complexos.
- Bom desempenho em problemas com distribuições de dados complexas.

Limitações:
- Alto custo computacional em grandes conjuntos de dados, especialmente durante a predição.
- Sensível a ruídos e outliers.
- Requer escolha adequada do valor de k e da métrica de distância para melhor desempenho.

## Recursos Computacionais

Testes foram realizados em um sistema computacional com as seguintes configurações de hardware:

| Componente | Especificação |
|---|---|
| Processador | Processador AMD Ryzen 5 5600X, 3.7GHz (4.6GHz Max Turbo) |
| Placa de Vídeo | Placa de Vídeo NV RTX3060TI 8GB |
| Memória RAM | Corsair VENGEANCE RGB PRO DDR4 32GB (2 x 16GB) |
| Placa Mãe | Placa Mãe Asus TUF Gaming B550M-Plus, AMD AM4, mATX, DDR4 |
| Armazenamento | SSD Kingston NV2 1TB NVMe M.2 2280 |
| Sistema Operacional | Microsoft Windows 11 Professional 64 Bits ESD |


Nesta seção, conhecendo os dados e de posse dos dados preparados, é hora de descrever os algoritmos de aprendizado de máquina selecionados para a construção dos modelos propostos. Inclua informações abrangentes sobre cada algoritmo implementado, aborde conceitos fundamentais, princípios de funcionamento, vantagens/limitações e justifique a escolha de cada um dos algoritmos. 

Explore aspectos específicos, como o ajuste dos parâmetros livres de cada algoritmo. Lembre-se de experimentar parâmetros diferentes e principalmente, de justificar as escolhas realizadas.

Como parte da comprovação de construção dos modelos, um vídeo de demonstração com todas as etapas de pré-processamento e de execução dos modelos deverá ser entregue. Este vídeo poderá ser do tipo _screencast_ e é imprescindível a narração contemplando a demonstração de todas as etapas realizadas.

# Avaliação dos modelos criados

## Métricas utilizadas

Nesta seção, as métricas utilizadas para avaliar os modelos desenvolvidos deverão ser apresentadas (p. ex.: acurácia, precisão, recall, F1-Score, MSE etc.). A escolha de cada métrica deverá ser justificada, pois esta escolha é essencial para avaliar de forma mais assertiva a qualidade do modelo construído. 

| Métrica | 
|---|
| Acurácia| 
| K-Fold Cross-Validation Mean Accuracy  | 
| Standart Deviation (Desvio Padrão) |
| Roc Auc (Receiver Operating Characteristic Area Under the Curve) |
| Precision (Precisão) |
| Recall |
| F1-Score |

![modelo e metrica 1](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/assets/81451748/c7ed54ef-a8ce-48ab-8b59-bf7741e24efd)

Acurácia (Accuracy):

A acurácia pode ser útil para avaliar a proporção de previsões corretas feitas pelo modelo de ML na classificação de indivíduos como propensos ou não a ter AVC.
Então uma alta acurácia indica que o modelo está fazendo previsões precisas,  é importante para garantir que os pacientes sejam corretamente identificados como de alto risco ou não.

K-fold cross-validation mean accuracy:

A validação cruzada k-fold, com a média da acurácia, pode fornecer uma estimativa mais robusta do desempenho do modelo em diferentes conjuntos de dados.
Dentro do contexto da prevenção de AVC, é importante que o modelo seja generalizável e capaz de fazer previsões precisas em diferentes populações. A validação cruzada k-fold ajuda a garantir que o modelo não esteja superestimando seu desempenho em um único conjunto de dados.

Desvio Padrão (Standard Deviation):

O desvio padrão das acurácias calculadas em cada iteração da validação cruzada k-fold pode indicar a variabilidade do desempenho do modelo.
Então um baixo desvio padrão sugere que o modelo é consistente em sua capacidade de fazer previsões precisas, enquanto um alto desvio padrão pode indicar inconsistências que precisam ser investigadas.

ROC AUC (Receiver Operating Characteristic Area Under the Curve):

A área sob a curva ROC é uma métrica útil para avaliar a capacidade do modelo de distinguir entre indivíduos propensos e não propensos a ter AVC.
Então um valor alto de ROC AUC indica que o modelo é capaz de fazer distinções claras entre os dois grupos, o que é crucial para identificar corretamente os indivíduos de alto risco.

Precisão (Precision) e Recall:

Precisão e recall podem ser aplicados para avaliar a precisão das previsões positivas e a capacidade do modelo de identificar corretamente os indivíduos de alto risco, respectivamente.
Uma alta precisão garante que as previsões positivas do modelo sejam confiáveis, enquanto um alto recall indica que o modelo está identificando corretamente a maioria dos casos de alto risco.
A precision penalisa quando tem falso positivo
O recall penaliza quando da falso negativo portanto lida bem com o falso negativo.

F1-Score:

O F1-Score é uma métrica útil para equilibrar precisão e recall, fornecendo uma medida única do desempenho do modelo.
Por isso em casos onde precisão e recall são igualmente importantes, o F1-Score pode ser uma métrica útil para avaliar o desempenho geral do modelo.
O F1 é a média do recall e da precisão.

Diante disso, no contexto da prevenção de AVC, todas essas métricas desempenham um papel importante na avaliação e seleção de modelos de ML, garantindo que o modelo seja preciso, robusto e capaz de identificar corretamente os indivíduos de alto risco.



## Discussão dos resultados obtidos

Nesta seção, discuta os resultados obtidos pelos modelos construídos, no contexto prático em que os dados se inserem, promovendo uma compreensão abrangente e aprofundada da qualidade de cada um deles. Lembre-se de relacionar os resultados obtidos ao problema identificado, a questão de pesquisa levantada e estabelecendo relação com os objetivos previamente propostos. 






Discussão sobre Recall:

O recall do modelo KNN foi melhor do que o do Random Forest (97%)
O recall é a proporção de verdadeiros positivos em relação ao total de exemplos que realmente pertencem à classe positiva. No contexto de prevenção de AVC, um recall mais alto para o modelo KNN sugere que ele é mais eficaz em identificar corretamente os indivíduos de alto risco de AVC.

Discussão sobre Precisão:

A precisão do Random Forest foi melhor do que a do KNN (92% e 83% respectivamente). O KNN é mto bom o recall com falso negativo e mto ruim com o falso positivo
A precisão é a proporção de verdadeiros positivos em relação ao total de exemplos previstos como positivos pelo modelo. Uma precisão mais alta para o Random Forest indica que ele faz menos previsões erradas de que um paciente terá AVC quando na verdade não terá.

Discussão sobre F1-Score:

O F1-Score do Random Forest foi o melhor entre os dois modelos (94%).

O F1-Score é a média harmônica entre precisão e recall e fornece uma medida única do desempenho do modelo. Um F1-Score mais alto para o Random Forest sugere que ele atinge um equilíbrio entre precisão e recall, sendo capaz de fazer previsões precisas e identificar corretamente os indivíduos de alto risco de AVC.

Comparação com Árvore de Decisão:

Observou-se que tanto a precisão quanto o recall da Árvore de Decisão foram quase iguais e bons (88% e 91% respectivamente )
Embora a Árvore de Decisão possa ter um desempenho semelhante em termos de precisão e recall, é importante considerar outras métricas, como F1-Score (que foi 90%), para avaliar seu desempenho geral em comparação com o Random Forest e o KNN.

Em resumo, diante do exposto, ao escolher entre o Random Forest e o KNN para prever AVC, é essencial considerar não apenas uma métrica isolada, mas uma análise abrangente das métricas de avaliação. O modelo que melhor equilibra precisão, recall e outras métricas relevantes será o mais adequado para prever eficazmente os casos de AVC. O Random Forest foi o modelo considerado mais adequado para o cenário em questão. 


Resultados da Avaliação dos Modelos de Aprendizado de Máquina para Previsão de AVC:

Após a aplicação do oversampling e a separação de 20% dos dados para teste, foram observadas diferenças significativas entre os modelos K-Nearest Neighbors (KNN) e Random Forest.
Modelo K-Nearest Neighbors (KNN)
Recall: Eficaz na minimização de falsos negativos, identificando corretamente indivíduos de risco.
Precisão: Apresentou dificuldades, resultando em muitos falsos positivos.
Acurácia: Inferior em comparação ao modelo Random Forest.
Desvio Padrão da Precisão: Baixo, indicando consistência apesar do desempenho global não ideal.
F1-Score: Baixo devido à precisão limitada.
Modelo Random Forest
Precisão e Recall: Equilibrados, evitando tanto falsos positivos quanto falsos negativos.
F1-Score: Elevado, refletindo um bom equilíbrio entre precisão e recall.
Conclusão:
O modelo KNN, apesar de bom recall, sofre com precisão, resultando em um F1-Score inferior. O modelo Random Forest apresenta um desempenho mais equilibrado e robusto, sendo mais adequado para identificar corretamente indivíduos de alto risco de AVC, minimizando erros e aumentando a confiabilidade das previsões.

# Pipeline de pesquisa e análise de dados

Em pesquisa e experimentação em sistemas de informação, um pipeline de pesquisa e análise de dados refere-se a um conjunto organizado de processos e etapas que um profissional segue para realizar a coleta, preparação, análise e interpretação de dados durante a fase de pesquisa e desenvolvimento de modelos. Esse pipeline é essencial para extrair _insights_ significativos, entender a natureza dos dados e, construir modelos de aprendizado de máquina eficazes.


1. Análise e Preparação de Dados:
Exploração dos Dados: Analisar o texto para entender a natureza dos dados e os atributos disponíveis.

Tratamento de Valores Ausentes e Outliers: Preencher os valores ausentes, como no caso do IMC, e remover outliers, como no caso da idade.

Codificação de Variáveis Categóricas: Converter variáveis categóricas em numéricas usando técnicas como one-hot encoding.

Feature Engineering: Criar novas features com base nos atributos existentes, como faixas etárias para a idade e medidas adicionais para o histórico de tabagismo.

Redução de Dimensionalidade: Identificar e reduzir a dimensionalidade dos dados, se necessário, para simplificar a modelagem.

2. Construção e Avaliação de Modelos:
Seleção de Modelos: Escolher algoritmos de aprendizado de máquina adequados, como Random Forest, Decision Tree e Support Vector Machine, com base na natureza dos dados e nos objetivos do projeto.

Treinamento de Modelos: Treinar os modelos selecionados usando o conjunto de dados preparado.

Avaliação de Desempenho: Avaliar o desempenho dos modelos usando métricas como acurácia, precisão, recall, F1-score e ROC AUC.

3. Ajuste de Parâmetros e Otimização:
Ajuste de Parâmetros: Experimentar diferentes valores de parâmetros para os modelos e selecionar aqueles que oferecem o melhor desempenho.

Validação Cruzada: Usar validação cruzada para garantir que os modelos sejam generalizáveis e não estejam superestimando o desempenho em um único conjunto de dados.

4. Avaliação Final e Discussão de Resultados:
Comparação de Modelos: Comparar os diferentes modelos em termos de métricas de desempenho para selecionar o mais adequado.

Discussão dos Resultados: Interpretar os resultados obtidos em relação ao problema identificado e aos objetivos do projeto, destacando as vantagens e limitações de cada modelo.

Revisão e Refinamento: Revisar e refinar o pipeline conforme necessário com base na discussão dos resultados e nas necessidades do projeto.

Este pipeline fornece uma estrutura abrangente para lidar com a análise de dados e a construção de modelos de aprendizado de máquina para prever o risco de AVC, garantindo uma abordagem sistemática e eficaz para o problema em questão.


      
![Sales Pipeline ](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/assets/81451748/8f2ed84e-3fd7-4722-bf79-8109cf29162d)



