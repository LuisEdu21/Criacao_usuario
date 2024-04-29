# Use a imagem base do Python
FROM python:3

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o código-fonte para dentro do contêiner
COPY . /app

# Instale as dependências do projeto
RUN pip install -r requirements.txt

ENV host_db_postgresql = 'host.docker.internal'
ENV name_db_postgresql = 'postgres'
ENV user_postgresql = 'postgres'
ENV password_postgresql = '1234'

# Execute o programa Python quando o contêiner for iniciado
CMD ["python", "main.py"]
