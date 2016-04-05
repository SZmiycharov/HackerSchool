#include <iostream>
#include <vector>
#include <numeric>
#include <time.h>
#include <stdio.h>
#include <limits>
#include <algorithm>
using namespace std;

int read_input()
{
    int input = -1;
    bool valid = false;
    do
    {
        cin >> input;
        if (cin.good() && input>0)
        {
            valid = true;
        }
        else
        {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(),'\n');
            cout << "Bad input! Try again(input is integer and >0 ): ";
        }
    } while (!valid);

    return input;
}

int MaxSumAtCurrentIteration (vector<int>& helper, int boat, int length)
{
    int maxPossibleSum = 0;
            for (int i = length-1; i >=0; i--)
            {
                if (maxPossibleSum + helper.at(i) <= boat)
                {
                    maxPossibleSum += helper.at(i);
                    helper.erase(helper.begin() + i);
                }
                if (maxPossibleSum == boat) break;
            }
            return maxPossibleSum;
}

int main()
{
    cout<<"Courses: ";
    int courses = read_input();
    cout<<"Number of goats: ";
    int numberOfGoats = read_input();
    int sum = 0;
    int result = 0;
    vector <int> goats;
    for(int i=0; i<numberOfGoats; i++)
    {
        cout<<"Goat "<<i+1<<": ";
        goats.push_back(read_input());
        sum = sum + goats.at(i);
    }
    std::sort(goats.begin(), goats.end());
    vector<int> helper(goats);
    int currentBoat = goats.at(numberOfGoats - 1);

    clock_t tStart = clock();

    while (true)
            {
                for (int i = 0; i < courses; i++)
                {
                    result += MaxSumAtCurrentIteration(helper, currentBoat, helper.size());
                }

                if (result == sum) break;
                else
                {
                    currentBoat++;
                    helper = goats;
                    result = 0;
                }
            }

    cout<<endl;
    printf("Time taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
    cout<<"Minimal boat: "<<currentBoat<<endl;










}
