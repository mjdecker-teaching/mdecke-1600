###
# @file linked_list_oracle.py
# 
# Test linked_list.py
# @author Michael John Decker, Ph.D.

import unittest
from linked_list import linked_list

# Helper function, as some may have had trouble with iterable parameter
# Normally, would just use the constructor
def create_linked_list(array) :

    alist = linked_list()
    for element in array :
        alist.push_back(element)

    return alist

class default_constructor_test(unittest.TestCase) :

    def test_default_ctor(self) :
        alist = linked_list()
        self.assertFalse(alist)

class constructor_test(unittest.TestCase) :

    def test_iterable_one_element(self) :
        alist = linked_list([42])
        self.assertTrue(alist)
        # front/back return nodes
        self.assertEqual(alist.front().item, 42)
        self.assertEqual(alist.back().item, 42)

    def test_iterable_multiple_element(self) :
        alist = linked_list('abc')
        self.assertTrue(alist)
        self.assertEqual(alist.front().item, 'a')
        self.assertEqual(alist.back().item, 'c')

class equals_test(unittest.TestCase) :
    def setUp(self) :
        self.empty = linked_list()

        self.single_num = create_linked_list([42])
        self.single_str = create_linked_list(['a'])
        self.two_num_1 = create_linked_list([42,2])
        self.two_num_2 = create_linked_list([2, 42])

        self.multiple_num = create_linked_list([0, 1, 2, 3, 4])
        self.multiple_num_same = create_linked_list([0, 1, 2, 3, 4])
        self.multiple_num_diff = create_linked_list([5, 6, 7, 8, 9])
        self.multiple_num_diff_front = create_linked_list([1, 1, 2, 3, 4])
        self.multiple_num_diff_back = create_linked_list([0, 1, 2, 3, 5])
        self.multiple_num_diff_mid = create_linked_list([0, 1, 3, 3, 4])

    def tearDown(self) :
        pass

    def test_empty_equal(self) :
        self.assertEqual(self.empty, linked_list())

    def test_single_equal(self) :
        self.assertEqual(self.single_num, create_linked_list([42]))
        self.assertEqual(self.single_str, create_linked_list(['a']))

    def test_multiple_equal(self) :
        self.assertEqual(self.multiple_num, self.multiple_num_same)

    def test_diff_type(self) :
        self.assertNotEqual(self.single_num, self.single_str)

    def test_different_sizes(self) :
        self.assertNotEqual(self.empty, self.single_num)
        self.assertNotEqual(self.single_num, self.two_num_1)
        self.assertNotEqual(self.single_num, self.two_num_2)
        self.assertNotEqual(self.two_num_1, self.single_num)
        self.assertNotEqual(self.two_num_2, self.single_num)

    def test_different_values(self) :
        self.assertNotEqual(self.multiple_num, self.multiple_num_diff)
        self.assertNotEqual(self.multiple_num, self.multiple_num_diff_front)
        self.assertNotEqual(self.multiple_num, self.multiple_num_diff_back)
        self.assertNotEqual(self.multiple_num, self.multiple_num_diff_mid)


class push_pop_test(unittest.TestCase) :

    def setUp(self) :
        self.alist = linked_list()

    def tearDown(self) :
        pass

    def test_push_back_only(self) :
        self.alist.push_back(42)
        self.assertTrue(self.alist.front().item, 42)
        self.assertTrue(self.alist.back().item, 42)

    def test_push_front_only(self) :
        self.alist.push_front(42)
        self.assertEqual(self.alist.front().item, 42)
        self.assertEqual(self.alist.back().item, 42)

    def test_push_front_pop(self) :
        self.alist.push_front(42)
        self.assertEqual(self.alist.pop_front(), 42)
        self.assertFalse(self.alist)

        self.alist.push_front(42)
        self.assertEqual(self.alist.pop_back(), 42)
        self.assertFalse(self.alist)

    def test_push_back_pop(self) :
        self.alist.push_back(42)
        self.assertEqual(self.alist.pop_back(), 42)
        self.assertFalse(self.alist)

        self.alist.push_back(42)
        self.assertEqual(self.alist.pop_front(), 42)
        self.assertFalse(self.alist)


    def test_multi_push_front(self) :
        self.alist.push_front(5)
        self.alist.push_front(4)
        self.assertEqual(self.alist.front().item, 4)
        self.assertEqual(self.alist.back().item, 5)      

        self.alist.push_front(3)
        self.assertEqual(self.alist.front().item, 3)
        self.assertEqual(self.alist.back().item, 5)   

        self.assertEqual(self.alist.pop_front(), 3)
        self.assertEqual(self.alist.pop_back(), 5)
        self.assertEqual(self.alist.pop_front(), 4)
        self.assertFalse(self.alist)

    def test_multi_push_back(self) :

        self.alist.push_back(3)
        self.alist.push_back(4)
        self.assertEqual(self.alist.front().item, 3)
        self.assertEqual(self.alist.back().item, 4)      

        self.alist.push_back(5)
        self.assertEqual(self.alist.front().item, 3)
        self.assertEqual(self.alist.back().item, 5)   

        self.assertEqual(self.alist.pop_front(), 3)
        self.assertEqual(self.alist.pop_front(), 4)
        self.assertEqual(self.alist.pop_back(), 5)
        self.assertFalse(self.alist)

    def test_torture(self) :

        self.alist.push_back(4)
        self.alist.push_front(3)
        self.assertEqual(self.alist.front().item, 3)
        self.assertEqual(self.alist.back().item, 4)      

        self.alist.push_front(2)
        self.alist.push_back(5)
        self.assertEqual(self.alist.front().item, 2)
        self.assertEqual(self.alist.back().item, 5)   

        self.assertEqual(self.alist.pop_front(), 2)
        self.assertEqual(self.alist.pop_back(), 5)
        self.assertEqual(self.alist.pop_back(), 4)
        self.assertTrue(self.alist)

        self.alist.push_front(1)
        self.alist.push_back(6)
        self.assertEqual(self.alist.pop_back(), 6)
        self.assertEqual(self.alist.pop_front(), 1)
        self.assertTrue(self.alist)

        self.alist.push_front(0)
        self.alist.push_back(7)
        self.alist.push_front(-1)
        self.assertEqual(self.alist.pop_front(), -1)
        self.assertEqual(self.alist.pop_back(), 7)
        self.assertEqual(self.alist.pop_back(), 3)
        self.assertEqual(self.alist.pop_front(), 0)
        self.assertFalse(self.alist)

class len_test(unittest.TestCase) :

    def setUp(self) :
        self.empty = linked_list()
        self.one = create_linked_list([42])
        self.multi = create_linked_list([1, 2, 3, 4, 5])

    def test_empty(self) :
        self.assertEqual(len(self.empty), 0)

    def test_one(self) :
        self.assertEqual(len(self.one), 1)

    def test_multi(self) :
        self.assertEqual(len(self.multi), 5)


class iter_test(unittest.TestCase) :
    def setUp(self) :
        self.empty = linked_list()
        self.one = create_linked_list([42])
        self.multi = create_linked_list([1, 2, 3, 4, 5])

    def test_empty(self) :
        # iteration gives nodes
        self.assertEqual([n.item for n in self.empty], [])

    def test_one(self) :
        self.assertEqual([n.item for n in self.one], [42])

    def test_multi(self) :
        self.assertEqual([n.item for n in self.multi], [1, 2, 3, 4, 5])

class reverse_test(unittest.TestCase) :
    def setUp(self) :
        self.empty = linked_list()
        self.one = create_linked_list([42])
        self.multi = create_linked_list([1, 2, 3, 4, 5])

    def test_empty(self) :
        # iteration gives nodes
        self.assertEqual([n.item for n in reversed(self.empty)], [])

    def test_one(self) :
        self.assertEqual([n.item for n in reversed(self.one)], [42])

    def test_multi(self) :
        self.assertEqual([n.item for n in reversed(self.multi)], [5, 4, 3, 2, 1])

class str_test(unittest.TestCase) :
    def setUp(self) :
        self.empty = linked_list()
        self.one = create_linked_list([42])
        self.multi = create_linked_list([1, 2, 3, 4, 5])

    def test_empty(self) :
        # supposed to have spaces, but not worth taking off
        self.assertEqual(str(self.empty).replace(' ', ''), '[]')

    def test_one(self) :
        # supposed to have spaces, but not worth taking off
        self.assertEqual(str(self.one).replace(' ', ''), '[42]')

    def test_multi(self) :
        # supposed to have spaces, but not worth taking off
        self.assertEqual(str(self.multi).replace(' ', ''), '[1,2,3,4,5]')

class contains_test(unittest.TestCase) :
    def setUp(self) :
        self.empty = linked_list()
        self.one = create_linked_list([42])
        self.multi_even = create_linked_list([1, 2, 3, 4])
        self.multi_odd = create_linked_list([1, 2, 3, 4, 5])

    def test_empty(self) :
        self.assertFalse(42 in self.empty)

    def test_one(self) :
        self.assertFalse(1 in self.one)
        self.assertTrue(42 in self.one)

    def test_even(self) :
        self.assertTrue(1 in self.multi_even)
        self.assertTrue(2 in self.multi_even)
        self.assertTrue(3 in self.multi_even)
        self.assertTrue(4 in self.multi_even)

        self.assertFalse(0 in self.multi_even)
        self.assertFalse(5 in self.multi_even)
        self.assertFalse(42 in self.multi_even)


    def test_odd(self) :
        self.assertTrue(1 in self.multi_odd)
        self.assertTrue(3 in self.multi_odd)
        self.assertTrue(5 in self.multi_odd)

        self.assertFalse(0 in self.multi_odd)
        self.assertFalse(6 in self.multi_odd)
        self.assertFalse(42 in self.multi_odd)

class lessthan_test(unittest.TestCase) :

    def setUp(self) :
        self.empty = linked_list()
        self.one_item = linked_list([2])

        self.list_one = linked_list([1, 2, 3])
        self.list_two = linked_list([1, 2, 3])
        self.list_three = linked_list([1, 2, 4])
        self.list_four = linked_list([1, 2])
        self.list_five = linked_list([1, 2, 3, 4])
        self.list_six = linked_list([2, 2, 3])
        self.list_seven = linked_list([1, 4, 3])

    def test_same(self) :
        self.assertFalse(self.empty < linked_list())
        self.assertFalse(self.list_one < self.list_two)

    def test_same_different_size(self) :
        self.assertTrue(self.empty < self.one_item)
        self.assertFalse(self.one_item < self.empty)

        self.assertTrue(self.empty < self.list_one)
        self.assertFalse(self.list_one < self.empty)

        self.assertTrue(self.list_four < self.list_three)
        self.assertFalse(self.list_three < self.list_four)

    def test_last_different(self) :
        self.assertTrue(self.list_one < self.list_three)
        self.assertFalse(self.list_two < self.list_one)

    def test_first_different(self) :
        self.assertTrue(self.list_one < self.one_item)
        self.assertFalse(self.one_item < self.list_one)

        self.assertTrue(self.list_one < self.list_six)
        self.assertFalse(self.list_six < self.list_one)

    def test_mid_different(self) :
        self.assertTrue(self.list_one < self.list_seven)
        self.assertFalse(self.list_seven < self.list_one)


if __name__ == '__main__' :
     unittest.main()
