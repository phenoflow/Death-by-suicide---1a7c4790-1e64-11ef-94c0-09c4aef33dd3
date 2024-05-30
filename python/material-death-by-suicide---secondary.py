# A. John, 2024.

import sys, csv, re

codes = [{"code":"X754.","system":"icd10"},{"code":"X751.","system":"icd10"},{"code":"X750.","system":"icd10"},{"code":"X758.","system":"icd10"},{"code":"X755.","system":"icd10"},{"code":"X753.","system":"icd10"},{"code":"X752.","system":"icd10"},{"code":"X756.","system":"icd10"},{"code":"X757.","system":"icd10"},{"code":"X75..","system":"icd10"},{"code":"X759.","system":"icd10"},{"code":"Y255.","system":"icd10"},{"code":"Y259.","system":"icd10"},{"code":"Y25..","system":"icd10"},{"code":"Y254.","system":"icd10"},{"code":"Y252.","system":"icd10"},{"code":"Y250.","system":"icd10"},{"code":"Y253.","system":"icd10"},{"code":"Y257.","system":"icd10"},{"code":"Y256.","system":"icd10"},{"code":"Y258.","system":"icd10"},{"code":"Y251.","system":"icd10"},{"code":"Y257.","system":"icd10"},{"code":"Y25..","system":"icd10"},{"code":"Y255.","system":"icd10"},{"code":"Y256.","system":"icd10"},{"code":"Y254.","system":"icd10"},{"code":"Y253.","system":"icd10"},{"code":"Y258.","system":"icd10"},{"code":"Y250.","system":"icd10"},{"code":"Y259.","system":"icd10"},{"code":"Y252.","system":"icd10"},{"code":"Y251.","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-suicide-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["material-death-by-suicide---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["material-death-by-suicide---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["material-death-by-suicide---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
