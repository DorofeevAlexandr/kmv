# kmv
Контроль машинного времени для кабельного завода.

Функции программы:
 - Чтение метража со счетчиков Си-30 по интерфейсу rs-485
 - Запись метража в csv файл
 - Вывод графиков работы производственных линий на экран
 - Расчет и вывод статистики на экран
 - Администрирование системы


------------------------------------------------
Для автоматической загрузки ПК при подаче напряжения в Bios нужно изменить следующий параметр:

Advanced -> IT8784 Super IO Configuration -> Restore on AC Power Loss := Power On

 
Для установкми Watchdog таймера нужно изменить следующие параметры:

Advanced -> IT8784 Super IO Configuration -> Watchdog Controller := Minute mode

...->Watchdog timer value input := 255

----------------------------------------------
Разворачивание проекта на сервере
1 ...клонировать проект из Github.
2 Создать виртуальное окружение и установить зависимости.

3 Поочередно запустить скрипты
create_db.py
create_admin.pycreate_and_init_default_lines.py create_data_trends.py 


3 Пробно запустить проект 
./run.sh

4 Установить вебсервер gunicorn
pip install gunicorn




2 Установить - supervisord 
apt-get install supervisor

Чтобы supervisord стал запускать наш проект, напишем конфигурационный файл. 
supervisor хранит их в папке /etc/supervisor/conf.d/
---------------

[program:kmv]
command=/home/amd/venv/bin/gunicorn --bind=0.0.0.0:5000 wsgi:app
directory=/home/amd/kmv/
autostart=true
autorestart=true
redirect_stderr=true

[program:kmv-celery]
command=/home/amd/venv/bin/celery -A tasks worker --loglevel=INFO
directory=/home/amd/kmv/
autostart=true
autorestart=true
redirect_stderr=true

[program:kmv-celery-beat]
command=/home/amd/venv/bin/celery -A tasks beat
directory=/home/amd/kmv/
autostart=true
autorestart=true
redirect_stderr=true

--------------

Сначала зарегистрируем новый конфиг с помощью команды 
supervisorctl reread

Чтобы supervisord запустил сервис в соответствии с нашим конфигом используем команду 
supervisorctl update

Убедимся, что наш сервис запустился 
supervisorctl status



===============================================================
The tty devices belong to the "dialout" group, I suspect you are not a member of this group and hence are denied access to /dev/ttyS0, so you need to add yourself to that group.
First check if you are a member of that group:
groups ${USER}
..this will list all the groups you belong to. If you don't belong to the dialout grup then add yourself to it, for example:
sudo gpasswd --add ${USER} dialout


==================================================================
