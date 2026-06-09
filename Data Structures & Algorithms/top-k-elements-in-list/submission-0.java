class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] returned = new int[k];
        for (int i : nums) {
            if (!map.containsKey(i)) {
                map.put(i, 0);
            }
            map.put(i, map.get(i) + 1);
        }
        PriorityQueue<Integer> pq = new PriorityQueue<>(new Comparator<Integer>(){
            @Override
            public int compare(Integer a, Integer b) {
                return map.get(b).compareTo(map.get(a));
            }
        });
        for (int key : map.keySet()) {
            pq.add(key);
        }
        for (int i = 0; i < k; i++) {
            returned[i] = pq.poll();
        }
        return returned;
    }
}
