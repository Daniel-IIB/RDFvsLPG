import time
from SPARQLWrapper import SPARQLWrapper, JSON

def run_sparql_query(endpoint, query):
    sparql = SPARQLWrapper(endpoint)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    
    start_time = time.time()
    results = sparql.query().convert()
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    return results, elapsed_time

def query_ifc_wall(endpoint, query_file_path):
    with open(query_file_path, 'r') as file:
        query = file.read()
    
    results, elapsed_time = run_sparql_query(endpoint, query)
    
    count = len(results["results"]["bindings"])
    return count, elapsed_time * 1000000

def main():

    endpoint = 'http://localhost:7200/repositories/GR2'
    
    query_file_path = 'sparql_query5.txt'
    
    elapsed_times = []
    
    for i in range(20):
        count, elapsed_time = query_ifc_wall(endpoint, query_file_path)
        elapsed_times.append(elapsed_time)
        print(f"{i + 1} {elapsed_time:.0f}")
    
    avg_elapsed_time = sum(elapsed_times[1:]) / len(elapsed_times[1:])
    
    print(f"Durchschnittliche Laufzeit fuer die Durchgaenge 2-20: {avg_elapsed_time:.0f} Mikrosekunden")
    print({count})

if __name__ == "__main__":
    main()