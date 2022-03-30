#include "Bag.h"
#include "BagIterator.h"
#include <exception>
#include <iostream>
using namespace std;


Bag::Bag() {
	//TODO - Implementation
	this->unique_array = new TElem[10];
	this->positions_array = new int[10];
	this->capacity_of_unique_array = 10;
	this->capacity_of_positions_array = 10;
	this->length_of_unique_array = 0;
	this->length_of_positions_array = 0;
}

void Bag::resize_unique() {
	/// n-length of uniqe array
	/// Complexity AC=BC=WC=O(n)
	TElem* new_resized_array = new TElem[this->capacity_of_unique_array * 2];
	int index;
	for (index = 0;index < this->length_of_unique_array;index++) {
		new_resized_array[index] = this->unique_array[index];
	}
	TElem* aux;
	aux = this->unique_array;
	this->capacity_of_unique_array *= 2;
	delete[] aux;
	this->unique_array = new_resized_array;
}

void Bag::resize_positions() {
	/// n-length of positions array
	/// Complexity AC=BC=WC=O(n)
	int index;
	int* aux;
	int* new_resized_pos_array = new int[this->capacity_of_positions_array * 2];
	for (index = 0;index < this->length_of_positions_array;index++) {
		new_resized_pos_array[index] = this->positions_array[index];
	}
	this->capacity_of_positions_array *= 2;
	aux = this->positions_array;
	delete[] aux;
	this->positions_array = new_resized_pos_array;
}

Bag::Bag(const Bag& elem) {
	this->capacity_of_unique_array = elem.capacity_of_unique_array;
	this->capacity_of_positions_array = elem.capacity_of_positions_array;
	this->length_of_unique_array = elem.length_of_unique_array;
	this->length_of_positions_array = elem.length_of_positions_array;
	this->unique_array = new TElem[this->capacity_of_unique_array];
	this->positions_array = new int[this->capacity_of_positions_array];
	int index;
	for (index = 0;index < this->length_of_unique_array;index++) {
		this->unique_array[index] = elem.unique_array[index];
	}
	for (index = 0;index < this->length_of_positions_array;index++) {
		this->positions_array[index] = elem.positions_array[index];
	}
}

void Bag::add(TElem elem) {
	//TODO - Implementation
	/// n- length of unique array   m-length of positions array
	/// Complexity AC=WC=O(2n) BC=O(n) --- resize parts not taken into consideration 
	if (this->search(elem)==true) {
		if (this->length_of_positions_array == this->capacity_of_positions_array) {
			this->resize_positions();
		}
		int index;
		for (index = 0;index < this->length_of_unique_array;index++) {
			if (this->unique_array[index] == elem) {
				break;
			}
		}
		this->positions_array[this->length_of_positions_array] = index;
		this->length_of_positions_array += 1;
	}
	else {
		if (this->length_of_unique_array == this->capacity_of_unique_array) {
			this->resize_unique();
		}
		if (this->length_of_positions_array == this->capacity_of_positions_array) {
			this->resize_positions();
		}
		this->unique_array[this->length_of_unique_array] = elem;
		this->length_of_unique_array += 1;
		this->positions_array[this->length_of_positions_array] = this->length_of_unique_array - 1;
		this->length_of_positions_array += 1;
	}
}


bool Bag::remove(TElem elem) {
	//TODO - Implementation
	/// n- length of unique array m-length of positions array
	/// Complexity BC=O(n), when the element does not exist
	/// WC=AC=O(n*m)
	int index;
	if (this->search(elem)==false) {
		return false;
	}
	else {
		int element_appear_count = this->nrOccurrences(elem);
		for (index = 0;index < this->length_of_unique_array;index++) {
			if (this->unique_array[index] == elem) {
				break;
			}
		}
		int aux = index;
		for (index = 0;index < this->length_of_positions_array;index++) {
			if (this->positions_array[index] == aux) {
				break;
			}
		}
		while (index + 1 < this->length_of_positions_array) {
			this->positions_array[index] = this->positions_array[index + 1];
			index += 1;
		}
		this->length_of_positions_array -= 1;
		if (element_appear_count == 1) {
			int aux2 = aux;
			while (aux < this->length_of_unique_array) {
				for (index = 0;index < this->length_of_positions_array;index++) {
					if (this->positions_array[index] == aux) {
						this->positions_array[index] -= 1;
					}
				}
				aux += 1;
			}
			while (aux2 + 1 < this->length_of_unique_array) {
				this->unique_array[aux2] = this->unique_array[aux2 + 1];
				aux2 += 1;
			}
			this->length_of_unique_array -= 1;
		}
		return true;
	}
}


bool Bag::search(TElem elem) const {
	//TODO - Implementation
	/// n- length of unique array
	/// Complexity BC=O(1), when we find the element on the first position
	/// AC=WC=O(n)
	int index;
	for (index = 0;index < this->length_of_unique_array;index++) {
		if (this->unique_array[index] == elem) {
			return true;
		}
	}
	return false;
}

int Bag::nrOccurrences(TElem elem) const {
	//TODO - Implementation
	/// n= length of unique array  m=length of positions array
	/// AC=WC=O(n+m)
	/// BC=O(n)
	int index;bool found_flag = false;
	for (index = 0;index < this->length_of_unique_array;index++) {
		if (this->unique_array[index] == elem) {
			found_flag = true;
			break;
		}
	}
	if (found_flag == false) {
		return 0;
	}
	else {
		int position = index;int count = 0;
		for (index = 0;index < this->length_of_positions_array;index++) {
			if (this->positions_array[index] == position) {
				count += 1;
			}
		}
		return count;
	}
}


int Bag::size() const {
	//TODO - Implementation
	///Complexity AC=WC=BC=O(1)
	return this->length_of_positions_array;
}


bool Bag::isEmpty() const {
	//TODO - Implementation
	///Complexity AC=WC=BC=O(1)
	if (this->length_of_positions_array == 0) {
		return true;
	}
	return false;
}

BagIterator Bag::iterator() const {
	return BagIterator(*this);
}

void Bag::addOcurrences(int nr, TElem elem) {

	///n- length of unique array  m-length of positions array
	/// Complexity approx:
	/// BC- O(nr), when the element is on the first position in the unique array, so we only add at the end of positions array a new entry
	/// AC- O(nr*n)
	/// WC- O(nr*n), here worst case when we do not find the element inside so we iterate trough the whole unique array
	if (nr < 0) {
		throw exception();
	}
	int count;
	for (count = 1;count <= nr;count++) {
		this->add(elem);
	}
}

Bag::~Bag() {
	delete[] this->unique_array;
	delete[] this->positions_array;
}

