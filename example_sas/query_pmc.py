from Bio import Entrez, Medline

# Query
Entrez.email = "your_email_address"
handle = Entrez.esearch(db="pmc", retmax=5, 
    term = "molina-contreras + shade + avoidance",
    retmode="xml")
record = Entrez.read(handle)
handle.close()

# Parse
ids = record["IdList"]
handle = Entrez.efetch(db="pmc", id=ids, rettype="medline")
records = Medline.parse(handle)
publications = list(records)
handle.close()

# Output
for i, pub in enumerate(publications):
    title = pub["TI"]
    pmcid = pub["PMC"]
    url = "https://www.ncbi.nlm.nih.gov/pmc/" + pmcid
    print(i, title, url)
