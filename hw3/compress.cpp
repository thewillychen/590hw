//Problem 3
#include "tree_node.hpp"
#include <iostream>
#include <fstream>
#include <string>
#include "util.c"

using namespace std;

Tree_node* create_root(){
	Tree_node* root = new Tree_node(0,0);
	root->first_child = (Tree_node*)NULL;
	root->sibling = (Tree_node*)NULL;
	root->parent = (Tree_node*)NULL;

	return root;
}

void compress(Tree_node* root, int maxLabel){
	Tree_node* current = root;
	int labelCount = 0;
	while(cin.peek() != EOF){
		char c;
		cin.get(c);
		Tree_node* child = find_child(current, c);
		if(child == NULL){
			maxLabel = labelCount;
			print_label(current->label, maxLabel);
			print_letter(c);

			labelCount = labelCount+1;
			insert_child(current,c,labelCount);
			current = root;
		}
		else{
			current = child;
		}
	}
	print_final_label(current->label, labelCount);
}

int main(int argc, char ** argv){
	Tree_node* root = create_root();
	int max = 10;
	compress(root, max);
	return 0;
}