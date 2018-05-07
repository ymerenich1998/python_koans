ABOUT_METHODS
Test_1
def my_function(a,b,c):
    return (a + b)*c

    def test_calling_a_my_function(self):
        self.assertEqual(35, my_function(2,3,7))
##################################################
ABOUT_LAMBDAS
Test_2
    def my_method(self,num):
        return (num/10)

    def test_my_lambdas(self):
        add_nin=lambda num: num/10

        self.assertEqual(0.9,self.my_method(9))
##################################################
ABOUT_METHODS
Test_3
    class Cat:
        def description(self):
            return "Cats are animals"

    class Cat2(Dog):
        def num_of_cats(self):
            return 2

    def test_three(self):
        Nani = self.Cat2
        self.assertEqual(True, issubclass(self.Cat2, object))
##################################################
ABOUT_CLASSES
Test_4
class Cars(object):

        comp =""

        def adding(self):
            return "We add in race {0}".format(self.comp)

        def destroy(self):
            return "We destroy {0}"

    def test_my_class_cars(self):
        cars= self.Cars()
        self.assertEqual('We add in race ',cars.adding())

    class MarkCars(Cars):

        comp = "Subaru"

    def test_my_class_MarkCars(self):
        cars=self.MarkCars()
        self.assertEqual('We add in race Subaru',cars.adding())
        self.assertEqual("Subaru",cars.comp)    
##################################################
ABOUT_LIST
Test_5
def test_x3_elements(self):
    c = [c * 3 for c in 'list' if c != 'i']
    self.assertEqual(['lll', 'sss', 'ttt'],c)

def test_my_range(self):
        a = [ i*i for i in range(1,10) if i % 2 == 0]
        self.assertEqual([4, 16, 36, 64],a)    
##################################################
ABOUT_LIST
Test_6
def test_my_set_and_pop(self):
    L = [1,2,3,4,1,2,6,7]
    L.pop()
    self.assertEqual({1, 2, 3, 4, 6},set(L))
##################################################
ABOUT_LIST
Test_7
def test_no_repeat_leater(self):
        a = set('abracadabra')
        b = set('alacazam')
        self.assertEqual({'a', 'r', 'c', 'd', 'b'}, a) # кількісь неповторюваних літер в a
        self.assertEqual({'d', 'r', 'b'}, a - b) # різниця (літери, що є в a, але не в b)
        self.assertEqual({'c', 'b', 'm', 'l', 'z', 'd', 'r', 'a'}, a|b) # об'єднання (літери, що є або в a або в b)
        self.assertEqual({'a', 'c'}, a&b) # перетин (літери, водночас присутні в a та b)
        self.assertEqual({'r', 'm', 'b', 'z', 'd', 'l'}, a^b) # симетрична різниця (літери, присутні або в a або в b, але не в обох одночасно) 
##################################################	
ABOUT_COMPREHENSION
Test_8
def test_my_array(self) :
        weather = ['sun', 'rain', 'wind', 'thunderstorm', 'storm', 'tornado']
        
        self.assertEqual('sun', weather[0]) 
        self.assertEqual('rain', weather[1])
        self.assertEqual('thunderstorm', weather[3])
        self.assertEqual('tornado', weather[-1]) 
        self.assertEqual('thunderstorm', weather[-3])   
##################################################  
ABOUT_LIST
Test_9
def test_list_comprehensions(self):
    sentence = "the quick chick fox goes over the lazy dog"
    words = sentence.split()
    word_lengths = [len(word) for word in words if word != "the"]
    word_lengths.pop(1)
    s = sum(word_lengths)
    self.assertEqual(s,23)       
##################################################  
ABOUT_CLASSES
Test_10
  def test_my_rewrite_Cars_method(self):
        cars=self.Cars()
        self.assertEqual('We add in race ',cars.adding())
        mark=self.MarkCars()
        self.assertEqual('We add in new race Subaru',mark.adds())
        self.assertEqual(False,(cars.__class__==mark.__class__))
        self.assertEqual('Cars',cars.__class__.__name__)
        self.assertEqual('MarkCars',mark.__class__.__name__)