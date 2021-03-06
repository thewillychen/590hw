//Problem 2
#include "tree_node.hpp"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

Tree_node* create_root(){
	Tree_node* root = new Tree_node(0,0);
	root->first_child = NULL;
	root->sibling = NULL;
	root->parent = NULL;

	return root;
}

void decompress(Tree_node* root, vector<Tree_node*> nodes){
	Tree_node* current = root;
	int labelCount = 0;
	int label;
	char junk;
	char c;

	while(cin.peek() != EOF){
		cin >> label;
		cin.get(junk);
		cin.get(c);

		Tree_node* current = nodes[label];
		print_path(current);
		labelCount = labelCount+1;
		if(cin.peek() != EOF){
			Tree_node* child = insert_child(current, c, labelCount);
			nodes.push_back(child);
			cout << c;
		}
	}
}

int main(int argc, char ** argv){
	Tree_node* root = create_root();
	vector<Tree_node*> nodes;
	nodes.push_back(root);
	decompress(root, nodes);
	return 0;
}