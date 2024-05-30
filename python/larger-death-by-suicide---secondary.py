# A. John, 2024.

import sys, csv, re

codes = [{"code":"X730.","system":"icd10"},{"code":"X732.","system":"icd10"},{"code":"X734.","system":"icd10"},{"code":"X733.","system":"icd10"},{"code":"X738.","system":"icd10"},{"code":"X731.","system":"icd10"},{"code":"X736.","system":"icd10"},{"code":"X73..","system":"icd10"},{"code":"X737.","system":"icd10"},{"code":"X735.","system":"icd10"},{"code":"X739.","system":"icd10"},{"code":"Y232.","system":"icd10"},{"code":"Y23..","system":"icd10"},{"code":"Y233.","system":"icd10"},{"code":"Y236.","system":"icd10"},{"code":"Y234.","system":"icd10"},{"code":"Y238.","system":"icd10"},{"code":"Y235.","system":"icd10"},{"code":"Y231.","system":"icd10"},{"code":"Y230.","system":"icd10"},{"code":"Y239.","system":"icd10"},{"code":"Y237.","system":"icd10"},{"code":"Y238.","system":"icd10"},{"code":"Y231.","system":"icd10"},{"code":"Y239.","system":"icd10"},{"code":"Y230.","system":"icd10"},{"code":"Y232.","system":"icd10"},{"code":"Y235.","system":"icd10"},{"code":"Y23..","system":"icd10"},{"code":"Y236.","system":"icd10"},{"code":"Y237.","system":"icd10"},{"code":"Y233.","system":"icd10"},{"code":"Y234.","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-suicide-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["larger-death-by-suicide---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["larger-death-by-suicide---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["larger-death-by-suicide---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
