#include "tree_node.hpp"
#include <iostream>
using namespace std;

//problem 1
Tree_node* find_child(Tree_node *parent, char c){
	Tree_node *current = parent->first_child;
	while(current != NULL){
		if(current->byte == c){
			return current;
		}
		current = current->sibling;
	}
	return NULL;
}

Tree_node* insert_child(Tree_node *parent, char byte, int label){
	Tree_node* child = new Tree_node(byte, label);
	child->parent = parent;
	child->first_child = NULL;
	child->sibling = NULL;

	if(parent->first_child == NULL){
		parent->first_child = child;
	}
	else{
		Tree_node *current = parent->first_child;
		while(current->sibling != NULL){
			current=current->sibling;
		}
		current->sibling = child;
	}
	return child;
}

void print_path(Tree_node *last_node){
	if(last_node->parent == NULL){ //base case of root
		return;	
	} 

	print_path(last_node->parent);
	cout << last_node->byte;
}