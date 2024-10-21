import doctest

# represent a year, month number, and date
# values should be a vaild date in the calender
CalenderInfo = tuple[int, int, int]

# represents type of show, the title of the show, a list of directors, a list of
# actors, and the date the show was added.
# all str values should be non empty strings
ShowInfo = tuple[str, str, list, list, CalenderInfo]

def raise_to_power(num: list[int], to_the_power: list[int]) -> None:
    '''
    this function takes two lists, the first list in the function
    will be raised to the power of whatever elements are in the second list so
    if position 0 is equal to 2 in list one and position 0 in list two is equal
    to 2, the new list should have in position zero 4 because that 2^2.
    >>> raise_to_power([1, 2, 3], [0, 0, 0])
    [1, 1, 1]
    >>> raise_to_power([],[4, 5, 7])
    []
    >>> raise_to_power([3, 3, 5, 4], [2, 1, 3]) 
    [9, 3, 125, 4]
    '''
    minimum = min(len(num), len(to_the_power))
    
    for position in range(minimum):
        
        num[position] **= to_the_power[position]
        
    print(num)
        
    
def create_date(date_str: str) -> CalenderInfo:
    '''
    this function takes a calender day as a str and transforms it into a valid
    tuple.
    >>> create_date('18-Aug-05')
    (2005, 8, 18)
    >>> create_date('30-Sep-06')
    (2006, 9, 30)
    >>> create_date('25-Dec-20')
    (2020, 12, 25)
    '''
    new_list = date_str.split('-')
    
    day = int(new_list[0])
    
    year = 2000 + int(new_list[2])
    
    if new_list[1] == 'Jan':
        month = 1
    elif new_list[1] == 'Feb':
        month = 2
    elif new_list[1] == 'Mar':
        month = 3
    elif new_list[1] == 'Apr':
        month = 4
    elif new_list[1] == 'May':
        month = 5
    elif new_list[1] == 'Jun':
        month = 6
    elif new_list[1] == 'Jul':
        month = 7
    elif new_list[1] == 'Aug':
        month = 8
    elif new_list[1] == 'Sep':
        month = 9
    elif new_list[1] == 'Oct':
        month = 10
    elif new_list[1] == 'Nov':
        month = 11
    else:
        month = 12
        
    info = year, month, day
    
    return info
        
def create_show(type_show: str, title: str, director: str, actor: str, date: str) -> ShowInfo:
    '''
    this function takes (as strings) the type of show, the title of the show, 
    the director, actors, and the date in which the show was created. Through
    this information the function should return a tuple contain all the 
    information.
    >>> create_show('Movie', 'Interstellar', 'Christopher Nolan', \
    'Matthew McConaughey:Jessica Chastain:Anne Hathaway:Timothee Chalamet', '5-Nov-14')
    ('Movie', 'Interstellar', ['Christopher Nolan'], ['Matthew McConaughey', 'Jessica Chastain', 'Anne Hathaway', 'Timothee Chalamet'], (2014, 11, 5))
    >>> create_show('Movie', 'Gravity', 'Alfonso Cuaron', \
    'Sandra Bullock:George Clooney:Ed Harris:Orto Ignatiussen', '4-Oct-13')
    ('Movie', 'Gravity', ['Alfonso Cuaron'], ['Sandra Bullock', 'George Clooney', 'Ed Harris', 'Orto Ignatiussen'], (2013, 10, 4))
    '''
    director_list = director.split(':')
    actor_list = actor.split(':')
    date = create_date(date)
    
    if director_list == ['']:
        director_list = []
        
    if actor_list == ['']:
        actor_list = []
    
    info = type_show, title, director_list, actor_list, date
    
    return info

def get_titles(list_of_show: list[ShowInfo]) -> list[str]:
    '''
    this function takes a list of netflix shows that are in tuples, and returns
    a list of the titles of each Netflix shows in the list in the order they 
    appear in the given list.
    >>> list_of_show = [\
    ('Movie', "Intersteller", ['Christopher Nolan'],\
    ['Matthew McConaughey', \
    'Jessica Chastain', 'Anne Hathaway', 'Timothee Chalamet'], \
    (2014, 11, 5)),\
    ('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
    'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], \
    (2018, 9, 21)),\
    ('TV Show', 'Naruto', ['Hayato Date'], \
    ['Yuri Lowenthal', 'Steve Blum', 'Kate Higgins', 'Junko Takeuchi', \
    'Dave Wittenberg'], \
    (2002, 10, 3))]
    
    >>> get_titles(list_of_show)
    ['Intersteller', 'Superbad', 'Maniac', 'Naruto']
    '''
    lo_titles = []
    for shows in list_of_show:
        title = shows[1]
        lo_titles.append(title)
        
    return lo_titles
        
        
def is_actor_in_show(list_of_shows: list[ShowInfo], actor: str) -> bool:
    '''
    this function takes a list of netflix shows and a name of an actor if the
    actor that is called in the function is a part of the show it will return
    True otherwise it will return False.
    >>> is_actor_in_show(('Movie', "Intersteller", ['Christopher Nolan'],\
    ['Matthew McConaughey', \
    'Jessica Chastain', 'Anne Hathaway', 'Timothee Chalamet'], \
    (2014, 11, 5)), 'Timothee Chalamet')
    True
    >>> is_actor_in_show(('Movie', "Intersteller", ['Christopher Nolan'],\
    ['Matthew McConaughey', \
    'Jessica Chastain', 'Anne Hathaway', 'Timothee Chalamet'], \
    (2014, 11, 5)), 'TiMOtheE cHalamet')
    True
    >>> is_actor_in_show(('TV Show', 'Naruto', ['Hayato Date'], \
    ['Yuri Lowenthal', 'Steve Blum', 'Kate Higgins', 'Junko Takeuchi', \
    'Dave Wittenberg'], \
    (2002, 10, 3)), 'Adam Sandler')
    False
    '''
    for shows in list_of_shows:
        list_of_actors = list_of_shows[3]
        for actors in list_of_actors:
            if actors.lower() == actor.lower():
                return True
            
        return False
    
    
def count_shows_before_date(list_of_shows: list[ShowInfo], calen: tuple) -> int:
    '''
    this function has a list of shows, and a calender date if the shows came
    out before the calender date. The return will show the number of shows that 
    came out before that date.
    >>> list_of_show = [\
    ('Movie', "Intersteller", ['Christopher Nolan'],\
    ['Matthew McConaughey', \
    'Jessica Chastain', 'Anne Hathaway', 'Timothee Chalamet'], \
    (2014, 11, 5)),\
    ('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
    'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], \
    (2018, 9, 21)),\
    ('TV Show', 'Naruto', ['Hayato Date'], \
    ['Yuri Lowenthal', 'Steve Blum', 'Kate Higgins', 'Junko Takeuchi', \
    'Dave Wittenberg'], \
    (2002, 10, 3))]
    
    >>> count_shows_before_date(list_of_show, (2003, 5, 6))
    1
    >>> count_shows_before_date(list_of_show, (2017, 11, 23))
    2
    >>> count_shows_before_date(list_of_show, (2020, 10, 18))
    4
    '''
    total = 0
    for shows in list_of_shows:
        for info in shows:
            date = shows[4]
            for num in date:
                if date[0] < calen[0]:
                    result = 1
                elif date[0] == calen[0] and date[1] < calen[1]:
                    result = 1
                elif date[0] == calen[0] and date[1] == calen[1] and date[2] < calen[2]:
                    result = 1
                else:
                    result = 0
                    
        total += result
            
    return total
                    
def get_shows_with_actor(list_show: list[ShowInfo], actor: str) -> list[ShowInfo]:
    '''
    this function takes a list of netflix shows and an actor, if the actor is in
    the list of shows, it will return a list of all the shows withing the list
    that the actor is creditied in.
    
    >>> list_of_show = [\
    ('Movie', "Intersteller", ['Christopher Nolan'],\
    ['Matthew McConaughey', \
    'Jessica Chastain', 'Anne Hathaway', 'Timothee Chalamet'], \
    (2014, 11, 5)),\
    ('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'],\
    (2019, 9, 1)),\
    ('Movie', 'Dune', ['Denis Villeneuve'], \
    ['Zendaya', 'Rebecca Ferguson', 'Oscar Isaac', 'Stellan Skarsgard', \
    'Jason Momoa', 'Timothee Chalamet', 'Christopher Walken', 'Josh Brolin', \
    'Florence Pugh'], \
    (2021, 10, 22)),\
    ('TV Show', 'Naruto', ['Hayato Date'], \
    ['Yuri Lowenthal', 'Steve Blum', 'Kate Higgins', 'Junko Takeuchi', \
    'Dave Wittenberg'], \
    (2002, 10, 3))]
    
    >>> get_shows_with_actor(list_of_show, 'Timothee Chalamet')
    [('Movie', 'Intersteller', ['Christopher Nolan'], ['Matthew McConaughey', 'Jessica Chastain', 'Anne Hathaway', 'Timothee Chalamet'], (2014, 11, 5)), ('Movie', 'Dune', ['Denis Villeneuve'], ['Zendaya', 'Rebecca Ferguson', 'Oscar Isaac', 'Stellan Skarsgard', 'Jason Momoa', 'Timothee Chalamet', 'Christopher Walken', 'Josh Brolin', 'Florence Pugh'], (2021, 10, 22))]

    >>> get_shows_with_actor(list_of_show, 'TiMOthEe chaLAmet')
    [('Movie', 'Intersteller', ['Christopher Nolan'], ['Matthew McConaughey', 'Jessica Chastain', 'Anne Hathaway', 'Timothee Chalamet'], (2014, 11, 5)), ('Movie', 'Dune', ['Denis Villeneuve'], ['Zendaya', 'Rebecca Ferguson', 'Oscar Isaac', 'Stellan Skarsgard', 'Jason Momoa', 'Timothee Chalamet', 'Christopher Walken', 'Josh Brolin', 'Florence Pugh'], (2021, 10, 22))]
    
    >>> get_shows_with_actor(list_of_show, 'Adam Sandler')
    []
    '''
    lof_show_with_actor = []
    for shows in list_show:
        result = is_actor_in_show(shows, actor)
        if result == True:
            lof_show_with_actor.append(shows)
            
    return lof_show_with_actor
            
    
        