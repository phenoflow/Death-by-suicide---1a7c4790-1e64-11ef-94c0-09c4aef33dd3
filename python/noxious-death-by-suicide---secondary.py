# A. John, 2024.

import sys, csv, re

codes = [{"code":"X694.","system":"icd10"},{"code":"X692.","system":"icd10"},{"code":"X69..","system":"icd10"},{"code":"X696.","system":"icd10"},{"code":"X695.","system":"icd10"},{"code":"X691.","system":"icd10"},{"code":"X697.","system":"icd10"},{"code":"X699.","system":"icd10"},{"code":"X693.","system":"icd10"},{"code":"X690.","system":"icd10"},{"code":"X698.","system":"icd10"},{"code":"Y190.","system":"icd10"},{"code":"Y19..","system":"icd10"},{"code":"Y194.","system":"icd10"},{"code":"Y198.","system":"icd10"},{"code":"Y195.","system":"icd10"},{"code":"Y191.","system":"icd10"},{"code":"Y192.","system":"icd10"},{"code":"Y196.","system":"icd10"},{"code":"Y193.","system":"icd10"},{"code":"Y197.","system":"icd10"},{"code":"Y199.","system":"icd10"},{"code":"Y197.","system":"icd10"},{"code":"Y196.","system":"icd10"},{"code":"Y191.","system":"icd10"},{"code":"Y190.","system":"icd10"},{"code":"Y19..","system":"icd10"},{"code":"Y194.","system":"icd10"},{"code":"Y192.","system":"icd10"},{"code":"Y193.","system":"icd10"},{"code":"Y198.","system":"icd10"},{"code":"Y195.","system":"icd10"},{"code":"Y199.","system":"icd10"},{"code":"X494.","system":"icd10"},{"code":"X490.","system":"icd10"},{"code":"X497.","system":"icd10"},{"code":"X498.","system":"icd10"},{"code":"X496.","system":"icd10"},{"code":"X49..","system":"icd10"},{"code":"X493.","system":"icd10"},{"code":"X491.","system":"icd10"},{"code":"X492.","system":"icd10"},{"code":"X499.","system":"icd10"},{"code":"X495.","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-suicide-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["noxious-death-by-suicide---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["noxious-death-by-suicide---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["noxious-death-by-suicide---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
