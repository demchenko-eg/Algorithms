#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
using namespace std;

const int MOD = 1000000007;
const int q = 127;
const int INF = numeric_limits<int>::max();

struct Node {
    int parent;
    int value;
    vector<int> children;
};

int n;
vector<Node> tree;
vector<int> internalAns;

vector<int> dfs(int u) {
    vector<int> cur;
    cur.push_back(tree[u].value);
    for (int child : tree[u].children) {
        vector<int> sub = dfs(child);
        vector<int> merged;
        merged.resize(cur.size() + sub.size());
        int i = 0, j = 0, k = 0;
        while(i < cur.size() && j < sub.size()){
            if(cur[i] < sub[j]){
                merged[k++] = cur[i++];
            } else {
                merged[k++] = sub[j++];
            }
        }
        while(i < cur.size()){
            merged[k++] = cur[i++];
        }
        while(j < sub.size()){
            merged[k++] = sub[j++];
        }
        cur = move(merged);
    }
    if(!tree[u].children.empty()){
        int mn = INF;
        for (int i = 1; i < cur.size(); i++) {
            int diff = cur[i] - cur[i-1];
            if(diff < mn)
                mn = diff;
        }
        internalAns[u] = mn;
    }
    return cur;
}

long long modExp(long long base, int exp) {
    long long res = 1;
    while(exp > 0) {
        if(exp & 1)
            res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return res;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n;
    tree.resize(n);
    internalAns.assign(n, -1);
    int root = -1;
    for (int i = 0; i < n; i++){
        int p, v;
        cin >> p >> v;
        tree[i].parent = p;
        tree[i].value = v;
        if(p == -1) {
            root = i;
        } else {
            tree[p].children.push_back(i);
        }
    }
    dfs(root);
    long long ans = 0;
    for (int i = 0; i < n; i++){
        if(internalAns[i] != -1){
            long long power = modExp(q, i);
            ans = (ans + (1LL * internalAns[i] * power) % MOD) % MOD;
        }
    }
    cout << ans << "\n";
    return 0;
}