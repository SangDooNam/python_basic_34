books = {
    'Harry Potter And The Sorcerer\'s Stone': 1241100000,
    'Harry Potter And The Chamber Of Secrets': 771300000,
    'Harry Potter And The Prisoner Of Azkaban': 65210000,
    'Harry Potter And The Goblet Of Fire': 645600000,
    'Harry Potter And The Order Of The Phoenix': 635600000,
    'Harry Potter And The Half Blood Prince': 661300000,
    'Harry Potter And The Deathly Hallows ': 652200000,
}

def top_three(dict):
    
    sorted_dict = sorted(dict.items(), key = lambda x : x[1], reverse = True)
    
    top_3 = sorted_dict[:3]
    
    for i, (title, sales) in enumerate(top_3, 1):
        
        
        print(f'{i}. {title} : {sales}')


top_three(books)