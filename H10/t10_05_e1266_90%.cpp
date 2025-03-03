#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;


void f1(size_t index, int curr, const vector<int>& tracks, int leng, int& best) {
    if (curr > leng) return;
    if (curr > best) best = curr;
    if (index >= tracks.size()) return;
    f1(index + 1, curr, tracks, leng, best);
    if (curr + tracks[index] <= leng) {
        f1(index + 1, curr + tracks[index], tracks, leng, best);
    }
}

int main() {
    string line;
    while (getline(cin, line)) {
        if (line.empty()) continue;
        istringstream iss(line);
        int length, count;
        iss >> length >> count;
        vector<int> tracks;
        int track;
        while (iss >> track) {
            tracks.push_back(track);
        }
        sort(tracks.rbegin(), tracks.rend());
        int best = 0;
        f1(0, 0, tracks, length, best);
        cout << "sum:" << best << endl;
    }
    return 0;
}