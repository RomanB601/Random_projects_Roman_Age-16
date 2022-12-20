from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file: # opens a file
    content = html_file.read()

    soup = BeautifulSoup(content, 'html5lib')
    #finds all of the html code that starts with dev and in the class card
    course_cards = soup.findAll('div', class_= 'card') 
    #loops over the array given by find all
    for course in course_cards:
        course_name = course.h5.text #makes all of the h5 tag into text
        course_price = course.a.text.split()[-1] #[-1] means last element
        print(f"{course_name} costs {course_price}")
    