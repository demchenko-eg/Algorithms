#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


bool can_place_cows(const vector<pair<int, int>>& intervals, int n, int d) {
    int count = 0;
    int last_pos = -1;

    for (const auto& [a, b] : intervals) {
        int pos = (last_pos == -1) ? a : max(a, last_pos + d);
        while (pos <= b) {
            count++;
            if (count == n) return true;
            last_pos = pos;
            pos += d;
        }
    }
    return false;
}

int max_min_distance(int n, const vector<pair<int, int>>& intervals) {
    int left = 1, right = intervals.back().second - intervals.front().first;
    int ans = 1;
    
    while (left <= right) {
        int mid = (left + right) / 2;
        if (can_place_cows(intervals, n, mid)) {
            ans = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return ans;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<pair<int, int>> intervals(m);
    for (int i = 0; i < m; i++) {
        cin >> intervals[i].first >> intervals[i].second;
    }
    sort(intervals.begin(), intervals.end());
    cout << max_min_distance(n, intervals) << endl;
    return 0;
}