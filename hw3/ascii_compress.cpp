#include "tree_node.hpp"
#include <iostream>
#include <fstream>
#include <string>

Tree_node* create_root(){
	Tree_node* root = new Tree_node();
	root->label = 0;
	root->byte = NULL;
	root->first_child = NULL;
	root->sibling = NULL;
	root->parent = NULL;

	return root;
}

void compress(string line, Tree_node* root){
	Tree_node* current = root;

	for(int i =0; i <line.length();i++){ //iterate over characters in the string
		char c = line[i];
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
	ifstream myfile;
	string line;
	root = create_root();
	myfile.open(argv[1]); //filename
	if(myfile.is_open()){
		while (getline(myfile,line)){
			compress(line, root);
		}
		myfile.close();
	}
	return 0;
}