# A. John, 2024.

import sys, csv, re

codes = [{"code":"X644.","system":"icd10"},{"code":"X649.","system":"icd10"},{"code":"X648.","system":"icd10"},{"code":"X642.","system":"icd10"},{"code":"X643.","system":"icd10"},{"code":"X646.","system":"icd10"},{"code":"X640.","system":"icd10"},{"code":"X64..","system":"icd10"},{"code":"X641.","system":"icd10"},{"code":"X647.","system":"icd10"},{"code":"X645.","system":"icd10"},{"code":"Y149.","system":"icd10"},{"code":"Y141.","system":"icd10"},{"code":"Y140.","system":"icd10"},{"code":"Y148.","system":"icd10"},{"code":"Y145.","system":"icd10"},{"code":"Y146.","system":"icd10"},{"code":"Y142.","system":"icd10"},{"code":"Y147.","system":"icd10"},{"code":"Y14..","system":"icd10"},{"code":"Y144.","system":"icd10"},{"code":"Y143.","system":"icd10"},{"code":"Y143.","system":"icd10"},{"code":"Y145.","system":"icd10"},{"code":"Y142.","system":"icd10"},{"code":"Y148.","system":"icd10"},{"code":"Y146.","system":"icd10"},{"code":"Y147.","system":"icd10"},{"code":"Y14..","system":"icd10"},{"code":"Y149.","system":"icd10"},{"code":"Y144.","system":"icd10"},{"code":"Y140.","system":"icd10"},{"code":"Y141.","system":"icd10"},{"code":"X442.","system":"icd10"},{"code":"X449.","system":"icd10"},{"code":"X446.","system":"icd10"},{"code":"X445.","system":"icd10"},{"code":"X441.","system":"icd10"},{"code":"X44..","system":"icd10"},{"code":"X444.","system":"icd10"},{"code":"X440.","system":"icd10"},{"code":"X448.","system":"icd10"},{"code":"X443.","system":"icd10"},{"code":"X447.","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-suicide-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["biological-death-by-suicide---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["biological-death-by-suicide---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["biological-death-by-suicide---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
