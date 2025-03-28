#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

// 配列の中身を表示する関数
void output(vector<int> A) {
    for (int i=0; i<A.size(); i++) {
        cout << A[i];
        if (i!=A.size()-1) cout << " ";
        else cout << endl;
    }
}

int main() {
    // 入力
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i=0; i<N; i++) cin >> A[i];

    // 選択ソート
    for (int k=0; k<N-1; k++) {
        // 未ソートの要素のうち最小値がある位置を求める
        auto min_element_itr = min_element(A.begin()+k, A.end());

        // 未ソートの要素の先頭 A[k] と最小値を入れ替え、
        // 次のループでは A[0]...A[k] をソート済みとみなす
        swap(A[k], *min_element_itr);

        // 現時点での配列の中身を出力する
        output(A);
    }
}
