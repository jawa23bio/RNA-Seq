# RNA-Seq Analysis
## Transcriptional Profile of Mammalian Cardiac Regeneration with mRNA-Seq
This analysis is based on the data published in the following study: O’Meara et al. Transcriptional Reversion of Cardiac Myocyte Fate During Mammalian Cardiac Regeneration. Circ Res. Feb 2015. PMID: 25477501

We have focused specifically on the data from the first figure of the paper, which involves the dataset containing samples from p0, p4, p7, and adult mouse heart ventricle cells. While our analysis deviates from the published methods to incorporate more up-to-date strategies and tools, our workflow aims to capture and recreate the same core biological signals observed in the original work.


## Methods: 
RNA sequencing data from biological samples ('AD', 'P0', 'P4', 'P7') with replicates ('rep1', 'rep2') was processed using a Snakemake pipeline. The GRCm39 reference genome and GTF annotation file were obtained from the Gencode database (release M34). Quality control analysis of raw sequencing data was conducted using FastQC(v0.12.1). Alignment of reads to the reference genome was performed using STAR aligner(2.7.11b). Gene expression quantification at the exon level was achieved using Verse (v1.0.5). MultiQC was employed to aggregate FastQC results into a single report. Custom Python scripts were utilized for parsing gene annotation, generating a counts matrix from exon-level expression data, and filtering the counts matrix. All analysis methods were integrated into the `rna_seq.snake` file for reproducibility and automation of the workflow. Further analysis, including differential expression and gene set enrichment analysis, were conducted in the `differential_expression.Rmd` file.

## References:
1. O'Meara, C. C., Wamstad, J. A., Gladstone, R. A., Fomovsky, G. M., Butty, V. L., Shrikumar, A., Gannon, J. B., Boyer, L. A., & Lee, R. T. (2015). Transcriptional reversion of cardiac myocyte fate during mammalian cardiac regeneration. Circulation research, 116(5), 804–815. https://doi.org/10.1161/CIRCRESAHA.116.304269
2. Andrews, S. (2010). FastQC:  A Quality Control Tool for High Throughput Sequence Data [Online]. Available online at: http://www.bioinformatics.babraham.ac.uk/projects/fastqc/
3. Dobin, A., Davis, C. A., Schlesinger, F., Drenkow, J., Zaleski, C., Jha, S., Batut, P., Chaisson, M., & Gingeras, T. R. (2013). STAR: ultrafast universal RNA-seq aligner. Bioinformatics (Oxford, England), 29(1), 15–21. https://doi.org/10.1093/bioinformatics/bts635
4. Zhu, Q., Fisher, S. A., Shallcross, J., & Kim, J. (2016). VERSE: a versatile and efficient RNA-Seq read counting tool. bioRxiv. doi:10.1101/053306
5. MultiQC: Summarize analysis results for multiple tools and samples in a single report. Philip Ewels, Måns Magnusson, Sverker Lundin and Max Käller. Bioinformatics (2016)
6. Love MI, Huber W, Anders S (2014). “Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2.” Genome Biology, 15, 550. doi:10.1186/s13059-014-0550-8.
7. Korotkevich G, Sukhov V, Sergushichev A (2019). “Fast gene set enrichment analysis.” bioRxiv. doi:10.1101/060012, http://biorxiv.org/content/early/2016/06/20/060012.
8. Mölder, F., Jablonski, K.P., Letcher, B., Hall, M.B., Tomkins-Tinch, C.H., Sochat, V., Forster, J., Lee, S., Twardziok, S.O., Kanitz, A., Wilm, A., Holtgrewe, M., Rahmann, S., Nahnsen, S., Köster, J., 2021. Sustainable data analysis with Snakemake. F1000Res 10, 33.
