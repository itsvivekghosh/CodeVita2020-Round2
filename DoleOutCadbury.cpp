/*
    Problem C: Dol out Cadbury
    
    In this problem, We have to find: 
        Print total number of children who will get chocolate.
*/

// Including main header File
#include<bits/stdc++.h>

// Some MACROS
#define int long long
#define LOOP(i, x, y) for(int i=x;i<=y;++i)
#define endl "\n"
#define init(s, o) s *o = new s();
#define d(obj) delete obj;
#define input(n) cin>>n;
#define print(n) cout<<n;
#define BOOST ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define ANSWER(a, b, ans, fun) ans += fun(a, b);

// Defining NameSpace
using namespace std;

// Class that calculates the Solution
class Solution {

    // Maximum Length, Minimum Length, Maximum Width, Minimum Width
    int mxLength, mnLength, mxWidth, mnWidth;
    // Stores our answer
    int ans = 0; 

    public:
        // Constructor that takes input and calls solve()
        Solution() {
            cin>>mnLength>>mxLength>>mnWidth>>mxWidth;
            input(mnLength)
            input(mxLength)
            input(mnWidth)
            input(mxWidth)
              
            solve();
        }

        // Destructor that shows the output
        ~Solution() {
            // Printing total number of children who will get chocolate.
            print(ans);
        }

        // SolveFunction that solves our problem that contains  our driver code
        void solve();
        // Computes all possibilities
        int compute(int, int);
};

// Compute all Possibilities and returns the No. of peices that can be shared ==>
int Solution::compute(int a, int b) {

    int c=0; // Count of Pieces
    while (a and b) { // Condition till either of the row or columns are 0
        c++; // till then keeping incrementing value of count
        if(a>b) a-=b; // if value of row is greater then column then decrease the value of row
        else b-=a;    // if value of column is greater then row then decrease the value of column
    }
    return c; // Return no. of Pieces
}

// Pseudo Code
void Solution::solve() {
    
    // Executing every combination from minimum Length to maximum Length and from 
    // minimum Width to Maximum Width
    LOOP(x, mnLength, mxLength) {

        LOOP(y, mnWidth, mxWidth) {
            // Computing Number of Pieces of the combination of row and column ie. x and y
            ANSWER(x, y, ans, compute)
        }
    }
}

// Driver Code
int32_t main() {

    BOOST
    
    init (Solution, obj);
    d(obj);
}