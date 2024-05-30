# A. John, 2024.

import sys, csv, re

codes = [{"code":"Y342.","system":"icd10"},{"code":"Y346.","system":"icd10"},{"code":"Y349.","system":"icd10"},{"code":"Y347.","system":"icd10"},{"code":"Y348.","system":"icd10"},{"code":"Y344.","system":"icd10"},{"code":"Y336.","system":"icd10"},{"code":"Y333.","system":"icd10"},{"code":"Y335.","system":"icd10"},{"code":"Y330.","system":"icd10"},{"code":"Y334.","system":"icd10"},{"code":"Y337.","system":"icd10"},{"code":"Y34..","system":"icd10"},{"code":"Y345.","system":"icd10"},{"code":"Y341.","system":"icd10"},{"code":"Y332.","system":"icd10"},{"code":"Y340.","system":"icd10"},{"code":"Y343.","system":"icd10"},{"code":"Y33..","system":"icd10"},{"code":"Y331.","system":"icd10"},{"code":"Y338.","system":"icd10"},{"code":"Y34..","system":"icd10"},{"code":"Y334.","system":"icd10"},{"code":"Y331.","system":"icd10"},{"code":"Y341.","system":"icd10"},{"code":"Y338.","system":"icd10"},{"code":"Y332.","system":"icd10"},{"code":"Y343.","system":"icd10"},{"code":"Y339.","system":"icd10"},{"code":"Y348.","system":"icd10"},{"code":"Y345.","system":"icd10"},{"code":"Y336.","system":"icd10"},{"code":"Y340.","system":"icd10"},{"code":"Y333.","system":"icd10"},{"code":"Y335.","system":"icd10"},{"code":"Y337.","system":"icd10"},{"code":"Y346.","system":"icd10"},{"code":"Y330.","system":"icd10"},{"code":"Y33..","system":"icd10"},{"code":"Y349.","system":"icd10"},{"code":"Y347.","system":"icd10"},{"code":"Y344.","system":"icd10"},{"code":"Y342.","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-suicide-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-suicide-event---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-suicide-event---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-suicide-event---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
