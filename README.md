# findcpg
Script to locate cpg islands in genome
(Obs): CpG dinucleotide frequency in window.

(Exp): (citosine count) * (guanine count) / window size

usage: CpG.py <sequence file> <min gc content> <min obs/exp> <window size>

## result:

Obs/Exp: <Obs/Exp of island>     GC Content: <gc_content of island>        start: <start_region>   end: <end_region>

## References:
Stothard P (2000) The Sequence Manipulation Suite: JavaScript programs for analyzing and formatting protein and DNA sequences. Biotechniques 28:1102-1104.
Gardiner-Garden M, Frommer M. CpG islands in vertebrate genomes. J Mol Biol. 1987 Jul 20;196(2):261-82. doi: 10.1016/0022-2836(87)90689-9. PMID: 3656447.
