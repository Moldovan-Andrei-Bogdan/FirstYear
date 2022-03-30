#pragma once

#include "Bag.h"

class DynamicVector {
private:
	TElem* elements;
	int length;
	int capacity;

public:
	int push(TElem element_to_add);
};