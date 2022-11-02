# yamdb_final
yamdb_final

https://github.com/BogdanOdilov/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg


## Адрес сайта
http://130.193.39.45/redoc/

## Пример запроса
http://130.193.39.45/api/v1/titles/

# Описание
Сайт является - базой отзывов о фильмах, книгах и музыке. Пользователи могут оставлять рецензии на произведения, а также комментировать эти рецензии. Администрация добавляет новые произведения и категории (книга, фильм, музыка и т.д.) Также присутствует файл docker-compose, позволяющий , быстро развернуть контейнер базы данных (PostgreSQL), контейнер проекта django + gunicorn и контейнер nginx

# Как запустить
Необходимое ПО
Docker: https://www.docker.com/get-started
Docker-compose: https://docs.docker.com/compose/install/

# Инструкция по запуску
Для запуска необходимо из корневой папки проекта ввести в консоль команду:

## docker-compose up --build
Затем узнать id контейнера, для этого вводим

## docker container ls
В ответ получаем примерно следующее

REPOSITORY           TAG             IMAGE ID       CREATED         SIZE  
bogdanodilov/infra   latest          5f6dc9f21a35   25 hours ago    175MB 
infra-web            latest          5f6dc9f21a35   25 hours ago    175MB 
<none>               <none>          a64cd1145b91   6 days ago      175MB 
nginx                1.21.3-alpine   513f9a9d8748   13 months ago   22.9MB
postgres             13.0-alpine     700e581c202e   2 years ago     159MB 
Нас интересует контейнер bogdanodilov/infra, заходим в него командой

## docker exec -it <CONTAINER ID> sh
И делаем миграцию БД, и сбор статики

## python manage.py migrate
## python manage.py collectstatic
При желании можно загрузить тестовую бд с контентом

## python manage.py loaddata fixtures.json
Как пользоваться
После запуска проекта, подробную инструкцию можно будет посмотреть по адресу http://0.0.0.0/redoc/

Автор
Богдан Одилов - https://github.com/BogdanOdilov
