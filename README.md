# EricOtofuji_LucasBorges_EP3
EP3 Design de Software
Projeto acadêmico do curso de engenharia do Insper - Instituto de Ensino e Pesquisa, como projeto intermediário (Exercício Problema de número 3) da disciplina de Design de Software
Professor orientador: Luciano P. Soares

Descrição do projeto original: 

Rua Quatá, 300 – Vila Olímpia 04546-042 São Paulo SP Brasil
55 11 45042400 www.insper.edu.br
Exercício Programa 3 – Design de Software 2015.1
Controle de Dieta
Descrição:
Neste projeto você terá de desenvolver uma aplicação para o controle da dieta semanal de uma pessoa usando os recursos de programação Python.
Integrantes
Este projeto é para ser realizado em duplas, você deverá encontrar alguém da sua turma para desenvolver esse projeto em conjunto. Se organizem para tentar desenvolver o projeto de forma que ambos aprendam o máximo possível. Aproveitem a oportunidade para praticar pair-programming.
Você pode conversar com os outros colegas a respeito do projeto mas não pode aceitar código pronto, o projeto é rigorosamente individual. Entregas muito parecidas receberão o conceito Insatisfatório.
Nome do repositório
Crie um repositório Git e nomeie-o com os nomes e sobrenomes da sua dupla e em seguida a string _EP3. Por exemplo se a dupla fosse o Fabio Miranda e o Luciano Soares o repositório deveria ser:
FabioMiranda_LucianoSoares_EP3
Evolução do projeto
Para esse projeto você deve entregar junto um flow chart que deverá esta no repositório Git. Você pode fazê-lo eletronicamente ou usar uma foto de um papel que você desenhou, mas ele deve estar de forma clara no repositório.
Rua Quatá, 300 – Vila Olímpia 04546-042 São Paulo SP Brasil
55 11 45042400 www.insper.edu.br
Você também deve testar o seu código usando rotinas automáticas de teste.
Para isso você pode usar o sistema de doctest. Verifique antes de entregar se
seus testes estão válidos, entrega de códigos com testes falhando é algo
grave. Mais informações em: https://docs.python.org/3.4/library/doctest.html
O código também deve estar modularizado juntando funções semelhantes em
arquivos Python separados. Organize seus arquivos da melhor forma possível
para você e outros conseguirem entender e modificar.
Seu repositório Git continua precisando mostrar os passos que vocês
seguiram para realizar o projeto, porém dessa vez o projeto é em dupla então
os dois integrantes devem estar no projeto e ficar claro pelos commits que
ambos contribuíram para o desenvolvimento. Assim procure fazer commits a
cada alteração relevante que fizer e publishes periódicos, também alterne os
computadores usados para o desenvolvimento.
Orientações
Desenvolva o projeto com o Python 3 e suas bibliotecas.
O programa deve carregar o arquivo fornecido pelo professor (alimentos.csv)
com uma tabela dos principais alimentos. Esse arquivo descreve na primeira
linha e os campos separado por vírgulas (CSV).
Nesse projeto o usuário deverá ser capaz de entrar com um arquivo passando
as suas informações básicas de nome, idade(anos), peso (kg), sexo (M,F),
altura (m) e fator de atividade física (mínimo, baixo, médio, alto, muito
ativo), além dos alimentos consumidos nos vários dias (não necessariamente
em ordem cronológica). Para isso use o modelo fornecido (usuário.csv). O
programa deverá calcular a quantidade diária de calorias usando a fórmula de
Harris-Benedict (http://fitseven.com.br/homens-depois-dos-30/vitaminas-enaturais/
necessidades-de-calorias-diarias).
Rua Quatá, 300 – Vila Olímpia 04546-042 São Paulo SP Brasil
55 11 45042400 www.insper.edu.br
O programa deverá exibir um gráfico mostrando a quantidade diária recomendada de calorias e a quantidade consumida de calorias, proteínas, carboidratos e gorduras, por dia. Para isso use alguma biblioteca para plotar gráficos como a matplotlib ou bokeh (não use o Excel para isso).
Ao final o programa deverá gerar um arquivo texto com o índice de massa corporal pela fórmula de Nick Trefethen, indicando se a pessoa está magra, saudável ou obesa, e as quantidade a mais ou a menos de calorias consumidas a cada dia.
Entrega:
A entrega é novamente em um repositório do Github indicado por você via Blackboard.
O prazo final é 17/04
Apresentações:
Alguns grupos terão oportunidade de apresentar e explicar seus projetos em um design review na aula consecutiva à entrega do projeto. A definição será por sorteio, não será necessário preparar slides mas todos devem estar aptos a apresentar.
Observações:
Este projeto não tem como objetivo os alunos criarem um programa preciso para os usuários, pois isso envolveria consultar profissionais da saúde e potenciais usuários, porém qualquer um interessado em aprofundar o funcionamento do sistema terá o apoio dos professores da disciplina para isso.
Tópicos extra:
Rua Quatá, 300 – Vila Olímpia 04546-042 São Paulo SP Brasil
55 11 45042400 www.insper.edu.br
Sugestões para quem quiser ir além:
 Proponha uma dieta para o usuário em função das suas características.
 Subdivida pelas alimentações do dia (café da manhã, almoço e jantar)
 Calcule o ganho ou perda estimados de massa – descubra como.
