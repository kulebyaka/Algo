namespace Models.Structures.LinkedList
{
	public class ListNode {

		public ListNode(int[] values, int index = 0)
		{
			this.Value = values[index];
			this.Next = index + 1 == values.Length 
				? null 
				: new ListNode(values, index+1);
		}
		public int Value;
		public ListNode Next;
		public ListNode(int val=0, ListNode next=null) {
			this.Value = val;
			this.Next = next;
		}
	}
}