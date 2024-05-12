FROM python:3.11.9 
#versão do py


WORKDIR /app
#define o diretório


COPY . /app
#copia tudo do diretório onde executo o "docker build" para o diretório app


COPY start.sh /app
#copia tudo do diretório start.sh para o app (aq se incia a aplicação)


RUN pip install --no-cache-dir -r dependencias.txt
#instala os pacotes indicados em dependencias.txt // --no-cache-dir: instrui o pip a não usar o cache durante a instalação, o que pode ajudar a evitar problemas de cache desatualizado


ENV POSTGRES_PORT=5433
#config da porta no postgres


CMD ["python", "app/app.py"]
#define o comando padrão a ser executado na incialização do container (executa todo app.py do diretório app)