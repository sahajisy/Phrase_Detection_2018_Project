
import re
def main_regex_matcher(path_test):
    master_list=[]
    sent_list=[]
    data = open(path_test,'r')
    for text in data:
        found = 0
        small_master_list=[]
        sent_list.append(text)
    
        m = re.search(' to (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) by ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Tell (.+?) me ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) after ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) by ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Thanks (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Please (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) will ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) me ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) and ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' that (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) before ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 11 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) this ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) tonight ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' that (.+?) tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' that (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) everyday ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) liquid ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' remember (.+?) this ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' dmello (.+?) Tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Pls (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' now (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' To (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 6 (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' we (.+?) varsha ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) Whom ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 9pm ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' know (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) tday ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' my (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Is (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) everyday ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' really (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' that (.+?) By ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) daily ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 2 (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' need (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' remind (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 7 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) At ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) everyday ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' that (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Actually (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) as ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' only (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' it (.+?) during ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' the (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' reminder (.+?) Today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' fr (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) 10 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' the (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Your (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' set (.+?) 6 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 10 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' if (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' I (.+?) asked ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' reminder (.+?) to ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' your (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' should (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' remind (.+?) tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Good (.+?) Afternoon ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) tomo ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' u (.+?) an ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' club7pm (.+?) also ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' have (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) to ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' remember (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' you (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' For (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) sunday ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' And (.+?) to ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' actually (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Plz (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) daily ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' know (.+?) are ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' m (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' you (.+?) so ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Hey (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' abt (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Is (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) tonight ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) 4 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) tonight ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 1 (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' pause (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' kar (.+?) reminder ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' a (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 35am (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 3 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' u (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Wednesday (.+?) by ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) tommorow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) Nov ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' my (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' reminder (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' About (.+?) 8 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' tomorrow (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' but (.+?) I ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 7am ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' a (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' that (.+?) by ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' To (.+?) At ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) 8 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) plz ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) Monday ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) 9 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) Arijit ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' it (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' the (.+?) by ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 4pm ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' had (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' add (.+?) aT ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' at (.+?) before ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' all (.+?) now ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' monday (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' an (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' have (.+?) plz ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) a ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' need (.+?) before ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' all (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' have (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' have (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' also (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' My (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' you (.+?) when ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' everyday (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) 9 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' am (.+?) please ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) by ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) 9 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' all (.+?) immediately ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) nov ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' u (.+?) after ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) please ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' too (.+?) 6 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Reminder (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Reminder (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' abt (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' had (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' had (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 9 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) Remind ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' had (.+?) before ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' wen (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 12222 (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Remind (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' u (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' u (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' abo (.+?) t ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me for (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' reminder for (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me about (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' have to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' reminder to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me of (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' want to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Thanks for (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Remind to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Reminder to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Tell me (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Reminder for (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about Brand (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' remind me (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' need to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' pm to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Remind me (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' am to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' remind to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' tomorrow to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Can u (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me that (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' I have (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' pm for (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' pm about (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' tell me (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' today for (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' today to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' know about (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' I need (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' reminder of (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me the (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' a reminder (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 6pm to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' supposed to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to know (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' u to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me on (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' I had (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 30am to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' going to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 30 to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Thursday to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' minutes to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' arent you (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me know (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Will u (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' is to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' I am (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 9am to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 9 to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' is for (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' am for (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Want to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' set to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' it for (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 6pm about (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' u for (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to schedule (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' i will (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Could u (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' can u (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Can you (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me if (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Saturday to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Need to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)

        if found==0 : # if none of the patterns match give it as Not found
            small_master_list.append('Not Found')
        master_list.append(small_master_list)

    no_no_words=['on','for','to','at','by'] # list of words which if occured in the output will be penalised while giving a score
    final_output=[]
    ############ selecting one from the options
    for options in master_list:
        if len(options)==1:
            final_output.append(options[0])#if only one pattern extracted use it 
        else:
            sent_score_list=[] # else score all the options to select the best one
            for option in options:
                l=option.split()
                score = 0
                score = len(l)
                for word in l:
                    if word in no_no_words:
                        score = score -3 #penalise the no_no_words
                    else:
                        pass
                sent_score_list.append(score)
            m = max(sent_score_list)
            indx=[i for i, j in enumerate(sent_score_list) if j == m] # returns a list of all the index which have max score
            index = indx[-1]#pick the last element as an index 
            final_output.append(options[index])

    tups=zip(sent_list, final_output)
    final_list = [list(l) for l in tups]

    for small_list in final_list:
        target = open("output.txt", "a")
        target.write('\n')
        target.write(' '.join(small_list[0].split())+'\t'+small_list[1])
        target.write('\n')
        target.close()
    return(final_output)
    

import re
def main_regex_matcher(path_test):
    master_list=[]
    sent_list=[]
    data = open(path_test,'r')
    for text in data:
        found = 0
        small_master_list=[]
        sent_list.append(text)
    
        m = re.search(' to (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) by ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Tell (.+?) me ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) after ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) by ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Thanks (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Please (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) will ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) me ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) and ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' that (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) before ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 11 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) this ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) tonight ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' that (.+?) tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' that (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) everyday ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) liquid ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' remember (.+?) this ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' dmello (.+?) Tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Pls (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' now (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' To (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 6 (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' we (.+?) varsha ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) Whom ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 9pm ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' know (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) tday ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' my (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Is (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) everyday ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' really (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' that (.+?) By ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) daily ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 2 (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' need (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' remind (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 7 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) At ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) everyday ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' that (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Actually (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) as ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' only (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' it (.+?) during ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' the (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' reminder (.+?) Today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' fr (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) 10 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' the (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Your (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' set (.+?) 6 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 10 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' if (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' I (.+?) asked ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' reminder (.+?) to ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' your (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' should (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' remind (.+?) tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Good (.+?) Afternoon ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) tomo ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' u (.+?) an ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' club7pm (.+?) also ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' have (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) to ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' remember (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' you (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' For (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) sunday ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' And (.+?) to ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' actually (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Plz (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) daily ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' know (.+?) are ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' m (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' you (.+?) so ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Hey (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' abt (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Is (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) tonight ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) 4 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) tonight ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 1 (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' pause (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' kar (.+?) reminder ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' a (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 35am (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 3 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' u (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Wednesday (.+?) by ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) tommorow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) Nov ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' my (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' reminder (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' About (.+?) 8 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' tomorrow (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' but (.+?) I ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 7am ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' a (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' that (.+?) by ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' To (.+?) At ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) 8 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) plz ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) Monday ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) 9 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) Arijit ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' it (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' the (.+?) by ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 4pm ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' had (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' add (.+?) aT ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' at (.+?) before ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' all (.+?) now ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' monday (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' an (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' have (.+?) plz ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) a ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' need (.+?) before ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' all (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' have (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' have (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' also (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' My (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' you (.+?) when ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' everyday (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) 9 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' am (.+?) please ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) by ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) 9 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' all (.+?) immediately ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) nov ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' u (.+?) after ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) please ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' too (.+?) 6 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Reminder (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Reminder (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' abt (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' had (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' had (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 9 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) Remind ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' had (.+?) before ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' wen (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 12222 (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Remind (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' u (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' u (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' abo (.+?) t ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me for (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' reminder for (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me about (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' have to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' reminder to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me of (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' want to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Thanks for (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Remind to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Reminder to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Tell me (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Reminder for (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about Brand (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' remind me (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' need to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' pm to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Remind me (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' am to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' remind to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' tomorrow to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Can u (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me that (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' I have (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' pm for (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' pm about (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' tell me (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' today for (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' today to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' know about (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' I need (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' reminder of (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me the (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' a reminder (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 6pm to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' supposed to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to know (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' u to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me on (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' I had (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 30am to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' going to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 30 to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Thursday to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' minutes to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' arent you (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me know (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Will u (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' is to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' I am (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 9am to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 9 to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' is for (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' am for (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Want to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' set to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' it for (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 6pm about (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' u for (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to schedule (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' i will (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Could u (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' can u (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Can you (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me if (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Saturday to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Need to (.*)', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)

        if found==0 : # if none of the patterns match give it as Not found
            small_master_list.append('Not Found')
        master_list.append(small_master_list)

    no_no_words=['on','for','to','at','by'] # list of words which if occured in the output will be penalised while giving a score
    final_output=[]
    ############ selecting one from the options
    for options in master_list:
        if len(options)==1:
            final_output.append(options[0])#if only one pattern extracted use it 
        else:
            sent_score_list=[] # else score all the options to select the best one
            for option in options:
                l=option.split()
                score = 0
                score = len(l)
                for word in l:
                    if word in no_no_words:
                        score = score -3 #penalise the no_no_words
                    else:
                        pass
                sent_score_list.append(score)
            m = max(sent_score_list)
            indx=[i for i, j in enumerate(sent_score_list) if j == m] # returns a list of all the index which have max score
            index = indx[-1]#pick the last element as an index 
            final_output.append(options[index])

    tups=zip(sent_list, final_output)
    final_list = [list(l) for l in tups]

    for small_list in final_list:
        target = open("output.txt", "a")
        target.write('\n')
        target.write(' '.join(small_list[0].split())+'\t'+small_list[1])
        target.write('\n')
        target.close()
    return(final_output)
    
