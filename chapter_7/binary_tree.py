# -*- coding: utf-8 -*-
#!/usr/bin/env python

""" A set of functions of binary trees """


def binary_tree(root):
	return [root, [], []]


def insert_left(tree, new):
	
	tree[1] = binary_tree(new)


def insert_right(tree, new):
	
	tree[2] = binary_tree(new)


def get_root_val(tree):
	return tree[0]


def get_left_child(tree):
	return tree[1]


def get_right_child(tree):
	return tree[2]






tree = binary_tree('A')
print tree
insert_left(tree, 'B')
print tree
insert_right(tree, 'C')
print tree
insert_left(tree[1], 'D')
print tree
print get_root_val(tree)
print get_left_child(tree)


# # >>parse_binary_tree('( 3 * 5 )')
# def parse_binary_tree(exp):
# 	list_exp = exp.split()
# 	tree = binary_tree(None)

# 	for exp in list_exp:

# 		if exp == '(':
# 			insert_left(tree, '')
# 			tree = get_left_child(tree)

# 		if exp in map(str, range(1,10)):
# 			tree[0] = exp
# 			tree = tree

# 		if exp in ['*', '+', '-', '/']:
# 			tree[0] = exp
# 			tree = get_right_child(tree)

# 	return tree

# print parse_binary_tree('( 3 * 5 )')



