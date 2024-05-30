# A. John, 2024.

import sys, csv, re

codes = [{"code":"X659.","system":"icd10"},{"code":"X655.","system":"icd10"},{"code":"X65..","system":"icd10"},{"code":"X653.","system":"icd10"},{"code":"X657.","system":"icd10"},{"code":"X651.","system":"icd10"},{"code":"X656.","system":"icd10"},{"code":"X654.","system":"icd10"},{"code":"X658.","system":"icd10"},{"code":"X652.","system":"icd10"},{"code":"X650.","system":"icd10"},{"code":"Y150.","system":"icd10"},{"code":"Y152.","system":"icd10"},{"code":"Y15..","system":"icd10"},{"code":"Y156.","system":"icd10"},{"code":"Y158.","system":"icd10"},{"code":"Y151.","system":"icd10"},{"code":"Y157.","system":"icd10"},{"code":"Y153.","system":"icd10"},{"code":"Y159.","system":"icd10"},{"code":"Y154.","system":"icd10"},{"code":"Y155.","system":"icd10"},{"code":"Y159.","system":"icd10"},{"code":"Y155.","system":"icd10"},{"code":"Y150.","system":"icd10"},{"code":"Y156.","system":"icd10"},{"code":"Y152.","system":"icd10"},{"code":"Y151.","system":"icd10"},{"code":"Y158.","system":"icd10"},{"code":"Y15..","system":"icd10"},{"code":"Y153.","system":"icd10"},{"code":"Y157.","system":"icd10"},{"code":"Y154.","system":"icd10"},{"code":"X457.","system":"icd10"},{"code":"X45..","system":"icd10"},{"code":"X458.","system":"icd10"},{"code":"X454.","system":"icd10"},{"code":"X450.","system":"icd10"},{"code":"X452.","system":"icd10"},{"code":"X453.","system":"icd10"},{"code":"X459.","system":"icd10"},{"code":"X456.","system":"icd10"},{"code":"X455.","system":"icd10"},{"code":"X451.","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-suicide-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-suicide-alcohol---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-suicide-alcohol---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-suicide-alcohol---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
