#include "SortedSet.h"
#include "SortedSetIterator.h"
#include <iostream>

SortedSet::SortedSet(Relation r) {
    //TODO - Implementation
    this->relation = r;
    this->root = nullptr;
    this->end = nullptr;
    this->length_of_set = 0;
}


bool SortedSet::add(TComp elem) {
    /// BC=WC=AC=Theta(number_of_nodes) if we take the search part into consideration along with add
    /// BC=Theta(1)(empty list) WC=AC=Theta(number_of_nodes) if we do not take into consideration the search part
    //TODO - Implementation
    if (this->search(elem)) {
        return false;
    } else {
        if (this->length_of_set == 0) {
            Node *node_to_add = new Node;
            node_to_add->info = elem;
            node_to_add->next = nullptr;
            this->root = node_to_add;
            this->end = node_to_add;
            this->length_of_set += 1;
        } else if (this->length_of_set >= 1) {
            if (this->relation(this->root->info, elem)) {
                Node *current_node = this->root->next;
                Node *prev_node = this->root;
                while (current_node != nullptr && this->relation(current_node->info, elem)) {
                    prev_node = prev_node->next;
                    current_node = current_node->next;
                }
                if (current_node != nullptr) {
                    Node *node_to_insert = new Node;
                    node_to_insert->info = elem;
                    node_to_insert->next = current_node;
                    prev_node->next = node_to_insert;
                    this->length_of_set += 1;
                } else {
                    Node *node_to_insert = new Node;
                    node_to_insert->info = elem;
                    node_to_insert->next = nullptr;
                    prev_node->next = node_to_insert;
                    this->end = node_to_insert;
                    this->length_of_set += 1;
                }
            } else {
                Node *node_to_insert = new Node;
                node_to_insert->info = elem;
                node_to_insert->next = this->root;
                this->root = node_to_insert;
                this->length_of_set += 1;
            }
        }
        return true;
    }
}


bool SortedSet::remove(TComp elem) {
    /// BC=WC=AC=Theta(number_of_nodes) if we take the search part into consideration along with add
    /// BC=Theta(1)(only one element in list) WC=AC=Theta(number_of_nodes) if we do not take into consideration the search part
    if (this->search(elem) == false) {
        return false;
    } else {
        if (this->length_of_set == 1) {
            delete this->root;
            this->root = nullptr;
            this->length_of_set -= 1;
        } else if (this->length_of_set > 1) {
            if (this->root->info != elem) {
                Node *current_node = this->root->next;
                Node *prev_node = this->root;
                while (current_node->info != elem) {
                    current_node = current_node->next;
                    prev_node = prev_node->next;
                }
                prev_node->next = current_node->next;
                delete current_node;
                this->length_of_set -= 1;
            } else {
                Node *aux = this->root->next;
                delete this->root;
                this->root = aux;
                this->length_of_set -= 1;
            }
        }
        return true;
    }
}


bool SortedSet::search(TComp elem) const {
    /// BC=Theta(1)(empty list) AC=WC=Theta(number_of_nodes_in_list)
    //TODO - Implementation
    Node *current_node = this->root;
    while (current_node != nullptr) {
        if (current_node->info == elem) {
            return true;
        }
        current_node = current_node->next;
    }
    return false;
}


int SortedSet::size() const {
    /// AC=WC=BC=Theta(1)
    //TODO - Implementation
    return this->length_of_set;
}


bool SortedSet::isEmpty() const {
    /// AC=WC=BC=Theta(1)
    //TODO - Implementation
    if (this->length_of_set == 0) {
        return true;
    }
    return false;
}

SortedSetIterator SortedSet::iterator() const {
    /// AC=BC=WC=Theta(1)
    return SortedSetIterator(*this);
}

void SortedSet::print_order() {
    Node *current_node = this->root;
    while (current_node != nullptr) {
        std::cout << current_node->info << " ";
        current_node = current_node->next;
    }
}

SortedSet::~SortedSet() {
    /// BC=Theta(1)(empty list) WC=AC=Theta(number_of_nodes_in_list)
    //TODO - Implementation
    Node *aux;
    while (this->root != nullptr) {
        aux = this->root;
        this->root = this->root->next;
        delete aux;
    }
}


