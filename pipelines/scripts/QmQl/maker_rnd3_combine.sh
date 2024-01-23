# combine
awk '{print FILENAME"\t"$0}' */*/*master_datastore_index.log | \
sed 's#/#\t#2' | awk '{print $3"\t"$1"/"$4"\t"$5}' > master_datastore_index.log

fasta_merge -o rnd3 -d master_datastore_index.log
gff3_merge -n -s -d master_datastore_index.log > rnd3_noSeq.gff
# transcript alignments
awk '{ if ($2 == "est_gff:est2genome") print $0 }' rnd3_noSeq.gff | \
sed 's/est_gff:est2genome/est2genome/' > rnd3.est2genome.gff
# protein alignments
awk '{ if ($2 == "protein_gff:protein2genome") print $0 }' rnd3_noSeq.gff | \
sed 's/protein_gff:protein2genome/protein2genome/' > rnd3.protein2genome.gff

