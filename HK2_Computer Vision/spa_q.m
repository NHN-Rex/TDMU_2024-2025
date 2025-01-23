function [BW2, BW3 ] = spa_q(BW1)
SE1 = strel('sphere', 10);
SE2 = strel('sphere', 10);
% se1=strel('line', 64, 512)
% se2=strel('line', 10, 64)
BW2 = imerode(BW1,SE1);
BW3 = imdilate(BW2,SE2);
end

