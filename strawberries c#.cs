using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace strawberriesNewTry
{
    class Program
    {
        static bool Contains(int [,] arr, int K, int L)
        {
            for(int i = 0; i<K; i++)
            {
                for(int j = 0; j<L; j++)
                {
                    if (arr[i, j] == 10000) return true;
                }
            }
            return false;
        }
        static void GoUp(ref int [,] arr, int L, int K, int currentDay, int maxDay, int indexi, int indexj)
        {
            indexi++;
            while(indexi<K)
            {
                if (currentDay >= maxDay) return;
                if (currentDay <= arr[indexi, indexj])
                {
                    arr[indexi, indexj] = currentDay;
                    indexi++;
                    currentDay++;
                }
                else break;
            }
        }
        static void GoDown(ref int [,] arr, int L, int K, int currentDay, int maxDay, int indexi, int indexj)
        {
            indexi--;
            while(indexi>=0)
            {
                if (currentDay >= maxDay) return;
                if (currentDay <= arr[indexi, indexj])
                {
                    arr[indexi, indexj] = currentDay;
                    indexi--;
                    currentDay++;
                }
                else break;
            }
        }
        static void GoLeft(ref int [,] arr, int L, int K, int currentDay, int maxDay, int indexi, int indexj)
        {
            indexj--;
            while(indexj>=0)
            {
                if (currentDay >= maxDay) return;
                if (currentDay <= arr[indexi, indexj])
                {
                    arr[indexi, indexj] = currentDay;
                    indexj--;
                    currentDay++;
                }
                else break;
            }
        }
        static void GoRight(ref int [,] arr, int L, int K, int currentDay, int maxDay, int indexi, int indexj)
        {
            indexj++;
            while(indexj<L)
            {
                if (currentDay >= maxDay) return;
                if (currentDay <= arr[indexi, indexj])
                {
                    arr[indexi, indexj] = currentDay;
                    indexj++;
                    currentDay++;
                }
                else break;
            }
        }

        static void Main(string[] args)
        {
            int K = 5, L = 5, R = 3, i1 =0, j1 = 0, i2 = K - 1, j2 = L - 1;
            int count = 0;

            R = R + 2;
            int[,] arr = new int[K, L];
            for (int i = 0; i < K; i++)
            {
                for (int j = 0; j < L; j++)
                {
                    arr[i, j] = 10000;
                }
            }
            arr[i2, j2] = 1;
            arr[i1, j1] = 1;
            int currentDay = 1;
            int helper = currentDay;
            while (true)
            {
                for (int i = 0; i < K; i++)
                {
                    for (int j = 0; j < L; j++)
                    {
                        if (arr[i, j] == currentDay)
                        {
                            GoUp(ref arr, L, K, currentDay + 1, R, i, j);
                            GoDown(ref arr, L, K, currentDay + 1, R, i, j);
                            GoLeft(ref arr, L, K, currentDay + 1, R, i, j);
                            GoRight(ref arr, L, K, currentDay + 1, R, i, j);
                        }
                    }
                }
                currentDay++;
                if (currentDay >= R) break;
            }

            for (int i = 0; i < K; i++)
            {
                for (int j = 0; j < L; j++)
                {
                    Console.Write(arr[i, j] + "   ");
                    if (arr[i, j] == 10000) count++;
                }
                Console.WriteLine();
            }

            Console.WriteLine("Count of OK strawberries: {0}", count);
            Console.ReadKey();
        }
    }
}
