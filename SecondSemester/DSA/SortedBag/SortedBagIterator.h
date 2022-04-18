#pragma once
#include "SortedBag.h"

class SortedBag;

class SortedBagIterator
{
	friend class SortedBag;

private:
	const SortedBag& bag;
	SortedBagIterator(const SortedBag& b);
    int head_of_dll;
    int tail_of_dll;
    int aux;
    int number_of_elements_of_dll;
    int count_of_elem;
	//TODO - Representation

public:
	TComp getCurrent();
	bool valid();
	void next();
	void first();
};

