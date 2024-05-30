# A. John, 2024.

import sys, csv, re

codes = [{"code":"Y300.","system":"icd10"},{"code":"Y301.","system":"icd10"},{"code":"Y305.","system":"icd10"},{"code":"Y302.","system":"icd10"},{"code":"Y309.","system":"icd10"},{"code":"Y304.","system":"icd10"},{"code":"Y306.","system":"icd10"},{"code":"Y308.","system":"icd10"},{"code":"Y307.","system":"icd10"},{"code":"Y303.","system":"icd10"},{"code":"Y30..","system":"icd10"},{"code":"Y301.","system":"icd10"},{"code":"Y308.","system":"icd10"},{"code":"Y302.","system":"icd10"},{"code":"Y304.","system":"icd10"},{"code":"Y30..","system":"icd10"},{"code":"Y306.","system":"icd10"},{"code":"Y305.","system":"icd10"},{"code":"Y300.","system":"icd10"},{"code":"Y307.","system":"icd10"},{"code":"Y303.","system":"icd10"},{"code":"Y309.","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-suicide-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-suicide-pushed---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-suicide-pushed---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-suicide-pushed---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
