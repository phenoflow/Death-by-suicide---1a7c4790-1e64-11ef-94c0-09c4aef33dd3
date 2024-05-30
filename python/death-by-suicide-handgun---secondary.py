# A. John, 2024.

import sys, csv, re

codes = [{"code":"X724.","system":"icd10"},{"code":"X721.","system":"icd10"},{"code":"X72..","system":"icd10"},{"code":"X723.","system":"icd10"},{"code":"X729.","system":"icd10"},{"code":"X722.","system":"icd10"},{"code":"X720.","system":"icd10"},{"code":"X726.","system":"icd10"},{"code":"X728.","system":"icd10"},{"code":"X727.","system":"icd10"},{"code":"X725.","system":"icd10"},{"code":"Y223.","system":"icd10"},{"code":"Y224.","system":"icd10"},{"code":"Y22..","system":"icd10"},{"code":"Y227.","system":"icd10"},{"code":"Y228.","system":"icd10"},{"code":"Y226.","system":"icd10"},{"code":"Y229.","system":"icd10"},{"code":"Y220.","system":"icd10"},{"code":"Y221.","system":"icd10"},{"code":"Y225.","system":"icd10"},{"code":"Y222.","system":"icd10"},{"code":"Y220.","system":"icd10"},{"code":"Y224.","system":"icd10"},{"code":"Y225.","system":"icd10"},{"code":"Y223.","system":"icd10"},{"code":"Y221.","system":"icd10"},{"code":"Y227.","system":"icd10"},{"code":"Y222.","system":"icd10"},{"code":"Y229.","system":"icd10"},{"code":"Y22..","system":"icd10"},{"code":"Y228.","system":"icd10"},{"code":"Y226.","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-suicide-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-suicide-handgun---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-suicide-handgun---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-suicide-handgun---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
