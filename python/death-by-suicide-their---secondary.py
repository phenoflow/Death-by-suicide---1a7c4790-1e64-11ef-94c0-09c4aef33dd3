# A. John, 2024.

import sys, csv, re

codes = [{"code":"X63..","system":"icd10"},{"code":"X66..","system":"icd10"},{"code":"X636.","system":"icd10"},{"code":"X667.","system":"icd10"},{"code":"X664.","system":"icd10"},{"code":"X633.","system":"icd10"},{"code":"X660.","system":"icd10"},{"code":"X665.","system":"icd10"},{"code":"X639.","system":"icd10"},{"code":"X635.","system":"icd10"},{"code":"X638.","system":"icd10"},{"code":"X634.","system":"icd10"},{"code":"X666.","system":"icd10"},{"code":"X669.","system":"icd10"},{"code":"X662.","system":"icd10"},{"code":"X661.","system":"icd10"},{"code":"X668.","system":"icd10"},{"code":"X663.","system":"icd10"},{"code":"X631.","system":"icd10"},{"code":"X630.","system":"icd10"},{"code":"X637.","system":"icd10"},{"code":"X632.","system":"icd10"},{"code":"Y169.","system":"icd10"},{"code":"Y134.","system":"icd10"},{"code":"Y163.","system":"icd10"},{"code":"Y13..","system":"icd10"},{"code":"Y138.","system":"icd10"},{"code":"Y136.","system":"icd10"},{"code":"Y139.","system":"icd10"},{"code":"Y132.","system":"icd10"},{"code":"Y166.","system":"icd10"},{"code":"Y162.","system":"icd10"},{"code":"Y167.","system":"icd10"},{"code":"Y16..","system":"icd10"},{"code":"Y137.","system":"icd10"},{"code":"Y133.","system":"icd10"},{"code":"Y161.","system":"icd10"},{"code":"Y165.","system":"icd10"},{"code":"Y135.","system":"icd10"},{"code":"Y164.","system":"icd10"},{"code":"Y131.","system":"icd10"},{"code":"Y130.","system":"icd10"},{"code":"Y168.","system":"icd10"},{"code":"Y160.","system":"icd10"},{"code":"Y131.","system":"icd10"},{"code":"Y160.","system":"icd10"},{"code":"Y130.","system":"icd10"},{"code":"Y161.","system":"icd10"},{"code":"Y135.","system":"icd10"},{"code":"Y168.","system":"icd10"},{"code":"Y169.","system":"icd10"},{"code":"Y134.","system":"icd10"},{"code":"Y133.","system":"icd10"},{"code":"Y13..","system":"icd10"},{"code":"Y166.","system":"icd10"},{"code":"Y139.","system":"icd10"},{"code":"Y137.","system":"icd10"},{"code":"Y167.","system":"icd10"},{"code":"Y16..","system":"icd10"},{"code":"Y136.","system":"icd10"},{"code":"Y132.","system":"icd10"},{"code":"Y165.","system":"icd10"},{"code":"Y164.","system":"icd10"},{"code":"Y138.","system":"icd10"},{"code":"Y162.","system":"icd10"},{"code":"Y163.","system":"icd10"},{"code":"X433.","system":"icd10"},{"code":"X435.","system":"icd10"},{"code":"X462.","system":"icd10"},{"code":"X466.","system":"icd10"},{"code":"X46..","system":"icd10"},{"code":"X467.","system":"icd10"},{"code":"X430.","system":"icd10"},{"code":"X434.","system":"icd10"},{"code":"X465.","system":"icd10"},{"code":"X461.","system":"icd10"},{"code":"X464.","system":"icd10"},{"code":"X463.","system":"icd10"},{"code":"X468.","system":"icd10"},{"code":"X436.","system":"icd10"},{"code":"X438.","system":"icd10"},{"code":"X437.","system":"icd10"},{"code":"X460.","system":"icd10"},{"code":"X431.","system":"icd10"},{"code":"X43..","system":"icd10"},{"code":"X439.","system":"icd10"},{"code":"X432.","system":"icd10"},{"code":"X469.","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-suicide-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-suicide-their---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-suicide-their---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-suicide-their---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
