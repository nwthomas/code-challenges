from intersecting_lists import SinglyLinkedList, get_intersection_of_lists
import unittest

class TestIntersectingLists(unittest.TestCase):
    def test_returns_intersecting_value(self):
        """Returns the Node where two singly-linked lists intersect"""
        list_1, list_2 = self.generate_intersecting_lists([51, 4, 3, 7, 8], [5, 10, 3])
        result = get_intersection_of_lists(list_1, list_2)
        self.assertEqual(result.value, 3)


    def generate_intersecting_lists(self, list_1, list_2):
        """Returns two singly-linked lists (with second having up to the connecting point) which intersect"""
        first_list = SinglyLinkedList(list_1[0])
        second_list = SinglyLinkedList(list_2[0])

        for value in list_1[1:]:
            first_list.add_value(value)
        
        for i, value in enumerate(list_2[1:]):
            if i == len(list_2[1:]) - 1:
                current = first_list.head

                while current:
                    if current.value == value:
                        second_list.tail.next = current
                        second_list.tail = current
                        break
                    else:
                        current = current.next
            else:
                second_list.add_value(value)

        return [first_list, second_list]

if __name__ == "__main__":
    unittest.main()
