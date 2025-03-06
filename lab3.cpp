#include <iostream>
#include <new>
using namespace std;

class Node {
public:
    int data;
    Node* next;
    Node(int x, Node* n) { data = x; next = n; }
};

class Queue {
    Node* front;
    Node* rear;
public:
    Queue() { front = nullptr; rear = nullptr; }
    void enqueue(int x) {
        Node* temp = new Node(x, nullptr);
        if (isEmpty()) { front = rear = temp; }
        else { rear->next = temp; rear = temp; }
    }
    void dequeue() {
        if (isEmpty()) { cout << "Queue is empty\n"; return; }
        Node* temp = front;
        front = front->next;
        if (front == nullptr) { rear = nullptr; }
        delete temp;
    }
    int top() {
        if (isEmpty()) { cout << "Queue is empty\n"; return -1; }
        return front->data;
    }
    bool isEmpty() { return (front == nullptr); }
    int size() {
        int count = 0;
        Node* current = front;
        while (current != nullptr) {
            count++;
            current = current->next;
        }
        return count;
    }
};

int main() {
    Queue q;
    if (q.isEmpty()) { cout << "Queue is empty\n"; }
    return 0;
}