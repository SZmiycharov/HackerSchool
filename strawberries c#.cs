using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Linq;

namespace straweberries
{
    class Program
    {
        static void ValidateInt(string input, ref int number)
        {
            while (true)
            {
                if (int.TryParse(input, out number) && int.Parse(input) > 0 && int.Parse(input) < 100000)
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
        static bool Contains(int [,] arr, int K, int L, int num)
        {
            for(int i = 0; i<K; i++)
            {
                for(int j = 0; j<L; j++)
                {
                    if (arr[i, j] == num) return true;
                }
            }
            return false;
        }

        static void MakeNeighborsBadStrawberries(ref int [,] arr, int arri, int arrj,
            int currentDay, int maxDay, int indexi, int indexj)
        {
            if (indexj >= arrj || indexj < 0 || indexi < 0 || indexi >= arri) return;
            else
            {
                if (currentDay >= maxDay) return;
                //idnexi, indexj - index of the bad strawberry
                if (indexj < arrj && indexi > 0 && indexj != arrj && arr[indexi - 1, indexj] >= currentDay)
                {
                    arr[indexi - 1, indexj] = currentDay;
                }
                if (indexj < arrj && indexi != arri && indexj > 0 && arr[indexi, indexj - 1] >= currentDay)
                {
                    arr[indexi, indexj - 1] = currentDay;
                }
                if (indexj + 1 < arrj && indexi != arri && arr[indexi, indexj + 1] >= currentDay)
                {
                    arr[indexi, indexj + 1] = currentDay;
                }
                if (indexj <= arrj && indexi + 1 < arri && indexj != arrj && arr[indexi + 1, indexj] >= currentDay)
                {
                    arr[indexi + 1, indexj] = currentDay;
                }
            }

            currentDay++;
            if (currentDay >= maxDay) return;
            else
            {
                MakeNeighborsBadStrawberries(ref arr, arri, arrj, currentDay, maxDay, indexi + 1, indexj);
                MakeNeighborsBadStrawberries(ref arr, arri, arrj, currentDay, maxDay, indexi - 1, indexj);
                MakeNeighborsBadStrawberries(ref arr, arri, arrj, currentDay, maxDay, indexi, indexj + 1);
                MakeNeighborsBadStrawberries(ref arr, arri, arrj, currentDay, maxDay, indexi, indexj - 1);
            }
        }

        static void Main(string[] args)
        {
            int K = 10, L = 10, R = 20, i1 = 0, j1 = 0, i2 = K-1, j2 = L-1;
            if (R > (K * L / 2)) Console.Write("0");
            else
            {
                int[,] arr = new int[K, L];
                for (int i = 0; i < K; i++)
                {
                    for (int j = 0; j < L; j++)
                    {
                        arr[i, j] = 100;
                    }
                }
                arr[i2, j2] = 1;
                arr[i1, j1] = 1;

                int currentDay = 2;

                MakeNeighborsBadStrawberries(ref arr, K, L, currentDay, R + 2, i1, j1);
                MakeNeighborsBadStrawberries(ref arr, K, L, currentDay, R + 2, i2, j2);

                for (int p = 0; p < K; p++)
                {
                    for (int q = 0; q < L; q++)
                    {
                        Console.Write("{0}   ", arr[p, q]);
                    }
                    Console.Write(Environment.NewLine + Environment.NewLine);
                }
                int count = 0;
                for (int p = 0; p < K; p++)
                {
                    for (int q = 0; q < L; q++)
                    {
                        if (arr[p, q] == 100) count++;
                    }
                }
                Console.WriteLine("Count: {0}", count);
            }
            /*string choice;
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
            if(choice =="y") 
            {
                Console.Write("Enter i2: ");
                ValidateInt(Console.ReadLine(), ref i2);
                Console.Write("Enter j2: ");
                ValidateInt(Console.ReadLine(), ref j2);
            }*/

            
            
            Console.ReadKey();
        }
    }
}
