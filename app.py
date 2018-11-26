import random
from datetime import datetime

DEFAULT_MEETING_SIZE = 3  # Meeting engager
NEW_MEMBER_CRITERIA = 15 # days
MEMBER_LIST = [ # [name, entered_at]
    ['junseon', '2018-01-01'],
    ['shbaek', '2018-01-01'], 
    ['tylor_shin', '2018-01-01'],
    ['taeheon', '2018-01-01'],
    ['hyeon', '2018-01-01'],
    ['yoonji', '2018-01-01'],
    ['yukyeong', '2018-01-01'],
    ['sanghyuk.jung', '2018-09-17'],
    ['changbae', '2018-11-05'],
    ['YujeongNoh', '2018-11-26']
]

def create_random_meeting(member_list, meeting_size = DEFAULT_MEETING_SIZE):
    pool_size = len(member_list)

    meeting_groups = []
    remained_size = pool_size
    remained_members = member_list

    while (True):
        if remained_size > meeting_size:
            meeting_group = [remained_members[n] for n in random.sample(range(remained_size), meeting_size)]
            remained_size -= len(meeting_group)
            remained_members = [item for item in remained_members if item not in meeting_group]
            meeting_groups.append(meeting_group)
        else:
            meeting_group = remained_members
            meeting_groups.append(meeting_group)
            break
    return meeting_groups
    
if __name__== "__main__":
    meeting_size = DEFAULT_MEETING_SIZE
    result = create_random_meeting(MEMBER_LIST, meeting_size=meeting_size)

    # print result
    print ("\n\nWelcome to gravity meeting: %s\n===========================================" % str(datetime.now()))
    print ("\nTotal are %d members, and each group have %d members:\n" % (len(MEMBER_LIST), meeting_size))

    for m in result:
        print ("Organizer: @" + str(m[0]) + ", " + str(m))
    
    print ("\n\n")
