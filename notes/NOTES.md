# 📌 NOTES

## AMAZON S3

Serviço de armazenamento de objetos em nuvem.
Armazena e recupera dados a qualquer momento.
Usado em várias aplicações como sites, aplicativos móveis, backups, com modelo de precificação "pague pelo que usa".

Principais Características:

Armazena dados como objetos em "buckets" que são containers de armazenamento.
Permite armazenar uma quantidade praticamente ilimitada de dados.
Projetado para 99,999999999% de durabilidade e 99,9% de disponibilidade, garantindo que os dados estejam acessíveis.
Oferece diversas ferramentas de segurança como gerenciamento de permissões para controlar quem pode acessar os dados.
Tem diferentes classes de armazenamento para diferentes padrões de acesso.
Permite o upload e download de dados através da internet, usando APIs, consoles web ou aplicativos.

## AWS LAMBDA FUNCTION

Serviço de computação sem servidor que executa código em resposta a eventos.
Não necessita de provisionar ou gerenciar servidores.
Escala automaticamente conforme a demanda, cobrando apenas pelo tempo de computação consumido.

Principais Características:

Não é necessário gerenciar servidores, o que reduz a sobrecarga administrativa.
O código é executado em resposta a eventos específicos, o que o torna ideal para sistemas reativos.
O Lambda dimensiona automaticamente a capacidade computacional com base na carga de trabalho recebida garantindo o desempenho consistente.
Paga apenas pelo tempo de computação utilizado, com cobrança zero quando o código não está em execução.
Suporta várias linguagens de programação, como Node.js, Python, Java e Go.
As funções são projetadas para serem "stateless", o que permite um rápido acionamento sem atrasos na configuração.

## AMAZON DYNAMODB
Banco de dados NoSQL totalmente gerenciado com escalabilidade, desempenho e flexibilidade.
Projetado para fornecer armazenamento e recuperação de dados de baixa latência em qualquer escala.
Permite trabalhar com dados não estruturados ou semiestruturado.
Permite a criação de aplicativos altamente escaláveis e confiáveis na nuvem.

Principais Características:

Serverless e totalmente gerenciado  - sem a necessidade de gerenciar infraestrutura, backups, conformidade e monitoramento.
Escalabilidade automática - se ajusta automaticamente à demanda, sem tempo de inatividade, e pode escalar até zero.
Alta performance - desempenho de milissegundos em qualquer escala, com latência consistente inferior a 10 ms.
Modelo de dados flexível - Suporta modelos de dados de chave-valor e documentos.
Tabelas globais - oferecem alta disponibilidade (SLA de 99,999%) e resiliência multirregional.
Alta disponibilidade - projetada para alta disponibilidade e resiliência com opções de consistência de leitura.
Segurança e conformidade - controles de segurança e padrões de conformidade para atender a requisitos específicos.
Integra-se facilmente - com outros serviços da AWS para análises e outras operações.
Flexibilidade de preços - precificação como capacidade sob demanda, que é ideal para padrões de uso imprevisíveis.

## LOCALSTACK

Emulador que permite rodar serviços de nuvem da AWS localmente em sua máquina usando contêineres Docker.
Oferece um ambiente para desenvolver e testar aplicações cloud e serverless sem precisar se conectar à nuvem real da AWS.

Principais Características:

Emulação de serviços - Simula mais de 90 serviços da AWS, como S3, DynamoDB, Lambda, SQS e SNS, em seu ambiente local.
Desenvolvimento offline - Permite trabalhar em projetos de nuvem mesmo sem conexão com a internet.
Aumento de produtividade - Acelera o ciclo de feedback, pois os testes são executados localmente de forma mais rápida.
Ambiente controlado - Possibilita a simulação de cenários sem afetar os ambientes de produção ou teste na nuvem.
Integração - Funciona com ferramentas como o AWS CLI e o Terraform.

## Hand On! Automatizando com Lambda Function

1- Criação de um script com uma função Lambda em Python que dispara o evento.
2- Upload de arquivos no S3 - um arquivo é enviado para o S3, o Lambda processa redimensionando, validando, etc.
3- Alteração na tabela do DynamoDB – Ao receber evento do DynamoDB o lambda salvar cópia em outro banco.
4- Requisições HTTP via API Gateway – Ao receber uma requisição o lambda entrega via API, também pode enviar e-mail ou mensagem no Slack/SNS quando algo acontece.

Observações Importantes:

- O tempo máximo de execução é de 15 minutos.
- A memória configurável é de 128 MB a 10 GB.
- É Ideal para tarefas rápidas não sendo viável para processos longos.
- É ideal para um fluxo básico de uma automação.
