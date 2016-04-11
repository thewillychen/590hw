#ifndef TREE_NODE_HPP
#define TREE_NODE_HPP

class Tree_node{
public:
	Tree_node();

	int label;
	char byte;
	Tree_node *first_child;
	Tree_node *sibling;
	Tree_node *parent;

	Tree_node(char newByte, int newLabel){
		byte = newByte;
		label = newLabel;
	}
};

Tree_node* find_child(Tree_node *parent, char c);
Tree_node* insert_child(Tree_node *parent, char byte, int label);
void print_path(Tree_node *last_node);

#endif