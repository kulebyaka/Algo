using System.Collections.Generic;
using Models.Resource.LeetCode;
using Models.Structures.Tree;
using NUnit.Framework;

namespace Tests
{
	[TestFixture]
	[Parallelizable(ParallelScope.All)]
	public class ArrayTestFixture
	{
		private static IEnumerable<TestCaseData> AddInputVariables()
		{
			yield return new TestCaseData(new[] { 0, 1, 0, 0, 1, 0, 0 }, 3);
			yield return new TestCaseData(new[] { 0, 1, 2, 3, 2, 0, 1 }, 6);
		}

		private static IEnumerable<TestCaseData> AddInput538()
		{
			yield return new TestCaseData(
				new int?[] { 4, 1, 6, 0, 2, 5, 7, null, null, null, 3, null, null, null, 8 },
				new int?[] { 30, 36, 21, 36, 35, 26, 15, null, null, null, 33, null, null, null, 8 }
			);
		}

		[Test, TestCaseSource(nameof(AddInputVariables))]
		public void P845TestEquality(int[] intArr, int result)
		{
			Assert.AreEqual(result, P845.LongestMountain(intArr));
		}

		[Test, TestCaseSource(nameof(AddInput538))]
		public void P538TestEquality(int?[] input, int?[] output)
		{
			var node = new BinaryTreeNode<int>(input);
			BinaryTreeNode<int> binaryTreeNode = new P538().ConvertBST(node);
			var converted = binaryTreeNode.ConvertToArray();
			Assert.AreEqual(output, converted);
		}
	}
}