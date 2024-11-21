# Usa a imagem base do Python 3
FROM python:3

# Instala o cliente do PostgreSQL
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && apt-get clean

# Define o diretório de trabalho no container
WORKDIR /usr/src/app

# Clona o repositório do GitHub
RUN apt-get install -y git && \
    git clone https://github.com/EduardoBllc/api_jms.git . && \
    apt-get remove -y git && apt-get autoremove -y

# Instala as dependências do projeto
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ARG DESENVOLVIMENTO
ENV DESENVOLVIMENTO=$DESENVOLVIMENTO

# Coleta os estáticos (CSS/JS) do projeto
RUN python manage.py collectstatic --noinput
# Realiza as migrações do banco de dados
RUN python manage.py migrate --noinput

# Welcome to the Django
CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]