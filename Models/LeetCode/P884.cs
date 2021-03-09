using System.Collections.Generic;
using System.Linq;
using Models.Attributes;

namespace Models.LeetCode
{
	[StringTag]
	public class P884
	{
		public static string Run()
		{
			var ret = P884.UncommonFromSentences("apple apple", "banana");
			return ret.ToString();
		}
		
		public static string[] UncommonFromSentences(string A, string B) {
			var x = new Dictionary<string, bool>();
			foreach (string s in A.Split(' '))
			{
				bool added = x.TryAdd(s, true);
				if (!added)
					x[s] = false;
			}
			
			foreach (string s in B.Split(' '))
			{
				bool added = x.TryAdd(s, true);
				if (!added)
					x[s] = false;
			}

			return  x.Where(a=>a.Value).Select(a=>a.Key).ToArray();
		}
	}
}