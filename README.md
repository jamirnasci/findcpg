# findcpg
Script to locate cpg islands in genome

(Obs): CpG dinucleotide frequency in window.

(Exp): (citosine count) * (guanine count) / window size

usage: CpG.py <sequence_file> <min_gc_content> <min_obs/exp> <window_size> <move_option>

move_option: if window is valid, is necessary choose a method to continue:

  jump: go to next +(window_size) window
  
  slide: go to next nucleotide

## result:

Obs/Exp: <Obs/Exp of island>     GC Content: <gc_content_of_island>        start: <start_region>   end: <end_region>

## References:
Stothard P (2000) The Sequence Manipulation Suite: JavaScript programs for analyzing and formatting protein and DNA sequences. Biotechniques 28:1102-1104.
Gardiner-Garden M, Frommer M. CpG islands in vertebrate genomes. J Mol Biol. 1987 Jul 20;196(2):261-82. doi: 10.1016/0022-2836(87)90689-9. PMID: 3656447.
