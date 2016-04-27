using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace warehouse
{
    class Program
    {
        static void ValidateInt(string input, ref int number)
        {
            while (true)
            {
                if (int.TryParse(input, out number) && int.Parse(input) >= 0)
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
        static void ClearElements(ref int[,] arr, int lastReachedLeftColumn, int lastReachedRightColumn,
                                  int lastReachedTopRow, int lastReachedBottomRow, int n)
        {
            for (int i = lastReachedLeftColumn; i <= lastReachedRightColumn; i++)
            {
                for (int j = lastReachedTopRow; j <= lastReachedBottomRow; j++)
                {
                    arr[j, i] = -1;
                }
            }
        }
        static void GoRight(ref int[,] arr, int i, int j, int n, ref int lastReachedRightColumn)
        {
            for (int p = j; p < n; p++)
            {
                if (arr[i, p] == 1)
                {
                    arr[i, p] = -1;
                }
                if (arr[i, p] == 0)
                {
                    lastReachedRightColumn = p - 1;
                    break;
                }
                if (p == n - 1) lastReachedRightColumn = p; 
            }
        }
        static void GoLeft(ref int[,] arr, int i, int j, int n, ref int lastReachedLeftColumn)
        {
            for (int p = j; p >= 0; p--)
            {
                if (arr[i, p] == 1)
                {
                    arr[i, p] = -1;
                }
                if (arr[i, p] == 0)
                {
                    lastReachedLeftColumn = p + 1;
                    break;
                }
                if (p == 0) lastReachedLeftColumn = p;
            }
        }
        static void GoDown(ref int[,] arr, int i, int j, int n, ref int lastReachedBottomRow)
        {
            for (int p = i; p < n; p++)
            {
                if (arr[p, j] == 1)
                {
                    arr[p, j] = -1;
                }
                if (arr[p, j] == 0)
                {
                    lastReachedBottomRow = p - 1;
                    break;
                }
                if (p == n - 1) lastReachedBottomRow = p;
            }
        }
        static void GoUp(ref int[,] arr, int i, int j, int n, ref int lastReachedTopRow)
        {
            for (int p = i; p >= 0; p--)
            {
                if (arr[p, j] == 1)
                {
                    arr[p, j] = -1;
                }
                if (arr[p, j] == 0)
                {
                    lastReachedTopRow = p + 1;
                    break;
                }
                if (p == 0) lastReachedTopRow = p;
            }
        }
        static void Main(string[] args)
        {
            int n = 0;
            Console.Write("n <for nxn matrix>= ");
            ValidateInt(Console.ReadLine(),ref n);
            int[,] arr = new int[n, n];
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    Console.Write("arr[{0},{1}]=", i, j);
                    ValidateInt(Console.ReadLine(), ref arr[i, j]);
                    if(arr[i,j]!=0 && arr[i,j]!=1)
                    {
                        Console.Write("Goods should be 1s, empty boxes should be 0s!");
                        Console.ReadKey();
                        Environment.Exit(0);
                    }
                }
            }
            //find possible ways in labyrinth
            int ways = 0;
            int helper = 0;
            //find horizontal ways
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    if (arr[i, j] != 0) break;
                    helper = j;
                }
                if (helper == n - 1) ways++;
            }
            //find vertycal ways
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    helper = j;
                    if (arr[j, i] != 0) break;
                }
                if (helper == n - 1) ways++;
            }

            //find the rectangles(goods) in the labyrinth
            int goods = 0;
            int lastReachedTopRow = 0;
            int lastReachedBottomRow = 0;
            int lastReachedRightColumn = 0;
            int lastReachedLeftColumn = 0;
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    if (arr[i, j] == 1)
                    {
                        GoUp(ref arr, i, j, n, ref lastReachedTopRow);
                        GoDown(ref arr, i, j, n, ref lastReachedBottomRow);
                        GoRight(ref arr, i, j, n, ref lastReachedRightColumn);
                        GoLeft(ref arr, i, j, n, ref lastReachedLeftColumn);
                        ClearElements(ref arr, lastReachedLeftColumn, lastReachedRightColumn, 
                            lastReachedTopRow, lastReachedBottomRow, n);
                        goods++;
                    }
                    else arr[i, j] = -1;
                }
            }


            Console.WriteLine("Ways: {0}", ways);
            Console.WriteLine("Rectangles: {0}", goods);
            Console.ReadKey();
        }
    }
}