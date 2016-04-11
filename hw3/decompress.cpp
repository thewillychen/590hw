//Problem 3
#include "tree_node.hpp"
#include <string>
#include <vector>
#include "util.c"

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
	char c;

	while((label = read_label(labelCount)) != -1 && read_letter(c)){
		Tree_node* current = nodes[label];
		print_path(current);
		labelCount = labelCount+1;
		Tree_node* child = insert_child(current, c, labelCount);
		nodes.push_back(child);
		cout << c;
	}

	if(label != -1){
		Tree_node* cur = nodes[label];
		print_path(cur);
	}
}

int main(int argc, char ** argv){
	Tree_node* root = create_root();
	vector<Tree_node*> nodes;
	nodes.push_back(root);
	decompress(root, nodes);
	return 0;
}