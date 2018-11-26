import random
from datetime import datetime, date, timedelta

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

# define member groups
original_members = []
new_members = []


def define_members(member_list):
    # To sperate original/new members.
    # New members are members who entered in 30 days.
    
    for m in member_list:
        # define member variables
        name = m[0]
        entered_at = datetime.strptime(m[1], "%Y-%m-%d") # It should contain time too

        # compare membrer's entered_at with today
        new_members.append(name) if entered_at.date() > date.today() - timedelta(NEW_MEMBER_CRITERIA) else original_members.append(name)

def create_random_meeting(meeting_size = DEFAULT_MEETING_SIZE):
    # create meeting groups.
    # meeting_size = pool_size_new + random_original_members

    pool_size_original = len(original_members) # origi
    pool_size_new = len(new_members)

    meeting_group_list = []
    remained_size = pool_size_original
    remained_members = original_members
    meeting_size = meeting_size - pool_size_new  # meeting_size reset including new_members
    
    while (True):    
        if remained_size > meeting_size * 2:
            # assign original_members to a meeting_group
            meeting_group = [remained_members[n] for n in random.sample(range(remained_size), meeting_size)]
            remained_size -= len(meeting_group)
            remained_members = [item for item in remained_members if item not in meeting_group]
            
            # assign new_members to the meeting_group
            meeting_group += new_members

            # record the meeting_group to meeting_group list
            meeting_group_list.append(meeting_group)
        else:
            meeting_group = remained_members
            meeting_group += new_members
            meeting_group_list.append(meeting_group)
            break
    return meeting_group_list
    
if __name__== "__main__":
    meeting_size = DEFAULT_MEETING_SIZE
    define_members(MEMBER_LIST)
    result = create_random_meeting(meeting_size=meeting_size)

    # print result
    print ("\n\nWelcome to gravity meeting: %s\n===========================================" % str(datetime.now()))
    print ("\nTotal are %d members, %d new members, and each group have %d members:\n" % (len(MEMBER_LIST), len(new_members), meeting_size))
    print ("new_members: %s\n" % str(new_members))
    for m in result:
        print ("Organizer: @" + str(m[0]) + ", " + str(m))
    
    print ("\n\n")
