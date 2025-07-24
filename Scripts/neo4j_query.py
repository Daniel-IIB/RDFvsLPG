from neo4j import GraphDatabase
import time

endpoint = "bolt://localhost:7687" 
username = "neo4j"             
password = "00000000"          

driver = GraphDatabase.driver(endpoint, auth=(username, password))

def run_query_and_measure_time(query):
    with driver.session(database="grundriss2") as session:
        start_time = time.time() 
        result = session.run(query)
        end_time = time.time()
        records = list(result)
        duration = (end_time - start_time) * 1000000
        return duration, records

query_file_path = "cypher_query0.txt"

with open(query_file_path, 'r') as file:
    query = file.read().strip()

elapsed_times = []

for i in range(20):
    duration, records = run_query_and_measure_time(query)
    elapsed_times.append(duration)

for idx, elapsed_time in enumerate(elapsed_times, start=1):
    print(f"{idx} {elapsed_time:.0f}")

avg_time = sum(elapsed_times[1:]) / (len(elapsed_times) - 1)
print(f"Durchschnittliche Laufzeit: {avg_time:.0f} Mikrosekunden")

print(f"Anzahl der gefundenen Instanzen: {len(records)}")

driver.close()