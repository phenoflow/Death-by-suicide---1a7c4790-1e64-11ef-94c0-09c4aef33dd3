# A. John, 2024.

import sys, csv, re

codes = [{"code":"X613.","system":"icd10"},{"code":"X61..","system":"icd10"},{"code":"X612.","system":"icd10"},{"code":"X619.","system":"icd10"},{"code":"X610.","system":"icd10"},{"code":"X614.","system":"icd10"},{"code":"X618.","system":"icd10"},{"code":"X615.","system":"icd10"},{"code":"X617.","system":"icd10"},{"code":"X611.","system":"icd10"},{"code":"X616.","system":"icd10"},{"code":"Y110.","system":"icd10"},{"code":"Y119.","system":"icd10"},{"code":"Y115.","system":"icd10"},{"code":"Y11..","system":"icd10"},{"code":"Y118.","system":"icd10"},{"code":"Y117.","system":"icd10"},{"code":"Y113.","system":"icd10"},{"code":"Y112.","system":"icd10"},{"code":"Y111.","system":"icd10"},{"code":"Y116.","system":"icd10"},{"code":"Y114.","system":"icd10"},{"code":"Y11..","system":"icd10"},{"code":"Y115.","system":"icd10"},{"code":"Y114.","system":"icd10"},{"code":"Y116.","system":"icd10"},{"code":"Y118.","system":"icd10"},{"code":"Y111.","system":"icd10"},{"code":"Y119.","system":"icd10"},{"code":"Y112.","system":"icd10"},{"code":"Y117.","system":"icd10"},{"code":"Y110.","system":"icd10"},{"code":"Y113.","system":"icd10"},{"code":"X414.","system":"icd10"},{"code":"X413.","system":"icd10"},{"code":"X418.","system":"icd10"},{"code":"X410.","system":"icd10"},{"code":"X41..","system":"icd10"},{"code":"X412.","system":"icd10"},{"code":"X415.","system":"icd10"},{"code":"X417.","system":"icd10"},{"code":"X416.","system":"icd10"},{"code":"X411.","system":"icd10"},{"code":"X419.","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-suicide-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["psychotropic-death-by-suicide---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["psychotropic-death-by-suicide---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["psychotropic-death-by-suicide---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
