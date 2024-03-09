# Introdução

O AVC é uma das principais causas de morte e incapacidade no mundo. A previsão precisa do AVC pode ajudar a prevenir eventos futuros e melhorar os resultados dos pacientes. O aprendizado de máquina oferece uma oportunidade promissora para desenvolver modelos de previsão de AVC precisos e eficazes.

# Problema

O Acidente Vascular Cerebral (AVC) é um problema sério que afeta muitas pessoas em todo o mundo. De acordo com uma reportagem do Estado de Minas a Organização Mundial da Saúde (OMS) cita o AVC como a segunda principal causa de morte no mundo, sendo responsável por cerca de 11% dos óbitos (SERRANO, 2022). Essa lesão traz um risco para a vida das vítimas, não só ocasionando mortes mas, também, trazendo incapacidades físicas e mentais em adultos, trazendo grandes impactos para a qualidade de vida e gerando altos custos para os sistemas de saúde. Dessa forma, é crucial que seja estudado as prováveis causas para seu acontecimento de modo a reconhecer padrões e prover prevenções e tratamentos para esse acidente.

# Questão de pesquisa

É possível estimar a probabilidade de um indivíduo sofrer um AVC com base em fatores de risco como idade, sexo, histórico familiar, tabagismo, diabetes, doenças cardíacas, hipertensão e uso de álcool?

# Cronograma

Coleta e pré-processamento de dados: 1 semana
Análise exploratória de dados: 1 semana
Seleção de variáveis: 1 semana
Treinamento e avaliação de modelos: 2 semanas
Comparação de modelos: 1 semana
Interpretação do modelo: 1 semana
Validação externa: 1 semana
Redação do relatório final: 2 semanas

[Saude+(PROJECT LIBRE.pdf](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/files/14471029/Saude%2B.PROJECT.LIBRE.pdf)

![Project Libre-Tarefas](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/assets/81451748/f8201179-514a-4183-91a0-3c2fca2617f4)

![Project Livre-Cronograma parte 1 e 2](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/assets/81451748/b4ef9f85-873e-469d-bf94-02fb0f52b375)


## Resultados Esperados

Identificação dos principais fatores de risco para AVC presentes no conjunto de dados.
Seleção do modelo de aprendizado de máquina mais eficaz para a tarefa de previsão de AVC.
Interpretação dos resultados do modelo de forma clinicamente relevante.
Discussão das implicações éticas e sociais da utilização de modelos de aprendizado de máquina para a previsão de AVC.

## Objetivos preliminares

A finalidade do trabalho é auxiliar a identificar pessoas que se encontram em grupo de risco para AVC. 

Para isso, será realizado um estudo na área e, a partir dos dados coletados, será treinado um modelo de Machine Learning que seja capaz de predizer se uma pessoa se encontra nesse grupo a partir de certos atributos.

A partir desse objetivo, será disponibilizado para os clientes da clínica Saúde+ uma série de recomendações caso se encontre em tal grupo de risco, como dicas de dieta, sintomas de um possível derrame, lista dos médicos cadastrados especializados na área, etc...


# Justificativa
O Correio Braziliense (2024) publicou um artigo que alerta para o aumento significativo das mortes por acidente vascular cerebral (AVC) nas próximas três décadas. De acordo com um relatório produzido por uma comissão de médicos, o número de óbitos por AVC pode aumentar em até 50% em relação a 2023, principalmente em países de renda média e baixa.
Atualmente, enfrentamos desafios significativos na prevenção do AVC, muitos dos quais estão enraizados em nossos estilos de vida modernos.
A vida sedentária, aliada a problemas de saúde como tabagismo e histórico familiar de AVC, é uma realidade para muitas pessoas. Muitos trabalham em escritórios, passando longas horas sentados, e mantêm uma alimentação pouco saudável.
Segundo a Organização Mundial da Saúde (OMS), o AVC é a segunda principal causa de morte em todo o mundo, sendo responsável por aproximadamente 11% do total de óbitos.
Entre os fatores de risco para o AVC, destacam-se a hipertensão arterial, doenças cardiovasculares, aterosclerose, diabetes mellitus, obesidade, sedentarismo, tabagismo, doenças genéticas de coagulação, idade avançada e histórico prévio de AVC.
É crucial que o público esteja ciente dos sintomas do AVC para reagir rapidamente diante dessa ameaça silenciosa.
Para auxiliar nesse processo de conscientização e prevenção, dados e estudos são fundamentais. Um conjunto de dados útil pode ser encontrado em: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset



### 1. Importância e Motivação

O acidente vascular cerebral (AVC) configura-se como um problema de saúde pública de alcance global, resultando em 5,5 milhões de óbitos e 110 milhões de DALYs (anos de vida perdidos por incapacidade) anualmente (Organização Mundial da Saúde, 2023). No Brasil, o AVC assume a posição de segunda principal causa de morte (Ministério da Saúde, 2023), sendo responsável por aproximadamente 100 mil óbitos a cada ano.

### 2.  Razões para Aprofundar o Estudo

Observa-se no Brasil uma escassez de modelos preditivos de AVC. A maior parte dos estudos existentes concentra-se na identificação de fatores de risco, não se dedicando à previsão da probabilidade de ocorrência de um evento.

- 2.2. Aprimoramento da Tomada de Decisão 
Um modelo preditivo preciso pode auxiliar os profissionais da saúde na identificação de pacientes com alto risco de AVC, possibilitando a implementação de medidas preventivas.

- 2.3. Redução da Carga da Doença
A prevenção do AVC pode gerar um impacto significativo na redução dos custos de saúde e da morbidade.


### 3.  Impacto na Sociedade

Um modelo preditivo de AVC preciso pode gerar um impacto significativo na sociedade brasileira:

- 3.1. Redução da Mortalidade

A detecção precoce e o tratamento adequado do AVC podem reduzir consideravelmente o número de óbitos.

- 3.2. Melhoria da Qualidade de Vida

A prevenção do AVC pode evitar sequelas graves, como hemiplegia e disfunção cognitiva.

- 3.3. Redução dos Custos de Saúde

A prevenção do AVC pode reduzir os custos de hospitalização, reabilitação e outros cuidados médicos.

### 4. Quantificação do Impacto

- 4.1. Custo do AVC no Brasil
O AVC impõe um custo anual de R$ 12,6 bilhões ao país (Ministério da Saúde, 2023).

- 4.2. Redução Potencial da Mortalidade
Estima-se que a redução da mortalidade por AVC possa variar entre 10% e 20% (Organização Mundial da Saúde, 2023).

- 4.3. Redução Potencial dos Custos de Saúde
A redução dos custos de saúde relacionados ao AVC pode alcançar de 10% a 20% (Ministério da Saúde, 2023).


# Público-Alvo

O nosso público-alvo tem uma ampla gama de profissionais de saúde, pesquisadores médicos, cientistas de dados e formuladores de políticas públicas. 
Aqui estão algumas categorias específicas dentro desse público:

 1 - Profissionais de Saúde: Médicos, enfermeiros, fisioterapeutas e outros profissionais de saúde que trabalham diretamente com pacientes em risco de AVC ou que já sofreram um AVC. Eles podem usar esses dados para entender melhor os fatores de risco, padrões de ocorrência e estratégias de prevenção.

 2 - Pesquisadores Médicos: Acadêmicos e pesquisadores que estudam doenças cardiovasculares, neurologia e fatores de risco para AVC. Eles podem usar esses conjuntos de dados para desenvolver novos modelos de previsão, identificar tendências emergentes e conduzir estudos epidemiológicos.

 3 - Cientistas de Dados e Analistas: Profissionais que trabalham com análise de dados e aprendizado de máquina, especialmente aqueles interessados em saúde e medicina. Eles podem usar esses dados para desenvolver algoritmos de previsão de AVC, identificar padrões ocultos nos dados e criar ferramentas de suporte à decisão para profissionais de saúde.

 4 - Formuladores de Políticas Públicas: Tomadores de decisão em níveis governamentais e não governamentais que estão envolvidos na formulação de políticas de saúde pública. Eles podem usar esses dados para entender melhor a carga do AVC em suas populações, avaliar a eficácia das intervenções de prevenção e desenvolver políticas direcionadas para reduzir o impacto do AVC na sociedade.

 5 - Educadores em Saúde: Profissionais envolvidos na educação pública sobre saúde, incluindo professores, instrutores de saúde comunitária e defensores da saúde. Eles podem usar esses dados para fornecer informações precisas sobre os fatores de risco de AVC, sinais de alerta e medidas preventivas para o público em geral.

Esses são alguns dos grupos que representam uma variedade de interesses e aplicações para conjuntos de dados de previsão de AVC, desde o diagnóstico e tratamento até a prevenção e políticas de saúde pública.

## Estado da arte

Pesquisa 1: Machine Learning and the Conundrum of Stroke Risk Prediction

1 - Quais pesquisas estão sendo desenvolvidas sobre esse tema?
Chahine, Magoon, Álamo, Boyle & Akoum (2023) Machine Learning and the Conundrum of Stroke Risk Prediction, National Library of Medicine, Vol. 12  pg 07, usou técnicas de aprendizado de máquina com algoritmo padrão predizem o risco usando associações estatísticas baseadas em regressão, têm acurácia preditiva moderada. Usaram as variáveis de risco coletadas na coorte Multi-Ethnic Study of Atherosclerosis para treinar um algoritmo SVM ML.
Esta revisão resume os esforços recentes para implantar o aprendizado de máquina (ML) para prever o risco de AVC e enriquecer a compreensão dos mecanismos subjacentes ao AVC. Com paradigma de avaliação e mitigação do risco de AVC está focado nos fatores de risco clínicos e comorbidades.
Chahine, Magoon, Álamo, Boyle & Akoum (2023) Compararam o Perfil de Risco de AVC de Framingham de 2017 com técnicas de ML para predição de risco de AVC (random survival forest [RSF], SVM, GBT e multilayer perceptron) em uma corte chinesa de 503.842 adultos.

2 - Detalhe e contextualize o problema, descreva o dataset utilizado.
Os escores de risco tradicionais dependem principalmente de comorbidades e características clínicas do paciente para prever o risco de AVC, no entanto, abordagens baseadas em aprendizado de máquina podem combinar recursos complexos para produzir uma avaliação de risco mais precisa.
 Modelos de classificação e regressão (por exemplo, máquina de vetores de suporte [SVM], floresta aleatória [RF], árvore intensificada por gradiente [GBT]) são mais comumente usados em pesquisas clínicas. Esses métodos pesquisam entre as variáveis preditoras disponíveis para encontrar as características mais bem vinculadas ao resultado. Modelos de aprendizagem profunda baseados em redes neurais, especialmente redes neurais convolucionais (CNNs), podem ser usados para extrair características de ECGs e podem ser usados em algoritmos de reconhecimento de imagem para encontrar padrões de dados em pixels de imagem.
O dataset foi extraído MedGen na biblioteca NLM fornece acesso à literatura científica. A inclusão em um banco de dados NLM não implica endosso ou acordo com, o conteúdo da NLM ou do National Institutes of Health. Cada símbolo ancora um link para o registro no banco de dados Gene do NCBI. A lista completa de relacionamentos Gene-MedGen é fornecida a partir do site FTP da Gene. Testes genéticos registrados no NIH Genetic Testing Registry (GTR) GeneReviews ClinVar OMIM Genes relacionados Transtornos com características clínicas semelhantes Literatura médica e de pesquisa Diretrizes práticas Recursos do consumidor Ontologias como HPO e ORDO.
Para Chahine, Magoon, Álamo, Boyle & Akoum (2023) o ML oferece algoritmos capazes de modelar relações complexas e ocultas entre múltiplas variáveis clínicas e fisiológicas e os resultados desejados.
Dataset utilizado foram características e dados demográficos dos pacientes, níveis de biomarcadores sanguínios, dados de imagem como base para predizer DCV. 
Avaliação Clínica do Risco de Acidente Vascular Cerebral na Fibrilação Atrial. Os primeiros esforços para desenvolver algoritmos de ML para prever o risco de AVC em pacientes com FA mostraram alguma promessa e alcançaram uma AUC tão alta quanto 0,892 em uma análise de coorte. Usando os dados do Seguro Nacional de Saúde da Coreia e forneceu melhor predição de AVC isquêmico em pacientes com FA em comparação com ACS2DS2-Escores da EAVc (AUC 0,727 versus 0,651, respectivamente).  
A carga de arritmia é um fator significativo na predição do risco de AVC, uma vez que pacientes com FA persistente ou permanente têm maior propensão a AVC do que pacientes com FA paroxística. [Rev.,Arrhythm Eletrofisiol (2023), Chahine, Magoon, Maidu, Del Álamo, & Akoum, Machine Learning and the Conundrum of Stroke Risk Prediction, Vol.12.e07,  DOI: 10.15420/aer.2022.34. Disponível em: Machine Learning and the Conundrum of Stroke Risk Prediction - PMC (nih.gov)].
Chahine et. al (2023) identificaram a RSF como o modelo de risco cardiovascular mais preditivo (incluindo acidente vascular cerebral) de nove modelos testados em uma população multirracial inicialmente assintomática.

Chahine et. al (2023) comparam estudos de  algoritmos de ML com métodos convencionais para previsão de risco de AVC são eles:
Máquina de vetor de suporte
Modelo de conjunto combinando árvores Gradient Boosted e modelos Cox
Redes neurais
Floresta aleatória
Algoritmo AutoPrognosis
Regressão logística
Rede neural profunda baseada em atenção
Floresta aleatória

As métricas utilizadas por  Chahine et. al (2023) e os resultados obtidos:
 | Entrada | Métrica | Precisão |
 | :---  |  :---:  |---:  |
 |Mesmos fatores de risco que a calculadora de risco ACC/AHA | Sensibilidade especificidade | 0,86 0,95 e AUC 0,92 |
 | :--- | :---: | ---: |
 | Fatores sociodemográficos, dieta, história médica, atividade física e medidas físicas |
 | Precisão Sensibilidade Especificidade VPP VPL | ♂ 76%, ♀ 80%; ♂ 76%, ♀ 67%; ♂ 76%, ♀ 81%; ♂ 26%, ♀ 24%; ♂ 97%, ♀ 97 |
 |  :--- |  :---: |  ---:|
 | Fatores de risco ACC/AHA e 22 variáveis adicionais | Sensibilidade especificidade VPP VPN AUC | 67,5%, 70,7%, 18,4%, 95,7%, 0,76 |
 | :--- | :---: |  ---: |
 | Imagem, ECG e biomarcadores séricos (735 variáveis) | Índice C, Escore Brier | 0,81, 0,083 |
 |  :--- |  :---: |  ---: |
 | 473 variáveis clínicas e laboratoriais| Sensibilidade VPP AUC | 69,9%, 2,6%, 0,774 |
 |  :--- |  :---: |  ---: |
 | Lista diversificada de comorbidades/variáveis demográficas/temporais de exposição | AUC | 0,892 |
 |  :--- |  :---:  |  ---: |
 |Informações demográficas, de exames de saúde e de histórico médico | AUC | 0,727 |
 |  :--- |  :---: |  ---: |
 |Carga de FA registrada em dispositivos eletrônicos implantáveis cardíacos | Sensibilidade especificidade AUC | 52%, 63%, 0,662 |


Pesquisa 2 https://iieta.org/journals/ria/paper/10.18280/ria.340609

1 - Quais pesquisas estão sendo desenvolvidas sobre esse tema?
Diversas pesquisas estão em andamento, como o desenvolvimento de modelos de predição mais precisos, estudos de subgrupos para identificar variações no risco entre diferentes grupos, e aplicações clínicas para personalizar a prevenção e o tratamento do AVC. O objetivo final é melhorar a prevenção, o diagnóstico e o tratamento do AVC, salvando vidas e reduzindo o impacto dessa doença devastadora.
Bandi, Bhattacharyya & Midhunchkkravarthy (2020) Prediction of Brain Stroke Severity Using Machine Learning. IIETA, Vol. 34, página 1. "Esta pesquisa do modelo Stroke Predictor (SPR) utilizando técnicas de aprendizado de máquina melhorou a precisão da previsão para 96,97% quando comparado com os modelos existentes."

2 - Detalhe e contextualize o problema, descreva o dataset utilizado.
Bandi, Bhattacharyya & Midhunchkkravarthy (2020) perceberam que o ML oferece algoritmos capazes de modelar relações complexas e ocultas entre múltiplas variáveis clínicas e fisiológicas e resultados desejados. A previsão de doenças vasculares (DCV) facilitam a tomada de decisão clínica pois é baseada em escores de risco que utilizam as características clínicas e comorbidades dos pacientes, mas o ML e/ou inteligência artificial (IA) têm o potencial de prever as consequências de diferenças sutis interindividuais na fisiologia e/ou anatomia, sendo muito mais promissora que combinam recursos complexos e produz avaliações de risco muito mais precisas.
Para Bandi et. al (2020) o estudo de prevenção de AVC utilizando ML visa resolver os seguintes problemas: Para Identificação de Fatores de Risco: Os pesquisadores estão usando técnicas de machine learning para identificar padrões e correlações em grandes conjuntos de dados de saúde para prever quem está em maior risco de desenvolver AVC. Isso pode incluir análise de dados demográficos, histórico médico, estilo de vida e biomarcadores.
-Diagnóstico Precoce: Algoritmos de machine learning estão sendo desenvolvidos para analisar imagens médicas, como tomografias computadorizadas (TC) e ressonâncias magnéticas (RM), a fim de detectar sinais precoces de AVC. Isso pode ajudar os médicos a diagnosticarem e tratar o AVC mais rapidamente, reduzindo o dano cerebral.
-Previsão de Recorrência: Uma vez que uma pessoa tenha sofrido um AVC, há um risco aumentado de recorrência. Modelos de machine learning estão sendo explorados para prever a probabilidade de um indivíduo sofrer um segundo AVC com base em seu histórico médico, fatores de estilo de vida e outros dados relevantes.
-Desenvolvimento de Sistemas de Monitoramento Remoto: Dispositivos vestíveis e sensores de saúde estão se tornando mais comuns, e os pesquisadores estão usando dados coletados por esses dispositivos para monitorar a saúde cardiovascular e prever eventos como AVC. Algoritmos de machine learning são usados para analisar os dados e identificar padrões que podem indicar um risco aumentado de AVC.
-Personalização do Tratamento: A resposta ao tratamento após um AVC pode variar de pessoa para pessoa. Pesquisas estão sendo realizadas para desenvolver modelos de machine learning que possam prever quais tratamentos serão mais eficazes para indivíduos com base em suas características individuais e perfil genético.
Essas são apenas algumas das muitas áreas de pesquisa em machine learning para a prevenção de AVC. O uso dessa tecnologia promete melhorar significativamente a detecção precoce, o tratamento e a prevenção de AVC, reduzindo assim o impacto devastador dessa condição de saúde.
Dataset utilizados:
Bandi, Midhunchakkaravarthy & Bhattacharyya. (2020). Dataset Stroke_Analysis [CSV]. Mendeley Data. Stroke_Analysis - Mendeley Data
Neste dataset inclui um total de 4.799 sujeitos, que contém 3.123 homens e 1.676 mulheres e o resumo dos atributos primários está disponível no conjunto de dados. Como parte do pré-processamento dos dados, do conjunto de dados disponível, exclui-se o atributo 'Gênero' neste trabalho de pesquisa.


Tabela 1. Resumo do conjunto de dados do artigo de Bandi et. Al (2020)
| Atributo | Mínimo | Máximo | Significar | Desvio | padrão |
| :---: | :---: | :---: | :---: | :---: |  ---:|
| Idade  | 1 | 90 | 47.12 | 23.69 |
| NIHSS   | 0 | 45 |  18.12 | 11.27 |
| Sra  | -1 | 6 | 3.67 | 1.87 |
| PA sistólica | 100 | 195 | 153.09 | 24.92 |
| PA diastólica | 59 | 135 | 103.65 | 18.34 |
| Glicose  | 70 | 295 | 225.85 | 56.11 |
| Paralisia  | 0 | 3 | 1.36 | 1.106 |
| Tabagismo  | 0 | 3 | 0.88 | 0.9 |
| IMC | 18  | 45 | 33.73 | 6.23 |
| Colesterol | 160 | 253 | 217.53 | 20.26 |

•	Variáveis demográficas dos participantes (idade, gênero, altura, peso, etc.).
•	Resultados de testes físicos (pressão arterial, frequência cardíaca em repouso, capacidade aeróbica, etc.).
•	Histórico médico dos participantes (presença de condições médicas pré-existentes, uso de medicamentos, etc.).
•	Dados de monitoramento durante o exercício (duração, intensidade, tipo de exercício, etc.).
•	Resultados de acompanhamento ao longo do tempo (alterações na pressão arterial, frequência cardíaca máxima alcançada, melhora na capacidade aeróbica, etc.).

3 - Algoritmos utilizados nas pesquisas.
Bandi et. al (2020) utilizaram os algoritmos que seguem:
Algoritmo de árvore de decisão de C4.5 e modelo de rede neural híbrida. Floresta de decisão bootstrap árvores impulsionadas regressão logística e rede neural profunda.
No algoritmo de aprendizagem supervisionada usa o modelo Naïve Bayes, que depende do teorema de Bayesm obteve nessa pesquisa 76,77 %. “Regressão multilinear” dentre os vários tipos de módulos de regressão linear. A regressão logística enquadra-se na técnica de aprendizagem supervisionada,
Em Previsão de AVC (SPN) na etapa 1: se o modelo treinado for 'Falso', carregue os dados treinados e comece a treinar o modelo. Etapa 2: a partir dos dados do usuário, inicialize os dados necessários para a previsão.
Redes Neurais Artificiais (RNAs) são modelos inspirados no funcionamento do cérebro humano e são frequentemente usados em pesquisas de machine learning devido à sua capacidade de aprender padrões complexos em grandes conjuntos de dados. E SVM que é um algoritmo de aprendizado supervisionado que é frequentemente usado para classificação e regressão. Ele funciona bem em conjuntos de dados de alta dimensionalidade e é eficaz na identificação de padrões não lineares.
As Redes Neurais Recorrentes (RNN) são frequentemente usadas em pesquisas que envolvem séries temporais, como dados de monitoramento de saúde ao longo do tempo. Elas são capazes de capturar dependências temporais nos dados.
Dos resultados:
Nesta, Árvores de decisão, são modelos simples e interpretáveis que são frequentemente usados para classificação e regressão, obteve performance de 93,12% na pesquisa em questão. Florestas aleatórias são uma extensão das árvores de decisão e combinam várias árvores para melhorar o desempenho preditivo.
Outra muito utilizada é CNNs que são frequentemente usadas em pesquisas que envolvem análise de imagens médicas, como tomografias computadorizadas (TC) e ressonâncias magnéticas (RM). Elas são eficazes na extração de características de imagens complexas.
E por último o SVM que é um algoritmo de aprendizado supervisionado que pode ser usado para classificação e regressão obteve performance de aproximadamente 83%. Ele é eficaz na identificação de padrões complexos e na separação de classes em espaços de alta dimensão.

4 - Identifique as métricas de avaliação empregadas.
A precisão (ACC) é avaliada pelo número de todas as identificações exatas separadas da soma de um número do conjunto de dados. EX: Precisão = Verdadeiro Positivo + Verdadeiro Negativo Verdadeiro Positivo + Verdadeiro Negativo + Falso Negativo + Falso Positivo
F1-Score determina quão específico é o classificador e também quão rígido ele pode ser. A proporção de alta precisão e baixa recuperação extrai as possibilidades mais precisas, mas omite vários exemplos que se tornam complexos durante a divisão. A expressão matemática é dada por:
EX: F1- Pontuação = 2∗11 precisão +1 lembrar
Precisão e Revocação, esta métrica mede a proporção de previsões positivas corretas em relação ao total de previsões positivas feitas pelo modelo. Revocação (ou sensibilidade) mede a proporção de instâncias positivas corretamente identificadas pelo modelo em relação ao total de instâncias positivas no conjunto de dados. 94 e 91 % aproximandamente comparaçaõ entre basic randomforest e improved random forest model.
O F1-Score é a média harmônica entre precisão e revocação. Ele fornece uma única métrica que leva em consideração tanto a precisão quanto a revocação do modelo. 94 e 91 % aproximandamente comparaçaõ entre basic randomforest e improved random forest model.
A curva ROC que é uma representação gráfica do desempenho de um modelo de classificação em diferentes limiares de decisão. A área sob a curva ROC (ROC-AUC) é uma métrica que quantifica a capacidade discriminativa do modelo em distinguir entre classes positivas e negativas.
A acurácia mede a proporção de previsões corretas feitas pelo modelo em relação ao total de previsões feitas. É uma métrica simples e amplamente utilizada, mas pode não ser adequada para conjuntos de dados desbalanceados. 96 e 94 % aproximadamente comparação entre basic randomforest e improved random forest model. 96 e 94 % aproximadamente comparação entre basic randomforest e improved random forest model.

As métricas de desemplenho utilizadas foram:
A precisão (ACC) é avaliada pelo número de todas as identificações exatas separadas pela soma de um número do conjunto de dados.
A sensibilidade é avaliada para o número de identificações de divisões positivas corretas para o número total de positivos.
A Especificidade é determinada pela quantidade total de identificações negativas corretas separadas pelo total de números negativos.
A Taxa de Falso Positivo é determinada pela avaliação FP / (FP+TN). Ele é determinado pela proporção de pontos negativos que são erroneamente tomados como positivos quando comparados com o de todos os pontos negativos dos dados.
O F1-Score determina o quão específico é o classificador e também o quão rígido ele pode ser. A proporção de alta precisão e baixa recordação desenha as possibilidades mais precisas, mas omite vários exemplos que se tornam complexos ao dividir. A expressão matemática é dada por:
A Precisão dá múltiplos resultados positivos quando distinguida por um número de resultados positivos identificados pelos classificadores.
5 - Resultados obtidos.
As pesquisas sobre machine learning para prevenção de AVC estão produzindo resultados importantíssimo que têm o potencial de melhorar significativamente a detecção precoce, o tratamento e a prevenção do AVC, reduzindo assim o impacto devastador dessa condição de saúde. O diagnóstico precoce, o monitoramento e a personalização do tratamento, além do Modelos Preditivos Precisos para identificando as pessoas com maior risco de AVC.
Neste estudo, uma técnica de conjunto Random Forest foi utilizada para prever o risco de AVC, alcançando uma precisão de 96,97% com uma taxa de erro de 0,03%. Os resultados indicam uma eficácia significativa na previsão de AVC usando este modelo. Como futuras pesquisas, sugere-se explorar métodos para diferentes tipos de AVC e níveis de risco, potencialmente utilizando conjuntos de dados de imagens.


Pesquisa 3: Stroke prediction through Data Science and Machine Learning Algorithms 

A pesquisa de Rodriguez (2021)  Stroke prediction through Data Science and Machine Learning Algorithms tem como objetivo criar um modelo preciso para prever o resultado do AVC com ciência de dados e aprendizado de máquina (ML) com base em dados anteriores e características individuais e fornecer informações úteis para a equipe médica implantar o tratamento necessário e diminuir riscos e consequências. 

Para Rodriguez (2021) é difícil interpretar os padrões ou extrair informações úteis dos dados pois entende que seja devido à quantidade de informações serem pouco perceptível e é onde as técnicas de ML são muito úteis para ensinar, como o próprio nome indica, máquinas a lidar com dados de forma mais eficiente. 

O dataset utilizado foi HealthData.gov, Liu, Fan & WU (2019). A hybrid machine learning approach to cerebral stroke prediction based on imbalanced medical-datasets  [RAR]. Mendley. Data for: A hybrid machine learning approach to cerebral stroke prediction based on imbalanced medical-datasets - Mendeley Data, que também é utilizado como conjunto de dados de referência em uma competição de Kaggle2. . 

Nele inclui informações sobre 5.110 indivíduos caracterizados por 10 características e inclui informações sobre a variável alvo que é o  AVC para todos eles, isso permite uma abordagem de aprendizagem supervisionada e é a mais frequente utilizada. O objetivo é montar um modelo conciso da distribuição de rótulos de classes em termos de características preditoras e depois é usado para atribuir rótulos de classe às instancias de teste. 

 

O dataset original  tinha 201 valores ausentes para IMC.  Mais de 30 %  tinha o status desconhecido para tabagismo, demonstrando  falta de informação assim utilizaram a idade de 18 ou menos para nunca. 

 

 

Algoritmos, métricas e resultados de Rodriguez (2021) foram: 

 

A precisão do modelo de Arvore de decisão foi 0,9011. De regressão logística 0,8059. Baías ingênuas 0,7907 e Classificador de vizinhos K 0,8790. O Floresta aleatória obteve precisão de 0,9232 de rede neural 0,82. Máquinas e vetores de suporte 0,822 e por fim Classificador XGBoost 0,91 

Segundo a pesquisa de Rodriguez (2021) Random Forest foi o algoritmo de ML de melhor desempenho para este problema específico, seguido por XGBoost e Decision Tree em termos de precisão do modelo. 

AUC  de 0,975 no Random Forest e uma AUC de 0,500 para Random prediction. Na Curva Receiver Operating Characteristic (ROC) quando maior a AUC, melhor o modelo de classificação correta das instancias. 

Foi utilizado a técnica SMOTE para equilibrar o conjunto de dados para melhorar o desempenho dos modelos de ML. 

Nesta pesquisa Rodriguez (2021) provou q atraves da CIencia de dados e do uso de algoriticmo de Aprendizagem de máquina , é possível prever or esultado do AVC  e que a metodologia CRISPI-DM ajuda na orientação da análise dos dados, tornando mais simples e efeicaz. 

Pesquisa 4 Aprendizado de máquina para acidente vascular cerebral: uma revisão - ScienceDirect 

 

( NAO FOI POSSÍVEL OBTER OS DADOS, POIS NÃO FOI POSSÍVEL ABRIR O PDF), Porém o trabalho é muito relevante. 

1 - Quais pesquisas estão sendo desenvolvidas sobre esse tema? 

Uma aplicação de ML e Deep Learning na área da saúde está crescendo, no entanto, algumas áreas de pesquisa não chamam atenção suficiente para a investigação científica, embora haja real necessidade de pesquisa. Portanto, o objetivo deste trabalho é classificar o estado da arte das técnicas de ML para acidente vascular cerebral em 4 categorias com base em suas funcionalidades ou similaridade e, em seguida, revisar sistematicamente os estudos de cada categoria.   

 

2 - Detalhe e contextualize o problema, descreva o dataset utilizado 

Para Sirsat, Fermé & Câmara (2020). Machine Learning for Brain Stroke: A Review, o AVC é um grande desafio relacionado à saúde e que nos últimos anos o ML tem crescido rapidamente e evoluído e que o AVC é um grande problema devido a alta taxa de mortalidade, para isso a detecção deve ser precoce.  

Segundo Sirsat et. al (2020) Machine Learning (ML) é uma tecnologia de ponta que pode ajudar os profissionais de saúde a tomar decisões clínicas e previsões. 

 

Foram 39 estudos  identificados a partir dos resultados da base de dados científica ScienceDirect web sobre ML para acidente vascular cerebral do ano de 2007 a 2019. 

 

3 - Algoritmos utilizados nas pesquisas 

Utilizado o modelo ML que têm a capacidade de aprender e melhorar a partir de dados passados sem serem explicitamente programados. Existem vários subtipos de ML, no entanto, nesta revisão, a aprendizagem supervisionada, a aprendizagem não supervisionada e a aprendizagem profunda são tipos focados no presente estudo.  

4 - Identifique as métricas de avaliação empregadas 

5 - Resultados obtidos. 

 Os resultados  encontrados em 8 estudos sobre prevenção de AVC, 18 estudos sobre diagnóstico de AVC, 4 estudos sobre tratamento de AVC e 9 estudos sobre prognóstico de AVC.  Foi observado que é difícil comparar os estudos, pois eles empregaram diferentes métricas de desempenho para diferentes tarefas, considerando diferentes conjuntos de dados, técnicas e parâmetros de ajuste. Assim, citam-se apenas as áreas de pesquisa que foram alvo de mais de um estudo e os estudos que relatam maior acurácia na classificação 

 

 

 

 

 

> **Links Úteis**:
> - [Google Scholar](https://scholar.google.com/)
> - [IEEE Xplore](https://ieeexplore.ieee.org/Xplore/home.jsp)
> - [Science Direct](https://www.sciencedirect.com/)
> - [ACM Digital Library](https://dl.acm.org/)

# Descrição do _dataset_ selecionado

Link para o dataset: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset/data

De acordo com a Organização Mundial da Saúde (OMS), o AVC é a 2ª principal causa de morte no mundo, responsável por aproximadamente 11% do total de mortes.
Este conjunto de dados é usado para prever se um paciente tem probabilidade de sofrer um derrame com base em parâmetros de entrada como sexo, idade, várias doenças e tabagismo. Cada linha dos dados fornece informações relevantes sobre o paciente.

Atributos:

1) id: Identificador único
2) gender: "Masculino", "Feminino" ou "Outro"
3) age: Idade do paciente
4) hypertension: 0 se o paciente não tiver hipertensão, 1 se tiver
5) heart_disease: 0 se o paciente não tiver doença cardíaca, 1 se tiver
6) ever_married: "Sim" ou "Não"
7) work_type: "Criança", "Esfera pública", "Nunca trabalhou", "Esfera privada" or "Conta própria"
8) Residence_type: "Rural" ou "Urbano"
9) avg_glucose_level: Nível médio de glicose no sangue
10) bmi: Indice de massa corporal
11) smoking_status: "fumou previamente", "nunca fumou", "fuma" ou "desconhecido"*
12) stroke: 0 se o paciente não tiver tido um derrame, 1 se tiver
    
*Nota: "desconhecido" em smoking_status significa que a informação não está disponível

# Canvas analítico

Canvas Analítico. O Canvas Analítico tem o papel de registrar a organização das ideias e apresentar o modelo de negócio.

![Business Model Canvas - Quadro 1](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/assets/81451748/53776c68-f1cd-4c6a-af19-2b75b6e2f41f)

> **Links Úteis**:
> - [Modelo do Canvas Analítico](https://github.com/ICEI-PUC-Minas-PMV-SI/PesquisaExperimentacao-Template/blob/main/help/Software-Analtics-Canvas-v1.0.pdf)


# Conclusões

O desenvolvimento de um modelo preditivo de AVC preciso pode ter um impacto significativo na saúde pública brasileira. Este estudo visa contribuir para esse objetivo, fornecendo um modelo que possa ser utilizado por profissionais de saúde para identificar pacientes com alto risco de AVC e tomar medidas preventivas.


# Referências

1. MINISTÉRIO DA SAÚDE. AVC. Brasília: Ministério da Saúde, 2023. Disponível em: https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/a/avc .
2. ORGANIZAÇÃO MUNDIAL DA SAÚDE. Acidente vascular cerebral (AVC). Cairo: Organização Mundial da Saúde, 2023. Disponível em: https://www.emro.who.int/health-topics/stroke-cerebrovascular-accident/index.html.
3. SERRANO, AMANDA. AVC é a segunda causa de mortes no mundo e avança nos países de baixa renda. Estado de Minas, Belo Horizonte, MG, 18 abr. 2022. Saúde. Disponível em: https://www.em.com.br/app/noticia/bem-viver/2022/04/18/interna_bem_viver,1360730/avc-e-a-segunda-causa-de-mortes-no-mundo-e-avanca-nos-paises-de-baixa-renda.shtml.
4. CORREIO BRAZILIENSE. Mortes por AVC vão disparar nas próximas três décadas. Correio Braziliense, Brasília, DF, 24 out. 2023. Disponível em: https://www.correiobraziliense.com.br/ciencia-e-saude/2023/10/5132443-mortes-por-avc-vao-disparar-nas-proximas-tres-decadas.html.
5. Rev.,Arrhythm Eletrofisiol (2023), CHAHINE, MAGOON, MAIDU, ÁLAMO, & AkOUM (2023). Machine Learning and the Conundrum of Stroke Risk Prediction, NIH- National Library of Medicine, DOI: 10.15420/aer.2022.34, EUA, v.12, e07, out/2022. Disponível em: Machine Learning e o enigma da previsão de risco de AVC - PMC (nih.gov). Acesso em: 08, 03 e 2024.

6. BANDI, BHATTACHARYYA & MIDHUNCHKKRAVARTHY (2020). Prediction of Brain Stroke Severity Using Machine Learning. IIETA, DOI: https://doi.org/10 18280/ria.340609, Vol. 34, página 1.Disponível em: https://iieta.org/journals/ria/paper/10.18280/ria.340609. Acesso em: 08, 03 e 2024.
7. RODRIGUEZ (2021). Stroke prediction through Data Science and Machine Learning Algorithms. School of Engineering and Sciences Tecnológico de Monterrey Monterrey. DOI: 10.13140/RG.2.2.33027.43040, Monterrei México. Disponível em: https://www.researchgate.net/publication/352261064. 
8. PREVISÂO da gravidade do acidente vascular cerebral usando aprendizado de máuina. IIETA, 2022. Disponível em: https://iieta.org/journals/ria/paper/10.18280/ria.340609. Acesso em: 04, 03 e 2024. Acesso em: 08, 03 e 2024.


> **Links Úteis**:
> - [Padrão
> - ABNT PUC Minas](https://portal.pucminas.br/biblioteca/index_padrao.php?pagina=5886)
