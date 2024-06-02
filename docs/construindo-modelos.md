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

**Descrição:**

O Random Forest é um algoritmo de aprendizado de máquina que faz parte da família de métodos ensemble learning. Ele funciona criando uma grande quantidade de árvores de decisão durante o treinamento e outputando a classe que é o modo das classes (classificação) ou média das predições das árvores individuais (regressão). Imagine uma floresta onde cada árvore representa um modelo de decisão individual. A combinação dessas árvores resulta em uma "floresta" que representa a sabedoria coletiva de todos os modelos individuais. Essa abordagem permite que o Random Forest supere as limitações de cada árvore individual e alcance resultados superiores.

**Funcionamento:**

1. **Seleção Aleatória de Dados:** Cada árvore no Random Forest é treinada usando uma amostra diferente dos dados de treinamento (bootstrap sampling).
2. **Seleção Aleatória de Variáveis:** Em cada nó de decisão, o algoritmo considera um subconjunto aleatório das variáveis em vez de todas as variáveis, promovendo a diversidade entre as árvores.
3. **Crescimento das Árvores:** As árvores são crescidas até a maior profundidade possível sem poda, permitindo que cada árvore se torne um modelo forte.
4. **Agregação das Previsões:** Para classificação, a classe final é determinada por votação majoritária das árvores. Para regressão, a predição final é a média das predições de todas as árvores.

**Parâmetros de Entrada Principais:**

- **n_estimators:** Número de árvores na floresta. Utilizado: 100 (default).
- **criterion:** Função de medição da qualidade de uma divisão. Utilizado: "gini" (default).
- **max_depth:** Profundidade máxima da árvore. Utilizado: None (default).
- **min_samples_split:** Número mínimo de amostras necessárias para dividir um nó. Utilizado: 2 (default).
- **min_samples_leaf:** Número mínimo de amostras necessárias para estar em um nó folha. Utilizado: 1 (default).
- **max_features:** Número de características a serem consideradas ao procurar a melhor divisão. Utilizado: "auto" (default).

**Vantagens:**

- **Alta acurácia e robustez:** O Random Forest frequentemente atinge alta precisão em suas previsões, mesmo em cenários com outliers e ruídos nos dados. A combinação de múltiplas árvores minimiza o impacto de erros individuais, tornando o modelo mais confiável.
- **Baixo viés e menor suscetibilidade a sobreajuste:** Este algoritmo tende a ter um viés reduzido, o que significa que suas previsões são menos propensas a serem enviesadas. Além disso, a combinação de várias árvores de decisão ajuda a evitar o sobreajuste, um problema comum em modelos individuais.
- **Capacidade de lidar com dados de alta dimensionalidade:** O Random Forest pode lidar com um grande número de variáveis sem sofrer problemas de multicolinearidade, que podem afetar outros modelos. Isso o torna adequado para conjuntos de dados complexos com muitas características.
- **Interpretabilidade das variáveis:** Ele permite a identificação das variáveis mais importantes para a predição, facilitando a compreensão dos fatores que mais influenciam o resultado final.

**Limitações:**

- **Alto custo computacional:** A construção de um Random Forest pode ser computacionalmente intensiva, especialmente para grandes conjuntos de dados, devido à necessidade de treinar múltiplas árvores de decisão.
- **Dificuldade na interpretação do modelo final:** Combinando diversas árvores, o modelo final pode ser complexo e difícil de interpretar, embora seja possível identificar as variáveis mais importantes.


**Matriz de confusão:**

![Random Forest](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/src/models/graficos/split_depois/sem%20normalizacao/RF_sem_normalizacao.png)

**Árovres dos estimadores:**

- Segue a árvore de 5 estimadores, truncada para profundidade 3 para facilitar a visualização:
![Random Forest](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/src/models/graficos/split_depois/sem%20normalizacao/random_forest_5_samples.png)

- A floresta com as 100 árvores criadas está disponível no arquivo de texto abaixo:
https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/src/models/floresta.txt
---

## 1.2 Decision Tree

**Descrição:**

As árvores de decisão são conhecidas por sua simplicidade e facilidade de interpretação. Elas representam decisões através de uma estrutura hierárquica semelhante a uma árvore, onde cada nó interno representa uma decisão baseada em uma variável, e cada folha representa um resultado ou valor. Essa estrutura clara e visual torna as árvores de decisão acessíveis e eficazes para diversos problemas, incluindo a predição de eventos como o AVC.

**Funcionamento:**

1. **Seleção do Melhor Ponto de Corte:** Em cada nó, o algoritmo seleciona a variável e o ponto de corte que melhor separam os dados em termos de pureza (medida pelo índice de Gini ou pela entropia).
2. **Crescimento da Árvore:** A árvore cresce repetindo o processo de divisão até que todos os nós sejam puros (ou quase puros), ou até que outras condições de parada sejam atendidas (como profundidade máxima da árvore).
3. **Predição:** Para realizar uma predição, o algoritmo segue as regras de decisão da raiz até uma folha, onde a folha representa a classe ou valor predito.

**Parâmetros de Entrada Principais:**

- **criterion:** Função de medição da qualidade de uma divisão. Utilizado: “gini” (default).
- **splitter:** Estratégia usada para escolher a divisão em cada nó. Utilizado: “best” (default).
- **max_depth:** Profundidade máxima da árvore. Utilizado: None (default).
- **min_samples_split:** Número mínimo de amostras necessárias para dividir um nó. Utilizado: 2 (default).
- **min_samples_leaf:** Número mínimo de amostras necessárias para estar em um nó folha. Utilizado: 1 (default).
- **max_features:** Número de características a serem consideradas ao procurar a melhor divisão. Utilizado: None (default).
- **random_state:** Controla a aleatoriedade do algoritmo. Utilizado: 42.

**Vantagens:**

- **Simplicidade e fácil interpretação:** Árvores de decisão são um dos modelos mais fáceis de entender e interpretar. As regras de decisão são claras e visuais, permitindo que tanto especialistas quanto leigos compreendam como o modelo chega às suas conclusões.
- **Baixo custo computacional:** O treinamento e a predição com árvores de decisão são computacionalmente eficientes, mesmo para grandes conjuntos de dados, tornando-as ideais para análises preliminares e exploração rápida dos dados.
- **Robustez a outliers:** Árvores de decisão são menos sensíveis a outliers em comparação com outros modelos, sendo menos afetadas por pontos de dados que se desviam significativamente do padrão geral.

**Limitações:**

- **Baixa acurácia em alguns casos:** A acurácia de uma árvore de decisão pode ser limitada em casos com dados complexos ou não lineares, pois ela constrói um único hiperplano para separar as classes.
- **Suscetibilidade a sobreajuste:** Árvores de decisão podem sofrer de sobreajuste se não forem podadas ou regularizadas adequadamente, adaptando-se excessivamente aos dados de treinamento em vez de aprender as características gerais.
- **Dificuldade em lidar com dados de alta dimensionalidade:** Árvores de decisão podem enfrentar problemas de multicolinearidade em conjuntos de dados com muitos atributos, onde variáveis altamente correlacionadas podem prejudicar a precisão do modelo.


**Matriz de confusão:**

![Decision Tree](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/src/models/graficos/split_depois/sem%20normalizacao/DT_sem_normalizacao.png)

**Árovres dos estimadores:**

- Segue a árvore gerada, truncada para profundidade 5 para facilitar a visualização:
![Random Forest](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/src/models/graficos/split_depois/sem%20normalizacao/decision_tree_depth4.png)

- A árvore gerada está disponível no arquivo de texto abaixo:
https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/src/models/decision_tree.txt
---
---

## 1.3 Support Vector Machine (SVM)

**Descrição:**

O Support Vector Machine (SVM) é um algoritmo de aprendizado de máquina conhecido por sua robustez e precisão na separação de classes em um dataset. Ele encontra a fronteira de decisão ideal para maximizar a margem entre as classes, tornando-o um modelo promissor para problemas como a predição de AVC. O SVM busca identificar os fatores que diferenciam pacientes com e sem AVC com alta precisão.

**Funcionamento:**

1. **Encontrar o Hiperplano de Separação:** O SVM procura o hiperplano que melhor separa as classes de dados, maximizando a margem entre os pontos de dados mais próximos de qualquer classe (os vetores de suporte).
2. **Utilização de Kernel:** Em casos de dados não linearmente separáveis, o SVM pode usar funções de kernel (como o kernel radial ou polinomial) para mapear os dados para um espaço de maior dimensão onde a separação linear é possível.
3. **Maximização da Margem:** O SVM ajusta o hiperplano de modo a maximizar a distância entre os vetores de suporte de diferentes classes, reduzindo assim o risco de erro de classificação.

**Parâmetros de Entrada Principais:**

- **C:** Parâmetro de regularização. Controla o trade-off entre a margem máxima e a classificação correta dos pontos de dados. Utilizado: 1.0 (default).
- **kernel:** Tipo de kernel a ser usado no algoritmo. Utilizado: “rbf” (default).
- **degree:** Grau do polinômio (se o kernel polinomial for escolhido). Utilizado: 3 (default).
- **gamma:** Coeficiente de kernel para os kernels “rbf”, “poly” e “sigmoid”. Utilizado: “scale” (default).
- **coef0:** Término independente no kernel polinomial e sigmoid. Utilizado: 0.0 (default).

**Vantagens:**

- **Alta acurácia em problemas com dados lineares e não lineares:** O SVM é conhecido por sua alta precisão em diversos tipos de problemas de classificação, incluindo aqueles com dados lineares e não lineares.
- **Robustez a outliers e ruídos nos dados:** O SVM é relativamente robusto a outliers e ruídos, focando na margem entre as classes e minimizando o impacto de pontos de dados isolados.
- **Boa capacidade de generalização:** O SVM tende a generalizar bem para novos dados não observados durante o treinamento, encontrando a fronteira de decisão ideal com base nas margens entre as classes.

**Limitações:**

- **Alto custo computacional:** O treinamento de um SVM pode ser computacionalmente intensivo, especialmente para grandes conjuntos de dados, devido ao processo de encontrar o hiperplano ideal com a margem máxima.
- **Dificuldade na interpretação do modelo final:** O modelo final do SVM pode ser difícil de interpretar, não oferecendo uma representação visual clara das regras de decisão utilizadas.
- **Sensível à escolha da função de kernel:** A escolha da função de kernel pode afetar a precisão do modelo, exigindo experimentação para encontrar a opção mais adequada.


**Matriz de confusão:**

![SVM](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/src/models/graficos/split_depois/sem%20normalizacao/SVM_sem_normalizacao.png)

---

## 1.4 Logistic Regression

**Descrição:**

A Regressão Logística é um algoritmo de classificação que estima a probabilidade de um evento ocorrer, modelando a relação entre uma variável dependente binária e uma ou mais variáveis independentes. Amplamente utilizada em diversas áreas, como a medicina, marketing e finanças, a regressão logística é apreciada por sua simplicidade e eficácia em problemas onde a resposta é uma variável categórica binária.

**Funcionamento:**

1. **Modelagem da Relação:** A regressão logística modela a relação entre as variáveis independentes (predictors) e a variável dependente binária (outcome) usando a função logística. A função logística, também conhecida como função sigmoide, transforma os valores resultantes em uma probabilidade que varia de 0 a 1.
2. **Cálculo das Probabilidades:** O modelo calcula a probabilidade de ocorrência de um evento (classe 1) usando a equação logit: log(p/(1-p)) = β0 + β1X1 + β2X2 + ... + βnXn, onde p é a probabilidade da classe 1, e β0, β1, ..., βn são os coeficientes do modelo.
3. **Tomada de Decisão:** As previsões são feitas com base nas probabilidades calculadas. Tipicamente, um limiar (threshold) é estabelecido (geralmente 0.5), onde probabilidades acima desse valor são classificadas como classe 1 e abaixo como classe 0.

**Parâmetros de Entrada Principais:**

- **penalty:** Especifica a norma usada na penalização. Utilizado: “l2” (default).
- **dual:** Booleano, usado quando o número de amostras é maior que o número de características. Utilizado: False (default).
- **tol:** Tolerância para o critério de parada. Utilizado: 1e-4 (default).
- **C:** Parâmetro de regularização inverso. Utilizado: 1.0 (default).
- **fit_intercept:** Especifica se deve ser ajustado um intercepto para este modelo. Utilizado: True (default).
- **solver:** Algoritmo a ser usado no problema de otimização. Utilizado: “lbfgs” (default).
- **random_state:** Controla a aleatoriedade do algoritmo. Utilizado: 42.

**Vantagens:**

- **Simplicidade e fácil interpretação:** Os coeficientes do modelo de regressão logística são fáceis de interpretar, facilitando a compreensão das relações entre variáveis independentes e o resultado. Cada coeficiente representa a mudança na razão de chances (odds ratio) da variável dependente por unidade de mudança na variável independente.
- **Baixo custo computacional:** A regressão logística é computacionalmente eficiente, sendo adequada para grandes conjuntos de dados tanto no treinamento quanto na predição.
- **Bom desempenho em problemas lineares e dados binários:** A regressão logística é eficaz em problemas onde existe uma relação linear entre as variáveis independentes e a variável dependente binária.

**Limitações:**

- **Baixa acurácia em problemas não lineares:** A regressão logística pode ter desempenho limitado em problemas onde as relações entre variáveis são não lineares. Para tais casos, outras abordagens, como o uso de polinômios ou a transformação das variáveis, podem ser necessárias.
- **Sensível a outliers e multicolinearidade:** Outliers podem distorcer os resultados do modelo, e a multicolinearidade (altas correlações entre variáveis independentes) pode dificultar a interpretação dos coeficientes. Técnicas de pré-processamento, como a remoção de outliers e a utilização de análise de componentes principais (PCA), podem ajudar a mitigar esses problemas.
- **Requer balanceamento das classes:** O desempenho do modelo pode ser prejudicado se as classes estiverem desbalanceadas. Métodos como reamostragem (oversampling ou undersampling) e o uso de técnicas como SMOTE (Synthetic Minority Over-sampling Technique) podem ajudar a equilibrar as classes.


**Matriz de confusão:**

![Logistic Regression](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/src/models/graficos/split_depois/sem%20normalizacao/LR_sem_normalizacao.png)

---

## 1.5 K-Nearest Neighbors (KNN)

**Descrição:**

O K-Nearest Neighbors (KNN) é um algoritmo baseado em instâncias que classifica pontos de dados com base na proximidade dos vizinhos mais próximos. Sem a necessidade de uma fase de treinamento explícita, o KNN é um método de aprendizado preguiçoso (lazy learning) que faz todas as computações durante a fase de predição, tornando-o intuitivo e direto para muitos problemas de classificação e regressão.

**Funcionamento:**

1. **Cálculo das Distâncias:** Para cada ponto de dados a ser classificado, o algoritmo calcula a distância entre esse ponto e todos os pontos do conjunto de treinamento usando uma métrica de distância, como a distância Euclidiana, Manhattan ou Minkowski.
2. **Seleção dos Vizinhos Mais Próximos:** O algoritmo seleciona os k pontos de dados mais próximos (vizinhos) do ponto em questão. O valor de k é um hiperparâmetro que deve ser definido pelo usuário e pode afetar significativamente o desempenho do modelo.
3. **Classificação:** A classe do ponto é determinada pela maioria das classes dos k vizinhos mais próximos (para classificação). Para problemas de regressão, a predição é feita pela média dos valores dos k vizinhos mais próximos.

**Parâmetros de Entrada Principais:**

- **n_neighbors:** Número de vizinhos a serem usados na classificação. Utilizado: 5 (default).
- **weights:** Função de peso usada na predição. Utilizado: “uniform” (default).
- **algorithm:** Algoritmo usado para computar os vizinhos mais próximos. Utilizado: “auto” (default). O parametro auto utiliza o algorítmo "KD Tree" com o nosso dataset.
- **leaf_size:** Tamanho da folha passada para BallTree ou KDTree. Utilizado: 30 (default).
- **p:** Potência do parâmetro da métrica de Minkowski. Utilizado: 2 (default).
- **metric:** Métrica a ser usada para a distância. Utilizado: “minkowski” (default).

**Vantagens:**

- **Simplicidade e fácil implementação:** O KNN é fácil de entender e implementar, sem necessidade de treinamento explícito, tornando-o acessível para iniciantes e útil em diversos cenários.
- **Não requer um modelo paramétrico:** O KNN não assume uma forma específica para a função de decisão, adaptando-se bem a várias distribuições de dados e sendo capaz de modelar relações complexas entre variáveis.
- **Bom desempenho em problemas com distribuições complexas:** O KNN é eficaz em problemas onde as distribuições de dados são complexas e não lineares, utilizando a proximidade dos pontos de dados para realizar a classificação ou regressão.

**Limitações:**

- **Alto custo computacional:** O KNN pode ser computacionalmente intensivo em grandes conjuntos de dados, especialmente durante a predição, devido à necessidade de calcular distâncias para todos os pontos de dados. Técnicas como a utilização de estruturas de dados eficientes (como k-d trees) podem ajudar a reduzir o tempo de execução.
- **Sensível a ruídos e outliers:** O desempenho do KNN pode ser afetado por ruídos e outliers, que podem influenciar negativamente as classificações baseadas na proximidade. Pré-processamento dos dados, como a remoção de outliers e a normalização, pode ajudar a mitigar esses efeitos.
- **Requer escolha adequada do valor de k e da métrica de distância:** A escolha do valor de k (número de vizinhos) e da métrica de distância pode afetar significativamente o desempenho do modelo. A seleção de k geralmente é feita através de validação cruzada, e a escolha da métrica de distância pode depender da natureza dos dados.


**Matriz de confusão:**

![KNN](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/src/models/graficos/split_depois/sem%20normalizacao/KNN_sem_normalizacao.png)

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


# Avaliação dos modelos criados

## Métricas utilizadas

### Matriz de Confusão

A matriz de confusão é uma tabela que avalia o desempenho de um modelo de classificação, comparando as previsões do modelo com os resultados reais. Ela tem a seguinte estrutura:

| -- | Previsão Positiva | Previsão Negativa |
|------------------|-----------------|-----------------|
| Real Positivo | Verdadeiro Positivo (TP) | Falso Negativo (FN) |
| Real Negativo |	Falso Positivo (FP)	| Verdadeiro Negativo (TN) |

Componentes:
Verdadeiro Positivo (TP): Casos positivos corretamente identificados.
Falso Negativo (FN): Casos positivos incorretamente identificados como negativos.
Falso Positivo (FP): Casos negativos incorretamente identificados como positivos.
Verdadeiro Negativo (TN): Casos negativos corretamente identificados.

Métricas Principais: 
Acurácia (Accuracy): Proporção de previsões corretas:
Acurácia = TP+TN / TP+TN+FP+FN 

Precisão (Precision): Proporção de verdadeiros positivos entre as previsões positivas.
Precisão = TP / TP+FP

Recall (Sensibilidade): Proporção de verdadeiros positivos entre os casos reais positivos.
Recall= TP / TP+FN

F1-Score: Média harmônica entre precisão e recall.
F1-Score= 2 X (Precisão×Recall / Precisão×Recall)

Importância:
A matriz de confusão ajuda a identificar e entender os tipos de erros (falsos positivos e falsos negativos) cometidos pelo modelo, permitindo a escolha e o ajuste das métricas de desempenho de acordo com a aplicação específica.


### Métricas de avaliação de classificação

Acurácia (Accuracy):
A acurácia pode ser útil para avaliar a proporção de previsões corretas feitas pelo modelo de ML na classificação de indivíduos como propensos ou não a ter AVC.
Então uma alta acurácia indica que o modelo está fazendo previsões precisas,  é importante para garantir que os pacientes sejam corretamente identificados como de alto risco ou não.

K-fold Cross-validation Mean Accuracy:
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

### Métricas Utilizadas e Justificativas

Accuracy (Acurácia):
Justificativa de Uso: A acurácia é uma métrica fundamental que indica a proporção de previsões corretas feitas pelo modelo em relação ao total de previsões. Ela é útil para ter uma visão geral do desempenho do modelo, especialmente quando as classes são balanceadas.
Justificativa de Não Uso: A acurácia pode ser enganosa em casos de classes desbalanceadas, onde o modelo pode apresentar alta acurácia apenas por prever a classe majoritária.

K-Fold Mean Accuracy (Média de Acurácia na Validação Cruzada K-Fold):
Justificativa de Uso: Esta métrica proporciona uma estimativa mais robusta da acurácia do modelo, pois avalia o desempenho em diferentes subconjuntos de dados, mitigando problemas de overfitting e subestimando a variabilidade do modelo.
Justificativa de Não Uso: Nenhuma. Esta métrica é valiosa para garantir que a acurácia observada não seja devido a um único conjunto de dados específico.

Standard Deviation (Desvio Padrão):
Justificativa de Uso: O desvio padrão das acurácias na validação cruzada indica a consistência do modelo. Um baixo desvio padrão sugere que o modelo tem desempenho consistente, enquanto um alto desvio padrão indica variabilidade nos resultados.
Justificativa de Não Uso: Nenhuma. Entender a variabilidade do modelo é crucial para avaliar a confiança nas previsões.

ROC AUC (Área Sob a Curva ROC):
Justificativa de Uso: A ROC AUC é uma métrica robusta que avalia a capacidade do modelo de distinguir entre classes positivas e negativas, independentemente do limiar escolhido. É especialmente útil para problemas de classificação binária onde o balanceamento entre as classes é uma preocupação.
Justificativa de Não Uso: Nenhuma. A ROC AUC é amplamente aplicável e fornece uma visão abrangente do desempenho do modelo.

Precision (Precisão):
Justificativa de Uso: A precisão mede a proporção de verdadeiros positivos entre todas as previsões positivas. É crucial quando o custo de falsos positivos é alto e queremos garantir que as previsões positivas sejam confiáveis.
Justificativa de Não Uso: Pode ser menos informativa quando a prioridade é minimizar falsos negativos, como em problemas onde é crucial identificar todos os casos positivos.

Recall (Sensibilidade):
Justificativa de Uso: O recall mede a proporção de verdadeiros positivos identificados entre todos os casos reais positivos. É vital em contextos onde é mais importante identificar todos os casos positivos, mesmo que isso resulte em mais falsos positivos, como na detecção de doenças.
Justificativa de Não Uso: Pode ser menos útil quando o foco é evitar falsos positivos, pois altos valores de recall podem resultar em muitos falsos positivos.

F1 Score:
Justificativa de Uso: O F1 Score é a média harmônica entre precisão e recall, equilibrando os dois aspectos. É útil quando precisamos de um equilíbrio entre a identificação de verdadeiros positivos e a minimização de falsos positivos.
Justificativa de Não Uso: Nenhuma. O F1 Score é valioso para obter uma visão equilibrada do desempenho do modelo.

### Métricas Não Utilizadas e Justificativas

Especificidade (True Negative Rate):
Justificativa de Não Uso: A especificidade não foi mencionada como uma métrica utilizada, possivelmente porque o foco principal é na identificação de casos positivos (minimização de falsos negativos) e no equilíbrio entre precisão e recall. Pode ser menos relevante em contextos onde a identificação correta dos negativos não é a principal prioridade.

Em resumo, as métricas selecionadas (acurácia, média de acurácia na validação cruzada, desvio padrão, ROC AUC, precisão, recall e F1 Score) foram escolhidas por suas capacidades de fornecer uma avaliação abrangente e equilibrada do desempenho do modelo de classificação, especialmente em um contexto onde a identificação correta de casos positivos (e a minimização de falsos negativos) é crucial. Métricas como a especificidade não foram incluídas, possivelmente porque não são o foco principal nesta análise específica.


## Discussão dos resultados obtidos

Nesta seção, discuta os resultados obtidos pelos modelos construídos, no contexto prático em que os dados se inserem, promovendo uma compreensão abrangente e aprofundada da qualidade de cada um deles. Lembre-se de relacionar os resultados obtidos ao problema identificado, a questão de pesquisa levantada e estabelecendo relação com os objetivos previamente propostos. 


| Model | Acurácia | K-Fold  Mean Accuracy | Standart Deviation | Roc Auc | Precision | Recall | F1-Score | Execução (s)| 
|-------|----------|-----------------------|--------------------|---------|-----------|--------|----------|----------|
| KNeighbors | 0.891002 | 0.8856883 | 1.287883 | 0.891229 | 0.831874 | 0.979381 | 0.899621 |  0.102 | 
| Random Forest | 0.939331 | 0.9363518 | 0.665223 | 0.939374 | 0.925150 | 0.955670 | 0.940162 | 0.814 | 
| Decision Tree | 0.902313 | 0.8980319 | 0.880905 | 0.902355 | 0.889222 | 0.918557 | 0.903651 | 0.032 | 
| Logistic Regression | 0.817994 | 0.8271815 | 1.082583 | 0.818070 | 0.799611 | 0.847423 | 0.822823 | 0.094 | 
| SVW | 0.767095 | 0.7793736 | 1.326972 | 0.767269 | 0.734361 | 0.835052 | 0.781476  | 1.882 | 


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


## Resumo dos Resultados da Avaliação dos Modelos de Aprendizado de Máquina para Previsão de AVC:

Após a aplicação do oversampling e a separação de 20% dos dados para teste, foram observadas diferenças significativas entre os modelos K-Nearest Neighbors (KNN) e Random Forest: 

Modelo K-Nearest Neighbors (KNN)
- Recall: Eficaz na minimização de falsos negativos, identificando corretamente indivíduos de risco.
- Precisão: Apresentou dificuldades, resultando em muitos falsos positivos.
- Acurácia: Inferior em comparação ao modelo Random Forest.
- Desvio Padrão da Precisão: Baixo, indicando consistência apesar do desempenho global não ideal.
- F1-Score: Baixo devido à precisão limitada.

  
Modelo Random Forest:
- Precisão e Recall: Equilibrados, evitando tanto falsos positivos quanto falsos negativos.
- F1-Score: Elevado, refletindo um bom equilíbrio entre precisão e recall.

  
**Conclusão**:
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



