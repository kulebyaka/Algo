using System.Collections.Generic;
using System.Linq;
using Models.Resource.LeetCode;
using NUnit.Framework;
using FluentAssertions;

namespace Tests.LeetCode;

//TestFixture for P22
[TestFixture]
[Parallelizable(ParallelScope.All)]
public class P22TestFixture
{
	[Test]
	[TestCase(3, new[] { "((()))", "(()())", "(())()", "()(())", "()()()" }),
	 TestCase(2, new[] { "()()", "(())" })]
	public void P22Test(int n, string[] expected)
	{
		var p22 = new P22();
		IList<string> actual = p22.GenerateParenthesis(n);
		actual.OrderBy(a => a).Should().BeEquivalentTo(expected.OrderBy(a => a));
	}
}