import re

f = open(r"test_article_17m.json","r")
f2 = open(r"test_article_processed2.json","w+")
f2.write("{\n")
for line in f.readlines():
    new_string = line.replace('<br />', '').replace(r'\n', '') #.replace('\\\"', '').replace('\\"', '').replace('\\', '').replace('“', '').replace('”', '')
    # new_string = re.sub('[0-9]*/[0-9]*', '', new_string)
    new_string = re.sub(r'[^A-Za-z0-9\. ]+', '', new_string)
    # print(len(new_string))
    f2.write(new_string[:104850])
f2.write("\n}")
f2.close()
f.close()
