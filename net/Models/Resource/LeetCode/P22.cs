using System.Collections.Generic;

namespace Models.Resource.LeetCode;

public class P22
{
	/// <summary>
	/// Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
	/// </summary>
	public IList<string> GenerateParenthesis(int n)
	{
		IList<string> result = new List<string>();
		if (n == 0)
			return result;
		GenerateParenthesis(n, n, "", result);
		return result;
	}

	private void GenerateParenthesis(int leftCounter, int rightCounter, string currentString, IList<string> result)
	{
		if (0 == leftCounter && 0 == rightCounter)
		{
			result.Add(currentString);
			return;
		}

		if (leftCounter > 0)
		{
			GenerateParenthesis(leftCounter - 1, rightCounter, currentString + "(", result);
		}

		if (leftCounter < rightCounter)
		{
			GenerateParenthesis(leftCounter, rightCounter - 1, currentString + ")", result);
		}
	}
}