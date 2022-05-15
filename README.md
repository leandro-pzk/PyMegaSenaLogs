# PyMegaSenaLogs

Instruções para execução do sistema:

Realizar o donwload dos arquivos deste diretório
Tem a instalação mais recente do docker desktop
docker-compose build
docker-compose up
Caso o banco de dados não tenha sido compilado em tempo de execução, realizar:
docker-compose down e apos conclusão, docker-compose up
Em outro terminal executar: docker-compose exec web sh
python manage.py createsuperuser
python manage.py migrate
Abrir a aplicação em localhost:8001
