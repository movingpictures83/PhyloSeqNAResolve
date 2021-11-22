# PhyloSeqNAResolve
# Language: Python
# Input: CSV
# Output: CSV
# Tested with: PluMA 1.1, Python 3.6
# Dependency: PhyloSeq 1.34.0

PluMA plugin that takes as input an OTU table (CSV file)
for PhyloSeq (McMurdie et al, 2013) and resolves all
unclassifiable levels in the taxonomy tree for each taxon.

The modified taxonomy table, in CSV format, is the output file.
