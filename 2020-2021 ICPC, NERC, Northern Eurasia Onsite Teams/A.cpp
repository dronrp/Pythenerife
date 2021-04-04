#include <bits/stdc++.h>

/*
ICPC 2020–2021, NERC – Northern Eurasia Finals, Onsite

Problem K:  King’s Task
Andrey Rosario, Alberto Rodríguez, Sergio Rodríguez
04/04/2021
*/
using namespace std;
bool perm1 (vector<int> &a, int n){
    for (int i = 0; i<n; i++){
        swap(a[i],a[n+i]);
    }
   
    return is_sorted(a.begin(), a.end());
}

bool perm2 (vector<int> &a, int n){
    for (int j = 0; j<n*2-1; j+=2){
      swap (a[j], a[j+1]);
    } 
    return is_sorted(a.begin(), a.end());
}

int main(){
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin>>n;
    vector<int> a(2*n); 
    vector<int> b(2*n);

    for (int i = 0; i<2*n; i++){
        int x; 
        cin >> x;
        a[i] = x;
        b[i] = x;
    }

    if (!is_sorted(a.begin(), a.end())){
        int ans1 = 0, ans2 = 0;
        for (int i = 0; i<n; i++){
          if (!perm2(a, n)){
            ans1++;
          } else {
            break;
          }
          
          if (!perm1(a, n)){
            ans1++;
          } else {
            break;
          }
        }

        if (!is_sorted(a.begin(), a.end())){
            ans1 = -1;
        }

        for (int i = 0; i<n; i++){
          if (!perm1(b, n)){
            ans2++;
          } else {
            break;
          }
          
          if (!perm2(b, n)){
            ans2++;
          } else {
            break;
          }
        }

        if (!is_sorted(b.begin(), b.end())){
            ans2 = -1;
        }
        if (ans1 < ans2){
            if (ans1 < 0){
                cout << -1 << "\n";
            } else {
                cout << ans1 + 1 << "\n";
            }
            
        } else {
            if (ans2 < 0){
                cout << -1 << "\n";
            } else {
                cout << ans2 + 1 << "\n";
            }
        }
        
    } else {
        cout << "0" << "\n";
    }
    
    return 0;
}