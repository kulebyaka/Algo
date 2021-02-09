using ConsoleApp.Models.LinkedList;

namespace ConsoleApp.LeetCode
{
	public class P206
	{
		public static string Run()
		{
			int[] input = {1,2,3,4,5};
			var x = new ListNode(input);
			var ret = P206.ReverseList(x);
			return ret.ToString();
		}
		public static ListNode ReverseList(ListNode head)
		{
			var current = head;
			if (current == null)
				return null;
			ListNode prev = null;
			ListNode x;
			while (true)
			{
				x = current.Next;
				current.Next = prev;
				if (x == null)
					return current;
				prev = current;
				current = x;
			}

		}
	}
}