#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Node{
public:
    bool end;
    unordered_map<char, Node*> child;
    Node() : end(false) {}
};

class Tree{
public:
    Node* root;
    Tree() {
        root = new Node();
    }

    bool insert(const string &num) {
        Node* node = root;
        for (char dig: num) {
            if (node->end)
                return false;
            if (node->child.find(dig) == node->child.end())
                node->child[dig] = new Node();
            node = node->child[dig];
        }
        if (node->end || !node->child.empty())
            return false;
        node->end = true;
        return true;
    }
};

string ch(const vector<string> &nums) {
    Tree tree;
    for (const string &num : nums) {
        if (!tree.insert(num))
            return "NO";
    }
    return "YES";
}

int main() {
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        vector<string> nums(n);
        for (int i=0; i<n; i++) {
            cin >> nums[i];
        }
        cout << ch(nums) << endl;
    }
    return 0;
}