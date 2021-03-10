% 컨볼루션을 사용하여 고주파수 성분이 포함된 2차원 데이터를 평활화가능

% peak 함수 사용: 2차원 데이터 생성 -> 다양한 등고선 레벨에 데이터 플로팅
Z = peaks(100);
levels = -7:1:10;
contour(Z,levels)

% 데이터에 랜덤 잡음 삽입 후 잡음 있는 등고선 플로팅
Znoise = Z + rand(100) - 0.5;
contour(Znoise, levels)

% conv2 함수는 커널을 사용하여 2차원 데이터를 컨볼루션함
% 커널 요소는 데이터의 특징을 제거 또는 향상 시키는 방법을 정의
% 더 큰 크기의 커널은 주파수 응답을 fine tuing 가능. 높은 정밀도 제공.

% 3x3 커널 K를 정의, conv2를 통해 Znoise 잡음 데이터를 평활화
K = 0.125 * ones(3);
Zsmooth1 = conv2(Znoise, K, 'same');
contour(Zsmooth1, levels);

% 5x5 커널을 사용해 잡음 데이터를 평활화
K = 0.045 * ones(5);
Zsmooth2 = conv2(Znoise, K, 'same');
contour(Zsmooth2, levels)
