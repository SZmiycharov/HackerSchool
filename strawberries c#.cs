using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace strawberriesNewTry
{
    class Program
    {
        static void ValidateInt(string input, ref int number)
        {
            while (true)
            {
                if (int.TryParse(input, out number) && int.Parse(input) >= 0 && int.Parse(input) < 100000)
                {
                    number = int.Parse(input);
                    break;
                }
                else
                {
                    Console.Write("Bad input! Try again: ");
                    input = Console.ReadLine();
                }
            }
        }
        static void GoUp(ref int [,] arr, int K, int L, int currentDay, int maxDay, int indexi, int indexj)
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
        static void GoDown(ref int [,] arr, int K, int L, int currentDay, int maxDay, int indexi, int indexj)
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
        static void GoLeft(ref int [,] arr, int K, int L, int currentDay, int maxDay, int indexi, int indexj)
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
        static void GoRight(ref int [,] arr, int K, int L, int currentDay, int maxDay, int indexi, int indexj)
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
            int K = 0, L = 0, R = 0, i1 =0, j1 = 0, i2 = 0, j2 = 0;
            int count = 0;
            string choice = "";

            Console.Write("Enter K: ");
            ValidateInt(Console.ReadLine(), ref K);
            Console.Write("Enter L: ");
            ValidateInt(Console.ReadLine(), ref L);
            Console.Write("Enter R: ");
            ValidateInt(Console.ReadLine(), ref R);
            Console.Write("Enter i1: ");
            ValidateInt(Console.ReadLine(), ref i1);
            Console.Write("Enter j1: ");
            ValidateInt(Console.ReadLine(), ref j1);
            Console.Write("Enter another one? <y or n>");
            choice = Console.ReadLine();
            if (choice == "y")
            {
                Console.Write("Enter i2: ");
                ValidateInt(Console.ReadLine(), ref i2);
                Console.Write("Enter j2: ");
                ValidateInt(Console.ReadLine(), ref j2);
            }


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
            if(i2!=0 || j2!=0)
            {
                arr[i1, j1] = 1;
            }
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
                            GoUp(ref arr, K, L, currentDay + 1, R, i, j);
                            GoDown(ref arr, K, L, currentDay + 1, R, i, j);
                            GoLeft(ref arr, K, L, currentDay + 1, R, i, j);
                            GoRight(ref arr, K, L, currentDay + 1, R, i, j);
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
