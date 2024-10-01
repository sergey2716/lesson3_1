def count_calls():
    global calls
    calls += 1
calls = 0
def string_info(string):
    count_calls()
    i = ()
    i += (len(string),string.upper(),string.lower())
    return i
def is_contains(string_info,list_to_search):
    count_calls()
    i = True
    j = ','.join(list_to_search).lower()
    if j.find(string_info.lower()) == -1:
        i =False
    return i



print(string_info('nik'))
print(string_info('ANTON'))
print(is_contains('anton',('olga','max','anton')))
print(is_contains('anton',('olga','max','nik')))
print(calls)