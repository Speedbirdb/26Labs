#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
};

class Stack {
private:
    Node* head; // Points to top element of stack.
    int num; // Number of elements (index-style tracking).
    int capacity; // Fixed size limit (resized when full).
public:
    Stack(int initialCapacity) {
        head = nullptr;
        num = -1;
        capacity = initialCapacity;
    }

    void push(int x) {
        if (num + 1 >= capacity) {
            increaseCapacity();
        }
        Node* newNode = new Node;
        newNode->data = x;
        newNode->next = head;
        head = newNode;
        num++;
    }

    int pop() {
        if (isEmpty()) {
            return -1;
        }
        Node* temp = head;
        int result = temp->data;
        head = head->next;
        delete temp;
        num--;
        return result;
    }

    int peek() {
        if (isEmpty()) {
            return -1;
        }
        return head->data;
    }

    bool isEmpty() {
        return num < 0;
    }

    void increaseCapacity() {
        capacity = capacity * 2;
    }

    bool deleteElement(int val) {
        if (isEmpty()) {
            return false;
        }
        if (head->data == val) {
            Node* temp = head;
            head = head->next;
            delete temp;
            num--;
            return true;
        }
        Node* current = head;
        while (current->next != nullptr) {
            if (current->next->data == val) {
                Node* temp = current->next;
                current->next = temp->next;
                delete temp;
                num--;
                return true;
            }
            current = current->next;
        }
        return false;
    }

    ~Stack() {
        while (!isEmpty()) {
            pop();
        }
    }
};

int main() {
    Stack stack(3);
    stack.push(1);
    stack.push(2);
    stack.push(3);
    stack.push(4);
    cout << stack.peek() << endl;
    cout << stack.pop() << endl;
    cout << stack.peek() << endl;
    cout << stack.deleteElement(2) << endl;
    cout << stack.deleteElement(5) << endl;
    return 0;
}