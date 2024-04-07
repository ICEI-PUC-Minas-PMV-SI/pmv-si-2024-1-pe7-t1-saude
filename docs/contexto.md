# Introdução

O AVC é uma das principais causas de morte e incapacidade no mundo. A previsão precisa do AVC pode ajudar a prevenir eventos futuros e melhorar os resultados dos pacientes. O aprendizado de máquina oferece uma oportunidade promissora para desenvolver modelos de previsão de AVC precisos e eficazes.

# Problema

O Acidente Vascular Cerebral (AVC) é um problema sério que afeta muitas pessoas em todo o mundo. De acordo com uma reportagem do Estado de Minas a Organização Mundial da Saúde (OMS) cita o AVC como a segunda principal causa de morte no mundo, sendo responsável por cerca de 11% dos óbitos (SERRANO, 2022). Essa lesão traz um risco para a vida das vítimas, não só ocasionando mortes mas, também, trazendo incapacidades físicas e mentais em adultos, trazendo grandes impactos para a qualidade de vida e gerando altos custos para os sistemas de saúde. Dessa forma, é crucial que seja estudado as prováveis causas para seu acontecimento de modo a reconhecer padrões e prover prevenções e tratamentos para esse acidente.

# Questão de pesquisa

É possível estimar a probabilidade de um indivíduo sofrer um AVC com base em fatores de risco como idade, sexo, histórico familiar, tabagismo, doenças cardíacas, hipertensão, etc...?

## Objetivos preliminares

A finalidade do trabalho é auxiliar a identificar pessoas que se encontram em grupo de risco para AVC. 

Para isso, será realizado um estudo na área e, a partir dos dados coletados, será treinado um modelo de Machine Learning que seja capaz de estimar com confiabilidade alta alta se uma pessoa se encontra nesse grupo a partir de certos atributos históricos.

A partir desse objetivo, será disponibilizado para os clientes da clínica Saúde+ uma série de recomendações caso se encontre em tal grupo de risco, como dicas de dieta, sintomas de um possível derrame, lista dos médicos cadastrados especializados na área, etc...


# Justificativa

O Acidente Vascular Cerebral (AVC) é um problema de saúde pública global com alta morbidade e mortalidade. Segundo a Sociedade Brasileira de Doenças Cerebrovasculares (SBDCV), o AVC é a principal causa de morte no Brasil, vitimando cerca de 130 mil pessoas por ano.

Estudos demonstram que a falta de educação de qualidade pode influenciar no risco de AVC. Pessoas com menor nível de escolaridade apresentam maior risco de AVC. Segundo pesquisa publicada na revista Stroke¹, o risco de AVC é 22% maior em pessoas com menos de 8 anos de estudo em comparação com aquelas com 12 anos ou mais. Fatores socioeconômicos desfavoráveis, como baixa renda e falta de acesso à educação, estão associados a um maior risco de AVC. Um estudo publicado na revista PLOS Medicine² verificou que a privação socioeconômica está associada a um aumento de 25% no risco de AVC.

No Brasil, as escolas públicas apresentam um desempenho inferior às escolas privadas em diversos indicadores, como taxas de aprovação e proficiência em português e matemática.

O dataset de Previsão de AVC visa desenvolver modelos preditivos para identificar pessoas com alto risco de AVC e contribuir para a prevenção do AVC no Brasil, especialmente em populações com menor nível de escolaridade.

A solução proposta pode trazer diversos benefícios, como a redução do número de AVCs no Brasil, melhoria da qualidade de vida das pessoas que sofreram AVC e redução dos custos com tratamento e reabilitação de AVC.


# Público-Alvo

O nosso público-alvo é direcionado a uma ampla gama de profissionais de saúde, pesquisadores médicos, cientistas de dados e formuladores de políticas públicas. A fim de identificar as necessidades, interesses e preocupações de cada grupo envolvido e desenvolver estratégias de engajamento e comunicação adequadas para colaboração eficaz no uso de conjuntos de dados de previsão de AVC. Aqui estão algumas personas dentro desse público:

Profissionais de Saúde:
Médicos: Especialistas em neurologia, cardiologia, medicina interna, etc.
Enfermeiros: Especializados em cuidados intensivos, reabilitação, etc.
Terapeutas: Fisioterapeutas, terapeutas ocupacionais, etc.

Pesquisadores Médicos:
Acadêmicos: Professores universitários, pesquisadores clínicos, etc.
Institutos de Pesquisa: Centros de pesquisa médica, laboratórios especializados, etc.
Organizações Sem Fins Lucrativos: Fundações de pesquisa médica, organizações de caridade, etc.

Cientistas de Dados:
Analistas de Dados: Especialistas em análise estatística e modelagem.
Engenheiros de Machine Learning: Desenvolvedores de algoritmos de previsão e aprendizado de máquina.
Especialistas em Visualização de Dados: Designers de interfaces de usuário e especialistas em visualização de dados.

Formuladores de Políticas Públicas:
Governamentais: Ministérios da Saúde, agências reguladoras, etc.
Organizações Internacionais: OMS, Banco Mundial, etc.
Organizações Não Governamentais: Grupos de advocacia de saúde, grupos de defesa dos pacientes, etc.

Pacientes e Cuidadores:
Indivíduos afetados por AVC e seus familiares.
Grupos de Apoio: Organizações de apoio a pacientes com AVC, fóruns online, etc.

Indústria e Parceiros Comerciais:
Empresas Farmacêuticas: Desenvolvedores de medicamentos e dispositivos médicos.
Empresas de Tecnologia: Fabricantes de dispositivos médicos, empresas de software de saúde, etc.
Seguradoras de Saúde: Prestadores de serviços de saúde e seguros médicos.

Educadores e Acadêmicos:
Instituições de Ensino: Universidades, escolas de medicina, etc.
Professores e Pesquisadores: Educadores envolvidos no treinamento de profissionais de saúde e pesquisadores médicos.

Esses são alguns dos grupos que representam uma variedade de interesses e aplicações para conjuntos de dados de previsão de AVC, desde o diagnóstico e tratamento até a prevenção e políticas de saúde pública.

## Estado da arte

Pesquisa 1: Machine Learning and the Conundrum of Stroke Risk Prediction
Pesquisas em Desenvolvimento:Chahine, Magoon, Álamo, Boyle & Akoum (2023) conduziram um estudo sobre o uso de técnicas de aprendizado de máquina (ML) para prever o risco de AVC. Eles compararam diferentes algoritmos de ML, como SVM, RF, GBT e multilayer perceptron, usando dados de uma grande coorte chinesa.Essa pesquisa visa aprimorar a previsão de risco de AVC, explorando associações estatísticas complexas e ocultas entre variáveis clínicas, fisiológicas e resultados de interesse.
Os escores de risco tradicionais para AVC dependem de características clínicas e comorbidades do paciente, mas métodos de ML podem oferecer uma avaliação mais precisa, combinando uma variedade de recursos.
Algoritmos de ML, como SVM, RF, GBT, entre outros, são comumente utilizados em pesquisas clínicas para encontrar características mais relevantes para a previsão de AVC.
O dataset utilizado inclui características e dados demográficos dos pacientes, biomarcadores sanguíneos e dados de imagem, fornecendo uma base para a previsão do risco de AVC.
Os estudos examinaram dados de pacientes com fibrilação atrial (FA), destacando a importância da carga de arritmia na predição do risco de AVC, com algoritmos de ML mostrando melhorias na predição em comparação com escores tradicionais.

Os pesquisadores compararam diferentes algoritmos de ML, como SVM, RF, GBT, redes neurais, entre outros, com métodos convencionais de previsão de risco de AVC.
Identificaram o modelo de floresta aleatória (RF) como o mais preditivo entre nove modelos testados em uma população multirracial inicialmente assintomática.
Essa pesquisa destaca a promessa do aprendizado de máquina na previsão do risco de AVC, mostrando avanços significativos em comparação com métodos convencionais.

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


Pesquisa 2: Prediction of Brain Stroke Severity Using Machine Learning

A pesquisa examina o uso de técnicas de aprendizado de máquina (ML) para a prevenção de acidente vascular cerebral (AVC), destacando várias áreas de pesquisa em andamento e os resultados obtidos. Aqui está um resumo das principais conclusões:
Pesquisas em Andamento: Diversas pesquisas estão em andamento, incluindo o desenvolvimento de modelos de predição mais precisos, estudos de subgrupos para identificar variações no risco entre diferentes grupos e aplicações clínicas para personalizar a prevenção e o tratamento do AVC.
Contextualização do Problema e Dataset Utilizado: A pesquisa aborda a importância do ML na previsão de AVC, destacando áreas como identificação de fatores de risco, diagnóstico precoce, previsão de recorrência, desenvolvimento de sistemas de monitoramento remoto e personalização do tratamento. O dataset utilizado inclui informações demográficas, resultados de testes físicos, histórico médico, dados de monitoramento durante o exercício e resultados de acompanhamento ao longo do tempo.
Algoritmos Utilizados: Os pesquisadores utilizaram uma variedade de algoritmos de ML, incluindo árvore de decisão, rede neural híbrida, florestas de decisão bootstrap, regressão logística, modelo Naïve Bayes, regressão multilinear, redes neurais artificiais (RNAs), SVM e redes neurais recorrentes (RNN).
Tabela 1. Resumo do conjunto de dados do artigo de Bandi et. Al (2020)
| Atributo | Mínimo | Máximo | Significar | Desvio padrão |
| :---: | :---: | :---: | :---: | ---: | 
| Idade  | 1 | 90 | 47.12 | 23.69 |
| NIHSS | 0 | 45 |  18.12 | 11.27 |
| Sra  | -1 | 6 | 3.67 | 1.87 |
| PA sistólica | 100 | 195 | 153.09 | 24.92 |
| PA diastólica | 59 | 135 | 103.65 | 18.34 |
| Glicose  | 70 | 295 | 225.85 | 56.11 |
| Paralisia | 0 | 3 | 1.36 | 1.106 |
| Tabagismo | 0 | 3 | 0.88 | 0.9 |
| IMC | 18  | 45 | 33.73 | 6.23 |
| Colesterol | 160 | 253 | 217.53 | 20.26 |

•	Variáveis demográficas dos participantes (idade, gênero, altura, peso, etc.).
•	Resultados de testes físicos (pressão arterial, frequência cardíaca em repouso, capacidade aeróbica, etc.).
•	Histórico médico dos participantes (presença de condições médicas pré-existentes, uso de medicamentos, etc.).
•	Dados de monitoramento durante o exercício (duração, intensidade, tipo de exercício, etc.).
•	Resultados de acompanhamento ao longo do tempo (alterações na pressão arterial, frequência cardíaca máxima alcançada, melhora na capacidade aeróbica, etc.).
Métricas de Avaliação Empregadas: Foram utilizadas várias métricas de avaliação, incluindo precisão (ACC), sensibilidade, especificidade, taxa de falso positivo, F1-Score e área sob a curva ROC (ROC-AUC), entre outras.
Resultados Obtidos: Os resultados indicam uma eficácia significativa na previsão de AVC usando modelos de ML, com uma precisão de 96,97% alcançada com uma técnica de conjunto Random Forest. Isso sugere um potencial promissor para melhorar a detecção precoce, o tratamento e a prevenção do AVC.
No geral, a pesquisa destaca a importância do ML na área da saúde, especificamente na prevenção de AVC, e demonstra resultados promissores que podem ter um impacto significativo na saúde pública.


Pesquisa 3: Stroke prediction through Data Science and Machine Learning Algorithms
Pesquisas em Andamento: A pesquisa de Rodriguez (2021) Stroke prediction through Data Science and Machine Learning Algorithms tem como objetivo criar um modelo preciso para prever o resultado do AVC com ciência de dados e aprendizado de máquina (ML) com base em dados anteriores e características individuais e fornecer informações úteis para a equipe médica implantar o tratamento necessário e diminuir riscos e consequências.
Para Rodriguez (2021) é difícil interpretar os padrões ou extrair informações úteis dos dados pois entende que seja devido à quantidade de informações serem pouco perceptível e é onde as técnicas de ML são muito úteis para ensinar, como o próprio nome indica, máquinas a lidar com dados de forma mais eficiente.
O dataset utilizado foi HealthData.gov, Liu, Fan & WU (2019). A hybrid machine learning approach to cerebral stroke prediction based on imbalanced medical-datasets [RAR]. Mendley. Data for: A hybrid machine learning approach to cerebral stroke prediction based on imbalanced medical-datasets - Mendeley Data, que também é utilizado como conjunto de dados de referência em uma competição de Kaggle2. .
Nele inclui informações sobre 5.110 indivíduos caracterizados por 10 características e inclui informações sobre a variável alvo que é o AVC para todos eles, isso permite uma abordagem de aprendizagem supervisionada e é a mais frequente utilizada. O objetivo é montar um modelo conciso da distribuição de rótulos de classes em termos de características preditoras e depois é usado para atribuir rótulos de classe às instancias de teste.
O dataset original tinha 201 valores ausentes para IMC. Mais de 30 % tinha o status desconhecido para tabagismo, demonstrando falta de informação assim utilizaram a idade de 18 ou menos para nunca.
Algoritmos Utilizados: Algoritmos, métricas e resultados de Rodriguez (2021) foram:
A precisão do modelo de Arvore de decisão foi 0,9011. De regressão logística 0,8059. Baías ingênuas 0,7907 e Classificador de vizinhos K 0,8790. O Floresta aleatória obteve precisão de 0,9232 de rede neural 0,82. Máquinas e vetores de suporte 0,822 e por fim Classificador XGBoost 0,91
Segundo a pesquisa de Rodriguez (2021) Random Forest foi o algoritmo de ML de melhor desempenho para este problema específico, seguido por XGBoost e Decision Tree em termos de precisão do modelo.
AUC de 0,975 no Random Forest e uma AUC de 0,500 para Random prediction. Na Curva Receiver Operating Characteristic (ROC) quando maior a AUC, melhor o modelo de classificação correta das instancias.
Foi utilizado a técnica SMOTE para equilibrar o conjunto de dados para melhorar o desempenho dos modelos de ML.
Resultados Obtidos: Nesta pesquisa Rodriguez (2021) provou que através da CIencia de dados e do uso de algoriticmo de Aprendizagem de máquina , é possível prever or esultado do AVC e que a metodologia CRISPI-DM ajuda na orientação da análise dos dados, tornando mais simples e efeicaz.

Pesquisa 4: Aprendizado de máquina para acidente vascular cerebral: uma revisão – ScienceDirect
A pesquisa revisa o uso de aprendizado de máquina (ML) e deep learning para o tratamento do acidente vascular cerebral (AVC), classificando as técnicas em quatro categorias e revisando sistematicamente estudos em cada categoria. Aqui está uma análise mais aprofundada:
Pesquisas em Andamento: A aplicação de ML e deep learning na saúde está crescendo, com um foco crescente no AVC devido à sua alta taxa de mortalidade e a necessidade de detecção precoce. A revisão identificou 39 estudos sobre ML para AVC, abrangendo os anos de 2007 a 2019.
Contextualização do Problema e Dataset Utilizado: O AVC é um grande desafio de saúde, e o ML tem sido reconhecido como uma ferramenta promissora para ajudar na detecção precoce e no tratamento. Os estudos revisados foram obtidos da base de dados científica ScienceDirect e abordaram diferentes aspectos do AVC, incluindo prevenção, diagnóstico, tratamento e prognóstico.
Algoritmos Utilizados: Os estudos revisados utilizaram uma variedade de algoritmos de ML, com foco em aprendizado supervisionado, não supervisionado e profundo. Esses algoritmos têm a capacidade de aprender e melhorar a partir de dados passados sem serem explicitamente programados, permitindo análises complexas de conjuntos de dados relacionados ao AVC.
Métricas de Avaliação Empregadas: Os estudos empregaram diferentes métricas de desempenho para avaliar a eficácia das técnicas de ML, incluindo acurácia, sensibilidade, especificidade, F1-Score e área sob a curva ROC. No entanto, a comparação entre estudos foi dificultada pela variedade de métricas utilizadas e pela heterogeneidade dos conjuntos de dados e técnicas empregadas.
Resultados Obtidos: Os estudos revisados abordaram diversas áreas de pesquisa relacionadas ao AVC, incluindo prevenção, diagnóstico, tratamento e prognóstico. Embora seja difícil comparar diretamente os resultados devido às diferenças nos métodos e métricas de avaliação, alguns estudos relataram maior acurácia na classificação em determinadas áreas, como prevenção e diagnóstico.
No geral, a pesquisa destaca o potencial do ML e deep learning para melhorar o entendimento, detecção e tratamento do AVC, mas também ressalta a necessidade de padronização nas métricas de avaliação e maior colaboração entre os pesquisadores para avançar nessa área.


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

![Canvas-analitico](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/docs/img/Canvas_analitico_v2.png)

# Conclusões

O desenvolvimento de um modelo preditivo de AVC preciso pode ter um impacto significativo na saúde pública brasileira. Este estudo visa contribuir para esse objetivo, fornecendo um modelo que possa ser utilizado por profissionais de saúde para identificar pacientes com alto risco de AVC e tomar medidas preventivas.

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

# Referências

1. MINISTÉRIO DA SAÚDE. AVC. Brasília: Ministério da Saúde, 2023. Disponível em: https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/a/avc .
2. ORGANIZAÇÃO MUNDIAL DA SAÚDE. Acidente vascular cerebral (AVC). Cairo: Organização Mundial da Saúde, 2023. Disponível em: https://www.emro.who.int/health-topics/stroke-cerebrovascular-accident/index.html.
3. SERRANO, AMANDA. AVC é a segunda causa de mortes no mundo e avança nos países de baixa renda. Estado de Minas, Belo Horizonte, MG, 18 abr. 2022. Saúde. Disponível em: https://www.em.com.br/app/noticia/bem-viver/2022/04/18/interna_bem_viver,1360730/avc-e-a-segunda-causa-de-mortes-no-mundo-e-avanca-nos-paises-de-baixa-renda.shtml.
4. CORREIO BRAZILIENSE. Mortes por AVC vão disparar nas próximas três décadas. Correio Braziliense, Brasília, DF, 24 out. 2023. Disponível em: https://www.correiobraziliense.com.br/ciencia-e-saude/2023/10/5132443-mortes-por-avc-vao-disparar-nas-proximas-tres-decadas.html.
5. Rev.,Arrhythm Eletrofisiol (2023), CHAHINE, MAGOON, MAIDU, ÁLAMO, & AkOUM (2023). Machine Learning and the Conundrum of Stroke Risk Prediction, NIH- National Library of Medicine, DOI: 10.15420/aer.2022.34, EUA, v.12, e07, out/2022. Disponível em: Machine Learning e o enigma da previsão de risco de AVC - PMC (nih.gov). Acesso em: 08, 03 e 2024.

6. BANDI, BHATTACHARYYA & MIDHUNCHKKRAVARTHY (2020). Prediction of Brain Stroke Severity Using Machine Learning. IIETA, DOI: https://doi.org/10 18280/ria.340609, Vol. 34, página 1.Disponível em: https://iieta.org/journals/ria/paper/10.18280/ria.340609. Acesso em: 08, 03 e 2024.
7. RODRIGUEZ (2021). Stroke prediction through Data Science and Machine Learning Algorithms. School of Engineering and Sciences Tecnológico de Monterrey Monterrey. DOI: 10.13140/RG.2.2.33027.43040, Monterrei México. Disponível em: https://www.researchgate.net/publication/352261064. 
8. PREVISÂO da gravidade do acidente vascular cerebral usando aprendizado de máuina. IIETA, 2022. Disponível em: https://iieta.org/journals/ria/paper/10.18280/ria.340609. Acesso em: 04, 03 e 2024. Acesso em: 08, 03 e 2024.
9.  PLOS MEDICINE. Disponível em: https://www.scielo.br/j/anp/a/jwY83PBY8VqGVLDhgZymxbT/?lang=pt&format=pdf
10.  IDEB 2019. Disponível em: https://undime.org.br/noticia/15-09-2020-15-37-ideb-2019-resultados-foram-divulgados-nesta-terca-feira-15
11. PROVA BRASIL 2019. Disponível em: https://undime.org.br/noticia/16-09-2020-09-24-inep-divulga-resultados-do-saeb-2019
12. SOCIEDADE BRASILEIRA DE CARDIOLOGIA. Disponível em: http://publicacoes.cardiol.br/portal/abc/portugues/aop/2019/aop-diretriz-prevencao-cardiovascular-portugues.pdf
13. DIRETRIZES DE ATENÇÃO E REABILITAÇÃO AO ACIDENTE VASCULAR CEREBRAL. Disponível em: https://bvsms.saude.gov.br/bvs/publicacoes/diretrizes_atencao_reabilitacao_acidente_vascular_cerebral.pdf
14. SISTEMAS DE INFORMAÇÕES DE MORTALIDADE - SIM. Disponível em: http://tabnet.saude.sp.gov.br/deftohtm.exe?tabnet/ind43_matriz.def

