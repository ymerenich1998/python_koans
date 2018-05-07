#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrays in the Ruby Koans
#

from runner.koan import *

class AboutLists(Koan):
    def test_creating_lists(self):
        empty_list = list()
        self.assertEqual(list, type(empty_list))
        self.assertEqual(0, len(empty_list))

    def test_list_literals(self):
        nums = list()
        self.assertEqual([], nums)

        nums[0:] = [1]
        self.assertEqual([1], nums)

        nums[1:] = [2]
        self.assertListEqual([1, 2], nums)

        nums.append(333)
        self.assertListEqual([1, 2, 333], nums)

    def test_accessing_list_elements(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual('peanut', noms[0])
        self.assertEqual('jelly', noms[3])
        self.assertEqual('jelly', noms[-1])
        self.assertEqual('butter', noms[-3])

    def test_slicing_lists(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual(['peanut'], noms[0:1])
        self.assertEqual(['peanut', 'butter'], noms[0:2])
        self.assertEqual([], noms[2:2])
        self.assertEqual(['and', 'jelly'], noms[2:20])
        self.assertEqual([], noms[4:0])
        self.assertEqual([], noms[4:100])
        self.assertEqual([], noms[5:0])

    def test_slicing_to_the_edge(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual(['and', 'jelly'], noms[2:])
        self.assertEqual(['peanut', 'butter'], noms[:2])

    def test_lists_and_ranges(self):
        self.assertEqual(range, type(range(5)))
        self.assertNotEqual([1, 2, 3, 4, 5], range(1,6))
        self.assertEqual([0, 1, 2, 3, 4], list(range(5)))
        self.assertEqual([5, 6, 7, 8], list(range(5, 9)))

    def test_ranges_with_steps(self):
        self.assertEqual([5, 4], list(range(5, 3, -1)))
        self.assertEqual([0, 2, 4, 6], list(range(0, 8, 2)))
        self.assertEqual([1, 4, 7], list(range(1, 8, 3)))
        self.assertEqual([5, 1, -3], list(range(5, -7, -4)))
        self.assertEqual([5, 1, -3, -7], list(range(5, -8, -4)))

    def test_insertions(self):
        knight = ['you', 'shall', 'pass']
        knight.insert(2, 'not')
        self.assertEqual(['you', 'shall', 'not', 'pass'], knight)

        knight.insert(0, 'Arthur')
        self.assertEqual(['Arthur', 'you', 'shall', 'not', 'pass'], knight)

    def test_popping_lists(self):
        stack = [10, 20, 30, 40]
        stack.append('last')

        self.assertEqual([10, 20, 30, 40, 'last'], stack)

        popped_value = stack.pop()
        self.assertEqual('last', popped_value)
        self.assertEqual([10, 20, 30, 40], stack)

        popped_value = stack.pop(1)
        self.assertEqual(20, popped_value)
        self.assertEqual([10, 30, 40], stack)

        # Notice that there is a "pop" but no "push" in python?

        # Part of the Python philosophy is that there ideally should be one and
        # only one way of doing anything. A 'push' is the same as an 'append'.

        # To learn more about this try typing "import this" from the python
        # console... ;)

    def test_making_queues(self):
        queue = [1, 2]
        queue.append('last')

        self.assertEqual([1, 2, 'last'], queue)

        popped_value = queue.pop(0)
        self.assertEqual(1, popped_value)
        self.assertEqual([2, 'last'], queue)

        # Note, popping from the left hand side of a list is
        # inefficient. Use collections.deque instead.

    #My_test_5
    def test_x3_elements(self):
        c = [c * 3 for c in 'list' if c != 'i']
        self.assertEqual(['lll', 'sss', 'ttt'],c)

    def test_sorting(self):
        a = [ i*i for i in range(1,10) if i % 2 == 0]
        self.assertEqual([4, 16, 36, 64],a)

    #My_test_6
    def test_my_set_and_pop(self):
        L = [1,2,3,4,1,2,6,7]
        L.pop()
        self.assertEqual({1, 2, 3, 4, 6},set(L))  

    #My_Test_7
    def test_no_repeat_leater(self):
        a = set('abracadabra')
        b = set('alacazam')
        self.assertEqual({'a', 'r', 'c', 'd', 'b'}, a) # кількісь неповторюваних літер в a
        self.assertEqual({'d', 'r', 'b'}, a - b) # різниця (літери, що є в a, але не в b)
        self.assertEqual({'c', 'b', 'm', 'l', 'z', 'd', 'r', 'a'}, a|b) # об'єднання (літери, що є або в a або в b)
        self.assertEqual({'a', 'c'}, a&b) # перетин (літери, водночас присутні в a та b)
        self.assertEqual({'r', 'm', 'b', 'z', 'd', 'l'}, a^b) # симетрична різниця (літери, присутні або в a або в b, але не в обох одночасно) 

    #My_Test_9
    def test_list_comprehensions(self):
        sentence = "the quick chick fox goes over the lazy dog"
        words = sentence.split()
        word_lengths = [len(word) for word in words if word != "the"]
        word_lengths.pop(1)
        s = sum(word_lengths)
        self.assertEqual(s,23)            
