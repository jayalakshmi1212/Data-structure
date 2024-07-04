# string="hello jaya"

# s=set()
# v=0
# for i in string:
#     if i in s:
#         v+=1
#     else:
#         s.add(i)
# print(v)

# def reverse_string(string):
#     reverse_list=list(string)
#     start=0
#     end=len(reverse_list)-1
#     while(start<end):
#         reverse_list[start],reverse_list[end]=reverse_list[end],reverse_list[start]
#         start+=1
#         end-=1
#     return "".join(reverse_list)
# reversed_s=reverse_string(string)
# print(reversed_s)

string_pal="malayalam"
# def check_palindrome(string_pal):
#     start=0
#     end=len(string_pal)-1
#     while(start<end):
#         if string_pal[start]==string_pal[end]:
#             return True
#         else:
#             return False
# find_pal=check_palindrome(string_pal)
# print(find_pal)


# def check_palindrome(string_pal):
#     start = 0
#     end = len(string_pal) - 1
    
#     while start < end:
#         if string_pal[start] != string_pal[end]:
#             return False
#         start += 1
#         end -= 1
    
#     return True

# def check_dup(string_pal,key):
#     v=0
#     for i in range(len(string_pal)):
#         if string_pal[i]==key:
#             v+=1
#     return v
# key='a'
# r=check_dup(string_pal,key)
# print(r)


def remove_dup(string_pal):
    val=set()
    result=""
    for i in string_pal:
        if i not in val:
            val.add(i)
            result+= i
    return result
remove=remove_dup(string_pal)
print(remove)