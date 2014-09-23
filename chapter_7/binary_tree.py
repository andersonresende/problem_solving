#!/usr/bin/env python

def binary_tree(root):
	return [root, [], []]


def insert_left(tree, new):
	if new:
		tree[1] = binary_tree(new)


def insert_right(tree, new):
	if new:
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

