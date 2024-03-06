# Introdução

(Texto descritivo introdutório apresentando a visão geral do projeto a ser desenvolvido considerando o contexto em que ele se insere, os objetivos gerais, a justificativa e o público-alvo do projeto.)

O AVC é uma das principais causas de morte e incapacidade no mundo. A previsão precisa do AVC pode ajudar a prevenir eventos futuros e melhorar os resultados dos pacientes. O aprendizado de máquina oferece uma oportunidade promissora para desenvolver modelos de previsão de AVC precisos e eficazes.


# Problema

O Acidente Vascular Cerebral (AVC) é um problema sério que afeta muitas pessoas em todo o mundo. De acordo com uma reportagem do Estado de Minas (https://www.em.com.br/app/noticia/bem-viver/2022/04/18/interna_bem_viver,1360730/avc-e-a-segunda-causa-de-mortes-no-mundo-e-avanca-nos-paises-de-baixa-renda.shtml) a Organização Mundial da Saúde (OMS) cita o AVC como a segunda principal causa de morte no mundo, sendo responsável por cerca de 11% dos óbitos. Essa lesão traz um risco para a vida das vítimas, não só ocasionando mortes mas, também, trazendo incapacidades físicas e mentais em adultos, trazendo grandes impactos para a qualidade de vida e gerando altos custos para os sistemas de saúde. Dessa forma, é crucial que seja estudado as prováveis causas para seu acontecimento de modo a reconhecer padrões e prover prevenções e tratamentos para esse acidente.

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

1 - Quais pesquisas estão sendo desenvolvidas sobre esse tema? 

Diversas pesquisas estão em andamento, como o desenvolvimento de modelos de predição mais precisos, estudos de subgrupos para identificar variações no risco entre diferentes grupos, e aplicações clínicas para personalizar a prevenção e o tratamento do AVC. O objetivo final é melhorar a prevenção, o diagnóstico e o tratamento do AVC, salvando vidas e reduzindo o impacto dessa doença devastadora.

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

1. Ministério da Saúde. (2023). AVC. https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/a/avc
2. Organização Mundial da Saúde. (2023). Acidente vascular cerebral (AVC). https://www.emro.who.int/health-topics/stroke-cerebrovascular-accident/index.html
3. Serrano, Amanda. AVC é a segunda causa de mortes no mundo e avança nos países de baixa renda. Estado de Minas, Belo Horizonte, MG, 18 abr. 2022. Saúde. Disponível em: https://www.em.com.br/app/noticia/bem-viver/2022/04/18/interna_bem_viver,1360730/avc-e-a-segunda-causa-de-mortes-no-mundo-e-avanca-nos-paises-de-baixa-renda.shtml.
4. Correio Braziliense. Mortes por AVC vão disparar nas próximas três décadas. Correio Braziliense, Brasília, DF, 24 out. 2023. Disponível em: https://www.correiobraziliense.com.br/ciencia-e-saude/2023/10/5132443-mortes-por-avc-vao-disparar-nas-proximas-tres-decadas.html.





SOBRENOME, Nome. PREVISÃO DA GRAVIDADE DO ACIDENTE VASCULAR CEREBRAL USANDO APRENDIZADO DE MÁQUINA. Nome do j, cidade de publicação (se houver), dia, mês e ano. Seção (caso exista). Disponível em: . Acesso em: dia, mês e ano.

PREVISÂO da gravidade do acidente vascular cerebral usando aprendizado de máuina. IIETA, 2022. Disponível em: https://iieta.org/journals/ria/paper/10.18280/ria.340609. Acesso em: 04, 03 e 2024.

> **Links Úteis**:
> - [Padrão
> - ABNT PUC Minas](https://portal.pucminas.br/biblioteca/index_padrao.php?pagina=5886)
