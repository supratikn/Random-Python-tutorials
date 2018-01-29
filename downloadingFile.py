from urllib import request


url="https://www.ibm.com/support/knowledgecenter/SVU13_7.2.1/com.ibm.ismsaas.doc/reference/AssetsImportCompleteSample.csv"

def downloadData(csv_url):

    response = request.urlopen(csv_url)
    csv = response.read()
    csvStr =str(csv)
    lines= csvStr.split("\\n")
    destination=r'goog.csv'
    file =open(destination,"w")
    for line in lines:
        file.write(line+ "\n")
    file.close()


downloadData(url)