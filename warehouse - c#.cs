using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace warehouse
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = 5;
            int[,] arr = new int[,] { { 1, 1, 1, 0, 1 }, 
                                      { 1, 1, 1, 0, 0 }, 
                                      { 0, 0, 0, 0, 1 }, 
                                      { 1, 1, 0, 0, 1 },
                                      { 0, 0, 0, 0, 0 }};
            bool toBreak = false;
            int breaker = 0;
            int goods = 0;
            int starti = 0;
            int startj = 0;
            int firstOccurenceOfZero = 0;
            int newstarti = 0;
            int newstartj = 0;
            int firstOccurenceOfOne = 0;
            int helper = 0;

            while (true)
            {
                for (int i = starti; i < n; i++)
                {
                    for (int j = startj; j < n; j++)
                    {
                        if(arr[i,j] == 1 && j == n-1)
                        {
                            for (int p = 0; p < n; p++)
                            {
                                
                            }
                        }
                        if (arr[i, j] == 1)
                        {
                            firstOccurenceOfOne++;
                            if (firstOccurenceOfOne == 1)
                            {
                                helper = j;
                            }
                        }
                        if (arr[i, j] == 0 && firstOccurenceOfOne != 0)
                        {
                            firstOccurenceOfZero++;
                            if (firstOccurenceOfZero == 1)
                            {
                                newstarti = i;
                                newstartj = j;
                            }
                            if (i != n - 1 && j != n - 1 && arr[i + 1, helper] == 0)
                            {
                                toBreak = true;
                                goods++;
                                starti = newstarti;
                                startj = newstartj;
                                firstOccurenceOfZero = 0;
                                firstOccurenceOfOne = 0;
                            }
                            break;
                        }
                        if (arr[i, j] == 0 && firstOccurenceOfOne == 0)
                        {
                            startj++;
                            toBreak = true;
                            break;
                        }
                    }
                    breaker = i;
                    if (toBreak) break;
                    
                }
                toBreak = false;
                if (breaker == n - 1) break;
                
            }
            

            
            int ways = 0;
            int helper2 = 0;
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    
                    if (arr[i, j] != 0) break;
                    helper2 = j;
                }
                if (helper2 == n-1) ways++;
            }
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    helper2 = j;
                    if (arr[j, i] != 0) break;
                }
                if (helper2 == n-1) ways++;
            }
            Console.WriteLine(ways);
            Console.WriteLine(goods);
            Console.ReadKey();


            
        }
    }
}
