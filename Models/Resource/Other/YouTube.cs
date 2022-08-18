namespace Models.Resource.Other;

public class YouTube
{
	// An ordered array is split in two and the parts are rearranged.
	// Find the split point
	public int SplitPoint(int[] array)
	{
		int key = array[0];
		int low = 0;
		int high = array.Length - 1;
		while (low <= high)
		{
			int mid = (low + high) / 2 + 1;
			if (mid == array.Length)
				return 0;

			if (array[mid - 1] > array[mid])
				return mid;

			if (key < array[mid])
				low = mid;
			else if (key > array[mid])
				high = mid;
		}

		return 0;
	}
}