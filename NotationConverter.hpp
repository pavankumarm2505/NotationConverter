#ifndef NOTATIONCONVERTER_H 
#define NOTATIONCONVERTER_H 
#include "NotationConverterInterface.hpp"
#include <iostream>

class Node{
    public: 
    std::string value; 
    Node* next; 
    Node* prev;
};
class dlinkeddeck: public Node{
    public:
    Node* head=NULL;
    bool checkinvchar(std::string inStr);
    void insertFront(std::string &a);
    void insertBack(std::string& b);
    void removeFront();
    void removeBack();
    std::string getFront();
    std::string getBack();
    bool isOperand(char x);
};
    



class NotationConverter: public dlinkeddeck{
    public:
    std::string postfixToInfix(std::string inStr);
    std::string infixToPostfix(std::string inStr);
    std::string infixToPrefix(std::string inStr);
    std::string prefixToInfix(std::string inStr);
    std::string prefixToPostfix(std::string inStr);
    std::string postfixToPrefix(std::string inStr);
};
#endif
