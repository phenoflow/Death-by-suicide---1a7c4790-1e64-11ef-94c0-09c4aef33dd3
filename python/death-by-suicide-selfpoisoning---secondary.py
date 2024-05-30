# A. John, 2024.

import sys, csv, re

codes = [{"code":"X679.","system":"icd10"},{"code":"X678.","system":"icd10"},{"code":"X670.","system":"icd10"},{"code":"X677.","system":"icd10"},{"code":"X67..","system":"icd10"},{"code":"Y178.","system":"icd10"},{"code":"Y170.","system":"icd10"},{"code":"Y177.","system":"icd10"},{"code":"Y179.","system":"icd10"},{"code":"Y17..","system":"icd10"},{"code":"Y177.","system":"icd10"},{"code":"Y179.","system":"icd10"},{"code":"Y17..","system":"icd10"},{"code":"Y170.","system":"icd10"},{"code":"Y178.","system":"icd10"},{"code":"X478.","system":"icd10"},{"code":"X47..","system":"icd10"},{"code":"X479.","system":"icd10"},{"code":"X477.","system":"icd10"},{"code":"X470.","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-suicide-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-suicide-selfpoisoning---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-suicide-selfpoisoning---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-suicide-selfpoisoning---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
