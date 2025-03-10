using Models.Resource.Other;
using NUnit.Framework;

namespace Tests;

[TestFixture]
public class YouTubeTestFixtures
{
	[Test]
	[TestCase(new int[] { 1, 2, 3, -2, -1 }, 3)]
	[TestCase(new int[] { 1, 2, 3, 4, -1 }, 4)]
	[TestCase(new int[] { 1, 2, 3, 4 }, 0)]
	public void FindSplitPointTest(int[] input, int expected)
	{
		var youTube = new YouTube();
		int result = youTube.SplitPoint(input);
		Assert.AreEqual(expected, result);
	}
}