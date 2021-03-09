using System;
using Models.Attributes;

namespace Models.Resource.LeetCode
{
	[ArrayTag]
	public class P845
	{
		public static int LongestMountain(int[] arr)
		{
			var maxMountain = 0;
			var currMountain = 1;
			if (arr.Length<3)
				return 0;
			
			var current = arr[0];
			bool? dirUp = true;
			for (int i = 1; i < arr.Length; i++)
			{
				if (dirUp == true)
				{
					if (arr[i] > current)
					{
						currMountain++;
					}
					else if (arr[i] < current && currMountain>1)
					{
						dirUp = false;
						currMountain++;
					}
					else
					{
						currMountain = 1;
					}
				}
				else
				{
					if (arr[i] >= current)
					{
						dirUp = true;
						if (currMountain>=3)
							maxMountain = Math.Max(currMountain, maxMountain);
						currMountain = arr[i] > current ?  2 : 1;
					}
					else
					{
						currMountain++;
					}
				}
				
				current = arr[i];
			}
			if (currMountain>=3 && dirUp == false )
				maxMountain = Math.Max(currMountain, maxMountain);
			return maxMountain;
		}
	}
}