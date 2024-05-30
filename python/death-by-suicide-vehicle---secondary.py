# A. John, 2024.

import sys, csv, re

codes = [{"code":"X820.","system":"icd10"},{"code":"X823.","system":"icd10"},{"code":"X828.","system":"icd10"},{"code":"X825.","system":"icd10"},{"code":"X824.","system":"icd10"},{"code":"X829.","system":"icd10"},{"code":"X82..","system":"icd10"},{"code":"X822.","system":"icd10"},{"code":"X827.","system":"icd10"},{"code":"X826.","system":"icd10"},{"code":"X821.","system":"icd10"},{"code":"Y328.","system":"icd10"},{"code":"Y32..","system":"icd10"},{"code":"Y320.","system":"icd10"},{"code":"Y327.","system":"icd10"},{"code":"Y324.","system":"icd10"},{"code":"Y323.","system":"icd10"},{"code":"Y326.","system":"icd10"},{"code":"Y322.","system":"icd10"},{"code":"Y321.","system":"icd10"},{"code":"Y329.","system":"icd10"},{"code":"Y325.","system":"icd10"},{"code":"Y32..","system":"icd10"},{"code":"Y326.","system":"icd10"},{"code":"Y324.","system":"icd10"},{"code":"Y325.","system":"icd10"},{"code":"Y321.","system":"icd10"},{"code":"Y328.","system":"icd10"},{"code":"Y329.","system":"icd10"},{"code":"Y327.","system":"icd10"},{"code":"Y323.","system":"icd10"},{"code":"Y320.","system":"icd10"},{"code":"Y322.","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-suicide-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-suicide-vehicle---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-suicide-vehicle---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-suicide-vehicle---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
