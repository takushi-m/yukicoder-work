#include<iostream>
#include<iomanip>
#include<vector>
#include<algorithm>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

void sample(){
  vector<vector<int>> vvi = vector<vector<int>>(20, vector<int>(10, 0));  // vvi[20][10]
  vector<vector<vector<int>>> vvvi = vector<vector<vector<int>>>(30, vector<vector<int>>(20, vector<int>(10, 0)));  // vvvi[30][20][10]

  vector<int> v = {3,2,1};
  sort(v.begin(), v.end());
  do {
    // pass
  } while(next_permutation(v.begin(), v.end()));

  for(auto x: v){
    cout<<x<<endl;
  }
}

int main(){
  int n;
  cin>>n;
  vector<ull> al = vector<ull>(n+1);
  vector<ull> bl = vector<ull>(n+1);

  for(int i=0;i<n+1;i++){
    cin>>al[i];
  }
  for(int i=0;i<n+1;i++){
    cin>>bl[i];
  }

  ull res = 0;
  for(int i=0;i<n+1;i++){
    for(int j=0;j<n+1;j++){
      if(i+j<=n){
        res += (ull)(al[i]*bl[j]);
        res %= (ull)(1000000007);
      }else{
        break;
      }
    }
  }
  cout<<res<<endl;
  return 0;
}
