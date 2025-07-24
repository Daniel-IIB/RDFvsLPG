import requests
import time

blazegraph_endpoint = "http://localhost:9999/blazegraph/sparql"
query_file_path = "sparql_query5.txt"

with open(query_file_path, 'r') as file:
    query = file.read().strip()

headers = {"Accept": "application/sparql-results+json"}
params = {"query": query}

elapsed_times = []
result_count = None

for i in range(20):
    start_time = time.time()
    response = requests.get(blazegraph_endpoint, headers=headers, params=params)
    end_time = time.time()
    elapsed_times.append((end_time - start_time) * 1000000)
    if i == 0:
        if response.status_code == 200:
            results = response.json()
            result_count = len(results["results"]["bindings"])
        else:
            print(f"Fehler bei der Anfrage: {response.status_code}")

for index, elapsed_time in enumerate(elapsed_times, start=1):
    print(f"{index} {elapsed_time:.0f}")

avg_time = sum(elapsed_times[1:]) / (len(elapsed_times) - 1)
print(f"Durchschnittliche Laufzeit: {avg_time:.0f} Mikrosekunden")
print(f"Anzahl der gefundenen Instanzen: {result_count}")