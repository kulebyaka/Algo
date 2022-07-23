using System;
using System.Collections.Generic;
using Models.Resource.Microsoft;
using Models.Structures.Tree;
using NUnit.Framework;

namespace Tests
{
	[TestFixture]
	[Parallelizable(ParallelScope.All)]
	public class MicrosoftTestFixture
	{
		[Test]
		[TestCase(10d, 0.1)]
		public void SqrtTest(double variable, double eps)
		{
			var microsoftTasks = new MicrosoftTasks();
			double mySqrt = MicrosoftTasks.Sqrt(variable, eps);
			double actualSqrt = Math.Sqrt(variable);
			Assert.True(Math.Abs(mySqrt - actualSqrt) < eps);
		} 
		
		[Test, TestCaseSource(nameof(AddInputNearestCommonNode))]
		public void NearestCommonNodeTest(int?[] bst, int a, int b, int expectedCommonRoot)
		{
			var microsoftTasks = new MicrosoftTasks();
			var commonRoot = MicrosoftTasks.FindCommonRoot(new BinaryTreeNode<int>(bst), a, b);
			Assert.AreEqual(commonRoot, expectedCommonRoot);
		} 
		
		// TestCaseData
		private static IEnumerable<TestCaseData> AddInputNearestCommonNode()
		{
			yield return new TestCaseData( new int?[]{5, 3, 8, 1, 4, null, 10}, 4, 8, 5);
		}
		
		[Test, TestCaseSource(nameof(solution1Input))]
		public void solution1(int[] bst, int expectedCommonRoot)
		{
			var commonRoot = MicrosoftReal.solution1(bst);
			Assert.AreEqual(commonRoot, expectedCommonRoot);
		} 
		private static IEnumerable<TestCaseData> solution1Input()
		{
			yield return new TestCaseData( new int[]{4, 2, 5, 8, 7, 3, 7}, 2);
			yield return new TestCaseData( new int[]{14, 21, 16, 35, 22}, 1);
			yield return new TestCaseData( new int[]{0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0}, 4);
		}
		
		[Test, TestCaseSource(nameof(solutionInput))]
		public void solution(int[] bst, int expectedCommonRoot)
		{
			var commonRoot = MicrosoftReal.solution(bst);
			Assert.AreEqual(commonRoot, expectedCommonRoot);
		}
		
		private static IEnumerable<TestCaseData> solutionInput()
		{
			yield return new TestCaseData( new int[]{4, 2, 5, 8, 7, 3, 7}, 2);
			yield return new TestCaseData( new int[]{14, 21, 16, 35, 22}, 1);
			yield return new TestCaseData( new int[]{0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0}, 4);
		}
		
		
	}
	
}