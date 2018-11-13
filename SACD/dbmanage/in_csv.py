import csv



def write_csv(filename, tabla):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            print "cucu"
            writer = csv.writer(csvfile)
            writer.writerows(tabla)
        return True
    except Exception as e:
        print e
        return False
