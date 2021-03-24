% 구형파의 푸리에 급수 전개가 어떻게 홀수 고조파의 합계로 이루어지는가

% 0부터 10까지(step_size=0.1) 이어지는 Time vector 생성 후 모든 point에서 sin 값을 구함

t = 0:.1:10;
y = sin(t);
plot(t,y);

% 기본파에 제3 고조파를 추가
y = sin(t) + sin(3*t)/3;
plot(t,y);

% 제1 고조파, 제3 고조파, 제5 고조파, 제7 고조파, 제9 고조파
y = sin(t) + sin(3*t)/3 + sin(5*t)/5 + sin(7*t)/7 + sin(9*t)/9;
plot (t,y);

% 기본파부터 제10 고조파까지 이동하면서 continuous하게 더 많은 
% 고조파로 구성된 벡터를 생성하고 모든 중간 step을 행렬의 행으로 저장

t = 0:.02:3.14;
y = zeros(10, length(t));
x = zeros(size(t));
for k = 1:2:19
    x = x + sin(k*t)/k;
    y((k+1)/2,:) = x;
end
plot(y(1:2:9,:)')
title('The bulding of a square wave: Gibbs'' effect')

% sin wave가 점진적으로 square wave로 변환되는 모습을 나타내는 3차원 곡면
surf(y);
shading interp
axis off ij