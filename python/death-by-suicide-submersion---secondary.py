# A. John, 2024.

import sys, csv, re

codes = [{"code":"X71..","system":"icd10"},{"code":"X710.","system":"icd10"},{"code":"X717.","system":"icd10"},{"code":"X718.","system":"icd10"},{"code":"X713.","system":"icd10"},{"code":"X716.","system":"icd10"},{"code":"X714.","system":"icd10"},{"code":"X719.","system":"icd10"},{"code":"X712.","system":"icd10"},{"code":"X715.","system":"icd10"},{"code":"X711.","system":"icd10"},{"code":"Y215.","system":"icd10"},{"code":"Y216.","system":"icd10"},{"code":"Y210.","system":"icd10"},{"code":"Y213.","system":"icd10"},{"code":"Y212.","system":"icd10"},{"code":"Y21..","system":"icd10"},{"code":"Y214.","system":"icd10"},{"code":"Y211.","system":"icd10"},{"code":"Y219.","system":"icd10"},{"code":"Y217.","system":"icd10"},{"code":"Y218.","system":"icd10"},{"code":"Y212.","system":"icd10"},{"code":"Y210.","system":"icd10"},{"code":"Y215.","system":"icd10"},{"code":"Y219.","system":"icd10"},{"code":"Y216.","system":"icd10"},{"code":"Y21..","system":"icd10"},{"code":"Y211.","system":"icd10"},{"code":"Y214.","system":"icd10"},{"code":"Y217.","system":"icd10"},{"code":"Y213.","system":"icd10"},{"code":"Y218.","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-suicide-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-suicide-submersion---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-suicide-submersion---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-suicide-submersion---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
