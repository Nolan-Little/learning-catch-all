from enum import IntEnum
from typing import Tuple, List
import random
from stopwatch import stopwatch

Nucleotide: IntEnum = IntEnum("Nucleotide", ("A", "C", "G", "T"))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]


def build_random_gene_str(min_len=27, max_len=90) -> str:
    gene_elems = []
    gene_length = random.randrange(min_len, max_len, 3)
    for _ in range(0, gene_length):
        gene_elems.append(random.choice(["A", "C", "G", "T"]))

    return "".join(gene_elems)

def string_to_gene(gene_str: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(gene_str)):
        if (i + 2 ) >= len(gene_str):
            return gene
        codon: Codon = (Nucleotide[gene_str[i]], Nucleotide[gene_str[i + 1]], Nucleotide[gene_str[i + 2]])
        gene.append(codon)
    return gene

def build_gene(min_len=2700000, max_len=9000000) -> Gene:
    gene_str = build_random_gene_str(min_len=min_len, max_len=max_len)
    return string_to_gene(gene_str=gene_str)

@stopwatch
def linear_search(gene, key_codon) -> Codon:
    for codon in gene:
        if codon == key_codon:
            return codon
    return None

@stopwatch
def binary_search(gene, key_codon):
    low: int = 0
    high: int = len(gene) - 1
    while low <= high:
        mid: int = (low + high) // 2
        codon = gene[mid]
        if codon < key_codon:
            low = mid + 1
        elif codon > key_codon:
            high = mid - 1
        else:
            return True
    return False

def sort_gene(gene) -> Gene:
    return sorted(gene)

if __name__ == '__main__':
    gene = build_gene()
    gene = sort_gene(gene)
    codon: Codon = (Nucleotide["A"], Nucleotide["G"], Nucleotide["T"])
    res = binary_search(gene, codon)
    print(res)