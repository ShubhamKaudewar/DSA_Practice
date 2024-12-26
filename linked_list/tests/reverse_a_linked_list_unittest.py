import unittest
from io import StringIO
from unittest.mock import patch
from linked_list.reverse_a_linked_list import SinglyLinkedList, print_singly_linked_list, reverse

class TestLinkedListReverse(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '5', '1', '2', '3', '4', '5'])
    @patch('os.environ', {'OUTPUT_PATH': 'output.txt'})
    def test_reverse(self, mock_input):
        # Mock the file write to capture the output
        output = StringIO()

        # Create the linked list and reverse it
        llist = SinglyLinkedList()
        llist.insert_node(1)
        llist.insert_node(2)
        llist.insert_node(3)
        llist.insert_node(4)
        llist.insert_node(5)

        reversed_llist = reverse(llist.head)

        # Write reversed list to output
        print_singly_linked_list(reversed_llist, ' ', output)

        # Verify the output
        self.assertEqual(output.getvalue().strip(), '5 4 3 2 1')


if __name__ == '__main__':
    unittest.main()
