clear all; close all;
X=imread('2.Lab2\visit.png');
X1=im2bw(X,0.8);
[X3, X4]=spa_q(X1);
%------------
kq=bwconncomp(X4);
kq.NumObjects
figure,
subplot(3,1,1); imshow(X); title('anh goc');
%subplot(2,2,2); imshow(X2); title('dao cua anh nhi phan');
subplot(3,1,2); imshow(X3); title('tach roi cac doi tuong');
subplot(3,1,3); imshow(X4); title('lam min');