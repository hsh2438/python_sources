import lmdb


data = ['hello', 'nice to meet you', 'lmdb example']

lmdb_name = 'test.lmdb'

# write example
write_db = lmdb.open(lmdb_name, map_size=1048576)

with write_db.begin(write=True) as txn:
    for idx, sentence in enumerate(data):
        txn.put(str(idx).encode(), sentence.encode())


# read example
read_db = lmdb.open(lmdb_name)
with read_db.begin(write=False) as txn:
    for idx in range(3):
        print(txn.get(str(idx).encode()).decode())
