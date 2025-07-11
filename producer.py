from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

produtos = ["banana", "abacaxi", "morango", "uva"]
clientes = list(range(1000, 1010))

print("Enviando mensagens para o Kafka...")

for i in range(10):
    fruta = random.choice(produtos)
    quantidade = random.randint(1,15)
    valor_unitario = round(random.uniform(1.5, 10.0), 2)
    total = round(quantidade * valor_unitario, 2)
    client_id = random.choice(clientes)

    mensagem = {
        "id": i,
        "cliente_id": client_id,
        "produto": fruta,
        "quantidade": quantidade,
        "valor_unitario": valor_unitario,
        "total": total
    }
    print(f"Enviando: {mensagem}")
    producer.send("vendas", value=mensagem)
    time.sleep(0.5)

producer.flush()