FROM python:3.8

# Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /myhello/

WORKDIR /myhello/

COPY . /myhello/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
