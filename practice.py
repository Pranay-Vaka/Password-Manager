import os
import random as r
import math
import sys
import datetime
from random import randint
import pandas
import tkinter.messagebox
import smtplib
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

def life_left():
    age = int(input("What is your age?: "))
    if age > 90:
        print("You are very lucky to live past 90!")
        sys.exit()
    elif age <= 90:
        pass
    years_left = 90 - age
    months_left = years_left * 12
    weeks_left = years_left * 52
    days_left = years_left * 365

    print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left")


def tip_calculator():
    print("Welcome to the tip calculator!")
    bill = float(input("What was the total bill?: £"))
    percent_tip = int(input("How much tip would you like to give? 10%, 12% or 15%?: "))
    people = int(input("How many people are splitting the bill?: "))
    multiplier = percent_tip / 100
    tip = round(bill * multiplier, 2)
    total_bill = bill + tip
    total_bill_pp = total_bill / people
    total_bill_pp = "{:.2f}".format(total_bill_pp)
    print(f"Each person should pay £{total_bill_pp}")


def odd_or_even():
    number = int(input("What is the number you want to check?: "))
    remainder = number % 2
    if remainder == 0:
        print("You have an even number")
    elif remainder != 0:
        print("You have an odd number")
    else:
        raise SyntaxError


def bmi_calc():
    height = float(input("What is your height in metres?: "))
    weight = float(input("What is your weight in kilograms?: "))
    bmi = weight / pow(height, 2)
    if bmi < 18.5:
        print(f"Your BMI is {bmi} and you are underweight")
    elif bmi >= 18.5 and bmi < 25:
        print(f"Your BMI is {bmi} and you are normal")
    elif bmi >= 25 and bmi < 30:
        print(f"Your BMI is {bmi} and you are overweight")
    elif bmi >= 30 and bmi < 35:
        print(f"Your BMI is {bmi} and you are obese")
    elif bmi >= 35:
        print(f"Your BMI is {bmi} and you are clinically obese")


def paint_area_calculator():


    def paint_calc(height, width, cover):
        number_of_cans = (height * width) / cover
        number_of_cans = math.ceil(number_of_cans)
        print(f"You need {number_of_cans} number of cans")

    test_h = float(input("What is the height of your wall in metres?: "))
    test_w = float(input("What is the width of your wall in metres?: "))

    coverage = 5

    paint_calc(height = test_h, width = test_w, cover = coverage)


def prime_check():

    def prime_checker(number):
        isprime = True
        for curr_num in range(2, number):
            remainder = number % curr_num
            if remainder == 0:
                isprime = False
        if isprime:
            print("This is a prime number")
        if not isprime:
            print("This is not a prime number")

    n = int(input("Check this number?: "))
    prime_checker(number = n)


def caesar():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    

    def encrypt(plain_text, shift_num):

        final_word = ""
        for letter in plain_text:
            letter_pos = alphabet.index(letter)
            new_letter_pos = letter_pos + shift_num
            if new_letter_pos > 25:
                new_letter_pos = new_letter_pos - 26
                new_letter = alphabet[new_letter_pos]
                final_word += new_letter
            else:
                new_letter = alphabet[new_letter_pos]
                final_word += new_letter

        print(f"The encrypted word is {final_word}")

    def decrypt(plain_text, shift_num):
        final_word = ""
        for letter in plain_text:
            letter_pos = alphabet.index(letter)
            new_letter_pos = letter_pos - shift_num
            if new_letter_pos < 0:
                new_letter_pos = new_letter_pos + 26
                new_letter = alphabet[new_letter_pos]
                final_word += new_letter
            else:
                new_letter = alphabet[new_letter_pos]
                final_word += new_letter

        print(f"The decrypted word is {final_word}")

    direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "e":
        encrypt(text, shift)
    elif direction == "d":
        decrypt(text, shift)

def stack():
    stack = ["", ""]
    pointer = 0

    def add():
        global pointer
        if pointer >= len(stack):
            print("The stack is full!")
            return
        else:
            value = input("What is the value you want to add?: ")
            stack[pointer] = value
            pointer += 1
            print(stack)

    def remove():
        global pointer
        if pointer == 0:
            print("The stack is empty")
            return
        else:
            index = 0
            for i in reversed(stack):
                if i == "":
                    pass
                    index += 1
                else:
                    stack[index - 1] = ""
                    pointer -= 1
                    print(stack)

def mothy_explain():
    x = 9
    y = 8
    print(x)
    print(y)
    temp_val = x
    x = y
    y = temp_val
    print(x)
    print(y)

def date():
    x = datetime.datetime.now()

    print(x.year)
    print(x.strftime("%A"))

def colour_wheel():
    bgcolor('black')
    x = 1
    speed(0)
    while x < 400:

        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)

    colormode(255)
    pencolor(r,g,b)
    fd(50 + x)
    rt(90.991)
    x += 1

    exitonclick()

def combinations(*items):
	ans = 1
	for item in items:
		ans *= item
	print(ans)

def factorial(num):
    print(math.factorial(num))

def long_word():
    string = str(input("What is your string?: "))
    list = string.split()
    big_len = 0
    index = 0
    for word in list:
        if len(word) > big_len:
            big_len = len(word)
            index = list.index(word)
        else:
            pass
    print(big_len)
    print(index)

def csv_test():
    with open("weather_data.csv", mode = "r") as data_file:
        print(pandas.read_csv(data_file))

def pandas_test():
    data = pandas.read_csv("/Users/pranayvaka/Desktop/Programming/weather_data.csv")
    temp_list = data["temp"].to_list()
    total = sum(temp_list)
    average = total / len(temp_list)
    print(round(average, 2))

def temp():
     data = pandas.read_csv("/Users/pranayvaka/Desktop/Programming/weather_data.csv")
     monday = data[data.day == "Monday"]
     celcius = int(monday.temp)
     farenheit = (celcius * 1.8) + 32
     print(farenheit)

def squirrels():
    with open("/Users/pranayvaka/Desktop/Programming/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv") as csv_data:
        pd_data = pandas.read_csv(csv_data)
        fur_colour_list = pd_data["Primary Fur Color"].to_list()
        specific_list = [fur_colour_list.count("Gray"), fur_colour_list.count("Cinnamon"), fur_colour_list.count("Black")]

        dict = {
            "Fur color": ["Grey", "Red", "Black"],
            "Count": specific_list
        }

        pandas_colour_data = pandas.DataFrame(dict)
        csv_colour_data = pandas_colour_data.to_csv()


def syllables(string):
    print(len(string.split("-")))

def snake_word(string, times):
    final_word = ""
    for letter in string:
        final_word += (letter * times)
    print(final_word)

def squared_nums():
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    squared_numbers = [int(math.pow(num, 2)) for num in numbers]

    print(squared_numbers)

def word_count():
    sentence = "What is the Airspeed Velocity of an Unladen Swallow"
    result = {word: len(word) for word in sentence.split()}
    print(result)

def dict_weather():
    dict = {
        "Monday": 12,
        "Tuesday": 14,
        "Wednesday": 15,
        "Thursday": 14,
        "Friday": 21,
        "Saturday": 22,
        "Sunday": 24
    }

    faren_dict = {day: ((temp_c * 9/5) + 32) for (day, temp_c) in dict.items()}
    print(faren_dict)

def multiply(x, y = 10):
    print(x * y)


def tikinter_entry():

    screen = Tk()

    def change_text():
        value = entry.get("1.0", END)
        label.config(text = value)


    label = Label(text = "Unknown")
    label.pack()

    entry = Text()
    entry.pack()

    button = Button(text = "Change text", command = change_text)
    button.pack()

    screen.mainloop()

def tkinter_test():
    screen = Tk()

    listbox = Listbox()
    fruits = ["apple", "orange", "pear", "banana"]
    for item in fruits:
        listbox.insert(fruits.index(item), item)

    screen.mainloop()

def miles_to_kilo():

    def calc_func():
        km = round(float(miles_entry.get()) * 1.609, 2)
        km_output.config(text = km)

    screen = Tk()
    screen.title("Test to KM converter")
    screen.config(padx = 10, pady = 10)

    equal_label = Label(text = "is equal to")
    equal_label.grid(row = 1, column = 0)

    miles_entry = Entry()
    miles_entry.grid(row = 0, column = 1)

    km_output = Label(text = 0)
    km_output.grid(row = 1, column = 1)

    calc_button = Button(text = "Calculate", command = calc_func)
    calc_button.grid(row = 2, column = 1)

    miles_unit = Label(text = "Miles")
    miles_unit.grid(row = 0, column = 2)

    km_unit = Label(text = "KM")
    km_unit.grid(row = 1, column = 2)

    screen.mainloop()

def tk_test():
    window = Tk()
    proceed = tkinter.messagebox.askyesno("test", "test")

    window.mainloop()

def mail_test():
	my_email = "gmai1mctest444@gmail.com"
	my_pass = "gmailtest"
	message = "Subject:New test Title\n\nThis the test body of the e-mail"

	with smtplib.SMTP("smtp.gmail.com") as connection:
	  connection.starttls()
	  connection.login(user = my_email, password = my_pass)
	  connection.sendmail(
	  from_addr = my_email,
	  to_addrs = "ytestmctest915@yahoo.com",
	  msg = message
	  )

def email_quotes():
	def check_day():
	  now = dt.datetime.now()
	  day = 0

	  if day == 0:
		  get_wish()
	  else:
		  pass

	def get_wish():
		with open("quotes.txt", "r") as data:
			content = data.read().split("\n")
			line_num = r.randint(0, len(content))
			send_mail(content[line_num])

	def send_mail():
		with smtplib.SMTP("smtp.gmail.com") as connection:
			connection.starttls()
			connection.login(user = "gmai1mctest444@gmail.com", password = "gmailtest")
			message = f"Subject:Monday motivation\n\n{line}"
			connection.sendmail(from_addr = "gmai1mctest444@gmail.com", to_addrs = "ytestmctest915@yahoo.com", msg = message)

	check_day()

def api_test():
	response = requests.get("http://api.open-notify.org/iss-now.json")
	data = response.json()
	print(data)

def sunset():

	parameters = {
	"lat": 51.507351,
	"lng": -0.127758
	}

	response = requests.get("http://api.sunrise-sunset.org/json", params = parameters)
	response.raise_for_status()
	data = response.json()
	print(data)

def fizz_buzz(max_num):
    for num in range(1, max_num):
        if num % 3 == 0 and num % 5 == 0:
            print("Fizzbuzz") 
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

def web_scrape():
    response = requests.get("https://news.ycombinator.com")
    yc_webpage = response.text
    soup = BeautifulSoup(yc_webpage, "html.parser")
    article_tag = soup.find(name = "a", class_ = "storylink")
    print(article_tag.getText())
    web_scrape()

def selenium_test():
    chrome_driver_path = "/Users/pranayvaka/Programming/chromedriver"
    driver = webdriver.Chrome(executable_path = chrome_driver_path)
    driver.get("https://www.amazon.co.uk/New-Apple-iPhone-12-128GB/dp/B08L5QVFCT/ref=sr_1_1?dchild=1&keywords=iphone&qid=1628250937&sr=8-1")
    price = driver.find_element_by_id("priceblock_ourprice")
    print(price.text)

def scrape_pyevents():
    dict = {}
    chrome_driver_path = "/Users/pranayvaka/Programming/chromedriver"
    driver = webdriver.Chrome(executable_path = chrome_driver_path)
    driver.get("https://www.python.org")

    event_times = driver.find_elements_by_css_selector(".event-widget time")
    event_names = driver.find_elements_by_css_selector(".event-widget a")
    
    for count in range(0, len(event_times)):
        dict.update({event_times[count].text: event_names[count].text})

    print(dict)

def meme(string:str, repeats:int):
    new_string = ""
    
    for i in string:
        new_string += repeats * i

    print(new_string)


def boomerang():
    counter = 0
    mid = 1
    last =  3

    array = [1, 5, 1, 2, 3, 3, 3, 5, 6, 5]
    
    for first in array:
        if last > len(array) - 1:
            break
        else:
            if array[first] == array[last] and array[mid] != array[first] and array[mid] != array[last]:
                counter += 1
                mid += 1
                last += 1
    print(counter)

def class_ex():

    class Person():

        def __init__(self, firstname, surname, age, gender):
                self.firstname = firstname
                self.surname = surname
                self.age = age
                self.gender = gender

        def get_details(self):
            self.firstname = input("Name?: ")     
            self.surname = input("Surname?: ")
            self.age = input("Age?: ")
            self.gender = input("Gender?: ")
        
        def say_name():
            print(f"{self.firstname} {self.surname}")
        
    Jack = Person()

    
    class Child(Person):

        def __init__(self, firstname, surname, age, gender, school):
            super().__init__(firstname, surname, age, gender)
            self.school = school

        def get_school(self):
            self.school = input("School?: ")

def mod(num1, num2):
    return num1 % num2


def os_call():
    os.system("touch tester.py /Programming")


def reverse(x):
    x = list(str(x))[::-1]
    
    if len(x) <= 1:
        x = "".join(x)
        return int(x)
    
    for i in list(enumerate(x)):
        
        if i[1] == "0": x.pop(i[0])

        elif i[1] != "0": break
        
    if x[-1] == "-":
        x.pop()
        x.insert(0, "-")

    x = "".join(x)
    return int(x)


class Vehicle():
    
    def __init__(self, max_speed, mileage, capacity = 0):

        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity
        
    
    def seating_capacity(self):
        
        return f"This vehicle has a capcity of {self.capacity}"


class Bus(Vehicle):

    def __init__(self, max_speed, mileage, capacity = 50):

        super().__init__(self, max_speed, mileage)
        self.capacity = capacity

    def seating_capacity(self):
        
        return f"This bus has a capcity of {self.capacity}"


def numpy():

    arr = np.array([1, 2, 3, 4, 5])
    
    """
    People use numpy because it is almost 50 times the normal arrays as they are stored 
    in one place in the memory, while lists are continuous. It is also optimised to the 
    latest CPU architecture

    The type of the numpy array is called an ndarray
    
    i - integer
    b - boolean
    u - unsigned integer
    f - float
    c - complex float
    m - timedelta
    M - datetime
    O - object
    S - string
    U - unicode string
    V - fixed chunk of memory for other type ( void )
    """

    #You can access the data type of the ndarray by using the arr.dtype attribute from object
    #The types above are the types that can be returned back from the attribute

    #You can specify what datatype the elements are for the ndarray using the dtype as an argument


    arr = np.array([1, 2, 3, 4, 5], dtype = "S") #This means that every single one of the elements will now be a string


    #You can convert the type of each of elements using the astype function


    arr = arr.astype("i") #Now each of the elements are an integer

    x = arr.copy()
    y = arr.view()
    
    """
    The difference between the copy and the view is that any changed to the copy does not affect the  
    original array any changes to the original array does not affect the copy. But for the view, any changes
    to the view will affect the original array and any changed to the original array will change the view. 
    The copy owns the data while the view does not own the data.
    """

    # You can check if the data has been owned or not by using the base attribute
    
    print(x.base) # The copy will return None
    print(y.base) # The view will return the original array

    print(arr.shape) # This will return the shape of the array which is (1, 5), which means 1 dimension and 5 elements in each array 

    # One way that you can change the dimensions of the array is by using the reshape method

    new_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    new_arr = new_arr.reshape(4, 3)

    # This means that there will be 4 arrays with 3 elements each 
    
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    newarr = arr.reshape(2, 3, 2) # This means that there are 2 arrays with 3 arrays containing 2 elements each
    
    # When you are iterating through a high dimensionsional list, it is hard to write so many for loops
    # So you can just use the nditer method

    for i in np.nditer(newarr): # This will iterate through each of the elements and you don't need to write so many for loops 
        print(i)
   
    # For each of the elements whle iterating, you can change the data types of the element, but this does not change the 
    # actual array, but the variable that holds the value that is being iterated through the array. Since it does not change
    # the actual array, the iterator needs extra buffer space in order to perform this action. We enable this by using 
    # flags = ["buffered"], and then  to change each of the datatype of the elements, we use op_dtypes = ["S"]. The datatype 
    # can be changed to any suitable data type. 

    for i in np.nditer(newarr, flags = ["buffered"], op_dtypes = ["S"]):
        print(i)

    # You can also iterate with a different step size

    for i in np.nditer(new_arr[:, ::2]): # This has a step size of 2
        print(i)
    
    arr = np.array([1, 2, 3, 4,], [5, 6, 7, 8])

    for i, j in np.ndenumerate(arr): # This will iterate through the list and give the index of the array depending on the dimensions 
        print(i, j) # For j that gives the actual value

    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])

    arr = np.concatenate((arr2, arr2)) # This just joins the two lists along each other

    arr1 = np.array([[1, 2], [3, 4]])

    arr2 = np.array([[5, 6], [7, 8]])

    arr = np.concatenate((arr1, arr2), axis = 1) # This will concatenate the two arrays along the 1 axis (y axis)

    arr = np.stack((arr1, arr2), axis = 1) # This will put the two arrays on top of each other and so 
    # it would result in [1, 2, 5, 6], [3, 4, 7, 8]

def machine_learning():
    """
    A data set is any collecion of data, from an array to a complete database

    We can split data types into three types:
    - Numerical 
    - Categorial
    - Ordinal

    Numerical values can be split up into discrete values (values that are limited to integers) and continuous (values that are infinte)

    Categorical data are values that can't be measured up against each other (like colour and name)

    Ordinal data are like categorical numbers but can be measured against each other (for example an A grade is better than a B grade)
    
    In machine learning for grouped data there are often three types of numbers that are of interest:
    - Mean (The average value)
    - Median (The midpoint)
    - Mode (The most common value)
        

    You can find the mean and median of a list using the numpy module
    """

    speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

    mean = np.mean(speed) # This will find the mean of the speeds

    median = np.median(speed) # This will find the median of the speeds

    mode = stats.mode(speed) # This will find the mode of the speeds and uses the scipy module

    """
    Standard deviation figures out how spread out the values are

    Low standard deviation means that the values are close to the mean

    High standard deviation means that the values are further from the mean

    You can figure out the standard deviation of a list using the numpy module
    """
    
    std = np.std(speed) # This will find the standard deviaiton of the speeds
    
    """
    Variance figures out the spread of the values from the mean, but this is just the square of the standard deviation
    This is good because if the value is negative then it does not affect less as a value that is positive

    A function in the numpy module can calculate the variance
    """

    variance = np.var(speed)

    """
    Percentiles describe the values that the given percent is lower than
    For example in the array
    ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

    The 75th percentile is 43, meaning that 75% of people are under the age of 43

    You can find the percentile of an object by using the percentile function
    """

    ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

    percentile = np.percentile(ages, 75) #The first argument is the array and the second is the percentile

    """
    You can get a uniformly random set of values (this means that each value has an equal chance of being picked)
    using the numpy module
    """

    random_set = np.random.uniform(0.0, 5.0, 250) # This will get 250 ranodm floats between 0 and 5
    
    # You can plot this on a histogram using the matplotlib module

    # plt.hist(random_set, 5)

    """
    Normal distribution is when you have  series of value that are randomly generated around a value (usually the mean)
    You can make the normal distribution using the numpy module 
    """
    
    normal = np.random.normal(5.0, 1.0, 100000) # This means that there is a mean of 5, a standard deviation of 1 and 100, 000 values
    # Therefore there the values should be concentrated around 5, but most of them should be less than 1 standard deviation away from the mean 
    
    # plt.hist(normal, 100) 
    
    """
    In order to plot a scatter plot you must take two arrays that are of the same length and use the matplotlob module to plot them
    """

    x = [5,7,8,7,2,17,2,9,4,11,12,9,6]

    y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

    # plt.scatter(x, y)

    # You can also use normal distribution in the scatter plots

    x = np.random.normal(5.0, 1.0, 1000)
    y = np.random.normal(10.0, 2.0, 1000)
    
    #plt.scatter(x, y)
    # This shows that it is normal distibution as most of the values are concentrated in the middle where the mean is

    # You can get the following values to be returned back when you equate it to the linear regression function
    
    x = [5,7,8,7,2,17,2,9,4,11,12,9,6]

    y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
    

    slope, intercept, r, p, std_err = stats.linregress(x, y)

    def plot(x): # This function will plot the regression line values
        return slope * x + intercept

    my_model = list(map(plot, x)) 

    """
    What the map model is that for each of the items in an iterable, it will apply the function that was mentioned as an argument.
    This is its own datatype and you should convert it into a list in order to make it easier to use
    """
    """
    plt.scatter(x, y)
    plt.plot(x, my_model)
    plt.show()
    """

    """
    The r is the value that says if the relationship is bad or good.
    If it is -1 then it has a strong negative correlation, but if it is +1 then it has a strong positive correlation
    The closer to 0, the weaker the correlation
    """

    """
    You can predict the values using the plot funnction
    ex. print(plot(2)) would give 99.60338484179543
    """
    
    """
    You can use polynomial regression if the linear regression is not accurate enough
    """

    x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
    y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

    my_model = np.poly1d(np.polyfit(x, y, 3)) 
    # The poly1d means that it is a one dimensional array that is being computed
    # The 3 (the third parameter for the polyfit) means the degree of the function is 3
    
    myline = np.linspace(1, 22, 100)

    # This draws out the line that will be on the graph
    # It will go from 1 to 22 on the x axis and up to 100 on the y 
    
    """
    plt.scatter(x, y)

    plt.plot(myline, my_model(myline)) # This is the polynomial regression line
    
    plt.show()
    """

    """
    Relationship is measured by something called the r squared value where the closer it is to 1, then the more related
    the values are, while the closer to 0 it is, the worser the relationship is
    """
    
    # print(r2_score(y, my_model(x))) this will ouput the r squared score for this model 
    
    
    
def two_sum(nums, target):
    
    found = True
    num1 = 0
    num2 = 0

    while found:
        for i in enumerate(nums):
            for j in enumerate(nums):
                if i[0] != j[0]:
                    if i[1] + j[1] == target:
                        num1 = j[0]
                        num2 = i[0]
                        found = False
    return [num1, num2]

print(two_sum([3,3], 6))
