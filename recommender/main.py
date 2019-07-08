#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd

#read tumor table as pandas df
tumorSample_table = pd.read_csv("EB++AdjustPANCAN_IlluminaHiSeq_RNASeqV2.geneExp.xena",sep='\t')

#read curated pathway templates as df
CELL_CYCLE_Table = pd.read_csv("curated/curated_pathway_templates.Cell_Cycle.tsv",sep='\t')
HIPPO_Table = pd.read_csv("curated/curated_pathway_templates.HIPPO.tsv",sep='\t')
MYC_Table = pd.read_csv("curated/curated_pathway_templates.MYC.tsv",sep='\t')
NOTCH_Table = pd.read_csv("curated/curated_pathway_templates.NOTCH.tsv",sep='\t')
NRF2_Table = pd.read_csv("curated/curated_pathway_templates.NRF2.tsv",sep='\t')
PI3K_Table = pd.read_csv("curated/curated_pathway_templates.PI3K.tsv",sep='\t')
RTK_RAS_Table = pd.read_csv("curated/curated_pathway_templates.RTK_RAS.tsv",sep='\t')
TGF_BETA_Table = pd.read_csv("curated/curated_pathway_templates.TGF-Beta.tsv",sep='\t')
TP53_Table = pd.read_csv("curated/curated_pathway_templates.TP53.tsv",sep='\t')
WNT_Table = pd.read_csv("curated/curated_pathway_templates.WNT.tsv",sep='\t')


# In[14]:


#Get genes set listed under each of 10 pathways

HIPPO  = set(HIPPO_Table['Gene'])
MYC = set(MYC_Table['Gene'])
NOTCH = set(NOTCH_Table['Gene'])
NRF2 = set(NRF2_Table['Gene'])
PI3K = set(PI3K_Table['Gene'])
RTK_RAS = set(RTK_RAS_Table['Gene'])
TGF_BETA = set(TGF_BETA_Table['Gene'])
TP53 = set(TP53_Table['Gene'])
WNT = set(WNT_Table['Gene'])

