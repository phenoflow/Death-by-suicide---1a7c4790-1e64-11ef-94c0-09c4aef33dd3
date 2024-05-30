# A. John, 2024.

import sys, csv, re

codes = [{"code":"X705.","system":"icd10"},{"code":"X702.","system":"icd10"},{"code":"X704.","system":"icd10"},{"code":"X709.","system":"icd10"},{"code":"X703.","system":"icd10"},{"code":"X70..","system":"icd10"},{"code":"X706.","system":"icd10"},{"code":"X707.","system":"icd10"},{"code":"X708.","system":"icd10"},{"code":"X700.","system":"icd10"},{"code":"X701.","system":"icd10"},{"code":"Y203.","system":"icd10"},{"code":"Y208.","system":"icd10"},{"code":"Y201.","system":"icd10"},{"code":"Y202.","system":"icd10"},{"code":"Y209.","system":"icd10"},{"code":"Y20..","system":"icd10"},{"code":"Y205.","system":"icd10"},{"code":"Y206.","system":"icd10"},{"code":"Y204.","system":"icd10"},{"code":"Y207.","system":"icd10"},{"code":"Y200.","system":"icd10"},{"code":"Y20..","system":"icd10"},{"code":"Y204.","system":"icd10"},{"code":"Y203.","system":"icd10"},{"code":"Y207.","system":"icd10"},{"code":"Y208.","system":"icd10"},{"code":"Y201.","system":"icd10"},{"code":"Y200.","system":"icd10"},{"code":"Y206.","system":"icd10"},{"code":"Y205.","system":"icd10"},{"code":"Y209.","system":"icd10"},{"code":"Y202.","system":"icd10"},{"code":"W755.","system":"icd10"},{"code":"W75..","system":"icd10"},{"code":"W751.","system":"icd10"},{"code":"W754.","system":"icd10"},{"code":"W757.","system":"icd10"},{"code":"W759.","system":"icd10"},{"code":"W750.","system":"icd10"},{"code":"W753.","system":"icd10"},{"code":"W756.","system":"icd10"},{"code":"W758.","system":"icd10"},{"code":"W752.","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-suicide-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-suicide-suffocation---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-suicide-suffocation---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-suicide-suffocation---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
