using System;
using System.Collections.Generic;
using System.Linq;

namespace Models.Resource.Microsoft
{
	public static class MicrosoftReal
	{
		/// <summary>
		/// Get the Number of mutations needed
		/// </summary>
		/// <see href="file:../Description/Task1.jpg">Task screen</see>
		/// <param name="A">array of integers</param>
		/// <returns></returns>
		public static int Task1(int[] A) {
			// write your code in C# 6.0 with .NET 4.5 (Mono)
			
			int n = A.Length;
			Array.Sort(A);
			int middle = A[n / 2];
			int stepsCount = 0;
 
			for (int i = 0; i < n; i++)
				stepsCount += Math.Abs(A[i] - middle);

			if (n % 2 != 0) 
				return stepsCount;
			
			int secondStepsCount = 0;
			middle = A[(n / 2) - 1];

			for (int i = 0; i < n; i++)
			{
				secondStepsCount += Math.Abs(A[i] - middle);
			}
			return Math.Min(stepsCount, secondStepsCount);
		}
		
		/// <summary>
		/// Get max count of even pairs on the circle
		/// </summary>
		/// <see href="file:../Description/DemoTask_2.jpg">Task screen</see>
		/// <param name="A">array of integers</param>
		/// <returns></returns>
		public static int Task2(int[] A) {
			// write your code in C# 6.0 with .NET 4.5 (Mono)
			int evenPairCount = 0;
			int length = A.Length;
			
			if ((A[^1] + A[0])%2==0)
			{
				for (int i = 0; i < length - 1; i++)
				{
					if ((A[i] + A[i + 1]) % 2 != 1)
						continue;
					var newArray = new List<int>();
					newArray.AddRange(A.Skip(i + 1).ToList());
					newArray.AddRange(A.Take(i + 1).ToList());
					A = newArray.ToArray();
					break;
				}
			}

			bool prevEven = A[^1]% 2==0;
			bool prevPairAdded = false;
			for (int i = 0; i < length; i++)
			{
				bool curEven = A[i] % 2==0;
				if (curEven == prevEven && !prevPairAdded)
				{
					evenPairCount++;
					prevPairAdded = true;
				}
				else
				{
					prevPairAdded = false;
				}

				prevEven = curEven;
			}

			return evenPairCount;
		}
	}
}