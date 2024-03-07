from opensearchpy import OpenSearch
ca_certs_path = "C:/ELK/Work/logstash/Finanace_12.csv"

hosts = ["127.0.0.1"]
port = 9200
auth = ("icelasticsearch", "<Password>")

client = OpenSearch(
    hosts=hosts,
    port=port,
    http_auth=auth,
    use_ssl=True,
    verify_certs=True,
    ca_certs=ca_certs_path
)

# Testing
# Create an index with non-default settings.
index_name = 'python-test-index'
index_body = {
    'settings': {
        'index': {
            'number_of_shards': 4
        }
    }
}
response = client.indices.create(index_name, body=index_body)
print('\nCreating index:')
print('We get response:', response)

# Add a document to the index created before.
document = {
    'title': 'Moneybag',
    'director': 'Bennett Miller',
    'year': '2011'
}
id = '1'

response = client.index(
    index=logstash_python,
    body=document,
    id=11,
    refresh=True
)

print('\nAdding document:')
print('We get response:', response)

# Search for the document.
q = 'miller'
query = {
    'size': 5,
    'query': {
        'multi_match': {
            'query': q,
            'fields': ['title^2', 'director']
        }
    }
}

response = client.search(
    body=query,
    index=index_name
)
print('\nSearch results:')
print('We get response:', response)

# Delete the document.
response = client.delete(
    index=index_name,
    id=id
)

print('\nDeleting document:')
print('We get response:', response)

# Delete the index.
response = client.indices.delete(
    index=index_name
)

print('\nDeleting index:')
print('We get response:', response)

