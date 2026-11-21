from reverse_linked_list import ListNode, reverse_list


def test_returns_none_if_no_head_node():
    """Returns None if there's no head node"""
    result = reverse_list(head=None)
    assert result is None


def test_reverses_linked_list():
    """Takes in a SLL and reverses it"""
    node_one = ListNode(1)
    node_one.next = ListNode(2)
    node_one.next.next = ListNode(3)
    node_one.next.next.next = ListNode(4)

    current = reverse_list(node_one)
    i = 4

    while current:
        node_val = current.val
        assert node_val == i
        current = current.next
        i -= 1
