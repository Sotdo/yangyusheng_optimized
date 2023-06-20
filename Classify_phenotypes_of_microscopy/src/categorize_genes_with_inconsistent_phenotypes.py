"""
This script is used to categorize genes with inconsistent phenotypes.
Previous work has manually checked the inconsistent phenotypes and categorized them to different levels of growth phenotypes.
"""
# %%
import pyforest
print(pyforest.active_imports())

genes_with_inconsistent_phenotypes = pd.read_excel("../data/3_grouped_genes/Hayles_2013_OB_grouped_genes.xlsx", sheet_name="Inconsistent phenotypes")

manual_categorized_genes = pd.read_excel("../tmp/previous_manual_check_of_insistent_phenotypes/Inconsistent_phenotypes_at_25_32_manual.xlsx")

categorized_genes_with_inconsistent_phenotypes = genes_with_inconsistent_phenotypes.merge(manual_categorized_genes[["SysID","Category_25", "Category_32"]], left_on="Systematic ID", right_on="SysID", how="left").drop(columns="SysID")
# %%
