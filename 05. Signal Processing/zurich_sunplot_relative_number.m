% Background
% 취리히 흑점 상대 수 : 태양 흑점 개수와 크기를 표로 만든 데이터 셋
% 약 1,700년대 ~ 2,000년대까지의 데이터 플로팅 

% 데이터 로딩
load sunspot.dat
year = sunspot(:, 1);
relNums = sunspot(:, 2);
plot(year, relNums)
xlabel('Year')
ylabel('Zurich Number')
title("Sunspot Data")

% 태양 흑점 활동 주기 특성
plot(year(1:50), relNums(1:50), 'b.-');
xlabel('Year')
ylabel('Zurich Number')
title('Sunspot Data')

% 데이터에서 주파수 성분 식별을 위해 fft 함수를 사용해 취리히 데이터에 푸리에 변환 수행
y = fft(relNums);

% 출력값의 첫 번째 element에 데이터의 합이 저장되어 있고, element 제거
y(1) = [];
plot(y, 'ro') % red o
xlabel('real(y)')
ylabel('imag(y)')
title('Fourier Coefficients')

% 푸리에 계수만으로는 해석이 어렵고, 더 의미 있는 계수의 측정값은 크기를 제곱한 것으로, 전력을 측정한 값
% 크기에서 계수의 절반이 반복되기에 절반에 대한 전력만 계산
% 전력 스펙트럼(Power Spectrum)을 Cycles/Year를 측정 단위로 취하는 주파수의 함수로 플로팅
n = length(y);
power = abs(y(1:floor(n/2))).^2; % power of first half of transform data
maxfreq = 1/2; % maximum frequency
freq = (1:n/2)/(n/2)*maxfreq; % equally spaced frequency grid
plot(freq, power)
xlabel('Cycles/Year')
ylabel('Power')

% 주기적 활동을 시각적으로 해석에 쉬우려면 Years/Cycle을 측정 단위로 취하는 주기 함수로 전력을 플로팅
period = 1./freq;
plot(period, power);
xlim([0 50]); %zoom in on max power
xlabel('Years/Cycle')
ylabel('Power')

% 결과적으로 11년 주기로 최대치에 도달