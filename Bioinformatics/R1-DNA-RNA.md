## Transcribing DNA Into RNA

```python
dna = 'GATGGAACTTGACTACGTAAATT'

# f = open('file.txt', 'r')
# rna = f.read()

def transcribe(dna):
    return ''.join([c if c != 'T' else 'U' for c in dna])

print(transcribe(dna))
```
```txt
GAUGGAACUUGACUACGUAAAUU
```

---
## Translating RNA Into Protein

```python
codons = {'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
          'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
          'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
          'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
          'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
          'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
          'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
          'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
          'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
          'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
          'UAA': '$', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
          'UAG': '$', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
          'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
          'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
          'UGA': '$', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
          'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'}

rna = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'

# f = open('file.txt', 'r')
# rna = f.read()

def translate(rna):
    protein = ''
    while True:
        tmp = rna[:3]
        if codons[tmp] == '$':
            break
        protein += codons[tmp]
        rna = rna[3:]
    return protein

print(translate(rna))
```
```txt
MAMAPRTEINSTRING
```

---
## Finding a Motif in DNA

```python
s = 'GATATATGCATATACTT'
t = 'ATAT'

def getLocations(s, t):
    locations = []
    n = len(s)

    for i in range(n):
        if s[:len(t)] == t:
            locations.append(i + 1)
        s = s[1:]
    return locations

print(getLocations(s, t))
```
```txt
[2, 4, 10]
```
