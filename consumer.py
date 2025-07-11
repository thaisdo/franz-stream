from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "vendas",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    auto_offset_reset="earliest",
    group_id="analisador-frutas",
    
)

print("Aguardando mensagens...\n")

for msg in consumer:
    dados = msg.value
    total = dados["total"]
    status = "SUSPEITA" if total > 100 else "NORMAL"

    print(f"[{status}] Cliente {dados['cliente_id']} commprou {dados['quantidade']}x {dados['produto']} (R$ {dados['total']})")