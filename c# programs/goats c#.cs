using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace goats
{
    class Program
    {
        static void ValidateInt (string input, ref int number)
        {
            while(true)
            {
                if (int.TryParse(input, out number) && int.Parse(input)>0)
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

        static int MaxSumAtCurrentIteration (List<int> helper, int boat, int length)
        {
            int maxPossibleSum = 0;
            for (int i = length-1; i >=0; i--)
            {
                if (maxPossibleSum + helper[i] <= boat)
                {
                    maxPossibleSum += helper[i];
                    helper.RemoveAt(i);
                }
                if (maxPossibleSum == boat) break;
            }
            return maxPossibleSum;
        }

        static void Main(string[] args)
        {
            List<int> goats = new List<int>();
            int result = 0;
            int currentElement = 0;
            int courses = 0;
            int numberOfGoats = 0;
            
            Console.Write("Number of courses: ");
            ValidateInt(Console.ReadLine(),ref courses);
            Console.Write("Number of goats: ");
            ValidateInt(Console.ReadLine(), ref numberOfGoats);
            

            for (int i = 0; i < numberOfGoats; i++)
            {
                
                Console.Write("Goat {0}: ", i);
                ValidateInt(Console.ReadLine(), ref currentElement);
                goats.Add(currentElement);
            }

            var watch = System.Diagnostics.Stopwatch.StartNew();
            goats.Sort();
            List<int> helperList = new List<int>(goats);
            int currentBoat = helperList[numberOfGoats - 1];
            int sum = helperList.Sum();

            while (true)
            {
                for (int i = 0; i < courses; i++)
                {
                    result += MaxSumAtCurrentIteration(helperList, currentBoat, helperList.Count());
                }

                if (result == sum) break;
                else
                {
                    currentBoat++;
                    helperList = new List<int>(goats);
                    result = 0;
                }
            }

            watch.Stop();
            var elapsedMs = watch.ElapsedMilliseconds;


            Console.WriteLine("Minimal boat: {0} ; Elapsed time in ms: {1}", currentBoat, elapsedMs);

            Console.ReadKey();
        }
    }
}
