// link:-> https://www.hackerrank.com/challenges/counting-valleys/ 

#include <bits/stdc++.h>

using namespace std;

int check_for_valley(int count,int * flag){
    if(count<0 && *flag == 0){
        *flag = 1;
        return 1;
    }
    else if(count >= 0){
        *flag=0;
        return 0;
    }
    return 0;
}

int countingValleys(int n, string s) {
    int flag = 0;
    int count = 0;
    int valley = 0;

    for(int i=0;i<n;i++){
        if(s[i]=='U'){
            count++;
        }
        else{
            count--;
        }
        valley = valley+check(count,&flag);
    }

    return valley;

}

int main()
{
    int n;
    cin >> n;
    string s;
    getline(cin, s);

    int result = countingValleys(n, s);

    cout << result << "\n";

    cout.close();

    return 0;
}
