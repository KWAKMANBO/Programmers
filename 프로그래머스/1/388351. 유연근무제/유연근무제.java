class Solution {
       public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = 0;
        // 출근 희망 시간 + 10분 으로 업데이트하기
        for (int i = 0; i < schedules.length; i++) {
            int time = schedules[i];
            schedules[i] = (time / 100 + (((time % 100) + 10) / 60)) * 100 + ((time % 100) + 10) % 60;
        }

        for (int i = 0; i < schedules.length; i++) {
            boolean check = true;
            int dayCnt = 0;
            for (int j = 0; j < 7; j++) {
                int currentDay = (startday - 1 + j) % 7;
                if (currentDay < 5) {
                    if (timelogs[i][j] > schedules[i]) {
                        check = !check;
                        break;
                    }
                }
            }
            if (check) answer++;

        }
        return answer;
    }
}