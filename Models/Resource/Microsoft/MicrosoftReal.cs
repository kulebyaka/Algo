using System;
using System.Collections.Generic;
using System.Linq;

namespace Models.Resource.Microsoft
{
	public static class MicrosoftReal
	{
		public static int solution(int[] A) {
			// write your code in C# 6.0 with .NET 4.5 (Mono)
			
			int n = A.Length;
			Array.Sort(A);
			var middle = A[n / 2];
			var stepsCount = 0;
 
			for (var i = 0; i < n; i++)
				stepsCount += Math.Abs(A[i] - middle);

			if (n % 2 != 0) 
				return stepsCount;
			
			var secondStepsCount = 0;
			middle = A[(n / 2) - 1];

			for (var i = 0; i < n; i++)
			{
				secondStepsCount += Math.Abs(A[i] - middle);
			}
			return Math.Min(stepsCount, secondStepsCount);
		}
		
		public static int solution1(int[] A) {
			// write your code in C# 6.0 with .NET 4.5 (Mono)
			var evenPairCount = 0;
			var length = A.Length;
			
			if ((A[A.Length - 1] + A[0])%2==0)
			{
				for (var i = 0; i < length - 1; i++)
				{
					if ((A[i] + A[i + 1]) % 2 != 1)
						continue;
					int firstOddIndex = i;
					var newArray = new List<int>();
					newArray.AddRange(A.Skip(firstOddIndex + 1).ToList());
					newArray.AddRange(A.Take(firstOddIndex + 1).ToList());
					A = newArray.ToArray();
					break;
				}
			}

			var prevEven = A[A.Length - 1]% 2==0;
			var prevPairAdded = false;
			for (var i = 0; i < length; i++)
			{
				var curEven = A[i] % 2==0;
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