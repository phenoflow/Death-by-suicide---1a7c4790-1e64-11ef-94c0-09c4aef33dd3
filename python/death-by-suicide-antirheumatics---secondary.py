# A. John, 2024.

import sys, csv, re

codes = [{"code":"X604.","system":"icd10"},{"code":"X609.","system":"icd10"},{"code":"X607.","system":"icd10"},{"code":"X605.","system":"icd10"},{"code":"X608.","system":"icd10"},{"code":"X601.","system":"icd10"},{"code":"X60..","system":"icd10"},{"code":"X602.","system":"icd10"},{"code":"X600.","system":"icd10"},{"code":"X603.","system":"icd10"},{"code":"X606.","system":"icd10"},{"code":"Y107.","system":"icd10"},{"code":"Y109.","system":"icd10"},{"code":"Y102.","system":"icd10"},{"code":"Y100.","system":"icd10"},{"code":"Y108.","system":"icd10"},{"code":"Y104.","system":"icd10"},{"code":"Y106.","system":"icd10"},{"code":"Y101.","system":"icd10"},{"code":"Y103.","system":"icd10"},{"code":"Y10..","system":"icd10"},{"code":"Y105.","system":"icd10"},{"code":"Y10..","system":"icd10"},{"code":"Y101.","system":"icd10"},{"code":"Y103.","system":"icd10"},{"code":"Y105.","system":"icd10"},{"code":"Y109.","system":"icd10"},{"code":"Y100.","system":"icd10"},{"code":"Y108.","system":"icd10"},{"code":"Y107.","system":"icd10"},{"code":"Y106.","system":"icd10"},{"code":"Y104.","system":"icd10"},{"code":"Y102.","system":"icd10"},{"code":"X405.","system":"icd10"},{"code":"X404.","system":"icd10"},{"code":"X409.","system":"icd10"},{"code":"X402.","system":"icd10"},{"code":"X403.","system":"icd10"},{"code":"X406.","system":"icd10"},{"code":"X408.","system":"icd10"},{"code":"X400.","system":"icd10"},{"code":"X401.","system":"icd10"},{"code":"X407.","system":"icd10"},{"code":"X40..","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-suicide-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-suicide-antirheumatics---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-suicide-antirheumatics---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-suicide-antirheumatics---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
