from Bio import Entrez
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC


def searchdna(txt_input):

    Entrez.api_key = "083f0bb35cdf428d071a00f4b76ab0a4a909"
    Entrez.email = "sarangi.srikant@gmail.com"

    # List of organisms/ genomes to search against
    genLst = ['NC_000852', 'NC_007346', 'NC_008724', 'NC_009899', 'NC_014637', 'NC_020104', 'NC_023423', 'NC_023640',
              'NC_023719', 'NC_027867']

    # Translate DNA seq to AA seq
    coding_dna = Seq(txt_input, IUPAC.unambiguous_dna)
    messenger_rna = coding_dna.transcribe()
    coding_aa = messenger_rna.translate(to_stop=True)

    matchLst = []

    for g in genLst:

        handle = Entrez.efetch(db="nucleotide", id=g, rettype="gb", retmode="xml")
        record = Entrez.read(handle)

        # Retrieve associated proteins/ CDS regions
        protLst = [x for x in record[0]['GBSeq_feature-table'] if x['GBFeature_key'] == 'CDS']

        # Run through list
        for p in protLst:
            # Retrieve amino acid sequence
            aaDict = [x for x in p['GBFeature_quals'] if x['GBQualifier_name'] == 'translation']
            aaSeq = aaDict[0]['GBQualifier_value']

            # Compare
            try:
                if str(coding_aa) == str(aaSeq):

                    proLoc = p['GBFeature_location']

                    # Find list item for product name
                    proEntry = [x for x in p['GBFeature_quals'] if x['GBQualifier_name'] == 'product']
                    proName = proEntry[0]['GBQualifier_value']
                    matchLst.append(['Location: ' + proLoc + ';' + 'Protein Name: ' + proName])
                    break

                else:
                    continue

            except (ValueError, TypeError):
                continue

    return matchLst
