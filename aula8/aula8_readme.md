## Aula 8 - Questões

a) O que acontece se um cliente fizer uma conexão, mas o servidor não chamar accept()? Como o parâmetro backlog passado como argumento na chamada listen() interfere nesse caso?
 
* a conexão é estabelecida com o SO mas não é processada pela aplicação
* O parâmetro backlog controla o número máximo de conexões pendentes

b) O servidor pode detectar o fim de uma conexão por FINISH ou RESET. Qual a diferença entre esses modos?

* FINISH: encerramento via protocolo por 4 mensagens trocadas entre CLIENTE e SERVIDOR
* RESET: não existe mais o canal de comunicação previamente estabelecido

c) O que acontece com a Thread no servidor quando um sensor é encerrado?

* A thread é finalizada pela sinalização via protocolo de RESET ou FINISH

d) Como o monitor separa os dados de sensores diferentes e identifica qual sensor fez a transmissão?

* por meio do ID da conexão 

e) O TCP oferece algum mecanismo para que o cliente saiba que o servidor foi encerrado?

* protocolo FINISH/RESET

f) O que seria necessário para fazer um servidor capaz de atender a múltiplos clientes sem o uso de threads?

* Utilização do paradigma de cooperação
* tornar chamadas de socket não bloqueantes

g) Por que é mais vantajoso que os sensores sejam clientes e o monitor o servidor? Qual seria o problema se o monitor fosse o cliente e cada sensor fosse um servidor?

* TCP fica inviável pois este protocolo não suporta descoberta de endereços
* portanto se o monitor fosse cliente ele não teria como saber os endereços dos sensores.
