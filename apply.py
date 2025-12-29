import pandas as pd

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    def sta(val):
        if(val["dna_sequence"].startswith("ATG")):
            return 1
        else:
            return 0
    def sto(val):
        if(val["dna_sequence"].endswith("TAA") or val["dna_sequence"].endswith("TAG") or val["dna_sequence"].endswith("TGA")):
            return 1
        else:
            return 0
    def ata(val):
        if("ATAT" in val["dna_sequence"]):
            return 1
        else:
            return 0
    def g(val):
        if("GGG" in val["dna_sequence"]):
            return 1
        else:
            return 0
    st=samples.apply(sta,axis=1)
    samples["has_start"]=st
    so=samples.apply(sto,axis=1)
    samples["has_stop"]=so
    at=samples.apply(ata,axis=1)
    samples["has_atat"]=at
    gg=samples.apply(g,axis=1)
    samples["has_ggg"]=gg
    return samples


    