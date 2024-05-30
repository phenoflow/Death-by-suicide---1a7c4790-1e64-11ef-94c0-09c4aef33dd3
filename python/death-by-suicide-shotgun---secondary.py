# A. John, 2024.

import sys, csv, re

codes = [{"code":"X773.","system":"icd10"},{"code":"X777.","system":"icd10"},{"code":"X77..","system":"icd10"},{"code":"X774.","system":"icd10"},{"code":"X770.","system":"icd10"},{"code":"X775.","system":"icd10"},{"code":"X772.","system":"icd10"},{"code":"X776.","system":"icd10"},{"code":"X779.","system":"icd10"},{"code":"X778.","system":"icd10"},{"code":"X771.","system":"icd10"},{"code":"Y273.","system":"icd10"},{"code":"Y274.","system":"icd10"},{"code":"Y275.","system":"icd10"},{"code":"Y279.","system":"icd10"},{"code":"Y276.","system":"icd10"},{"code":"Y271.","system":"icd10"},{"code":"Y272.","system":"icd10"},{"code":"Y270.","system":"icd10"},{"code":"Y27..","system":"icd10"},{"code":"Y278.","system":"icd10"},{"code":"Y277.","system":"icd10"},{"code":"Y273.","system":"icd10"},{"code":"Y278.","system":"icd10"},{"code":"Y279.","system":"icd10"},{"code":"Y27..","system":"icd10"},{"code":"Y271.","system":"icd10"},{"code":"Y276.","system":"icd10"},{"code":"Y272.","system":"icd10"},{"code":"Y274.","system":"icd10"},{"code":"Y275.","system":"icd10"},{"code":"Y277.","system":"icd10"},{"code":"Y270.","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-suicide-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-suicide-shotgun---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-suicide-shotgun---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-suicide-shotgun---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
