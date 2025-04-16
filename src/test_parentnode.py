import unittest
from htmlnode import LeafNode, ParentNode

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_no_tag_error(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_parent_no_children_error(self):
        parent_node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_parent_props(self):
        child_node = LeafNode("b", "child")
        parent_node = ParentNode("a", [child_node], {"href": "https://www.google.com"})
        self.assertEqual(
            parent_node.to_html(),
            '<a href="https://www.google.com"><b>child</b></a>'
        )

    def test_parent_multiple_children(self):
        parent_node = ParentNode("div", [
            LeafNode("", "I'm Boring"),
            LeafNode("b", "I'm Bold"),
            LeafNode("i", "I'm Crooked")
            ])
        self.assertEqual(
            parent_node.to_html(),
            "<div><>I'm Boring</><b>I'm Bold</b><i>I'm Crooked</i></div>"
        )
        

if __name__ == "__main__":
    unittest.main()