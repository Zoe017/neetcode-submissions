class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs == null) {
            return new ArrayList<>();
        }
        Map<String, List<String>> map = new HashMap<>();
        for (String w : strs) {
            char[] arr = w.toCharArray();
            Arrays.sort(arr);
            String sorted = new String(arr);
            if (!map.containsKey(sorted)) {
                map.put(sorted, new ArrayList<>());
            }
            map.get(sorted).add(w);
        }
        List<List<String>> returned = new ArrayList<>();
        for (String key : map.keySet()) {
            returned.add(map.get(key));
        }
        return returned;
    }
}
