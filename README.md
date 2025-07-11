# FruitKafkaFlow

Um pipeline simples end-to-end usando Kafka, Python e Kafka UI para simular vendas de frutas, detectar compras suspeitas e visualizar dados em tempo real.

---

## O que esse projeto faz?

- **Produz mensagens Kafka** simulando vendas de frutas com dados como quantidade, preço e cliente.
- **Consome mensagens Kafka** e classifica compras como `NORMAL` ou `SUSPEITA` com base no valor total.
- **Kafka UI** para visualizar e explorar mensagens e tópicos via interface web.
- Todo o ambiente Kafka (Kafka Broker, Zookeeper, Kafka UI) roda via Docker Compose para fácil setup.

---

## Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/) instalado e rodando
- [Python 3.11+](https://www.python.org/downloads/) instalado
- (Opcional) [pipenv](https://pipenv.pypa.io/en/latest/) ou `venv` para criar ambiente virtual Python

---

## Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/thaisdo/franz-stream.git
cd franz-stream
```

### 2. Inicie os containers Kafka, Zookeeper e Kafka UI

```bash
docker-compose up -d
```
- Espere alguns segundos até os containers subirem.

### 3. Crie o tópico vendas (opcional)
Se quiser garantir que o tópico existe:
```bash
docker exec -it kafka kafka-topics --create --topic vendas --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

### 4. Crie um ambiente virtual Python e instale dependências
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows PowerShell
pip install -r pyproject.toml
```

### 5. Rode o consumidor (fica ouvindo mensagens)
```python
python consumer.py
```

### 6. Em outro terminal, rode o produtor para enviar mensagens
```python
python producer.py
```

### 7. Acesse a UI do Kakfa UI - 8080
```bash
http://localhost:8080
```

## Estrutura do projeto

```bash
├── consumer.py          # Consome e analisa mensagens Kafka
├── producer.py          # Produz mensagens simulando vendas de frutas
├── docker-compose.yml   # Configuração Docker Kafka, Zookeeper e Kafka UI
├── pyproject.toml       # Dependências Python (kafka-python, etc)
└── README.md            # Este arquivo
```