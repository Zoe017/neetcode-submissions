class Solution {
    public int longestConsecutive(int[] nums) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int num : nums) {
            pq.add(num);
        }
        if (pq.isEmpty()) {
            return 0;
        }
        int len = 1;
        int max = 1;
        int prev = pq.poll();
        while (!pq.isEmpty()) {
            int next = pq.poll();
            if (prev == next - 1) {
                len += 1;
            } else if (prev < next - 1) {
                len = 1;
            }
            if (len >= max) {
                max = len;
            }
            prev = next;
        }
        return max;
    }
}
