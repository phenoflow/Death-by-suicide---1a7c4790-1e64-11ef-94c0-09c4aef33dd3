# A. John, 2024.

import sys, csv, re

codes = [{"code":"X741.","system":"icd10"},{"code":"X74..","system":"icd10"},{"code":"X743.","system":"icd10"},{"code":"X747.","system":"icd10"},{"code":"X740.","system":"icd10"},{"code":"X744.","system":"icd10"},{"code":"X742.","system":"icd10"},{"code":"X748.","system":"icd10"},{"code":"X749.","system":"icd10"},{"code":"X745.","system":"icd10"},{"code":"X746.","system":"icd10"},{"code":"Y243.","system":"icd10"},{"code":"Y247.","system":"icd10"},{"code":"Y248.","system":"icd10"},{"code":"Y245.","system":"icd10"},{"code":"Y241.","system":"icd10"},{"code":"Y242.","system":"icd10"},{"code":"Y240.","system":"icd10"},{"code":"Y249.","system":"icd10"},{"code":"Y246.","system":"icd10"},{"code":"Y244.","system":"icd10"},{"code":"Y24..","system":"icd10"},{"code":"Y244.","system":"icd10"},{"code":"Y249.","system":"icd10"},{"code":"Y242.","system":"icd10"},{"code":"Y243.","system":"icd10"},{"code":"Y240.","system":"icd10"},{"code":"Y246.","system":"icd10"},{"code":"Y241.","system":"icd10"},{"code":"Y247.","system":"icd10"},{"code":"Y24..","system":"icd10"},{"code":"Y245.","system":"icd10"},{"code":"Y248.","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-suicide-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-suicide-firearm---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-suicide-firearm---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-suicide-firearm---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
