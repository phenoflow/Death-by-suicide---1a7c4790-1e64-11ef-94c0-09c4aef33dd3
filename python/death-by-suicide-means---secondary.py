# A. John, 2024.

import sys, csv, re

codes = [{"code":"X831.","system":"icd10"},{"code":"X832.","system":"icd10"},{"code":"X846.","system":"icd10"},{"code":"X840.","system":"icd10"},{"code":"X833.","system":"icd10"},{"code":"X843.","system":"icd10"},{"code":"X849.","system":"icd10"},{"code":"X838.","system":"icd10"},{"code":"X844.","system":"icd10"},{"code":"X839.","system":"icd10"},{"code":"X84..","system":"icd10"},{"code":"X842.","system":"icd10"},{"code":"X845.","system":"icd10"},{"code":"X834.","system":"icd10"},{"code":"X841.","system":"icd10"},{"code":"X835.","system":"icd10"},{"code":"X837.","system":"icd10"},{"code":"X836.","system":"icd10"},{"code":"X830.","system":"icd10"},{"code":"X848.","system":"icd10"},{"code":"X83..","system":"icd10"},{"code":"X847.","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-suicide-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-suicide-means---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-suicide-means---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-suicide-means---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
