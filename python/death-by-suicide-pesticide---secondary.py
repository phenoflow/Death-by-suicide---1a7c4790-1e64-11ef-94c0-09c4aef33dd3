# A. John, 2024.

import sys, csv, re

codes = [{"code":"X686.","system":"icd10"},{"code":"X687.","system":"icd10"},{"code":"X682.","system":"icd10"},{"code":"X684.","system":"icd10"},{"code":"X683.","system":"icd10"},{"code":"X688.","system":"icd10"},{"code":"X689.","system":"icd10"},{"code":"X681.","system":"icd10"},{"code":"X680.","system":"icd10"},{"code":"X68..","system":"icd10"},{"code":"X685.","system":"icd10"},{"code":"Y183.","system":"icd10"},{"code":"Y186.","system":"icd10"},{"code":"Y18..","system":"icd10"},{"code":"Y181.","system":"icd10"},{"code":"Y182.","system":"icd10"},{"code":"Y185.","system":"icd10"},{"code":"Y188.","system":"icd10"},{"code":"Y189.","system":"icd10"},{"code":"Y180.","system":"icd10"},{"code":"Y187.","system":"icd10"},{"code":"Y184.","system":"icd10"},{"code":"Y181.","system":"icd10"},{"code":"Y188.","system":"icd10"},{"code":"Y186.","system":"icd10"},{"code":"Y183.","system":"icd10"},{"code":"Y189.","system":"icd10"},{"code":"Y180.","system":"icd10"},{"code":"Y184.","system":"icd10"},{"code":"Y182.","system":"icd10"},{"code":"Y187.","system":"icd10"},{"code":"Y18..","system":"icd10"},{"code":"Y185.","system":"icd10"},{"code":"X483.","system":"icd10"},{"code":"X482.","system":"icd10"},{"code":"X487.","system":"icd10"},{"code":"X481.","system":"icd10"},{"code":"X48..","system":"icd10"},{"code":"X486.","system":"icd10"},{"code":"X489.","system":"icd10"},{"code":"X488.","system":"icd10"},{"code":"X480.","system":"icd10"},{"code":"X485.","system":"icd10"},{"code":"X484.","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-suicide-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-suicide-pesticide---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-suicide-pesticide---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-suicide-pesticide---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
