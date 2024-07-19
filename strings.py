############################ reverse #######################################
def reverse(string1):
    reverse_list=list(string1)
    start=0
    end=len(reverse_list)-1
    while(start<end):
        reverse_list[start],reverse_list[end]=reverse_list[end],reverse_list[start]
        start+=1
        end-=1
    return "".join(reverse_list)
print(reverse("hello"))


########################## target elements more than one #######################
def target_elem_morethan_one(str1,target):
    count=0
    for i in str1:
        if i==target:
            count+=1
            if count>1:
                return i
    return None
print(target_elem_morethan_one("heyyylloo",'l'))

################################# concated string ##################################
def concated_string(str1,str2):
    return str1+" "+str2
print(concated_string("hello","how r u"))

################################ find repeated elem #################################
def find_repeated_elem(str1):
    count=0
    str2=set()
    for i in str1:
        if i in str2:
            count+=1
        else:
            str2.add(i)
    return count
        
print(find_repeated_elem("helllo"))

####################################remove dup char#########################################
def remove_dup_char(str1):
    seen=set()
    result=[]
    for i in str1:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return "".join(result)
print(remove_dup_char("heeey"))

####################################last string length#################################
def last_string_length(str1):
    sent=str1.split()
    if sent:
        return len(sent[-1])
    else:
        return 0

print(last_string_length(" move on jaya move on"))

######################################sentence length#########################################

def sentence_length(str1):
    count=0
    for i in str1:
        count+=1
    return count
print(sentence_length("i want to learn astronomy"))

###without space
def sentence_length(str1):
    count=0
    for i in str1:
        if i !=" ":
         count+=1
    return count
print(sentence_length("i want to learn astronomy"))

def largest_word(string):
    string1=string.split()
    largest_word=0
    large=" "
    for i in string1:
       if len(i) > largest_word:
           largest_word=len(i)
           large=i
    return large
print(largest_word("movee on jayaa move on"))