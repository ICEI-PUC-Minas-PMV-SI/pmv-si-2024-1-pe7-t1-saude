# Introdução

(Texto descritivo introdutório apresentando a visão geral do projeto a ser desenvolvido considerando o contexto em que ele se insere, os objetivos gerais, a justificativa e o público-alvo do projeto.)

O AVC é uma das principais causas de morte e incapacidade no mundo. A previsão precisa do AVC pode ajudar a prevenir eventos futuros e melhorar os resultados dos pacientes. O aprendizado de máquina oferece uma oportunidade promissora para desenvolver modelos de previsão de AVC precisos e eficazes.


# Problema

O Acidente Vascular Cerebral (AVC) é um problema sério que afeta muitas pessoas em todo o mundo. De acordo com uma reportagem do Estado de Minas (https://www.em.com.br/app/noticia/bem-viver/2022/04/18/interna_bem_viver,1360730/avc-e-a-segunda-causa-de-mortes-no-mundo-e-avanca-nos-paises-de-baixa-renda.shtml) a Organização Mundial da Saúde (OMS) cita o AVC como a segunda principal causa de morte no mundo, sendo responsável por cerca de 11% dos óbitos. Essa lesão traz um risco para a vida das vítimas, não só ocasionando mortes mas, também, trazendo incapacidades físicas e mentais em adultos, trazendo grandes impactos para a qualidade de vida e gerando altos custos para os sistemas de saúde. Dessa forma, é crucial que seja estudado as prováveis causas para seu acontecimento de modo a reconhecer padrões e prover prevenções e tratamentos para esse acidente.

# Questão de pesquisa

O objetivo deste estudo é determinar o modelo de aprendizado de máquina mais eficaz para prever a ocorrência de AVC em pacientes, considerando os fatores de risco presentes no conjunto de dados de Fedesoriano.

## Hipótese

Os modelos de aprendizado de máquina podem ser usados ​​para prever com precisão a ocorrência de AVC em pacientes, utilizando os fatores de risco presentes no conjunto de dados de Fedesoriano.

## Metodologia

### 1. Coleta e Pré-processamento de Dados

O conjunto de dados de Fedesoriano será utilizado (https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset).
O conjunto de dados será limpo e pré-processado para lidar com valores ausentes e inconsistentes.
As variáveis ​​serão padronizadas para garantir uma escala uniforme.
### 2. Análise Exploratória de Dados

A distribuição das variáveis ​​será visualizada para identificar outliers.
Medidas estatísticas descritivas serão calculadas.
As correlações entre as variáveis ​​serão identificadas.
### 3. Seleção de Variáveis

Técnicas de seleção de variáveis ​​serão utilizadas para identificar os preditores mais importantes.
A importância estatística e a relevância clínica das variáveis ​​serão consideradas.
### 4. Treinamento e Avaliação de Modelos

Diferentes modelos de aprendizado de máquina serão treinados, como:
Regressão logística
Árvore de decisão
Floresta aleatória
Redes neurais artificiais
O desempenho dos modelos será avaliado usando métricas como:
Acurácia
Precisão
Recall
F1-score
### 5. Comparação de Modelos

O desempenho dos diferentes modelos de aprendizado de máquina será comparado.
O modelo com o melhor desempenho para a tarefa de previsão de AVC será selecionado.
### 6. Interpretação do Modelo

Os fatores de risco mais importantes para AVC de acordo com o modelo selecionado serão identificados.
Os resultados do modelo serão interpretados de forma clinicamente relevante.
### 7. Validação Externa

O modelo selecionado será validado em um conjunto de dados externo.
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

(Aqui você deve descrever os objetivos preliminares do trabalho indicando que o objetivo geral é experimentar modelos de aprendizado de máquina adequados para solucionar o problema apresentado acima. 

Apresente também alguns (pelo menos 2) objetivos específicos dependendo de onde você vai querer concentrar a sua prática investigativa, ou como você vai aprofundar no seu trabalho.

Por exemplo: um objetivo específico pode estar relacionado a predizer a tendência de alta, estabilidade ou queda de uma determinada ação em uma determinada janela do tempo ou então, predizer o valor exato de uma determinada ação.
Lembre-se que, à medida que a pesquisa/experimentação evolui, os objetivos podem evoluir também, portanto, não se esqueça de fazer as atualizações necessárias.
 
> **Links Úteis**:
> - [Objetivo geral e objetivo específico: como fazer e quais verbos utilizar](https://blog.mettzer.com/diferenca-entre-objetivo-geral-e-objetivo-especifico/)



A finalidade do trabalho é auxiliar a identificar pessoas que se encontram em grupo de risco para AVC. 

Para isso, será realizado um estudo na área e, a partir dos dados coletados, será treinado um modelo de Machine Learning que seja capaz de predizer se uma pessoa se encontra nesse grupo a partir de certos atributos.

A partir desse objetivo, será disponibilizado para os clientes da clínica Saúde+ uma série de recomendações caso se encontre em tal grupo de risco, como dicas de dieta, sintomas de um possível derrame, lista dos médicos cadastrados especializados na área, etc...

# Objetivo Específico

Este estudo visa desenvolver um modelo de aprendizado de máquina para prever a probabilidade de um paciente sofrer um AVC. O modelo será treinado e validado usando o conjunto de dados "Stroke Prediction Dataset" disponível no Kaggle (https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset).


# Justificativa
### 1. Importância e Motivação

O AVC é um problema de saúde pública global, com 5,5 milhões de mortes e 110 milhões de DALYs (anos de vida perdidos por incapacidade) a cada ano (https://www.emro.who.int/health-topics/stroke-cerebrovascular-accident/index.html). No Brasil, o AVC é a segunda principal causa de morte (https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z), responsável por 100 mil mortes anualmente.


### 2.  Razões para Aprofundar o Estudo

Falta de modelos preditivos: No Brasil, existem poucos modelos preditivos de AVC. A maioria dos estudos se concentra em identificar fatores de risco, mas não em prever a probabilidade de um evento.
Melhorar a tomada de decisão: Um modelo preditivo preciso pode ajudar os profissionais de saúde a identificar pacientes com alto risco de AVC e tomar medidas preventivas.
Reduzir a carga da doença: A prevenção do AVC pode reduzir significativamente os custos de saúde e a morbidade.

### 3.  Impacto na Sociedade

Um modelo preditivo de AVC preciso pode ter um impacto significativo na sociedade brasileira:

Redução da mortalidade: A detecção precoce e o tratamento do AVC podem reduzir significativamente o número de mortes.
Melhoria da qualidade de vida: A prevenção do AVC pode evitar sequelas graves, como hemiplegia e disfunção cognitiva.
Redução dos custos de saúde: A prevenção do AVC pode reduzir os custos de hospitalização, reabilitação e outros cuidados médicos.

### 4. Quantificação do Impacto

Custo do AVC no Brasil: R$ 12,6 bilhões por ano (https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z).
Redução potencial da mortalidade: 10% a 20% (https://www.emro.who.int/health-topics/stroke-cerebrovascular-accident/index.html).
Redução potencial dos custos de saúde: 10% a 20% (https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z).


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

1 - Quais pesquisas estão sendo desenvolvidas sobre esse tema? 

Mortes por AVC vão disparar nas próximas três décadas (correiobraziliense.com.br): Relatório produzido por comissão de médicos indica que, em três décadas, o número de óbitos aumentará 50% em relação a 2023, principalmente em países de renda média e baixa. Medidas de prevenção e tratamento podem evitar a tendência. 

Modelo de aprendizado de máquina prevê AVC no momento da triagem - TecMundo: De acordo com o estudo, publicado no Journal of Medical Internet Research em fevereiro, o AVC está hoje "entre as condições médicas mal diagnosticadas mais comuns e perigosas". Os erros atingem particularmente pessoas negras, hispânicas, mulheres, idosos em Medicare e pessoas em áreas rurais dos EUA. Isso ocorre porque nem todos os pacientes exibem os sintomas característicos dessa grave condição médica, como problemas de fala, queda facial e fraqueza nos membros. 

Número de internações por AVC aumentou quase 40% em nove anos | Jornal Hoje | G1 (globo.com): Diabetes, hipertensão, obesidade e colesterol alto são alguns dos fatores de risco para o problema. A diabetes é um dos principais fatores de riscos para o AVC. Além dela estão a hipertensão arterial, obesidade, colesterol alto, tabagismo e sedentarismo. 

avc.org.br/sobre-a-sbavc/numeros-do-avc-no-brasil-e-no-mundo: De acordo com outro registro, o portal de Transparência do Registro Civil, mantido pela ARPEN Brasil (Associação Nacional dos Registradores de Pessoas Naturais), o número de óbitos por AVC no Brasil foi de 101.965, em 2019 e 102.812 em 2020, números parecidos com os dados oficiais do SUS, que podem variar um pouco de acordo com a metodologia aplicada nos critérios de busca (CIDs considerados na pesquisa). O AVC, de acordo com este mesmo banco de dados, já matou no ano de 2022, de 1º de janeiro até 13 de outubro, 87.518 brasileiros. O número equivale à média de 12 óbitos por hora, ou 307 vítimas fatais por dia, tornando o AVC novamente a principal causa de morte no país. No mesmo período, o infarto, por exemplo, vitimou 81.987 pessoas, e a Covid-19, 59.165 cidadãos. Portanto, o AVC, que até meados da década de 2010-2015 era a primeira causa de morte no nosso país, passou para o segundo lugar, de forma similar ao que vemos no resto do mundo e em países mais desenvolvidos, e novamente em 2022, embora com dados menos oficiais (SIM x Registro Civil), retoma a posição de primeiro lugar em mortalidade no nosso país. 





2 - Detalhe e contextualize o problema, descreva o dataset utilizado

Dificuldade na Prevenção do AVC
Atualmente, enfrentamos desafios significativos na prevenção do AVC, muitos dos quais estão enraizados em nossos estilos de vida modernos.
A vida sedentária, aliada a problemas de saúde como tabagismo e histórico familiar de AVC, é uma realidade para muitas pessoas. Muitos trabalham em escritórios, passando longas horas sentados, e mantêm uma alimentação pouco saudável.
Segundo a Organização Mundial da Saúde (OMS), o AVC é a segunda principal causa de morte em todo o mundo, sendo responsável por aproximadamente 11% do total de óbitos.
Entre os fatores de risco para o AVC, destacam-se a hipertensão arterial, doenças cardiovasculares, aterosclerose, diabetes mellitus, obesidade, sedentarismo, tabagismo, doenças genéticas de coagulação, idade avançada e histórico prévio de AVC.
É crucial que o público esteja ciente dos sintomas do AVC para reagir rapidamente diante dessa ameaça silenciosa.
Para auxiliar nesse processo de conscientização e prevenção, dados e estudos são fundamentais. Um conjunto de dados útil pode ser encontrado em: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset

3 - Algoritmos utilizados nas pesquisas
Principais pesquisas são:
Prediction of Brain Stroke Severity Using Machine Learning
Algoritmo de árvore de decisão de C4.5 e modelo de rede neural híbrida.
Floresta de decisão bootstrap árvores impulsionadas regressão logística e rede neural profunda.
O algoritmo de aprendizagem supervisionada usa o modelo Naïve Bayes, que depende do teorema de Bayes. “Regressão multilinear” dentre os vários tipos de módulos de regressão linear. A regressão logística enquadra-se na técnica de aprendizagem supervisionada,
Previsão de AVC (SPN)


4 - Identifique as métricas de avaliação empregadas  

A precisão (ACC) é avaliada pelo número de todas as identificações exatas separadas da soma de um número do conjunto de dados.

EX: Precisão =  Verdadeiro Positivo  +  Verdadeiro   Negativo  Verdadeiro Positivo  +  Verdadeiro   Negativo  +  Falso Negativo  +  Falso Positivo 

F1-Score determina quão específico é o classificador e também quão rígido ele pode ser. A proporção de alta precisão e baixa recuperação extrai as possibilidades mais precisas, mas omite vários exemplos que se tornam complexos durante a divisão. A expressão matemática é dada por:

EX:  F1- Pontuação = 2∗11 precisão +1 lembrar 



 5 - Resultados obtidos.


 


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

(Inclua todas as referências (livros, artigos, sites, etc) utilizados no desenvolvimento do trabalho utilizando o padrão ABNT.)

(falta utilizar o apdra ABNT)
https://miro.com/app/board/uXjVNmjzMv4=/#tpicker-content
https://www.correiobraziliense.com.br/ciencia-e-saude/2023/10/5132443-mortes-por-avc-vao-disparar-nas-proximas-tres-decadas.html
https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset
https://1drv.ms/w/s!AkfLoi_fDEzRnQyaP9yUT4npZXtH?e=Jh7vbH
https://vitorborbarodrigues.medium.com/m%C3%A9tricas-de-avalia%C3%A7%C3%A3o-acur%C3%A1cia-precis%C3%A3o-recall-quais-as-diferen%C3%A7as-c8f05e0a513c#:~:text=M%C3%A9tricas%20de%20Avalia%C3%A7%C3%A3o%201%20Acur%C3%A1cia%3A%2

1. MINISTÉRIO DA SAÚDE. AVC. Disponível em: https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/a/avc. Acesso em: 01 mar. 2024.

2. ORGANIZAÇÃO MUNDIAL DA SAÚDE. AVC. Disponível em: https://www.emro.who.int/health-topics/stroke-cerebrovascular-accident/index.html. Acesso em: 01 mar. 2024.

3. SORIANO, F. Stroke Prediction Dataset. Kaggle. Disponível em: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset. Acesso em: 01 mar. 2024.
4.  Fedesoriano. Stroke Prediction Dataset. Kaggle. 2021. https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset

5. Saria, S., et al. "Ethical Considerations in the Use of Machine Learning for Stroke Prediction." Journal of the American Medical Informatics Association 26.10 (2019): 2208-2213. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9279513/
6. Serrano, Amanda. AVC é a segunda causa de mortes no mundo e avança nos países de baixa renda. Estado de Minas [online], Minas Gerais, 02 mar. 2024. Saúde. Disponível em: https://www.em.com.br/app/noticia/bem-viver/2022/04/18/interna_bem_viver,1360730/avc-e-a-segunda-causa-de-mortes-no-mundo-e-avanca-nos-paises-de-baixa-renda.shtml. Acesso em: 02 mar. 2024.





SOBRENOME, Nome. PREVISÃO DA GRAVIDADE DO ACIDENTE VASCULAR CEREBRAL USANDO APRENDIZADO DE MÁQUINA. Nome do j, cidade de publicação (se houver), dia, mês e ano. Seção (caso exista). Disponível em: . Acesso em: dia, mês e ano.

PREVISÂO da gravidade do acidente vascular cerebral usando aprendizado de máuina. IIETA, 2022. Disponível em: https://iieta-org.translate.goog/journals/ria/paper/10.18280/ria.340609?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt-BR&_x_tr_pto=wapp. Acesso em: 04, 03 e 2024.

> **Links Úteis**:
> - [Padrão ABNT PUC Minas](https://portal.pucminas.br/biblioteca/index_padrao.php?pagina=5886)
