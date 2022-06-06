# TDE 2 

Marcio Vinicius de Souza da Rocha 

## Pergunta 1

```
$ id marcio
uid=1000(marcio) gid=1000(marcio) grupos=1000(marcio),998(wheel)
```

O usuário em questão pertence aos grupos **marcio** e **wheel**, neste caso o grupo **wheel** é o grupo de administradores, portanto o usuário *marcio* é administrador do sistema.

## Pergunta 2

### conteúdo do arquivo teste.sh 

```
#!/bin/bash
echo "Bem vindo!"
```

### Permissões do arquivo 

```
$ ls -l teste.sh
-rw-r--r-- 1 marcio marcio 30 jun  6 18:41 teste.sh
```
O arquivo possui somente as permissões de escrita e leitura, respectivamente **r** & **w**. 

Dessa maneira não é possível executar o script, e ao tentar exectutálo aparece a mensagem de permissão negada.

```
$ chmod u=rwx,g=rw,o=r teste.sh
```

após executar o comando para alterar as pemissões do arquivo é possível executar o mesmo.

```
$ ls -l
-rwxrw-r-- 1 marcio marcio 30 jun  6 18:41 teste.sh
```
## Pergunta 3

```
convidado$ cat teste.sh
#!/bin/bash
echo "Bem vindo!"
convidado$ ./teste.sh
bash: ./teste.sh: Permissão negada
convidado$ rm teste.sh
rm: não foi posível remover 'teste.sh': Permissão negada
convidado$ mv teste.sh teste2.sh
mv: não foi possível mover 'teste.sh' para 'teste2.sh': Permissão negada
convidado$ cp teste.sh ~/teste2.sh
convidado$ 
```
* Ler o arquivo: é possível ler o arquivo, pois ele tem permissão de leitura **r**
* Executar o arquivo: não é possível pois não tem permissão de execução **w** para o usuário *convidado*
* Apagar o arquivo: não é possível pois o usuário não tem permissão de escrita **w**
* Renomear o arquivo: não é possível pois o usuário não tem permissão de escrita **w**
* Copiar o arquivo para $HOME: é possível pois o usuário tem permissão de leitura do arquivo

## Pergunta 4

```
$ id convidado
uid=1001(convidado) gid=1001(convidado) grupos=1001(convidado),1000(marcio)
$ ls -l 
total 16
drwxr-xr-x 4 marcio marcio 4096 jun  6 19:24 .
drwxr-xr-x 3 marcio marcio 4096 jun  6 19:37 ..
drwxr--r-- 2 marcio marcio 4096 jun  6 19:24 privado
drwxrwxr-x 2 marcio marcio 4096 jun  6 19:24 publico
```

1. É possível copiar o arquivo pois o usuário *convidado* tem permissão
2. Não é possível copiar o arquivo pois o usuário *convidado* não tem permissão
3. Não é possível acessar a pasta pois o usuário *convidado* não tem permissão
4. É possível executar o script pois o usuário *convidado* tem permissão

