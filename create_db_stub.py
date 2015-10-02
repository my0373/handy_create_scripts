import random

def main():
    db_name = "test_db"
    num_rows = 1000
    first_names = ["Dave",
                   "Bob",
                   "Tom",
                   "Phil",
                   "Gladys",
                   "Henry",
                   "Harry",
                   "Jenny",
                   "Helen",
                   "Mary",
                   "Mark",
                   "Luke",
                   "John",
                   "Matt",
                   "Matthew"]
    surnames = ["Smith", "Jones", "Taylor", "Williams", "Brown", "Davies", "Evans", "Wilson", "Thomas", "Roberts",
               "Johnson", "Lewis", "Walker", "Robinson", "Wood", "Thompson", "White", "Watson", "Jackson", "Wright",
               "Green", "Harris", "Cooper", "King", "Lee", "Martin", "Clarke", "James", "Morgan", "Hughes", "Edwards",
               "Hill", "Moore", "Clark", "Harrison", "Scott", "Young", "Morris", "Hall", "Ward", "Turner", "Carter",
               "Phillips", "Mitchell", "Patel", "Adams", "Campbell", "Anderson", "Allen", "Cook", "Bailey", "Parker",
               "Miller", "Davis", "Murphy", "Price", "Bell", "Baker", "Griffiths", "Kelly", "Simpson", "Marshall",
               "Collins", "Bennett", "Cox", "Richardson", "Fox", "Gray", "Rose", "Chapman", "Hunt", "Robertson", "Shaw",
               "Reynolds", "Lloyd", "Ellis", "Richards", "Russell", "Wilkinson", "Khan", "Graham", "Stewart", "Reid",
               "Murray", "Powell", "Palmer", "Holmes", "Rogers", "Stevens", "Walsh", "Hunter", "Thomson", "Matthews",
               "Ross", "Owen", "Mason", "Knight", "Kennedy", "Butler", "Saunders", "Cole", "Pearce", "Dean", "Foster",
               "Harvey", "Hudson", "Gibson", "Mills", "Berry", "Barnes", "Pearson", "Kaur", "Booth", "Dixon", "Grant",
               "Gordon", "Lane", "Harper", "Ali", "Hart", "Mcdonald", "Brooks", "Ryan", "Carr", "Macdonald", "Hamilton",
               "Johnston", "West", "Gill", "Dawson", "Armstrong", "Gardner", "Stone", "Andrews", "Williamson", "Barker",
               "George", "Fisher", "Cunningham", "Watts", "Webb", "Lawrence", "Bradley", "Jenkins", "Wells", "Chambers",
               "Spencer", "Poole", "Atkinson", "Lawson", ]

    locations = ["Bristol","Bath","Midsomer Norton","Cambridge","London","Farnborough","Glasgow","Carlisle",]

    print('drop database if exists {};'.format(db_name))
    print('create database {};'.format(db_name))
    print('use {};'.format(db_name))
    print('create table people (id int,first_name varchar(20),surname varchar(20));')
    print('create table location (id int,city varchar(30));')
    for row in range(1,num_rows):

        fn = first_names[random.randint(0,len(first_names) - 1 )]
        sn = surnames[random.randint(0,len(surnames) - 1 )]
        ln = locations[random.randint(0,len(locations) - 1 )]


        print('INSERT INTO people VALUES ({},"{}","{}");'.format(row,fn,sn))
        print('INSERT INTO location VALUES ({},"{}");'.format(row,ln))


if __name__ == "__main__":
    main()
