class Solution {
    public boolean isValidSudoku(char[][] board) {
        int n = board.length;
        for (int i = 0; i < n; i++) {
            HashSet<Character> temp = new HashSet<>();
            for (int j = 0; j < n; j++) {
                char c = board[i][j];
                if (c == '.') continue;
                if (!temp.add(c)) {
                    return false;
                }
            }
        }
        for (int j = 0; j < n; j++) {
            HashSet<Character> temp1 = new HashSet<>();
            for (int i = 0; i < n; i++) {
                char c = board[i][j];
                if (c == '.') continue;
                if (!temp1.add(c)) {
                    return false;
                }
            }
        }
        for (int i = 0; i < 9; i = i + 3) {
            for (int j = 0; j < 9; j = j + 3) {
                HashSet<Character> temp2 = new HashSet<>();
                for (int row = i; row < i + 3; row++) {
                    for (int col = j; col < j + 3; col++) {
                        char c = board[row][col];

                        if (c == '.') {
                            continue;
                        }

                        if (!temp2.add(c)) {
                            return false;
                        }
                    }
                }
            }
        }
        return true;
        
    }
}
