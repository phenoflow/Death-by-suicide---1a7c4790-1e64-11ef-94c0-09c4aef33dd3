# A. John, 2024.

import sys, csv, re

codes = [{"code":"X78..","system":"icd10"},{"code":"X792.","system":"icd10"},{"code":"X815.","system":"icd10"},{"code":"X818.","system":"icd10"},{"code":"X799.","system":"icd10"},{"code":"X811.","system":"icd10"},{"code":"X81..","system":"icd10"},{"code":"X793.","system":"icd10"},{"code":"X796.","system":"icd10"},{"code":"X782.","system":"icd10"},{"code":"X780.","system":"icd10"},{"code":"X790.","system":"icd10"},{"code":"X786.","system":"icd10"},{"code":"X784.","system":"icd10"},{"code":"X813.","system":"icd10"},{"code":"X79..","system":"icd10"},{"code":"X785.","system":"icd10"},{"code":"X817.","system":"icd10"},{"code":"X814.","system":"icd10"},{"code":"X797.","system":"icd10"},{"code":"X791.","system":"icd10"},{"code":"X794.","system":"icd10"},{"code":"X781.","system":"icd10"},{"code":"X810.","system":"icd10"},{"code":"X816.","system":"icd10"},{"code":"X798.","system":"icd10"},{"code":"X812.","system":"icd10"},{"code":"X787.","system":"icd10"},{"code":"X795.","system":"icd10"},{"code":"X783.","system":"icd10"},{"code":"X819.","system":"icd10"},{"code":"X789.","system":"icd10"},{"code":"X788.","system":"icd10"},{"code":"Y28..","system":"icd10"},{"code":"Y280.","system":"icd10"},{"code":"Y281.","system":"icd10"},{"code":"Y298.","system":"icd10"},{"code":"Y282.","system":"icd10"},{"code":"Y296.","system":"icd10"},{"code":"Y284.","system":"icd10"},{"code":"Y287.","system":"icd10"},{"code":"Y297.","system":"icd10"},{"code":"Y299.","system":"icd10"},{"code":"Y290.","system":"icd10"},{"code":"Y295.","system":"icd10"},{"code":"Y286.","system":"icd10"},{"code":"Y288.","system":"icd10"},{"code":"Y289.","system":"icd10"},{"code":"Y283.","system":"icd10"},{"code":"Y285.","system":"icd10"},{"code":"Y293.","system":"icd10"},{"code":"Y291.","system":"icd10"},{"code":"Y292.","system":"icd10"},{"code":"Y294.","system":"icd10"},{"code":"Y29..","system":"icd10"},{"code":"Y286.","system":"icd10"},{"code":"Y289.","system":"icd10"},{"code":"Y296.","system":"icd10"},{"code":"Y292.","system":"icd10"},{"code":"Y294.","system":"icd10"},{"code":"Y28..","system":"icd10"},{"code":"Y287.","system":"icd10"},{"code":"Y293.","system":"icd10"},{"code":"Y299.","system":"icd10"},{"code":"Y281.","system":"icd10"},{"code":"Y284.","system":"icd10"},{"code":"Y29..","system":"icd10"},{"code":"Y290.","system":"icd10"},{"code":"Y298.","system":"icd10"},{"code":"Y288.","system":"icd10"},{"code":"Y285.","system":"icd10"},{"code":"Y297.","system":"icd10"},{"code":"Y282.","system":"icd10"},{"code":"Y280.","system":"icd10"},{"code":"Y283.","system":"icd10"},{"code":"Y295.","system":"icd10"},{"code":"Y291.","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-suicide-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-suicide-objects---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-suicide-objects---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-suicide-objects---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
