"""
This script will merge the categories of all genes.
"""
# %%
import pyforest

# load data
genes_with_one_phenotype = pd.read_excel("../data/4_categorized_genes/Hayles_2013_OB_category_genes_with_one_phenotype.xlsx", sheet_name="One basic phenotype")
genes_with_multi_phenotypes = pd.read_excel("../data/4_categorized_genes/Hayles_2013_OB_category_genes_with_multi_phenotypes.xlsx", sheet_name="Multi basic phenotypes")
genes_with_inconsistent_phenotypes = pd.read_excel("../data/4_categorized_genes/Hayles_2013_OB_category_genes_with_inconsistent_phenotypes.xlsx", sheet_name="Inconsistent phenotypes")

# concat the categories of all genes
all_genes_with_categories = pd.concat([genes_with_one_phenotype, genes_with_multi_phenotypes, genes_with_inconsistent_phenotypes], ignore_index=True)

# %%
