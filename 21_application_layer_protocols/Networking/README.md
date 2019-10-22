# Тесты бэкенд с использованием SSH клиента 

```
Добавить тесты, использующие SSH клиент для реализации следующих сценариев: 
перезагрузка сервера opencart с последующей проверкой, что opencart доступен, 
рестарт сервиса для opencart с последующей проверкой, что сервис доступен.
```


### How to use:
* Запустите docker image `bitnami/opencart:3` с перенаправлением портом:
```sh
~ docker run -p 4422:22 -p 8443:443 -p 8080:80 -d bitnami/opencart:3
```
* Посмотрите список запущенных контейнеров:
```sh
~ docker ps
```
* Подключитесь к контейнеру:
```sh
~ docker exec -it {CONTAINER_ID} sh
```
* Выполните следующие команды в контейнере:
```sh
~ apt-get update
~ apt-get upgrade
~ apt-get install openssh-server nmap nano
```
* Вам нужно установить пароль для учетной записи `root`:
```sh
~ sudo passwd
```
* Введите один и тот же пароль дважды:
* Вам также нужно отредактировать `sshd_config` и изменить следующую строку:
```sh
~ nano /etc/ssh/sshd_config

... 
PermitRootLogin without-password -> PermitRootLogin yes
...
```
* Необходимо сгенерировать SSH-ключ на локальной компьютере:
```sh
~ ssh-keygen
```
```
ssh-keygen - утилита для генерации публичного и приватного ключей. 
Приватный ключ никогда нельзя никому показывать. 
Ключи всегда должны быть защищены паролем.
```
* Необходимо сгенерировать SSH-ключ в контейнере:
```sh
~ ssh-keygen
```
* Чтобы авторизоваться на сервере по ключу выполните команду:
```sh
~ ssh-copy-id user@server
```
* Если у вас не получилось выполните команду выше, то скопируйте свой публичный
ключ с локальной машины и добавьте его в контейнере:
```sh
~ cat ~/.ssh/id_rsa.pub
~ nano ~/.ssh/authorized_keys
```
* Затем сделайте рестарт службы SSH:
```sh
~ service ssh restart
```
* Теперь вы можете подключиться с локальной машины в контейнер:
```sh
~ ssh root@localhost -p 4422
```