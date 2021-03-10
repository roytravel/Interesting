% dt = 0.001;
% ts = 0:dt:1;
% xs = sin(2*pi*30*ts) + sin(2*pi*100*ts) + sin(2*pi*140*ts);
% figure(1);
% plot(ts, xs, 'LineWidth', 1.3);
% 
% sigma = 2;
% ys = xs + sigma*randn(size(ts));
% 
% figure(2);
% plot(ts(1:size(ts,2)/5), xs(1:size(ts,2)/5), 'k', 'LineWidth', 1.3);
% hold on;
% plot(ts(1:size(ts,2)/5), ys(1:size(ts,2)/5), 'r', 'LineWidth', 1.3);
% legend('Raw Signal', 'Noisy Signal');


Fs = 1000; % Sampling frequency
T = 1/Fs; % Sampling period
L = 1500; % Length of signal
t = (0:L-1)*T; % Time vector


% 진폭:0.7, 정현파:50Hz, 진폭1의 120Hz 정현파를 포함하는 신호 생성
Signal = 0.7 * sin(2 * pi * 50 * t) + sin(2 * pi * 120 * t);

% 분산 4, 평균0의 백색 잡음(White Noise)으로 손상시킴
X = Signal + 2 * randn(size(t));

% 잡음이 있는 신호를 Time domain에 플로팅
plot(1000*t(1:100), X(1:100))
title('Signal Corrupted with Zero-Mean Random Noise')
xlabel('t (milliseconds)')
ylabel('X(t)')

% 신호의 푸리에 변환을 계산
Y = fft(X);

% 양방향 스펙트럼 P2를 계산
P2 = abs(Y/L);
% 단방향 스펙트럼 P1을 계산
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);

% 주파수 영역 f를 정의, 단방향 진폭 스펙트럼 P1을 플로팅.
% 잡음이 추가됐기 때문에 진폭이 정확히 0.7과 1이 아님.
% 평균적으로 신호가 길수록 더 나은 주파수 근삿값을 얻을 수 있음
f = Fs*(0:(L/2))/L;
plot(f, P1)
title('Single-Sided Amplitude Spectrum of X(t)')
xlabel('f (Hz)')
ylabel('|P1(f)|')

% 손상되지 않은 원래 신호의 푸리에 변환을 사용해 정확한 진폭 0.7과 1.0을 가져옴
Y = fft(Signal);
P2 = abs(Y/L);
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);

plot(f,P1)
title('Single-Sided Amplitude Spectrum of S(t)')
xlabel('f (Hz)')
ylabel('|P1(f)|')

% 가우스 펄스(Gaussian Pulse)
Fs = 100; % Sampling frequency
t = -0.5:1/Fs:0.5; % Time vector
L = length(t); % Signal length

X = 1/(4*sqrt(2*pi*0.01))*(exp(-t.^2/(2*0.01)));
plot(t, X)
title('Gaussian Pulse in Time Domain')
xlabel('Time (t)')
ylabel('X(t)')

% fft 함수를 사용하여 신호를 frequency domain으로 변환
n = 2^nextpow2(L);

% 가우스 펄스를 frequency domain으로 변환
Y = fft(X, n);

% 주파수 영역을 정의, 고유한 주파수를 플로팅
f = Fs*(0:(n/2))/n;
P = abs(Y/n);

plot(f, P(1:n/2+1))
title('Gaussian Pulse in Frequency Domain')
xlabel('Frequency (f)')
ylabel('|P(f)|')

% 코사인파
% Time domain과 Frequency domain의 cosine wave를 비교
% 샘플링 주파수 1kHz와 신호 지속 시간 1초로 신호 파라미터를 지정
Fs = 1000; % Sampling frequency
T = 1/Fs; % Sampling period
L = 1000; % Length of signal
t = (0:L-1)*T; % Time vector

x1 = cos(2 * pi * 50 * t); % First row wave
x2 = cos(2 * pi * 150 * t); % Second row wave
x3 = cos(2 * pi * 300 * t); % Third row wave

X = [x1; x2; x3];

for i = 1:3
    subplot(3, 1, i)
    plot(t(1:100), X(i,1:100))
    title(['Row ', num2str(i),' in the Time Domain'])
end

% 알고리즘 성능을 위해 fft를 사용해 입력값을 후행 0으로 패딩 가능
n = 2^nextpow2(L);
% X의 행을 따라, 즉 각 신호에 대해 fft를 사용하도록 dim 인수 지정
dim = 2;
% 신호의 푸리에 변환 계산
Y = fft(X, n, dim);

P2 = abs(Y/L);
P1 = P2(:,1:n/2+1);
P1(:,2:end-1) = 2*P1(:, 2:end-1);

for i = 1:3
    subplot(3, 1, i)
    plot(0:(Fs/n):(Fs/2-Fs/n),P1(i,1:n/2))
    title(['Row ', num2str(i), ' in the Frequency Domain'])
end
