#include "tree_node.hpp"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

Tree_node* create_root(){
	Tree_node* root = new Tree_node();
	root->label = 0;
	root->byte = NULL;
	root->first_child = (Tree_node*)NULL;
	root->sibling = (Tree_node*)NULL;
	root->parent = (Tree_node*)NULL;

	return root;
}

void compress(Tree_node* root){
	Tree_node* current = root;

	while(cin.peek() != EOF){
		char c;
		cin.get(c);
		child = find_child(current, c);
		if(child == NULL){
			cout << current->label << " ";
			cout.put(c);

			insert_child(current,c,current->label+1);
			current = root;
		}
		else{
			current = child;
		}
	}
	cout << current->label << "\n";
}

int main(int argc, char ** argv){
	root = create_root();
	compress(root);
	return 0;
}