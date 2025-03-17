#include <iostream>

class Node {
    public:
        Node(int dt=0, Node* nxt=0)
        {
            this->data = dt;
            this->next = nxt;
        }
    public:
        int data;
        Node* next;
};

int main()
{
    Node *header = 0;
    for (int i = 0; i<5; i++) 
        header = new Node(i, header);
    while (header != 0) {
        std::cout<< header->data << std::endl;
        Node *p = header;
        header = header->next;
        delete p;
    }
    return 0;
}

