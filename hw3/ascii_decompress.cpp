#include "tree_node.hpp"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

Tree_node* create_root(){
	Tree_node* root = new Tree_node();
	root->label = 0;
	root->byte = NULL;
	root->first_child = NULL;
	root->sibling = NULL;
	root->parent = NULL;

	return root;
}

void decompress(string line, Tree_node* root, vector<Tree_node*> nodes){
	Tree_node* current = root;

	for(int i =0; i <line.length();i++){ //iterate over characters in the string
		//get label somehow
		int label = something;
		Tree_node* current = nodes[label];
		print_path(current);
		char nextByte = more parsing stuff;
		labelCount = labelCount+1;
		insert_child(current, nextByte, labelCount);
		cout << nextByte;


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
	vector<Tree_node*> nodes;
	nodes.push_back(root);
	labelCount =0;
	myfile.open(argv[1]); //filename
	if(myfile.is_open()){
		while (getline(myfile,line)){
			decompress(line, root, nodes);
		}
		myfile.close();
	}
	return 0;
}