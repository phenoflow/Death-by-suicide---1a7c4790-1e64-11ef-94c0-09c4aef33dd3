# A. John, 2024.

import sys, csv, re

codes = [{"code":"X767.","system":"icd10"},{"code":"X765.","system":"icd10"},{"code":"X76..","system":"icd10"},{"code":"X768.","system":"icd10"},{"code":"X769.","system":"icd10"},{"code":"X760.","system":"icd10"},{"code":"X763.","system":"icd10"},{"code":"X766.","system":"icd10"},{"code":"X762.","system":"icd10"},{"code":"X764.","system":"icd10"},{"code":"X761.","system":"icd10"},{"code":"Y26..","system":"icd10"},{"code":"Y266.","system":"icd10"},{"code":"Y265.","system":"icd10"},{"code":"Y264.","system":"icd10"},{"code":"Y269.","system":"icd10"},{"code":"Y263.","system":"icd10"},{"code":"Y268.","system":"icd10"},{"code":"Y267.","system":"icd10"},{"code":"Y261.","system":"icd10"},{"code":"Y260.","system":"icd10"},{"code":"Y262.","system":"icd10"},{"code":"Y266.","system":"icd10"},{"code":"Y260.","system":"icd10"},{"code":"Y261.","system":"icd10"},{"code":"Y267.","system":"icd10"},{"code":"Y26..","system":"icd10"},{"code":"Y264.","system":"icd10"},{"code":"Y263.","system":"icd10"},{"code":"Y269.","system":"icd10"},{"code":"Y262.","system":"icd10"},{"code":"Y265.","system":"icd10"},{"code":"Y268.","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-suicide-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-suicide-flame---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-suicide-flame---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-suicide-flame---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
