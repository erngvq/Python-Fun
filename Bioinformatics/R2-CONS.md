## Consensus and Profile

```python
def loadFasta(filename):
    if filename.endswith('.gz'):
        fp = gzip.open(filename, 'r')
    else:
        fp = open(filename, 'r')
    data = fp.read().split('>')
    fp.close()
    data.pop(0)     
    headers = []
    sequences = []
    for sequence in data:
        lines = sequence.split('\n')
        headers.append(lines.pop(0))
        sequences.append('+' + ''.join(lines))
    return (headers, sequences)
```
```python
hdr, seq = loadFasta('dna_collection.txt')
matrix = [list(dna[1:]) for dna in seq]

profile = [[], [], [], []]
consensus = ''

for i in range(len(matrix[0])):
    dct = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for j in range(len(matrix)):
        dct[matrix[j][i]] += 1

    consensus += max(dct, key=dct.get)

    profile[0].append(dct['A'])
    profile[1].append(dct['C'])
    profile[2].append(dct['G'])
    profile[3].append(dct['T'])

dct = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
print(consensus)
for i, e in enumerate(profile):
    print(dct[i], end=': ')
    print(*e)
```
```txt
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
```

---
## Overlap Graphs

```python
hdr, dna = loadFasta('dna_strings.txt')
dna = [e[1:] for e in dna]

k = 3
lst = []

for i in range(len(dna)):
    for j in range(len(dna)):
        if dna[i] == dna[j]:
            continue
        if dna[i][-k:] == dna[j][:k]:
            lst.append((hdr[i], hdr[j]))

for e in lst:
    print(e[0] + ' ' + e[1])
```
```txt
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
```
