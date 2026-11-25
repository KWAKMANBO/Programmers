class Solution {
    public int solution(int h1, int m1, int s1, int h2, int m2, int s2) {
        int answer = 0;

        // 초로 변환
        int start = h1 * 3600 + m1 * 60 + s1;
        int end = h2 * 3600 + m2 * 60 + s2;

        double h = start / 120.0 % 360;
        double m = start / 10.0 % 360;
        double s = start * 6.0 % 360;

        if (s == h || s == m) {
            answer++;
        }

        for (int t = start; t < end; t++) {
            double nextH = (t + 1) / 120.0 % 360;
            double nextM = (t + 1) / 10.0 % 360;
            double nextS = (t + 1) * 6.0 % 360;


            // 00시 즉 360도되는 순간을 처리
            double tmpH = nextH == 0.0 ? 360.0 : nextH;
            double tmpM = nextM == 0.0 ? 360.0 : nextM;
            double tmpS = nextS == 0.0 ? 360.0 : nextS;

            // 00시 00분 00초에만 세 침이 겹치므로 처리
            if (tmpH == 360 && tmpM == 360 && tmpS == 360) {
                answer++;
            }else{
                // else를 사용하지 않으면 00시 00분 00초에 카운트가 3번이됨
                if (s < h && tmpH <= tmpS) answer++;

                if (s < m && tmpM <= tmpS) answer++;
            }
            
            h = nextH;
            m = nextM;
            s = nextS;
        }

        return answer;
    }
}