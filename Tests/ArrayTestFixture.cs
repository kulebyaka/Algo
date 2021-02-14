using System.Collections.Generic;
using Models.LeetCode;
using NUnit.Framework;

namespace Tests
{
	[TestFixture]
	[Parallelizable(ParallelScope.All)]
	public class ArrayTestFixture
	{
		private static IEnumerable<TestCaseData> AddInputVariables()
		{
			yield return new TestCaseData(new[]{0,1,0,0,1,0,0}, 3);
			yield return new TestCaseData(new[]{0,1,2,3,2,0,1}, 6);
		}

		[Test, TestCaseSource(nameof(AddInputVariables))]
		public void TestEquality(int[] intArr, int result)
		{
			Assert.AreEqual(result, P845.LongestMountain(intArr));
		}
	}
}